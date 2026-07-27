# Windows 特有操作

## 查看注册表

```atp
terminal#t1:reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion
```

```json
{"id":"t1","code":0,"text":"success","data":"ProgramFilesDir: C:\\Program Files"}
```

---

## 管理 Windows 服务

```atp
terminal#t2:sc query MariaDB
```

```json
{"id":"t2","code":0,"text":"success","data":"SERVICE_NAME: MariaDB\nSTATE: STOPPED"}
```

---

## 启动 Windows 服务

```atp
terminal#t3:net start MariaDB
```

```json
{"id":"t3","code":0,"text":"success","data":"MariaDB service started"}
```

---

## 查看系统信息

```atp
terminal#t4:systeminfo | findstr /c:"OS Name" /c:"Total Physical Memory"
```

```json
{"id":"t4","code":0,"text":"success","data":"OS Name: Microsoft Windows 10\nTotal Physical Memory: 32,768 MB"}
```

---

## 环境变量操作

```atp
terminal#t5:echo %GOPATH% && echo %GOROOT%
```

```json
{"id":"t5","code":0,"text":"success","data":"D:\\env\\go\nD:\\env\\go-v1.26.2"}
```