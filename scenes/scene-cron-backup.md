# 定时任务与备份

## 设置定时任务

```atp
terminal#t1:echo "0 3 * * * /usr/bin/backup.sh" | crontab -
```

```json
{"id":"t1","code":0,"text":"success","data":"cron job set"}
```

---

## 创建备份脚本

```atp
create#c1:./backup.sh
text@t1:
#!/bin/bash
DATE=$(date +%Y%m%d)
tar -czf /backup/project_$DATE.tar.gz ./project
t1
```

```json
{"id":"c1","code":0,"text":"success","data":"./backup.sh"}
```

---

## 执行备份

```atp
terminal#t2:bash ./backup.sh
workdir:./
```

```json
{"id":"t2","code":0,"text":"success","data":"backup completed: project_20260727.tar.gz"}
```

---

## 清理过期备份

```atp
terminal#t3:find ./backup -name "*.tar.gz" -mtime +30 -delete
```

```json
{"id":"t3","code":0,"text":"success","data":"old backups cleaned"}
```

---

## 查看定时任务列表

```atp
terminal#t4:crontab -l
```

```json
{"id":"t4","code":0,"text":"success","data":"0 3 * * * /usr/bin/backup.sh"}
```