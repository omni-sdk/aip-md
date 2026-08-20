# AIP - Agent Interaction Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Universal Language for AI-OS Interaction.

[中文文档](./README.md)

---

It only takes a few minutes to learn how to let AI generate instructions to operate systems and control devices.

AIP is designed for AI Agent development, LLM tool calling, AI workflow orchestration, cross-platform automation, IoT device command control, remote server management, teaching scenarios, and more.

Prompt Guide: Copy the content of [PROMPT.md](./PROMPT.md) into your LLM's system prompt, and the AI will learn to generate AIP instructions.

Verified by 2131 test cases, see [TEST_REPORT.md](./TEST_REPORT.md).

---

● What is AIP?

AIP (Agent Interaction Protocol) is an operating instruction protocol designed to provide a unified syntax for AI, humans, and devices. It defines a simple instruction format that allows different ends to interact with operating systems in the same way.

**What scenarios is AIP suitable for?**

```
Scenario: AI operating personal computers
Note: AI generates AIP instructions to create files and execute commands
Example: make#c1:./photos/  →  precise directory creation

Scenario: Automating personal repetitive tasks
Note: Write a series of operations as AIP instruction files for repeatable execution
Example: run#r1:./daily_backup.cmd  →  one command for batch operations

Scenario: Developer project initialization
Note: Use AIP instruction files to define project scaffolding
Example: One instruction file creates the complete directory structure

Scenario: Cross-platform operations
Note: AIP instruction format is unified, platform automatically selects Linux PTY or Windows BAT
Note: Command syntax must be written according to the platform

Scenario: IoT device control
Note: After implementing the AIP engine on the device, control via unified instruction format
Example: light#t1:ON  →  turn on light

Scenario: Industrial machinery control
Note: Use AIP instruction layer over serial/ethernet instead of proprietary PLC protocols
Example: conveyor#c1:START speed:50

Scenario: AI tool calling
Note: Provide a unified instruction generation format for large models
Example: execute#t1:echo hi  →  plain text, no JSON escaping needed

Scenario: Remote device management
Note: Manage remote servers via AIP's SSH/FTP instructions
Example: ssh#s1:192.168.0.100 + execute#t1:systemctl restart nginx
```

---

● AI-Level Comparison

AIP's plain-text design is more friendly for AI generation, fundamentally different from JSON formats.

| Dimension | AIP | JSON Function Calling |
|----------|-----|----------------------|
| **AI Generation** | Direct text output, no escaping | Requires JSON escaping (quotes, newlines, backslashes) |
| **Escape Handling** | Not needed (plain text + hash sentry) | Needs nested quote and special character handling |
| **Token Usage** | Lower: `execute#t1:echo hi` (24 chars) | Higher: `{"name":"run_cmd","arguments":{"cmd":"echo hi"}}` (96 chars) |
| **Verification** | Built-in id + hash boundaries | Requires external schema validation |
| **Parse Tolerance** | Hash sentry prevents boundary errors | Single unescaped character breaks entire JSON |
| **Readability** | Human readable and writable | Requires understanding JSON structure |
| **Multi-line** | Native hash sentry mode | Requires `\n` escaping or array strings |

**Token usage comparison:**

```
# AIP (24 characters)
execute#t1:echo hi

# JSON Function Calling (96 characters)
{"tool":"execute","id":"t1","parameters":{"command":"echo hi"}}
```

**Three-party verification:**

```
Party 1 — AI generates:     execute#t1:echo hi
Party 2 — AIP Engine:       validates syntax + id uniqueness + hash boundaries
Party 3 — OS/Device:        executes and returns code:20 or error
```

---

● Where does AIP run?

AIP sits in the middleware protocol layer between AI and OS/hardware.

```
┌─────────────────────────────────────────────┐
│  AI Layer                                    │
│  Generates AIP instruction text              │
└──────────────────┬──────────────────────────┘
                   │ WebSocket / HTTP / Stdio
┌──────────────────▼──────────────────────────┐
│  AIP Engine Layer                            │
│  Instruction parsing, registry, scheduling   │
│  Cross-platform: Linux PTY / Windows BAT     │
└──────────────────┬──────────────────────────┘
                   │ System Calls
┌──────────────────▼──────────────────────────┐
│  OS Layer                                    │
│  Linux / Windows / macOS (planned)           │
│  File I/O, Process, Network                  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  Hardware/Device Layer                       │
│  IoT Devices, Database, Remote Servers       │
└─────────────────────────────────────────────┘
```

---

● Comparison with existing solutions

| Solution | Syntax | Cross-Platform | Multi-line | Tx Tracking | Permission Isolation | AI Friendly | Extensible |
|------|------|:------:|:----:|:--------:|:--------:|:-------:|:------:|
| **AIP** | `execute#t1:echo hi` | ✅ | ✅ Sentry | ✅ id | ✅ workspace | ✅ Plain Text | ✅ Hotplug |
| Function Calling | Nested JSON | ❌ | ❌ | ❌ | ❌ | ❌ JSON Escape | ❌ |
| Shell Scripts | bash/bat syntax | ❌ | ✅ | ❌ | ❌ | ❌ Complex | ❌ |
| Ansible | YAML playbook | ✅ | ✅ | ❌ | ❌ | ❌ YAML Verbose | ✅ |
| MCP | JSON-RPC | ❌ | ❌ | ✅ | ❌ | ❌ JSON Escape | ✅ |
| REST API | HTTP + JSON | ❌ | ❌ | ❌ | ❌ | ❌ Custom | ❌ |
| gRPC | Protobuf | ❌ | ❌ | ❌ | ❌ | ❌ Compile | ❌ |

---

● Core: Instruction Syntax Rules

### Instruction Format

```
namespace.command#id:main_param         ← Recommended (namespace.command)
command#id:main_param                   ← Compatible (no namespace)
command#id@hash:                        ← Multi-line main param (sentry start)
multi-line content
hash                                    ← Sentry end
key:value                               ← Single-line param
key@hash2:
multi-line content
hash2
```

### ID Rules

```
Unique transaction identifier, 4-32 characters, consisting of letters, digits, - and _.
Used for traceability, ordering, retry, and multi-instruction isolation.
Each output must have a unique id.
```

### Hash Rules

```
Hash serves as sentry boundary marker, 6-32 random characters (letters, digits, - and _).
Each hash must be unique and paired, wrapping multi-line content
to ensure instruction integrity.
```

---

● Instruction List

| Command | Description |
|------|------|
| make | Create file or directory, with optional content |
| write | Overwrite file content, supports line range |
| delete | Delete file or directory (recycled to .trash) |
| read | Read file content, supports line/char ranges |
| list | List directory contents |
| tree | Show directory tree |
| rename | Rename file or directory |
| move | Move file or directory |
| copy | Copy file or directory |
| append | Append content to end of file |
| stat | View file metadata |
| find | Recursively search for files |
| replace | Replace file content, supports recursive and line range |
| insert | Insert content at specified position |
| length | Calculate length of sub-command result |
| regex | Regular expression search |
| uname | Show current system info |
| ftp | FTP remote file management |
| ssh | SSH remote management |
| pipe | Save sub-command results to file |
| zip | Compress file or directory |
| unzip | Extract file |
| execute | Execute command (cross-platform) |
| terminal | Terminal execution (execute fallback) |
| daemon | Background process management |
| chmod | Set file permissions |
| chown | Set file ownership |
| sys_power | System power (lock, sleep, shutdown, reboot) |
| knowledge | Knowledge base management |
| task | Task management |
| when | Conditional trigger execution |
| fetch | Access network APIs, web pages, download files |
| run | Run AIP instruction file |
| help | Get help document |
| version | Get AIP version |

---

● Examples

### File Creation and Reading

```
make#c1:./project/
make#c2:./project/README.md
text@t2:
# My Project
This is a new project created by AIP.
t2
read#r1:./project/README.md
```

### Executing System Commands

```
execute#t1:echo hello
execute#t2:go build -o app
at:./demo
terminal#t3:echo world
```

### Remote Management

```
ssh#s1:
host:192.168.0.100
port:22
user:admin
pass:password123
ssh#s1:session_id
cmd:systemctl restart nginx
ftp#f1:
host:10.0.0.50
user:ftpuser
pass:ftppass123
```

### Conditional Trigger

```
when#w1:make#c1:./temp/
if:[c1.code]==20
then@t1:
stat#s1:./temp/
t1
```

### Network Request

```
fetch#f1:https://api.example.com/data
mode:links
fetch#f2:https://api.example.com/data
method:post
payload:{"name":"test"}
```

---

● Extended Tools

AIP ecosystem includes independently maintained Go tools for extended capabilities. See [AIP Tools](../aip-tools/README.md) for local tools such as browser automation, crypto data, weather, news, paper search, wiki, etc. External tools are indexed in [AIP Tools Extend](../aip-tools/README-extend.md), including dbkit, mailkit, mqtt-kit, office-kit, serial-kit, syskit, tcp-scan, and more.

---

● Author

| Item | Info |
|------|------|
| Author | Shi XIngyue |
| GitHub | [@sinmofun](https://github.com/sinmofun) |
| Email | joe_sen@yeah.net |
| License | MIT License |

---

● License

MIT License - see [LICENSE](./LICENSE)

Copyright (c) 2026 Shi XIngyue