# 为什么不用 JSON？

## 问题

为什么 AITP 使用自定义的纯文本格式，而不是 JSON？

## 解答

JSON 需要在嵌套引号、换行符、反斜杠等方面进行复杂的转义处理。AI 生成 JSON 时，一个未转义的字符就会导致整个 JSON 解析失败。

AITP 的纯文本格式对 AI 生成更友好：
- 不需要处理 JSON 转义
- Token 消耗更低（约 70% 的节省）
- 人类可直接读写
- 多行内容通过 hash 哨兵保护，不会出现边界错乱

## 对比

```
# AITP (28 字符)
terminal#t1:echo hello

# JSON Function Calling (96 字符)
{"tool":"terminal","id":"t1","parameters":{"command":"echo hello"}}
```