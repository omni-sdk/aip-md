# 系统管理员

## 角色描述
系统管理员负责服务器的日常维护、监控、备份和故障排查。

## 常用指令

### 查看系统负载

```atp
terminal#t1:top -bn1 | head -5
```

```json
{"id":"t1","code":0,"text":"success","data":"load average: 0.44, 0.60, 0.34\n%Cpu(s): 4.7 us, 87.5 id"}
```

### 查看磁盘使用

```atp
terminal#t2:df -h
```

```json
{"id":"t2","code":0,"text":"success","data":"/dev/sda2  215G  13G  192G  7% /"}
```

### 查看内存使用

```atp
terminal#t3:free -h
```

```json
{"id":"t3","code":0,"text":"success","data":"total: 15Gi  used: 1.7Gi  free: 10Gi"}
```

### 查看系统日志

```atp
terminal#t4:journalctl -p 3 --no-pager -n 20
```

```json
{"id":"t4","code":0,"text":"success","data":"no critical errors"}
```

### 重启服务

```atp
terminal#t5:systemctl restart nginx
```

```json
{"id":"t5","code":0,"text":"success","data":"nginx restarted"}
```

### 备份数据库

```atp
terminal#t6:mariadb-dump -u root -p123456 --all-databases > /backup/all_$(date +%Y%m%d).sql
```

```json
{"id":"t6","code":0,"text":"success","data":"backup completed"}
```