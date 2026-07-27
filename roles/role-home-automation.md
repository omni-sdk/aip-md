# 家庭自动化管理员

## 角色描述
家庭自动化管理员负责智能家居设备的联动控制、场景设置和自动化规则配置。

## 常用指令

### 回家模式

```atp
light#l1:ON
name:living_room
light#l2:ON
name:entrance
ac#a1:SET_TEMP
name:living_room
value:24
```

```json
{"id":"l1","code":0,"text":"success","data":"living_room light on"}
{"id":"l2","code":0,"text":"success","data":"entrance light on"}
{"id":"a1","code":0,"text":"success","data":"living_room AC set to 24°C"}
```

### 离家模式

```atp
light#l3:OFF
ac#a2:OFF
door#d1:LOCK
name:gate
```

```json
{"id":"l3","code":0,"text":"success","data":"all lights off"}
{"id":"a2","code":0,"text":"success","data":"all AC off"}
{"id":"d1","code":0,"text":"success","data":"gate locked"}
```

### 睡前模式

```atp
light#l4:OFF
name:living_room
light#l5:ON
name:bedroom
value:30
door#d2:LOCK
name:all
```

```json
{"id":"l4","code":0,"text":"success","data":"living_room light off"}
{"id":"l5","code":0,"text":"success","data":"bedroom light on at 30%"}
{"id":"d2","code":0,"text":"success","data":"all doors locked"}
```

### 查询室内温度

```atp
sensor#s1:TEMPERATURE
name:living_room
```

```json
{"id":"s1","code":0,"text":"success","data":"26.5°C"}
```