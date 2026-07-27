# 安全工程师

## 角色描述
安全工程师负责系统安全审计、漏洞扫描、证书管理和入侵检测。

## 常用指令

### 检查开放端口

```atp
terminal#t1:ss -tlnp
```

```json
{"id":"t1","code":0,"text":"success","data":"LISTEN 0.0.0.0:22  sshd\nLISTEN 0.0.0.0:80  nginx\nLISTEN 127.0.0.1:3306  mariadb"}
```

### 检查登录日志

```atp
terminal#t2:last -20
```

```json
{"id":"t2","code":0,"text":"success","data":"sa  pts/0  192.168.0.182  Jul 27 12:00"}
```

### 检查 SSH 认证日志

```atp
terminal#t3:grep "Failed password" /var/log/auth.log | tail -10
```

```json
{"id":"t3","code":0,"text":"success","data":"Jul 27 11:45 sshd[1234]: Failed password for root from 10.0.0.50"}
```

### 检查文件完整性

```atp
terminal#t4:sha256sum /usr/bin/sshd /usr/sbin/nginx
```

```json
{"id":"t4","code":0,"text":"success","data":"e3b0c44... /usr/bin/sshd\n98fc1c1... /usr/sbin/nginx"}
```

### 查看防火墙规则

```atp
terminal#t5:iptables -L -n -v
```

```json
{"id":"t5","code":0,"text":"success","data":"Chain INPUT (policy ACCEPT)\nChain FORWARD (policy ACCEPT)\nChain OUTPUT (policy ACCEPT)"}
```

### 扫描可疑进程

```atp
terminal#t6:ps aux | grep -v "\\[" | sort -rnk 3 | head -10
```

```json
{"id":"t6","code":0,"text":"success","data":"root  1234  nginx\nsa  5678  python3"}
```