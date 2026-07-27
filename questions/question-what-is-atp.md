# ATP 是什么？

## 问题

ATP 是什么？它能做什么？

## 解答

ATP (AI Transfer Protocol) 是一套标准化的操作指令协议，为 AI、人和设备提供统一的操作语法。

它定义了一套简洁的指令格式，让不同端之间可以通过相同的方式与操作系统交互。AI 通过生成 ATP 指令来操作电脑、控制设备、管理服务器，无需依赖模糊的自然语言描述。

ATP 的指令格式是纯文本，不需要 JSON 转义，对 AI 生成非常友好，Token 消耗比 JSON Function Calling 低约 70%。

## 示例

```atp
terminal#t1:echo hello
```

```json
{"id":"t1","code":0,"text":"success","data":"hello"}
```