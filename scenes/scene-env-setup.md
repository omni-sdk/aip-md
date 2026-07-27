# 开发环境配置

## 安装 Go 环境

```atp
terminal#t1:wget https://go.dev/dl/go1.26.5.linux-amd64.tar.gz && tar -C /usr/local -xzf go1.26.5.linux-amd64.tar.gz
timeout:120s
```

```json
{"id":"t1","code":0,"text":"success","data":"Go 1.26.5 installed"}
```

---

## 配置环境变量

```atp
create#c1:./env.sh
text@t1:
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
export GOPROXY=https://goproxy.cn,direct
t1
```

```json
{"id":"c1","code":0,"text":"success","data":"./env.sh"}
```

---

## 安装 Node.js 依赖

```atp
terminal#t2:npm install
workdir:./project
timeout:120s
```

```json
{"id":"t2","code":0,"text":"success","data":"added 245 packages"}
```

---

## 安装 Python 依赖

```atp
terminal#t3:pip install -r requirements.txt
workdir:./project
timeout:120s
```

```json
{"id":"t3","code":0,"text":"success","data":"Successfully installed django, numpy, pandas"}
```