# ATP 与其他方案有什么不同？

## 问题

ATP 与 Function Calling、MCP、Ansible 等方案有什么区别？

## 解答

| 方案 | AI 友好度 | 跨平台 | 事务追踪 | 权限隔离 |
|------|:--------:|:------:|:--------:|:--------:|
| **ATP** | ✅ 纯文本 | ✅ | ✅ id | ✅ workspace |
| Function Calling | ❌ JSON 转义 | ❌ | ❌ | ❌ |
| MCP | ❌ JSON-RPC | ❌ | ✅ | ❌ |
| Ansible | ❌ YAML 繁琐 | ✅ | ❌ | ❌ |

ATP 的核心优势在于对 AI 生成友好，纯文本格式不需要处理 JSON 转义，Token 消耗更低。