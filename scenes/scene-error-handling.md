# 错误处理与重试

## 命令执行失败

```atp
terminal#t1:ls /nonexistent_dir
```

```json
{"id":"t1","code":1,"text":"terminal: command failed","data":"ls: cannot access '/nonexistent_dir': No such file or directory"}
```

---

## 超时自动终止

```atp
terminal#t2:sleep 10 && echo never
timeout:1s
```

```json
{"id":"t2","code":4,"text":"terminal: timeout after 1s","data":""}
```

---

## 条件判断：创建成功后读取

```atp
when#w1:create#c1:./test.txt
text@t1:
success
t1
if:[c1.code]==0
then@then1:
read#r1:./test.txt
then1
```

```json
{"id":"c1","code":0,"text":"success","data":"./test.txt"}
{"id":"r1","code":0,"text":"success","data":"success"}
```

---

## 异步执行

```atp
terminal#t3:go build -o app.exe
workdir:./project
async:true
```

```json
{"id":"t3","code":2,"text":"async pending","data":"async started, log: /logs/terminal.log"}
```

---

## 文件不存在

```atp
read#r2:./nonexistent_file.txt
```

```json
{"id":"r2","code":5,"text":"read: file not found: ./nonexistent_file.txt","data":null}
```