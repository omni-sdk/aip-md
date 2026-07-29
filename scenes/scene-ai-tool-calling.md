# AI 工具调用

## AI 生成指令

用户说："帮我在桌面上创建一个名为 photos 的文件夹"

AI 生成的 AIP 指令：

```atp
create#c1:./photos/
```

AIP 引擎执行并返回：

```json
{"id":"c1","code":0,"text":"success","data":"./photos/"}
```

---

## AI 生成系统命令

用户说："查看一下服务器的磁盘使用情况"

AI 生成的 AIP 指令：

```atp
terminal#t1:df -h
```

AIP 引擎执行并返回：

```json
{"id":"t1","code":0,"text":"success","data":"/dev/sda2  215G  13G  192G  7% /"}
```

---

## AI 生成物联网指令

用户说："把客厅的灯关掉"

AI 生成的 AIP 指令：

```atp
light#t1:OFF
name:living_room
```

AIP 引擎执行并返回：

```json
{"id":"t1","code":0,"text":"success","data":"living_room light turned off"}
```

---

## AI 生成远程管理指令

用户说："重启 192.168.0.100 服务器上的 nginx"

AI 生成的 AIP 指令：

```atp
ssh#s1:
host:192.168.0.100
user:admin
pass:password123
```

```json
{"id":"s1","code":0,"text":"success","data":"session_id: abc123"}
```

AI 继续生成：

```atp
ssh#s2:abc123
cmd:systemctl restart nginx
```

```json
{"id":"s2","code":0,"text":"success","data":"nginx restarted"}
```