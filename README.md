# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go)](https://go.dev/)
[![Version](https://img.shields.io/badge/version-2.6.0-blue)](https://github.com/sinmofun/atp)

## 什么是 ATP？

ATP (AI Transfer Protocol) 是一套**标准化的 AI 操作指令协议**，旨在为 AI、人类运维人员和自动化设备提供一套通用的"普通话"——让 AI 能够像人类一样，通过统一的指令语法直接操作操作系统和硬件设备。

```
AI 大脑          →  ATP 指令  →  操作系统
人类运维        →  ATP 指令  →  服务器/设备
自动化脚本      →  ATP 指令  →  数据库/容器
```

## 核心设计理念

- **一套语法，三方通用**：AI、人、自动化脚本使用完全相同的指令格式
- **指令自注册**：所有指令通过 `init()` 自动注册到引擎，支持热插拔
- **跨平台一致**：同一套指令在 Linux 和 Windows 下行为统一
- **哨兵模式**：多行内容通过 hash 边界保护，防止截断与注入
- **平台分离架构**：核心逻辑与平台实现通过 `_unix.go` / `_windows.go` 分离

## 快速开始

### 环境要求

- Go 1.26+ (推荐)
- 支持的 OS: Linux, Windows, macOS (计划中)

### 克隆项目

```bash
git clone https://github.com/sinmofun/atp.git
cd atp
```

### 编译

```bash
go build -o atp_ws ./server/atp_ws.go
```

### 运行

```bash
./atp_ws
```

服务默认监听在 `ws://127.0.0.1:9000/ws`

### 基础使用

```bash
# 文件操作
create#c1:./hello.txt
text@t1:
Hello, World!
t1

# 读取文件
read#r1:./hello.txt

# 执行系统命令
terminal#t1:echo Hello from ATP

# 网络请求
fetch#f1:https://api.github.com/repos/sinmofun/atp
```

## 指令列表 (36个)

| # | 指令 | 功能 | 平台 |
|---|------|------|------|
| 1 | `create` | 创建文件/目录 | 全平台 |
| 2 | `read` | 读取文件内容 | 全平台 |
| 3 | `update` | 修改文件内容 | 全平台 |
| 4 | `delete` | 删除文件/目录 | 全平台 |
| 5 | `copy` | 复制文件/目录 | 全平台 |
| 6 | `move` | 移动文件/目录 | 全平台 |
| 7 | `rename` | 重命名 | 全平台 |
| 8 | `append` | 追加内容到文件 | 全平台 |
| 9 | `insert` | 在指定位置插入内容 | 全平台 |
| 10 | `list` | 列出目录内容 | 全平台 |
| 11 | `tree` | 树形展示目录 | 全平台 |
| 12 | `stat` | 查看文件元信息 | 全平台 |
| 13 | `find` | 递归查找文件 | 全平台 |
| 14 | `replace` | 替换文件内容 | 全平台 |
| 15 | `terminal` | **全功能终端执行器** | Linux/Windows |
| 16 | `run` | 执行 ATP 指令文件 | 全平台 |
| 17 | `length` | 计算数据长度 | 全平台 |
| 18 | `regex` | 正则提取数据 | 全平台 |
| 19 | `save` | 持久化执行结果 | 全平台 |
| 20 | `zip` | 压缩文件/目录 | 全平台 |
| 21 | `unzip` | 解压文件 | 全平台 |
| 22 | `chmod` | 修改文件权限 | 全平台 |
| 23 | `chown` | 修改文件归属 | 全平台 |
| 24 | `uname` | 查看系统信息 | 全平台 |
| 25 | `fetch` | HTTP 网络请求 | 全平台 |
| 26 | `ftp` | FTP 远程文件管理 | 全平台 |
| 27 | `ssh` | SSH 远程命令执行 | 全平台 |
| 28 | `daemon` | 后台进程管理 | 全平台 |
| 29 | `sys_power` | 系统电源管理 | 全平台 |
| 30 | `knowledge` | 知识库管理 | 全平台 |
| 31 | `task` | 任务管理 | 全平台 |
| 32 | `when` | 条件触发执行 | 全平台 |
| 33 | `config` | 配置管理 | 全平台 |
| 34 | `workspace` | 工作区管理 | 全平台 |
| 35 | `replace` | 递归替换 | 全平台 |
| 36 | `WebSocket` | WebSocket 服务 | 全平台 |

## terminal 指令 —— 全功能终端执行器

`terminal` 是 ATP 的核心执行指令，在 Linux 下基于 PTY 伪终端实现，在 Windows 下基于临时 BAT 脚本执行。

### 平台差异

| 特性 | Linux | Windows |
|------|-------|---------|
| 底层实现 | PTY 伪终端 (creack/pty) | 临时 BAT 脚本 |
| 环境变量 | 自动加载 .bashrc/.profile | 仅系统默认变量 |
| 交互式命令 | 支持 | 不支持 |
| 后台进程 | 支持 `&` | 支持 `start` |
| 输出格式 | 可能含 ANSI 转义序列 | 纯文本 |

### 参数说明

| 参数 | 必填 | 默认值 | 说明 |
|------|:--:|------|------|
| 主参数 | 是 | — | 单行命令直接写；多行命令用 `@hash` 哨兵 |
| `workdir` | 否 | `./` | 工作目录，基于 workspace 配置解析 |
| `timeout` | 否 | `30s` | 超时，纯数字默认秒，支持 `5ms/10s/1m/1h` |
| `encoding` | 否 | `utf-8` | `utf-8` / `gbk` / `gb2312` / `gb18030` / `big5` |
| `async` | 否 | `false` | 异步执行，通过 `log` 查看结果 |
| `log` | 否 | — | `页码,条数`，查看历史日志 |

## 项目结构

```
atp/
├── engine/          # 核心引擎（指令注册、解析、执行）
├── commands/        # 内置指令实现
│   ├── execute.go       # execute 指令（Windows 实现）
│   ├── execute_unix.go  # execute 指令（Unix 实现）
│   ├── terminal.go      # terminal 指令（公共逻辑）
│   ├── terminal_unix.go # terminal 指令（Unix PTY 实现）
│   └── terminal_windows.go # terminal 指令（Windows BAT 实现）
├── configure/       # 配置管理（YAML/JSON）
├── logger/          # 日志模块
├── server/          # WebSocket 服务
├── config/          # 配置文件目录
├── cmd/             # 测试文件
├── docs/            # 项目文档
└── workspace/       # 工作区
```

## 错误码

| Code | 含义 | 典型场景 |
|:----:|------|----------|
| 0 | 成功 | 指令正常执行 |
| 1 | 失败（通用） | 通用执行错误 |
| 2 | 异步执行中 | `async:true` 已启动 |
| 3 | 指令未找到 | 指令名未注册 |
| 4 | 超时 | 超过 `timeout` 限制 |
| 5 | 文件/路径不存在 | 目标文件或目录不存在 |

## 测试状态

| 维度 | 测试项数 | 通过 | 通过率 |
|------|---------|------|--------|
| terminal Linux 多维度测试 | 120 | 118 | 98.3% |
| terminal Linux 压力测试 | 709 | 709 | 100% |
| terminal Windows 多维度测试 | 90 | 75 | 83.3% |
| terminal Windows 压力测试 | 250 | 250 | 100% |
| execute 指令测试 | 250 | 250 | 100% |
| 其他指令测试 | 1103 | 1099 | 99.6% |
| **总计** | **2522** | **2501** | **99.2%** |

## 版本历史

| 版本 | 日期 | 更新内容 |
|------|------|---------|
| v2.6.0 | 2026-07-27 | terminal 跨平台支持、ResolveWorkdirPath 路径修复、Windows 多维度测试 |
| v2.5.0 | 2026-07-09 | API 手册独立成文档，新增指令白名单机制 |
| v2.4.0 | 2026-07-08 | 多行命令哨兵模式、日志轮转优化 |
| v2.3.0 | 2026-07-05 | 新增 Inspect/SetAllowedCommands/RemoveAll |
| v2.0.0 | 2026-06-18 | 初始版本，核心引擎 + 30+ 内置指令 |

## 作者

- 作者: Shi Xingyue (史兴跃)
- GitHub: [@joe_sen](https://github.com/joe_sen)
- 联系方式: joe_sen@yeah.net

## 许可证

MIT License - 详见 [LICENSE](./LICENSE)

Copyright (c) 2026 Shi Xingyue (史兴跃)