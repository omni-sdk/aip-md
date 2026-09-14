# 无网络、无云端、无 API

> AIP 是协议，不是服务。
> 它可以跑在任何地方，哪怕完全没有互联网。

---

## 场景：离线的工业平板

一台野外作业用的工业平板，安装在信号盲区的基站机房里。

平板本地跑着一个 AIP 引擎（Go 编译的单文件，约 12MB），没有云、没有 API、没有 SSH 隧道。

---

## 本地采样

```atp
execute#sample1:sensorctl read --channel temp --format json
at:./tools
timeout:5s
```

```text
id:sample1
code:20
text:success
data@d1:
{"channel":"temp","value":38.7,"unit":"C","ts":"2026-09-14T02:15:03Z"}
d1
```

---

## 本地记录

```atp
append#log1:./logs/sensor_20260914.log
text@l1:
2026-09-14T02:15:03Z temp=38.7C
l1
```

```text
id:log1
code:20
text:success
data:./logs/sensor_20260914.log
```

---

## 本地阈值判断与告警

```atp
when#w1:execute#sample2:sensorctl read --channel temp
at:./tools
if:[sample2.data]~=38
then@t1:
execute#alarm1:beep -f 880 -l 500
t1
```

```text
id:sample2
code:20
text:success
data:{"channel":"temp","value":38.7,"unit":"C"}
```

```text
id:alarm1
code:20
text:success
data:beep triggered
```

---

## 场景：直升机巡检

一架执行电力巡线的直升机，飞越山区，无线电暂时失联 20 分钟。

机载 AIP 引擎按照预设指令文件继续工作：

```atp
run#r1:./missions/patrol.cmd
```

```text
id:r1
code:20
text:success
data@d2:
capture#c1 -> ./photos/lat31.2_lon121.5.jpg (code:20)
capture#c2 -> ./photos/lat31.3_lon121.6.jpg (code:20)
append#a1 -> ./logs/patrol.log (code:20)
d2
```

等信号恢复，再把结果批量上报。

---

## 为什么这很独特

- **AIP 不依赖服务器**：它是一个 Go 二进制，可以跑在任何有 CPU 的设备上
- **无网络照样工作**：指令、执行、日志、告警全在本地闭环
- **协议 vs 服务**：很多"AI 工具调用"方案本质上是一个云服务，断网就瘫痪；AIP 不是