# 远程设备管理

## SSH 登录远程服务器

```atp
ssh#s1:
host:192.168.0.100
user:admin
pass:password123
```

```json
{"id":"s1","code":0,"text":"success","data":"session_id: abc123def456"}
```

---

## 在远程服务器执行命令

```atp
ssh#s1_exec:abc123def456
cmd:systemctl restart nginx
```

```json
{"id":"s1_exec","code":0,"text":"success","data":"nginx restarted successfully"}
```

---

## 查看远程服务器磁盘使用

```atp
ssh#s1_disk:abc123def456
cmd:df -h
```

```json
{"id":"s1_disk","code":0,"text":"success","data":"/dev/sda1  100G  45G  55G  45% /"}
```

---

## FTP 登录

```atp
ftp#f1:
host:10.0.0.50
user:ftpuser
pass:ftppass123
```

```json
{"id":"f1","code":0,"text":"success","data":"session_id: ftp789ghi012"}
```

---

## FTP 下载文件

```atp
ftp#f1_dl:ftp789ghi012
retr:/remote/file.txt
```

```json
{"id":"f1_dl","code":0,"text":"success","data":"file.txt downloaded"}
```

---

## FTP 上传文件

```atp
ftp#f1_ul:ftp789ghi012
stor:./local_file.txt
```

```json
{"id":"f1_ul","code":0,"text":"success","data":"local_file.txt uploaded"}
```