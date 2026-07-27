# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go)](https://go.dev/)
[![Version](https://img.shields.io/badge/version-2.6.0-blue)](https://github.com/sinmofun/atp)

The Universal Language for AI-OS Interaction.

---

## 一、什么是 ATP？

ATP (AI Transfer Protocol) 是一套标准化的操作指令协议。它定义了一套**人、AI、设备三者通用的"普通话"**，让任何一端都能通过统一的语法规则，精确、无歧义地操作操作系统和硬件设备。

**ATP 能快速解决什么问题？**

```
问题: AI 大模型如何操作你的电脑？
传统: 每个 AI 平台定义自己的工具调用格式，互不兼容
ATP:  一套指令语法，所有 AI 平台通用

问题: 运维脚本如何跨平台统一？
传统: Linux 写 bash，Windows 写 bat，语法完全不同
ATP:  同一套指令，Linux/Windows 自动适配

问题: IoT 设备如何接收统一指令？
传统: 每个厂商定义自己的控制协议
ATP:  标准化的指令格式，设备端只需实现协议引擎
```

---

## 二、ATP 运行在哪个环节？

ATP 是连接 **AI 大脑** 与 **操作系统/硬件** 之间的中间协议层。

```
┌─────────────────────────────────────────────┐
│  AI 层                                       │
│  (ChatGPT, Claude, 本地大模型, Agent...)     │
│                                               │
│  生成 ATP 指令文本  →  terminal#t1:echo hello │
└──────────────────┬──────────────────────────┘
                   │ WebSocket / HTTP / 标准输入
┌──────────────────▼──────────────────────────┐
│  ATP 引擎层                                   │
│                                               │
│  ┌─────────┐  ┌──────────┐  ┌─────────────┐ │
│  │ 指令解析 │  │ 指令注册 │  │ 执行调度    │ │
│  │ (语法树) │  │ (热插拔) │  │ (同步/异步) │ │
│  └─────────┘  └──────────┘  └─────────────┘ │
│                                               │
│  跨平台适配: Linux PTY / Windows BAT / ...   │
└──────────────────┬──────────────────────────┘
                   │ 系统调用
┌──────────────────▼──────────────────────────┐
│  操作系统层                                   │
│                                               │
│  Linux      Windows      macOS (计划中)       │
│  文件系统   进程管理     网络请求              │
│  终端命令   权限控制     压缩解压              │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  硬件/设备层                                  │
│                                               │
│  IoT 设备    数据库      远程服务器            │
│  (通过 SSH/FTP/WebSocket 远程管理)            │
└─────────────────────────────────────────────┘
```

**各层说明:**

| 层级 | 作用 | ATP 提供的指令 |
|------|------|----------------|
| **AI 层** | 大模型生成操作指令 | 全部指令 |
| **ATP 引擎层** | 解析、验证、执行指令 | 指令注册、解析、调度 |
| **操作系统层** | 真实执行操作 | terminal, execute, create, read... |
| **硬件/设备层** | 远程设备管理 | ssh, ftp, fetch |

---

## 三、与市面上各种方案的对比

### 3.1 指令格式对比

| 方案 | 语法示例 | 跨平台 | 多行支持 | 事务追踪 | 权限隔离 | 安全隔离 |
|------|---------|:------:|:--------:|:--------:|:--------:|:--------:|
| **ATP** | `terminal#t1:echo hello` | ✅ | ✅ 哨兵模式 | ✅ id 追踪 | ✅ workspace | ✅ 白名单 |
| Function Calling | `{"name":"run_cmd","args":{...}}` | ❌ | ❌ JSON | ❌ | ❌ | ❌ |
| Shell 脚本 | `#!/bin/bash` | ❌ | ✅ | ❌ | ❌ | ❌ |
| Ansible | YAML playbook | ✅ | ✅ | ❌ | ❌ | ❌ |
| MCP (Model Context Protocol) | JSON-RPC | ❌ | ❌ | ✅ | ❌ | ❌ |

**权限隔离说明:**
- **workspace 隔离**: ATP 的所有文件操作指令（create、read、delete、list 等）严格限定在配置的 `workspace` 目录内，无法越权访问系统其他路径
- **白名单机制**: 通过 `SetAllowedCommands` 可以精确控制 AI 只能执行哪些指令，例如只允许文件读取，禁止执行系统命令
- **执行隔离**: `execute` 和 `terminal` 指令的工作目录基于 `workspace` 配置，无法随意切换目录

### 3.2 测试数据对比

| 测试维度 | ATP (Linux) | ATP (Windows) | 传统脚本 | Function Calling |
|----------|:-----------:|:-------------:|:--------:|:----------------:|
| 基础命令 | 100% | 100% | 100% | 依赖平台 |
| 管道/重定向 | 100% | 83% | 100% | 不支持 |
| 超时控制 | 100% | 100% | 手动实现 | 手动实现 |
| 异步执行 | 100% | 100% | 复杂 | 不支持 |
| 交互式命令 | 支持(PTY) | 不支持 | 支持 | 不支持 |
| 进程树清理 | 100% | 100% | 需手动 | 无保证 |
| 事务追踪 | 内置 id | 内置 id | 无 | 无 |
| 指令组合 | when/then/else | when/then/else | 需脚本 | 不支持 |
| 权限隔离 | workspace | workspace | 无限制 | 无限制 |
| 指令白名单 | 支持 | 支持 | 无 | 无 |

### 3.3 ATP 的核心优势

1. **真正的跨平台**: 同一指令在 Linux 和 Windows 下行为一致，自动适配底层实现
2. **事务级追踪**: 每条指令都有唯一 id，支持断点重试、结果关联
3. **哨兵模式**: hash 边界保护多行内容，防止截断和注入
4. **工作区隔离**: 所有文件操作基于 workspace 配置，防止越权
5. **指令白名单**: 精确控制 AI 的可执行指令范围
6. **指令热插拔**: 通过 `init()` 自动注册，新增指令零配置

---

## 四、ATP 的核心：指令语法规则

ATP 的精髓在于定义了**一套精确、无歧义的指令描述语言**。

### 指令规则

```
namespace.command#id:主参数          ← 推荐格式（命名空间.指令名）
command#id:主参数                    ← 兼容格式（无命名空间）
command#id@hash:                    ← 主参数多行（哨兵块开始）
多行主参数内容
hash                                 ← 哨兵块结束
单行参数:参数值
多行参数@hash2:
任意多行内容
hash2
```

### id 规则

```
事务唯一编号，长度 4~16 位，由字母、数字组合而成。
用于事务溯源、任务排序、断点重试、多指令隔离。
每次输出的 id 必须保持唯一性。
```

### hash 规则

```
hash 值作为哨兵内容边界标识，长度 6~16 位，由随机字母+数字组合。
每组 hash 值与其他范围 hash 保持完全不重复，
且完整包裹多行参数或文本，确保指令完整性，
防止截断、篡改、边界错乱。
每组的 hash 必须保持唯一性且成对出现。
```

### 为什么这样设计？

```
传统方式:
  "把文件 a.txt 的内容改为 hello world"
  → AI 输出: 用 sed 命令替换... (不精确，依赖 Shell 环境)

ATP 方式:
  update#u1:./a.txt
  text@abc123:
  hello world
  abc123
  
  → AI 输出精确指令，引擎验证 hash 边界后执行，无歧义
```

---

## 五、示例：物联网开关灯

假设你有一个智能灯泡，通过 ATP 引擎连接到网络。

### 场景：用一条指令开灯

```
terminal#light1:echo ON > /dev/smart_light
```

### 场景：用指令组合实现定时关灯

```
when#w1:create#c1:./light_timer.txt
text@t1:
OFF
t1
if:[c1.code]==0
then@then1:
terminal#t2:echo OFF > /dev/smart_light
then1
```

### 场景：AI 自动判断并控制

```
AI 收到用户请求: "帮我打开客厅的灯"
AI 生成 ATP 指令:
  terminal#ai_living_room:echo ON > /dev/living_room_light

ATP 引擎执行 → 灯亮
AI 收到结果: code:0, text:"success"
AI 回复用户: "客厅灯已打开"
```

### 同样的指令，操作不同的设备

```
# 控制灯泡
terminal#t1:echo ON > /dev/light

# 控制空调
terminal#t2:echo 26 > /dev/ac/temperature

# 控制门锁
terminal#t3:echo LOCK > /dev/door

# 查询温度传感器
read#r1:/dev/temperature_sensor
```

---

## 六、快速开始

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

```
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

---

## 七、作者

| 项目 | 信息 |
|------|------|
| 作者 | Shi Xingyue (史兴跃) |
| GitHub | [@joe_sen](https://github.com/joe_sen) |
| 邮箱 | joe_sen@yeah.net |
| 许可证 | MIT License |

---

## 八、许可证

MIT License - 详见 [LICENSE](./LICENSE)

Copyright (c) 2026 Shi Xingyue (史兴跃)