# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go)](https://go.dev/)
[![Version](https://img.shields.io/badge/version-2.6.0-blue)](https://github.com/sinmofun/atp)

The Universal Language for AI-OS Interaction.

[English Document](./README.md)

---

● 什么是 ATP？

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

**各层说明:**

| 层级 | 作用 | ATP 提供的指令 |
|------|------|----------------|
| **AI 层** | 大模型生成操作指令 | 全部指令 |
| **ATP 引擎层** | 解析、验证、执行指令 | 指令注册、解析、调度 |
| **操作系统层** | 真实执行操作 | terminal, execute, create, read... |
| **硬件/设备层** | 远程设备管理 | ssh, ftp, fetch |

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

● 示例：物联网开关灯

### 控制灯泡

```
# 开灯（所有灯）
light#t1ss012:ON

# 关灯（所有灯）
light#t1ss012:OFF

# 指定某个灯
light#t2ss013:ON
name:living_room
```

### 控制门锁

```
# 锁门（大门）
door#t3ss223:LOCK
name:gate

# 锁门（车库）
door#t4ss224:LOCK
name:garage
```

### 控制空调

```
ac#t6ss301:SET_TEMP
value:26
name:living_room
```

### 查询传感器

```
sensor#t8ss401:TEMPERATURE
name:outdoor
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