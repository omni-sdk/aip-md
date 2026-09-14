# 文件 CRUD 操作

## 创建文件

```atp
make#c1:./project/
```

```text
id:c1
code:20
text:success
data:./project/
```

---

## 创建文件并写入内容

```atp
make#c2:./project/README.md
text@t2:
# My Project
This is a new project created by AIP.
t2
```

```text
id:c2
code:20
text:success
data:./project/README.md
```

---

## 读取文件内容

```atp
read#r1:./project/README.md
```

```text
id:r1
code:20
text:success
data@t3:
# My Project
This is a new project created by AIP.
t3
```

---

## 列出目录内容

```atp
list#l1:./project/
```

```text
id:l1
code:20
text:success
data:README.md
```

---

## 追加内容到文件末尾

```atp
append#a1:./project/README.md
text@t4:
Appended line by AIP.
t4
```

```text
id:a1
code:20
text:success
data:./project/README.md
```

---

## 删除文件

```atp
delete#d1:./project/README.md
```

```text
id:d1
code:20
text:success
data:./project/README.md
```

---

## 删除目录

```atp
delete#d2:./project/
```

```text
id:d2
code:20
text:success
data:./project/
```