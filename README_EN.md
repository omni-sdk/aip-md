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

● How was AIP formed?

AIP was not designed in a vacuum—its birth stems from a simple observation and a long journey of exploration.

**The Starting Point: Rethinking Function Calling**

In AI Agent development, the author discovered fundamental flaws in existing LLM tool-calling solutions—particularly JSON Function Calling. A single unescaped character in AI-generated JSON could crash the entire request. Nested structures, escape hell, and wasted tokens plagued both AI and developers. These pain points sparked the search for a more natural AI-OS interaction paradigm.

**The Exploration: Drawing from Existing Standards**

To find the optimal solution, the author systematically studied various data exchange and configuration formats across the industry, extracting design inspiration:

| Technology | Inspiration Drawn |
|-----------|-----------|
| **JSON / YAML** | Clear structure, but complex escaping and redundant brackets |
| **Protobuf** | Efficient and compact, but AI-unfriendly and requires compilation |
| **INI / TOML** | The simplicity of `key:value`, perfect for single-line parameters |
| **XML / HTML** | The deterministic boundary concept of tag closure |
| **HTTP / RFC2046** | Protocol layering and multi-part boundary identifier design philosophy |
| **JavaScript Template Literals** | The elegance of native multi-line string support |
| **Shell Here Document** | The `<<EOF ... EOF` multi-line content boundary approach |

**The Formation: Distilling LLM Generative Patterns**

Through extensive real-world testing and iteration, the author summarized the core principles of LLM structured instruction generation:

1. **LLMs excel at generating plain text**: Avoid making AI handle escape characters; plain text generation accuracy far exceeds JSON
2. **Boundary markers beat bracket pairing**: Using explicit hash sentries to mark multi-line content boundaries is far more reliable than nested brackets

**Alignment with National Standards**

The design philosophy of this project aligns closely with China's national standard **GB/Z 185-2026 "Artificial Intelligence — Agent Interconnection"** series (particularly Part 7: "Agent Tool Calling"). AIP's core concepts—plain text interaction, multi-agent instruction standardization, and cross-platform unified scheduling—resonate strongly with the standard's objectives.

As an open-source community-driven protocol, AIP serves as a **lightweight, plain-text community implementation reference** for GB/Z 185-2026 in the domain of tool calling and automated operations, offering developers a rapid path from theory to practice.

**Alignment with National Standards**

The design philosophy of this project aligns closely with China's national standard **GB/Z 185-2026 "Artificial Intelligence — Agent Interconnection"** series (particularly Part 7: "Agent Tool Calling"). AIP's core concepts—plain text interaction, multi-agent instruction standardization, and cross-platform unified scheduling—resonate strongly with the standard's objectives.

As an open-source community-driven protocol, AIP serves as a **lightweight, plain-text community implementation reference** for GB/Z 185-2026 in the domain of tool calling and automated operations, offering developers a rapid path from theory to practice.
3. **Single-line beats multi-line**: Simple single-line instruction format achieves extremely high one-shot generation success rates
4. **Transaction tracking is indispensable**: Every instruction needs a unique ID for async callbacks, error tracing, and checkpoint recovery

After dozens of version iterations and refinements, AIP ultimately took its current form: **plain text, single-line priority, hash sentry boundaries, id transaction tracking**. It is not an imaginary construct, but an operating instruction protocol born from real pain points, absorbing the essence of multiple technologies, and purpose-built for LLM generation.

AIP (Agent Interaction Protocol) is an operating instruction protocol designed to provide a unified syntax for AI, humans, and devices. It defines a simple instruction format that allows different ends to interact with operating systems in the same way.

**What scenarios is AIP suitable for?**

```
Scenario: AI operating personal computers
Note: AI generates AIP instructions to create files and execute commands
Example: create#c1:./photos/  →  precise directory creation

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
Example: terminal#t1:echo hello  →  plain text, no JSON escaping needed

Scenario: Remote device management
Note: Manage remote servers via AIP's SSH/FTP instructions
Example: ssh#s1:192.168.0.100 + terminal#t1:systemctl restart nginx
```

---

● AI-Level Comparison

AIP's plain-text design is more friendly for AI generation, fundamentally different from JSON formats.

| Dimension | AIP | JSON Function Calling |
|----------|-----|----------------------|
| **AI Generation** | Direct text output, no escaping | Requires JSON escaping (quotes, newlines, backslashes) |
| **Escape Handling** | Not needed (plain text + hash sentry) | Needs nested quote and special character handling |
| **Token Usage** | Lower: `terminal#t1:echo hello` (28 chars) | Higher: `{"name":"run_cmd","arguments":{"cmd":"echo hello"}}` (96 chars) |
| **Verification** | Built-in id + hash boundaries | Requires external schema validation |
| **Parse Tolerance** | Hash sentry prevents boundary errors | Single unescaped character breaks entire JSON |
| **Readability** | Human readable and writable | Requires understanding JSON structure |
| **Multi-line** | Native hash sentry mode | Requires `\n` escaping or array strings |

**Token usage comparison:**

```
# AIP (28 characters)
terminal#t1:echo hello

# JSON Function Calling (96 characters)
{"tool":"terminal","id":"t1","parameters":{"command":"echo hello"}}
```

**Three-party verification:**

```
Party 1 — AI generates:     terminal#t1:echo hello
Party 2 — AIP Engine:       validates syntax + id uniqueness + hash boundaries
Party 3 — OS/Device:        executes and returns code:0 or error
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
| **AIP** | `terminal#t1:echo hello` | ✅ | ✅ Sentry | ✅ id | ✅ workspace | ✅ Plain Text | ✅ Hotplug |
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
Unique transaction identifier, 4-16 characters, alphanumeric.
Used for traceability, ordering, retry, and multi-instruction isolation.
Each output must have a unique id.
```

### Hash Rules

```
Hash serves as sentry boundary marker, 6-16 random alphanumeric characters.
Each hash must be unique and paired, wrapping multi-line content
to ensure instruction integrity.
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
This is a new project created by AIP.
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
Updated by AIP.
t3

# Append content to file
append#a1:./project/README.md
text@t4:
Appended line by AIP.
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
| Author | Shi XIngyue |
| GitHub | [@sinmofun](https://github.com/sinmofun) |
| Email | joe_sen@yeah.net |
| License | MIT License |

---

● License

MIT License - see [LICENSE](./LICENSE)

Copyright (c) 2026 Shi XIngyue