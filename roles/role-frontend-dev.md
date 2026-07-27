# 前端开发者

## 角色描述
前端开发者负责 Web 前端开发、构建、打包和静态资源管理。

## 常用指令

### 安装依赖

```atp
terminal#t1:npm install
workdir:./project
timeout:120s
```

```json
{"id":"t1","code":0,"text":"success","data":"added 312 packages"}
```

### 启动开发服务器

```atp
terminal#t2:npm run dev
workdir:./project
async:true
```

```json
{"id":"t2","code":2,"text":"async pending","data":"dev server starting on http://localhost:3000"}
```

### 构建生产版本

```atp
terminal#t3:npm run build
workdir:./project
timeout:120s
```

```json
{"id":"t3","code":0,"text":"success","data":"build completed, output: ./dist/"}
```

### 运行测试

```atp
terminal#t4:npm test
workdir:./project
timeout:60s
```

```json
{"id":"t4","code":0,"text":"success","data":"23 tests passed, 0 failed"}
```

### 压缩静态资源

```atp
zip#z1:./dist
to:./deploy/frontend.zip
format:zip
level:9
```

```json
{"id":"z1","code":0,"text":"success","data":"./deploy/frontend.zip"}
```