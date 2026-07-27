# 系统监控

## 查看 CPU 温度

```atp
terminal#t1:sensors | grep Package
```

```json
{"id":"t1","code":0,"text":"success","data":"Package id 0: +48.0°C"}
```

---

## 查看内存使用

```atp
terminal#t2:free -h
```

```json
{"id":"t2","code":0,"text":"success","data":"total: 15Gi  used: 1.7Gi  free: 10Gi"}
```

---

## 查看磁盘使用

```atp
terminal#t3:df -h /
```

```json
{"id":"t3","code":0,"text":"success","data":"/dev/sda2  215G  13G  192G  7% /"}
```

---

## 查看进程负载

```atp
terminal#t4:top -bn1 | head -5
```

```json
{"id":"t4","code":0,"text":"success","data":"load average: 0.44, 0.60, 0.34\n%Cpu(s): 4.7 us, 87.5 id"}
```

---

## 查看系统日志

```atp
terminal#t5:journalctl -p 3 --no-pager -n 10
```

```json
{"id":"t5","code":0,"text":"success","data":"no critical errors"}
```