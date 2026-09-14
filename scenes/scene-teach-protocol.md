# 用 AIP 教协议思维

> 不是教编程，是教指令、边界、事务、状态码这套思维。
> AIP 把抽象的协议概念，变成了可动手、可观察、可犯错的具体操作。

---

## 第一课：指令的结构

学生写下第一条指令：

```atp
make#s1:./demo/
```

```text
id:s1
code:20
text:success
data:./demo/
```

教师提问：`make` 是什么？`s1` 是什么？`./demo/` 是什么？

答案：
- `make` 是指令名，告诉引擎"我要创建"
- `s1` 是事务编号，唯一标识这一次操作
- `./demo/` 是参数，说明创建什么

---

## 第二课：为什么需要边界

学生写了一条多行指令，但忘了写结束哨兵：

```atp
make#s2:./demo/hello.txt
text@m1:
Hello AIP
```

引擎返回：

```text
id:s2
code:40
text:parameter block not closed, missing m1
```

学生第一次意识到：**边界必须有始有终**，否则解析器不知道内容在哪里结束。

正确版本：

```atp
make#s2:./demo/hello.txt
text@m1:
Hello AIP
m1
```

```text
id:s2
code:20
text:success
data:./demo/hello.txt
```

---

## 第三课：为什么需要状态码

学生写了一条读取不存在文件的指令：

```atp
read#r1:./not_exist.txt
```

```text
id:r1
code:42
text:read: file not found: ./not_exist.txt
data:
```

教师问：为什么返回 `42` 而不是 `20`？

学生查状态码表：
- `20` = 成功
- `40` = 通用失败
- `42` = 文件/路径不存在

**协议需要精确的错误反馈**。不同的错误码，意味着后续可以采取不同的处理策略。

---

## 第四课：为什么需要事务追踪

学生连续写下三条指令：

```atp
make#t1:./a.txt
make#t2:./b.txt
make#t3:./c.txt
```

```text
id:t1
code:20
text:success
data:./a.txt

id:t2
code:20
text:success
data:./b.txt

id:t3
code:42
text:file not found: ./c.txt's parent
data:
```

教师问：三条指令，哪条失败了？

学生回答：`t3`，因为返回里只有它 code 不是 20。

**每一个操作必须有唯一的编号**，才能在批量执行中精准定位失败点。

---

## 第五课：为什么需要自愈

学生写了一条执行指令：

```atp
execute#e1:go build
```

```text
id:e1
code:52
text:execute: command failed: exit status 1 | ./logs/execute_001.log
data:go: go.mod file not found
```

教师引导：现在怎么办？

学生尝试读取日志：

```atp
read#r2:./logs/execute_001.log
```

```text
id:r2
code:20
text:success
data@d1:
# CMD: go build
# ERROR: go.mod file not found in current directory
d1
```

学生理解了：**引擎不只是执行，还负责把错误上下文完整保留下来**，供 AI 或人自主诊断。

正确做法：先 `make` 出 `go.mod`，再 `execute#e2:go build`。

---

## 为什么这很独特

- 抽象的"协议"概念，被拆成五个可动手的步骤
- 学生不是在背规则，而是在**犯错、看返回、理解状态码**
- AIP 是教协议思维最好的载体：它简单、可执行、反馈精准