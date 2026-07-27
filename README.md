# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Universal Language for AI-OS Interaction.

[English Document](./README_EN.md)

---

你只需要几分钟就学会让 AI 生成指令来操作系统、控制设备。

ATP 适用于 AI Agent 开发、LLM 工具调用、AI 工作流编排、跨平台自动化操作、IoT 设备指令控制、远程服务器管理、教学场景等。

直接使用提示词: 将 [PROMPT.md](./PROMPT.md) 的内容复制到大模型的系统提示中，AI 即可学会生成 ATP 指令。

经过 2131 个测试用例验证，详见 [TEST_REPORT.md](./TEST_REPORT.md)。

▶ 场景速览: [文件操作](./scenes/scene-file-crud.md) · [物联网控制](./scenes/scene-iot-control.md) · [系统指令](./scenes/scene-system-command.md) · [远程管理](./scenes/scene-remote-management.md) · [AI 工具调用](./scenes/scene-ai-tool-calling.md) · [代码运行](./scenes/scene-code-run.md) · [数据库](./scenes/scene-database.md) · [Docker](./scenes/scene-docker.md) · [Git](./scenes/scene-git.md) · [网络诊断](./scenes/scene-network.md) · [定时备份](./scenes/scene-cron-backup.md) · [系统监控](./scenes/scene-monitor.md) · [智能家居](./scenes/scene-smart-home.md) · [DevOps](./scenes/scene-devops.md) · [错误处理](./scenes/scene-error-handling.md) · [教学](./scenes/scene-teaching.md) · [更多...](./scenes/)

▶ 角色示例: [系统管理员](./roles/role-system-admin.md) · [DevOps](./roles/role-devops.md) · [数据科学家](./roles/role-data-scientist.md) · [家庭自动化](./roles/role-home-automation.md) · [物联网开发](./roles/role-iot-developer.md) · [后端开发](./roles/role-backend-dev.md) · [前端开发](./roles/role-frontend-dev.md) · [安全工程师](./roles/role-security-engineer.md) · [更多...](./roles/)

▶ 常见问题: [ATP 是什么？](./questions/question-what-is-atp.md) · [为什么不用 JSON？](./questions/question-why-not-json.md) · [如何开始使用？](./questions/question-how-to-use.md) · [如何跨平台？](./questions/question-cross-platform.md) · [如何保证安全？](./questions/question-security.md) · [与其他方案对比](./questions/question-vs-other.md) · [如何扩展？](./questions/question-extend.md) · [实际用途？](./questions/question-practical.md) · [更多...](./questions/)

---

● 什么是 ATP？

ATP (AI Transfer Protocol) 是一套操作指令协议，旨在为 AI、人和设备提供一套统一的操作语法。它定义了一套简洁的指令格式，让不同端之间可以通过相同的方式与操作系统交互。

**ATP 适合哪些场景？**

```
场景: AI 操作个人电脑
说明: AI 通过生成 ATP 指令来创建文件、执行命令，替代模糊的自然语言描述
示例: create#c1:./photos/  →  精确创建目录

场景: 个人日常重复任务
说明: 将一系列操作写成 ATP 指令文件，可重复执行
示例: run#r1:./daily_backup.cmd  →  一条命令完成批量操作

场景: 开发者项目初始化
说明: 用 ATP 指令文件定义项目脚手架，替代手动创建目录和文件
示例: 一条指令文件即可创建完整的目录结构和初始文件

场景: 跨平台操作
说明: ATP 的指令格式是统一的，底层根据平台自动选择 Linux PTY 或 Windows BAT 执行
注意: 指令格式统一，但执行的命令语法需根据平台编写

场景: IoT 设备控制
说明: 设备端实现 ATP 引擎后，可通过统一指令格式控制
示例: light#t1:ON  →  开灯

场景: 工业机械控制
说明: 在串口或以太网之上使用 ATP 指令层，替代私有 PLC 协议
示例: conveyor#c1:START speed:50

场景: AI 工具调用
说明: 为大模型提供统一的指令生成格式，替代各家自定义的工具调用方案
示例: terminal#t1:echo hello  →  纯文本，无需 JSON 转义

场景: 远程设备管理
说明: 通过 ATP 的 SSH/FTP 指令管理远程服务器
示例: ssh#s1:192.168.0.100 + terminal#t1:systemctl restart nginx
```

---

● AI 层面的对比

ATP 的纯文本设计对 AI 生成更友好，与 JSON 格式有本质区别。

| 维度 | ATP | JSON Function Calling |
|----------|-----|----------------------|
| **AI 生成方式** | 直接文本输出，无需转义 | 需要 JSON 转义（引号、换行、反斜杠） |
| **转义处理** | 不需要（纯文本 + hash 哨兵） | 需要处理嵌套引号和特殊字符 |
| **Token 消耗** | 较少: `terminal#t1:echo hello` (28 字符) | 较多: `{"name":"run_cmd","arguments":{"cmd":"echo hello"}}` (96 字符) |
| **三方校验** | 内置 id + hash 边界 | 需要外部 schema 验证 |
| **解析容错** | Hash 哨兵防止边界错乱 | 一个未转义字符破坏整个 JSON |
| **可读性** | 人类可直接读写 | 需要理解 JSON 结构 |
| **多行支持** | 原生 hash 哨兵模式 | 需要 `\n` 转义或数组字符串 |

**Token 消耗对比示例:**

```
# ATP (28 字符)
terminal#t1:echo hello

# JSON Function Calling (96 字符)
{"tool":"terminal","id":"t1","parameters":{"command":"echo hello"}}
```

**三方校验:**

```
第一方 — AI 生成:       terminal#t1:echo hello
第二方 — ATP 引擎:      验证语法 + id 唯一性 + hash 边界
第三方 — OS/设备:        执行并返回 code:0 或错误信息
```

---

● ATP 运行在哪个环节？

ATP 位于 AI 与操作系统/硬件之间的中间协议层。

```
┌─────────────────────────────────────────────┐
│  AI 层                                       │
│  生成 ATP 指令文本                           │
└──────────────────┬──────────────────────────┘
                   │ WebSocket / HTTP / 标准输入
┌──────────────────▼──────────────────────────┐
│  ATP 引擎层                                   │
│  指令解析、注册、执行调度                     │
│  跨平台: Linux PTY / Windows BAT             │
└──────────────────┬──────────────────────────┘
                   │ 系统调用
┌──────────────────▼──────────────────────────┐
│  操作系统层                                   │
│  Linux / Windows / macOS (计划中)            │
│  文件系统、进程管理、网络请求                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  硬件/设备层                                  │
│  IoT 设备、数据库、远程服务器                 │
└─────────────────────────────────────────────┘
```

---

● 与市面上各种方案的对比

| 方案 | 语法 | 跨平台 | 多行 | 事务追踪 | 权限隔离 | AI 友好 | 扩展性 |
|------|------|:------:|:----:|:--------:|:--------:|:-------:|:------:|
| **ATP** | `terminal#t1:echo hello` | ✅ | ✅ 哨兵 | ✅ id | ✅ workspace | ✅ 纯文本 | ✅ 热插拔 |
| Function Calling | JSON 嵌套调用 | ❌ | ❌ | ❌ | ❌ | ❌ JSON 转义 | ❌ |
| Shell 脚本 | bash / bat 语法 | ❌ | ✅ | ❌ | ❌ | ❌ 语法复杂 | ❌ |
| Ansible | YAML playbook | ✅ | ✅ | ❌ | ❌ | ❌ YAML 繁琐 | ✅ |
| MCP | JSON-RPC | ❌ | ❌ | ✅ | ❌ | ❌ JSON 转义 | ✅ |
| REST API | HTTP + JSON | ❌ | ❌ | ❌ | ❌ | ❌ 需独立定义 | ❌ |
| gRPC | Protobuf | ❌ | ❌ | ❌ | ❌ | ❌ 编译依赖 | ❌ |

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
且完整包裹多行参数或文本，确保指令完整性。
每组的 hash 必须保持唯一性且成对出现。
```

---

● 作者

| 项目 | 信息 |
|------|------|
| 作者 | Shi XIngyue |
| GitHub | [@sinmofun](https://github.com/sinmofun) |
| 邮箱 | joe_sen@yeah.net |
| 许可证 | MIT License |

---

● 许可证

MIT License - 详见 [LICENSE](./LICENSE)

Copyright (c) 2026 Shi XIngyue