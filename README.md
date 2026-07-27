# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Universal Language for AI-OS Interaction.

[English Document](./README_EN.md)

---

● 什么是 ATP？

ATP (AI Transfer Protocol) 是一套标准化的操作指令协议。它定义了一套**人、AI、设备三者通用的"普通话"**，让任何一端都能通过统一的语法规则，精确、无歧义地操作操作系统和硬件设备。

**ATP 能快速解决什么问题？**

```
问题: AI 操作你的个人电脑
传统: AI 输出模糊的自然语言 "请在桌面上创建一个名为照片的文件夹"
ATP:  create#c1:./photos/  →  精确、一步到位

问题: 个人日常重复任务自动化
传统: 写复杂的 cron 脚本或批处理文件，难以修改
ATP:  run#r1:./daily_backup.cmd  →  一条命令，重复使用

问题: 开发者快速搭建项目
传统: 手动创建目录结构、写样板代码、安装依赖
ATP:  一条指令文件，一次性完成整个项目脚手架

问题: 运维脚本跨平台统一
传统: Linux 写 bash，Windows 写 bat，语法完全不同
ATP:  同一套指令，Linux/Windows 自动适配

问题: IoT 设备统一控制
传统: 每个厂商定义自己的控制协议，互不兼容
ATP:  标准化指令格式，设备端只需实现协议引擎

问题: 工业机械控制
传统: 私有 PLC 协议，集成昂贵，厂商锁定
ATP:  统一指令层，通过串口/以太网发送简单的开关/调速指令

问题: AI 平台工具调用碎片化
传统: 每个 AI 平台发明自己的 function calling 格式
ATP:  一套指令语法，所有 AI 平台通用

问题: 远程设备管理
传统: SSH 命令因系统版本差异容易出错
ATP:  ssh#s1:192.168.0.100 + terminal#t1:systemctl restart nginx
```

---

● AI 层面的对比

ATP 的纯文本设计针对 AI 生成效率进行了优化，与基于 JSON 的格式有本质区别。

| 维度 | ATP | JSON Function Calling |
|----------|-----|----------------------|
| **AI 生成速度** | 直接文本输出，无需转义 | 需要 JSON 转义（引号、换行、反斜杠） |
| **转义复杂度** | 零 —— 纯文本 + hash 哨兵 | 高 —— 嵌套引号、Unicode 转义、特殊字符 |
| **Token 效率** | 短: `terminal#t1:echo hello` | 长: `{"name":"run_cmd","arguments":{"cmd":"echo hello"}}` |
| **三方校验** | 内置 id + hash 边界 | 需要外部 schema 验证 |
| **解析错误恢复** | Hash 哨兵防止边界错误 | 一个未转义字符破坏整个 JSON |
| **人类可读性** | 直接可读可写 | 需要理解 JSON 结构 |
| **指令长度** | ~30-50 字符（单行） | ~80-150 字符（格式化 JSON） |
| **多行支持** | 原生 hash 哨兵模式 | 需要 `\n` 转义或数组字符串 |

**Token 效率示例:**

```
# ATP (28 字符)
terminal#t1:echo hello

# JSON Function Calling (96 字符)
{"tool":"terminal","id":"t1","parameters":{"command":"echo hello"}}

ATP 每次指令调用节省 70% 的 token 消耗。
```

**三方校验机制:**

```
第一方 — AI 生成:       terminal#t1:echo hello
第二方 — ATP 引擎:      验证语法 + id 唯一性 + hash 边界完整性
第三方 — OS/设备:        执行并返回 code:0 或错误信息
```

---

● ATP 运行在哪个环节？

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

---

● 与市面上各种方案的对比

### 指令格式对比

| 方案 | 语法示例 | 跨平台 | 多行支持 | 事务追踪 | 权限隔离 |
|------|---------|:------:|:--------:|:--------:|:--------:|
| **ATP** | `terminal#t1:echo hello` | ✅ | ✅ 哨兵模式 | ✅ id 追踪 | ✅ workspace + 白名单 |
| Function Calling | `{"name":"run_cmd",...}` | ❌ | ❌ JSON | ❌ | ❌ |
| Shell 脚本 | `#!/bin/bash` | ❌ | ✅ | ❌ | ❌ |
| Ansible | YAML playbook | ✅ | ✅ | ❌ | ❌ |
| MCP | JSON-RPC | ❌ | ❌ | ✅ | ❌ |

### 测试数据对比

| 测试维度 | ATP (Linux) | ATP (Windows) | 传统脚本 |
|----------|:-----------:|:-------------:|:--------:|
| 基础命令 | 100% | 100% | 100% |
| 管道/重定向 | 100% | 83% | 100% |
| 超时控制 | 100% | 100% | 手动实现 |
| 异步执行 | 100% | 100% | 复杂 |
| 事务追踪 | 内置 id | 内置 id | 无 |
| 权限隔离 | workspace | workspace | 无限制 |
| 指令白名单 | 支持 | 支持 | 无 |

---

● ATP 的核心：指令语法规则

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

---

● 示例

### 物联网设备控制

```
# 控制灯泡
light#t1ss012:ON
light#t2ss013:OFF
name:living_room

# 控制门锁
door#t3ss223:LOCK
name:gate
door#t5ss225:UNLOCK
name:gate

# 工业机械控制
conveyor#c1ss501:START
speed:50
conveyor#c2ss502:STOP

robot#r1ss601:MOVE
axis:x
position:120

# 查询传感器
sensor#t8ss401:TEMPERATURE
name:outdoor
```

### 文件 CRUD

```
# 创建文件或目录
create#c1:./project/
create#c2:./project/README.md
text@t2:
# My Project
This is a new project created by ATP.
t2

# 读取文件
read#r1:./project/README.md
encoding:utf8

# 列出目录内容
list#l1:./project/

# 修改文件（完整替换）
update#u1:./project/README.md
text@t3:
# My Project - Updated
Updated by ATP.
t3

# 追加内容到文件末尾
append#a1:./project/README.md
text@t4:
Appended line by ATP.
t4

# 删除文件
delete#d1:./project/README.md

# 删除目录
delete#d2:./project/
```

### 系统指令执行

```
# 查看系统信息
terminal#t1:uname -a
terminal#t2:echo %OS%   (Windows)
terminal#t3:df -h        (Linux 磁盘使用)

# 进程管理
terminal#t4:ps aux | grep nginx
terminal#t5:tasklist | findstr /c:"atp_ws"   (Windows)

# 网络诊断
terminal#t6:ping -c 4 8.8.8.8     (Linux)
terminal#t7:ping -n 4 8.8.8.8     (Windows)

# 定时任务
terminal#t8:echo "0 3 * * * /usr/bin/backup.sh" | crontab -

# 文件压缩
zip#z1:./project
to:./project_backup.zip
format:zip
level:6

# 文件解压
unzip#uz1:./project_backup.zip
to:./restored/
```

### 快速开发

```
# 一条指令文件创建整个项目脚手架
run#r1:./init_project.cmd

# init_project.cmd 内容:
#   create#c1:./src/
#   create#c2:./tests/
#   create#c3:./README.md
#   text@t1:
#   # My Project
#   t1
```

### 远程设备管理

```
# SSH 登录远程服务器
ssh#s1:
host:192.168.0.100
user:admin
pass:password123

# 在远程服务器执行命令
ssh#s1:session_id
cmd:systemctl restart nginx

# FTP 文件传输
ftp#f1:
host:10.0.0.50
user:ftpuser
pass:ftppass123
ftp#f1:session_id
retr:/remote/file.txt
```

### 执行结果

每条指令执行后都会返回统一的结果格式：

```json
{
  "id": "t1ss012",
  "code": 0,
  "text": "success",
  "data": "light turned on"
}
```

---

● 作者

| 项目 | 信息 |
|------|------|
| 作者 | Shi Xingyue (史兴跃) |
| GitHub | [@sinmofun](https://github.com/sinmofun) |
| 邮箱 | joe_sen@yeah.net |
| 许可证 | MIT License |

---

● 许可证

MIT License - 详见 [LICENSE](./LICENSE)

Copyright (c) 2026 Shi Xingyue (史兴跃)