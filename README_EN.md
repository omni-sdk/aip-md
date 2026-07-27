# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The Universal Language for AI-OS Interaction.

[中文文档](./README.md)

---

● What is ATP?

ATP (AI Transfer Protocol) is a standardized operating instruction protocol. It defines a **universal "common language" for humans, AI, and devices**, enabling any party to precisely and unambiguously operate operating systems and hardware devices through a unified syntax.

**What problems does ATP solve?**

```
Problem: AI operating your personal computer
Legacy: AI outputs vague natural language "please create a folder named photos"
ATP:    create#c1:./photos/  →  precise, single-step execution

Problem: Automating repetitive personal tasks
Legacy: Write complex cron jobs or batch scripts, hard to modify
ATP:    run#r1:./daily_backup.cmd  →  one command, reusable

Problem: Rapid prototyping for developers
Legacy: Set up project structure, write boilerplate, install dependencies manually
ATP:    A single instruction file creates the entire scaffold in one shot

Problem: Cross-platform ops scripting
Legacy: Linux uses bash, Windows uses bat, completely different syntax
ATP:    Same instruction set, automatically adapts to Linux/Windows

Problem: IoT & device control
Legacy: Each vendor defines its own control protocol, no interoperability
ATP:    Standardized format, device only needs the protocol engine

Problem: Industrial machinery control
Legacy: Proprietary PLC protocols, expensive integration, vendor lock-in
ATP:    Unified instruction layer over serial/ethernet, simple on/off/speed commands

Problem: AI model tool-calling fragmentation
Legacy: Each AI platform invents its own function-calling format
ATP:    One instruction syntax, universally compatible across all AI platforms

Problem: Remote device management
Legacy: SSH commands differ across OS versions, error-prone
ATP:    ssh#s1:192.168.0.100 + terminal#t1:systemctl restart nginx
```

---

● AI-Level Comparison

ATP's plain-text design is optimized for AI generation efficiency, unlike JSON-based formats.

| Dimension | ATP | JSON Function Calling |
|----------|-----|----------------------|
| **AI Generation Speed** | Direct text output, no escaping | Requires JSON escaping (quotes, newlines, backslashes) |
| **Escape Complexity** | Zero — plain text with hash sentries | High — nested quotes, Unicode escapes, special chars |
| **Token Efficiency** | Short: `terminal#t1:echo hello` | Long: `{"name":"run_cmd","arguments":{"cmd":"echo hello"}}` |
| **Three-Party Verification** | Built-in id + hash boundaries | Requires external schema validation |
| **Parse Error Recovery** | Hash sentry prevents boundary errors | Single unescaped character breaks entire JSON |
| **Human Readability** | Directly readable and writable | Requires understanding JSON structure |
| **Instruction Length** | ~30-50 chars (single-line) | ~80-150 chars (formatted JSON) |
| **Multi-line Support** | Native hash sentry mode | Requires `\n` escaping or array strings |

**Token Efficiency Example:**

```
# ATP (28 chars)
terminal#t1:echo hello

# JSON Function Calling (96 chars)
{"tool":"terminal","id":"t1","parameters":{"command":"echo hello"}}

ATP saves 70% tokens per instruction call.
```

**Three-Party Verification:**

```
Party 1 — AI generates:     terminal#t1:echo hello
Party 2 — ATP Engine:       validates syntax + id uniqueness + hash boundaries
Party 3 — OS/Device:        executes and returns code:0 or error
```

---

● Where does ATP run?

ATP is the **middleware protocol layer** connecting the **AI brain** with the **OS/hardware**.

```
┌─────────────────────────────────────────────┐
│  AI Layer                                    │
│  (ChatGPT, Claude, Local LLM, Agents...)     │
│                                               │
│  Generates ATP instructions                  │
└──────────────────┬──────────────────────────┘
                   │ WebSocket / HTTP / Stdio
┌──────────────────▼──────────────────────────┐
│  ATP Engine Layer                            │
│                                               │
│  ┌──────────┐  ┌──────────┐  ┌───────────┐  │
│  │ Parser   │  │ Registry │  │ Scheduler │  │
│  │ (Syntax) │  │ (Hotplug)│  │ (Sync/Async)│ │
│  └──────────┘  └──────────┘  └───────────┘  │
│                                               │
│  Cross-platform: Linux PTY / Windows BAT     │
└──────────────────┬──────────────────────────┘
                   │ System Calls
┌──────────────────▼──────────────────────────┐
│  OS Layer                                    │
│                                               │
│  Linux      Windows      macOS (planned)     │
│  File I/O   Process      Network             │
│  Terminal   Permission   Archive             │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│  Hardware/Device Layer                       │
│                                               │
│  IoT Devices    Database    Remote Servers   │
│  (Managed via SSH/FTP/WebSocket)             │
└─────────────────────────────────────────────┘
```

---

● Comparison with existing solutions

### Instruction Format Comparison

| Solution | Syntax | Cross-Platform | Multi-line | Tx Tracking | Permission Isolation |
|------|---------|:------:|:--------:|:--------:|:--------:|
| **ATP** | `terminal#t1:echo hello` | ✅ | ✅ Sentry | ✅ id | ✅ workspace + whitelist |
| Function Calling | `{"name":"run_cmd",...}` | ❌ | ❌ JSON | ❌ | ❌ |
| Shell Scripts | `#!/bin/bash` | ❌ | ✅ | ❌ | ❌ |
| Ansible | YAML playbook | ✅ | ✅ | ❌ | ❌ |
| MCP | JSON-RPC | ❌ | ❌ | ✅ | ❌ |

### Test Data Comparison

| Dimension | ATP (Linux) | ATP (Windows) | Shell Scripts |
|----------|:-----------:|:-------------:|:--------:|
| Basic Commands | 100% | 100% | 100% |
| Pipes/Redirects | 100% | 83% | 100% |
| Timeout Control | 100% | 100% | Manual |
| Async Execution | 100% | 100% | Complex |
| Transaction Tracking | Built-in id | Built-in id | None |
| Permission Isolation | workspace | workspace | Unrestricted |
| Command Whitelist | Supported | Supported | None |

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
Unique transaction identifier, 4-16 characters, alphanumeric.
Used for traceability, ordering, retry, and multi-instruction isolation.
Each output must have a unique id.
```

### Hash Rules

```
Hash serves as sentry boundary marker, 6-16 random alphanumeric characters.
Each hash must be unique and paired, wrapping multi-line content
to ensure instruction integrity, preventing truncation, tampering, and boundary errors.
```

---

● Examples

### IoT Device Control

```
# Light control
light#t1ss012:ON
light#t2ss013:OFF
name:living_room

# Door lock control
door#t3ss223:LOCK
name:gate
door#t5ss225:UNLOCK
name:gate

# Industrial machinery
conveyor#c1ss501:START
speed:50
conveyor#c2ss502:STOP

robot#r1ss601:MOVE
axis:x
position:120

# Temperature sensor
sensor#t8ss401:TEMPERATURE
name:outdoor
```

### File CRUD

```
# Create file or directory
create#c1:./project/
create#c2:./project/README.md
text@t2:
# My Project
This is a new project created by ATP.
t2

# Read file
read#r1:./project/README.md
encoding:utf8

# List directory
list#l1:./project/

# Update file (full replacement)
update#u1:./project/README.md
text@t3:
# My Project - Updated
Updated by ATP.
t3

# Append content to file
append#a1:./project/README.md
text@t4:
Appended line by ATP.
t4

# Delete file
delete#d1:./project/README.md

# Delete directory
delete#d2:./project/
```

### System Command Execution

```
# System info
terminal#t1:uname -a
terminal#t2:echo %OS%   (Windows)
terminal#t3:df -h        (Linux disk usage)

# Process management
terminal#t4:ps aux | grep nginx
terminal#t5:tasklist | findstr /c:"atp_ws"   (Windows)

# Network diagnostic
terminal#t6:ping -c 4 8.8.8.8     (Linux)
terminal#t7:ping -n 4 8.8.8.8     (Windows)

# Cron job
terminal#t8:echo "0 3 * * * /usr/bin/backup.sh" | crontab -

# File compression
zip#z1:./project
to:./project_backup.zip
format:zip
level:6

# File extraction
unzip#uz1:./project_backup.zip
to:./restored/
```

### Rapid Development

```
# Create entire project scaffold with one instruction file
run#r1:./init_project.cmd

# Inside init_project.cmd:
#   create#c1:./src/
#   create#c2:./tests/
#   create#c3:./README.md
#   text@t1:
#   # My Project
#   t1
```

### Remote Device Management

```
# SSH login
ssh#s1:
host:192.168.0.100
user:admin
pass:password123

# Execute remote command
ssh#s1:session_id
cmd:systemctl restart nginx

# FTP file transfer
ftp#f1:
host:10.0.0.50
user:ftpuser
pass:ftppass123
ftp#f1:session_id
retr:/remote/file.txt
```

### Execution Result

Each instruction returns a unified result format:

```json
{
  "id": "t1ss012",
  "code": 0,
  "text": "success",
  "data": "light turned on"
}
```

---

● Author

| Item | Info |
|------|------|
| Author | Shi Xingyue (史兴跃) |
| GitHub | [@sinmofun](https://github.com/sinmofun) |
| Email | joe_sen@yeah.net |
| License | MIT License |

---

● License

MIT License - see [LICENSE](./LICENSE)

Copyright (c) 2026 Shi Xingyue (史兴跃)