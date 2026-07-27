# 权限与用户管理

## 修改文件权限

```atp
chmod#c1:0755
file:./scripts/deploy.sh
```

```json
{"id":"c1","code":0,"text":"success","data":"./scripts/deploy.sh"}
```

---

## 修改文件归属

```atp
chown#o1:
group:www-data
user:www-data
file:./web/index.html
```

```json
{"id":"o1","code":0,"text":"success","data":"./web/index.html"}
```

---

## 批量修改权限

```atp
chmod#c2:0644
recurse:true
files@f1:
./web/css/
./web/js/
./web/images/
f1
```

```json
{"id":"c2","code":0,"text":"success","data":"3 directories updated"}
```

---

## 查看文件权限

```atp
terminal#t1:ls -la ./scripts/deploy.sh
```

```json
{"id":"t1","code":0,"text":"success","data":"-rwxr-xr-x 1 sa sa 1024 Jul 27 12:00 deploy.sh"}
```