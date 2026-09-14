# 物联网设备控制

> 说明：本场景演示的是设备端实现 AIP 引擎后的语义设计。当前 AIP 引擎不内置 IoT 指令，设备厂商需按照 AIP 协议规范在设备端自行注册 light、ac、door、conveyor 等指令。

## 控制灯泡

### 开灯（所有灯）

```atp
light#t1ss012:ON
```

```text
id:t1ss012
code:20
text:success
data:all lights turned on
```

### 关灯（所有灯）

```atp
light#t1ss012:OFF
```

```text
id:t1ss012
code:20
text:success
data:all lights turned off
```

### 指定某个灯

```atp
light#t2ss013:ON
name:living_room
```

```text
id:t2ss013
code:20
text:success
data:living_room light turned on
```

---

## 控制门锁

### 锁门（大门）

```atp
door#t3ss223:LOCK
name:gate
```

```text
id:t3ss223
code:20
text:success
data:gate locked
```

### 解锁

```atp
door#t5ss225:UNLOCK
name:gate
```

```text
id:t5ss225
code:20
text:success
data:gate unlocked
```

---

## 工业机械控制

### 传送带启动

```atp
conveyor#c1ss501:START
speed:50
```

```text
id:c1ss501
code:20
text:success
data:conveyor started at speed 50
```

### 传送带停止

```atp
conveyor#c2ss502:STOP
```

```text
id:c2ss502
code:20
text:success
data:conveyor stopped
```

### 机械臂移动

```atp
robot#r1ss601:MOVE
axis:x
position:120
```

```text
id:r1ss601
code:20
text:success
data:robot moved to x:120
```

---

## 查询传感器

```atp
sensor#t8ss401:TEMPERATURE
name:outdoor
```

```text
id:t8ss401
code:20
text:success
data:28.5°C
```