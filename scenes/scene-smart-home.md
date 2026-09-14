# 智能家居联动

> 说明：本场景演示的是设备端实现 AIP 引擎后的语义设计。当前 AIP 引擎不内置 IoT 指令，需设备端自行注册。

## 检测到室内温度过高 → 自动开空调

```atp
ac#a1:SET_TEMP
name:living_room
value:24
```

```text
id:a1
code:20
text:success
data:living_room AC set to 24°C
```

---

## 检测到日落 → 自动开灯

```atp
light#l1:ON
name:living_room
```

```text
id:l1
code:20
text:success
data:living_room light on
```

---

## 检测到所有人离开 → 关闭所有设备

```atp
light#l2:OFF
ac#a2:OFF
```

```text
id:l2
code:20
text:success
data:all lights off

id:a2
code:20
text:success
data:living_room AC off
```

---

## 检测到异常开门 → 发送警报

```atp
append#a1:./logs/alerts.log
text@t1:
ALERT: garage door opened
t1
```

```text
id:a1
code:20
text:success
data:./logs/alerts.log
```