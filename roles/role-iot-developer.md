# 物联网开发者

## 角色描述
物联网开发者负责嵌入式设备的指令编写、传感器数据采集和设备间通信。

## 常用指令

### 控制传送带

```atp
conveyor#c1:START
speed:80
```

```json
{"id":"c1","code":0,"text":"success","data":"conveyor started at speed 80"}
```

### 机械臂操作

```atp
robot#r1:MOVE
axis:x
position:200
robot#r2:MOVE
axis:y
position:150
robot#r3:GRAB
```

```json
{"id":"r1","code":0,"text":"success","data":"x axis moved to 200"}
{"id":"r2","code":0,"text":"success","data":"y axis moved to 150"}
{"id":"r3","code":0,"text":"success","data":"object grabbed"}
```

### 读取温度传感器

```atp
sensor#s1:TEMPERATURE
name:boiler_room
```

```json
{"id":"s1","code":0,"text":"success","data":"42.8°C"}
```

### 读取湿度传感器

```atp
sensor#s2:HUMIDITY
name:greenhouse
```

```json
{"id":"s2","code":0,"text":"success","data":"78%"}
```

### 控制灌溉系统

```atp
irrigation#i1:START
zone:3
duration:600
```

```json
{"id":"i1","code":0,"text":"success","data":"zone 3 irrigation started for 600 seconds"}
```

### 读取所有传感器

```atp
sensor#s3:ALL
name:factory_floor
```

```json
{"id":"s3","code":0,"text":"success","data":"temperature: 35.2°C, humidity: 55%, pressure: 1013hPa"}
```