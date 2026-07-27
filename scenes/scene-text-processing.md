# 文本处理与日志分析

## 过滤日志中的错误

```atp
terminal#t1:grep ERROR /var/log/app.log | tail -20
```

```json
{"id":"t1","code":0,"text":"success","data":"2026-07-27 12:00 ERROR: database connection timeout\n2026-07-27 12:05 ERROR: disk full"}
```

---

## 统计访问量

```atp
terminal#t2:cat /var/log/nginx/access.log | wc -l
```

```json
{"id":"t2","code":0,"text":"success","data":"15423"}
```

---

## 查找大文件

```atp
terminal#t3:find /var/log -size +100M -exec ls -lh {} \;
```

```json
{"id":"t3","code":0,"text":"success","data":"/var/log/app.log  250M"}
```

---

## 批量替换文件内容

```atp
replace#rp1:./config/
raw@r1:
localhost
r1
to@t1:
192.168.0.100
t1
```

```json
{"id":"rp1","code":0,"text":"success","data":"3 files updated"}
```