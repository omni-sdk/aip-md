# 网络诊断与管理

## 查看当前 IP

```atp
terminal#t1:ipconfig
```

```json
{"id":"t1","code":0,"text":"success","data":"IPv4 Address: 192.168.0.182"}
```

---

## 网络连通测试

```atp
terminal#t2:ping -n 4 baidu.com
```

```json
{"id":"t2","code":0,"text":"success","data":"Packets: Sent = 4, Received = 4, Lost = 0"}
```

---

## 查看端口监听

```atp
terminal#t3:netstat -an | findstr LISTENING
```

```json
{"id":"t3","code":0,"text":"success","data":"TCP  127.0.0.1:9000  LISTENING\nTCP  0.0.0.0:3306   LISTENING"}
```

---

## 下载文件

```atp
fetch#f1:https://example.com/file.zip
save:./downloads/file.zip
```

```json
{"id":"f1","code":0,"text":"success","data":"./downloads/file.zip"}
```

---

## DNS 解析

```atp
terminal#t4:nslookup github.com
```

```json
{"id":"t4","code":0,"text":"success","data":"Address: 20.205.243.166"}
```