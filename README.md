# ATP - AI Transfer Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Go Version](https://img.shields.io/badge/Go-1.26+-00ADD8?logo=go)](https://go.dev/)
[![Version](https://img.shields.io/badge/version-2.6.0-blue)](https://github.com/sinmofun/atp)

The Universal Language for AI-OS Interaction.

[中文文档](./README_CN.md)

---

● What is ATP?

ATP (AI Transfer Protocol) is a standardized operating instruction protocol. It defines a **universal "common language" for humans, AI, and devices**, enabling any party to precisely and unambiguously operate operating systems and hardware devices through a unified syntax.

**What problems does ATP solve?**

```
Problem: How does an AI model operate your computer?
Legacy: Each AI platform defines its own tool-calling format, incompatible with others
ATP:    One instruction syntax, universally compatible across all AI platforms

Problem: How to unify cross-platform operations?
Legacy: Linux uses bash, Windows uses bat, completely different syntax
ATP:    Same instruction set, automatically adapts to Linux/Windows

Problem: How do IoT devices receive unified commands?
Legacy: Each vendor defines its own control protocol
ATP:    Standardized instruction format, device only needs to implement the protocol engine
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

● IoT Example: Smart Home

### Light Control

```
# Turn on all lights
light#t1ss012:ON

# Turn off all lights
light#t1ss012:OFF

# Control a specific light
light#t2ss013:ON
name:living_room
```

### Door Lock Control

```
# Lock the gate
door#t3ss223:LOCK
name:gate

# Lock the garage
door#t4ss224:LOCK
name:garage

# Unlock
door#t5ss225:UNLOCK
name:gate
```

### Temperature Sensor

```
sensor#t8ss401:TEMPERATURE
name:outdoor
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