# 数据库操作

## 连接 MariaDB 并查询

```atp
terminal#t1:mariadb -u root -p123456 -e "SHOW DATABASES;"
```

```json
{"id":"t1","code":0,"text":"success","data":"information_schema\nmysql\nperformance_schema\nsys"}
```

---

## 创建数据库

```atp
terminal#t2:mariadb -u root -p123456 -e "CREATE DATABASE my_app;"
```

```json
{"id":"t2","code":0,"text":"success","data":"database created"}
```

---

## 导入 SQL 文件

```atp
terminal#t3:mariadb -u root -p123456 my_app < ./backup.sql
workdir:./data
```

```json
{"id":"t3","code":0,"text":"success","data":"SQL imported"}
```

---

## 备份数据库

```atp
terminal#t4:mariadb-dump -u root -p123456 my_app > ./backup.sql
workdir:./data
```

```json
{"id":"t4","code":0,"text":"success","data":"backup completed"}
```