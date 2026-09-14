# 不同品牌、不同协议、同一套指令

> AIP 不解决"协议适配"，它解决协议之上的统一表达。
> 一盏灯是 Zigbee，一台空调是红外，一台门锁是 Wi-Fi，一台传送带是串口。
> 四种不同的物理协议，四种不同的通信方式，因为都实现了 AIP 引擎，所以统一下发。

---

## 场景：一个控制台，四种协议

```atp
light#l1:ON
name:living_room

ac#a1:SET_TEMP
name:living_room
value:24

door#d1:LOCK
name:gate

conveyor#c1:START
speed:50
```

```text
id:l1
code:20
text:success
data:living_room light on (zigbee)

id:a1
code:20
text:success
data:living_room AC set to 24C (infrared)

id:d1
code:20
text:success
data:gate locked (wifi)

id:c1
code:20
text:success
data:conveyor started at speed 50 (serial)
```

四条指令，四种物理协议，一套语法。

---

## 设备如何实现

每台设备厂商在自己的固件里实现一个 AIP 引擎（可以是 Go、C、Rust 或 Arduino）。

引擎的职责：
1. 监听本机协议的指令入口（串口 / Wi-Fi / 蓝牙 / 红外）
2. 解析 AIP 指令，识别 `command#id:param`
3. 执行硬件动作
4. 返回标准 AIP 响应（`id` / `code` / `text` / `data`）

---

## 为什么这很独特

- AIP 不关心底层是 Zigbee 还是串口
- 它只规定**指令长什么样**
- 这是协议分层思想的极致实践：物理层由厂商负责，语义层由 AIP 统一
- 一个控制台，就能管好一个"协议动物园"