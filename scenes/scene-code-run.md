# 代码编写与运行

## 编译 Go 项目

```atp
terminal#t1:go build -o app.exe ./cmd/main.go
workdir:./project
```

```json
{"id":"t1","code":0,"text":"success","data":"build completed"}
```

---

## 运行 Python 脚本

```atp
terminal#t2:python3 main.py
workdir:./project
```

```json
{"id":"t2","code":0,"text":"success","data":"Hello from Python"}
```

---

## 安装依赖

```atp
terminal#t3:pip install -r requirements.txt
workdir:./project
```

```json
{"id":"t3","code":0,"text":"success","data":"Successfully installed requests, flask"}
```

---

## 运行测试

```atp
terminal#t4:go test ./...
workdir:./project
timeout:60s
```

```json
{"id":"t4","code":0,"text":"success","data":"ok  atp/commands  0.234s\nok  atp/engine   0.156s"}
```

---

## 格式化代码

```atp
terminal#t5:gofmt -w .
workdir:./project
```

```json
{"id":"t5","code":0,"text":"success","data":"formatted"}
```