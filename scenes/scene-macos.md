# macOS 特有操作

## 安装 Homebrew 包

```atp
terminal#t1:brew install wget
timeout:120s
```

```json
{"id":"t1","code":0,"text":"success","data":"wget installed"}
```

---

## 查看系统信息

```atp
terminal#t2:system_profiler SPHardwareDataType | grep "Model Name\|Processor\|Memory"
```

```json
{"id":"t2","code":0,"text":"success","data":"Model Name: MacBook Pro\nProcessor: Apple M4\nMemory: 32 GB"}
```

---

## 管理 Launch 服务

```atp
terminal#t3:launchctl list | grep com.example
```

```json
{"id":"t3","code":0,"text":"success","data":"com.example.app  running"}
```

---

## 磁盘工具

```atp
terminal#t4:diskutil list | grep "Apple_APFS"
```

```json
{"id":"t4","code":0,"text":"success","data":"Apple_APFS Container disk1  500.0 GB"}
```