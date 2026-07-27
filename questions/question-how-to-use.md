# 如何使用 ATP？

## 问题

我该如何开始使用 ATP？

## 解答

1. 将 [PROMPT.md](../PROMPT.md) 的内容复制到你的大模型系统提示中
2. AI 即可学会生成 ATP 指令
3. 将 AI 生成的 ATP 指令发送到 ATP 引擎执行
4. 引擎返回 JSON 格式的执行结果

## 示例

用户：帮我在桌面上创建一个名为 photos 的文件夹

AI 生成 ATP 指令：
```atp
create#c1:./photos/
```

ATP 引擎返回：
```json
{"id":"c1","code":0,"text":"success","data":"./photos/"}
```