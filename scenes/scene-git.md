# Git 版本控制

## 查看仓库状态

```atp
terminal#t1:git status --short
workdir:./project
```

```json
{"id":"t1","code":0,"text":"success","data":"M  README.md\nA  new_feature.go"}
```

---

## 提交并推送

```atp
terminal#t2:git add -A && git commit -m "feat: add new feature" --quiet && git push origin main
workdir:./project
```

```json
{"id":"t2","code":0,"text":"success","data":"pushed to origin/main"}
```

---

## 创建新分支

```atp
terminal#t3:git checkout -b feature/new-module
workdir:./project
```

```json
{"id":"t3","code":0,"text":"success","data":"switched to branch feature/new-module"}
```

---

## 查看提交历史

```atp
terminal#t4:git log --oneline -5
workdir:./project
```

```json
{"id":"t4","code":0,"text":"success","data":"4af05f3 docs: add scenes\nd7a031e docs: update author\nc956978 docs: add file CRUD examples"}
```

---

## 克隆远程仓库

```atp
terminal#t5:git clone https://github.com/sinmofun/atp.git
```

```json
{"id":"t5","code":0,"text":"success","data":"repository cloned"}
```