# 人写草稿，AI 补全，共同编辑

> 协作不是"聊天"，而是在同一份源文件上共同编辑。
> 人类工程师写下粗糙草稿，AI 读完补全缺失的参数、修正错误、添加条件判断。

---

## 场景：工程师的草稿

工程师手写了一份粗糙的 AIP 草稿：

```atp
make#c1:./build/
execute#e1:go build
```

AI 读完，立刻发现三个问题：

1. `execute#e1:go build` 缺少 `-o` 输出参数，构建产物不会命名
2. 缺少 `at:./build` 工作目录，会在错误位置执行
3. 缺少超时和编码，长时间构建可能卡死

AI 补全后的完整版本：

```atp
make#c1:./build/

execute#e1:go build -o app.exe ./cmd/main.go
at:./build
timeout:120s
encoding:utf8
```

---

## 场景：AI 主动加条件判断

工程师写下：

```atp
execute#e1:systemctl restart nginx
```

AI 读完补全：

```atp
when#w1:terminal#check:systemctl is-active nginx
if:[check.data]!=active
then@t1:
terminal#e1:systemctl restart nginx
t1
else@t2:
append#a1:./logs/nginx.log
text@m1:
nginx already running, skip restart
m1
t2
```

---

## 为什么这很独特

- 不是"人下命令，AI 执行"的单向模式
- 而是"人和 AI 使用同一种语法，在同一份文件上反复修改"
- AI 不需要你告诉它"帮我优化"，它看到草稿就知道哪里缺了东西