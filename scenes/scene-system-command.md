# 系统指令执行

## 查看系统信息

### Linux 系统信息

```atp
terminal#t1:uname -a
```

```json
{"id":"t1","code":0,"text":"success","data":"Linux X 6.8.0-136-generic #136~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Fri Jul  3 16:29:11 UTC  x86_64 x86_64 x86_64 GNU/Linux"}
```

### Windows 系统信息

```atp
terminal#t2:ver
```

```json
{"id":"t2","code":0,"text":"success","data":"Microsoft Windows [Version 10.0.17763.9020]"}
```

### Linux 磁盘使用

```atp
terminal#t3:df -h
```

```json
{"id":"t3","code":0,"text":"success","data":"/dev/sda2  215G  13G  192G  7% /"}
```

---

## 进程管理

### 查找 nginx 进程

```atp
terminal#t4:ps aux | grep nginx
```

```json
{"id":"t4","code":0,"text":"success","data":"root  1234  nginx: master process"}
```

---

## 网络诊断

### Linux ping

```atp
terminal#t6:ping -c 4 8.8.8.8
```

```json
{"id":"t6","code":0,"text":"success","data":"4 packets transmitted, 4 received, 0% packet loss"}
```

### Windows ping

```atp
terminal#t7:ping -n 4 8.8.8.8
```

```json
{"id":"t7","code":0,"text":"success","data":"Packets: Sent = 4, Received = 4, Lost = 0"}
```

---

## 文件压缩

```atp
zip#z1:./project
to:./project_backup.zip
format:zip
level:6
```

```json
{"id":"z1","code":0,"text":"success","data":"./project_backup.zip"}
```

---

## 文件解压

```atp
unzip#uz1:./project_backup.zip
to:./restored/
```

```json
{"id":"uz1","code":0,"text":"success","data":"./restored/"}
```