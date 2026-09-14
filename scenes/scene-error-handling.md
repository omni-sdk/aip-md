# 错误处理与重试

## 命令执行失败

```atp
terminal#t1:ls /nonexistent_dir
```

```text
id:t1
code:52
text:terminal: command failed
data@d1:
ls: cannot access '/nonexistent_dir': No such file or directory
d1
```

---

## 超时自动终止

```atp
terminal#t2:sleep 10 && echo never
timeout:1s
```

```text
id:t2
code:50
text:terminal: timeout after 1s
data:
```

---

## 条件判断：创建成功后读取

```atp
when#w1:make#c1:./test.txt
if:[c1.code]==20
then@then1:
read#r1:./test.txt
then1
```

```text
id:c1
code:20
text:success
data:./test.txt

id:r1
code:20
text:success
data:
```

---

## 异步执行

```atp
terminal#t3:go build -o app.exe
at:./project
async:true
```

```text
id:t3
code:10
text:async pending
data:async started, log: /logs/terminal.log
```

---

## 文件不存在

```atp
read#r2:./nonexistent_file.txt
```

```text
id:r2
code:42
text:read: file not found: ./nonexistent_file.txt
data:
```