# 智能家居联动

## 检测到室内温度过高 → 自动开空调

AI 收到传感器数据后自动生成指令：

```atp
ac#a1:SET_TEMP
name:living_room
value:24
```

```json
{"id":"a1","code":0,"text":"success","data":"living_room AC set to 24°C"}
```

---

## 检测到日落 → 自动开灯

```atp
light#l1:ON
name:living_room
```

```json
{"id":"l1","code":0,"text":"success","data":"living_room light on"}
```

---

## 检测到所有人离开 → 关闭所有设备

```atp
light#l2:OFF
ac#a2:OFF
```

```json
{"id":"l2","code":0,"text":"success","data":"all lights off"}
{"id":"a2","code":0,"text":"success","data":"living_room AC off"}
```

---

## 检测到异常开门 → 发送警报

```atp
terminal#t1:echo "ALERT: garage door opened at $(date)" >> /var/log/alerts.log
```

```json
{"id":"t1","code":0,"text":"success","data":"alert logged"}
```