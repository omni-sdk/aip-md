# 文件 CRUD 操作

## 创建文件

```atp
create#c1:./project/
```

```json
{"id":"c1","code":0,"text":"success","data":"./project/"}
```

---

## 创建文件并写入内容

```atp
create#c2:./project/README.md
text@t2:
# My Project
This is a new project created by AITP.
t2
```

```json
{"id":"c2","code":0,"text":"success","data":"./project/README.md"}
```

---

## 读取文件内容

```atp
read#r1:./project/README.md
encoding:utf8
```

```json
{"id":"r1","code":0,"text":"success","data":"# My Project\nThis is a new project created by AITP."}
```

---

## 列出目录内容

```atp
list#l1:./project/
```

```json
{"id":"l1","code":0,"text":"success","data":"README.md"}
```

---

## 追加内容到文件末尾

```atp
append#a1:./project/README.md
text@t4:
Appended line by AITP.
t4
```

```json
{"id":"a1","code":0,"text":"success","data":"./project/README.md"}
```

---

## 删除文件

```atp
delete#d1:./project/README.md
```

```json
{"id":"d1","code":0,"text":"success","data":"./project/README.md"}
```

---

## 删除目录

```atp
delete#d2:./project/
```

```json
{"id":"d2","code":0,"text":"success","data":"./project/"}
```