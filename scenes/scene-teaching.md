# 教学场景

## 学习 Linux 命令

教师：请同学们看这条指令

```atp
terminal#t1:ls -la /home
```

```json
{"id":"t1","code":0,"text":"success","data":"total 12\ndrwxr-xr-x 3 root root 4096 Jan 1 2026 .\ndrwxr-xr-x 1 sa sa 4096 Jul 27 2026 sa"}
```

---

## 学习文件操作

```atp
create#c1:./learning/basics.txt
text@t1:
Linux is an open-source operating system.
It was created by Linus Torvalds in 1991.
t1
```

```json
{"id":"c1","code":0,"text":"success","data":"./learning/basics.txt"}
```

---

## 演示 Git 工作流

教师可以用 AIP 指令来演示完整的 Git 操作流程：

```atp
terminal#t2:git init learning-project
terminal#t3:echo "# Learning Project" > learning-project/README.md
terminal#t4:git -C learning-project add -A && git -C learning-project commit -m "init"
```

```json
{"id":"t2","code":0,"text":"success","data":"Initialized empty Git repository"}
{"id":"t3","code":0,"text":"success","data":"README.md created"}
{"id":"t4","code":0,"text":"success","data":"[master 7e4bb26] init"}
```

---

## AI 辅助教学

学生问：请帮我创建一个简单的 Python 项目结构

AI 生成 AIP 指令：

```atp
create#c2:./python_project/
create#c3:./python_project/main.py
text@t2:
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
t2
create#c4:./python_project/README.md
text@t3:
# Python Project
A simple project created with AIP.
t3
```

```json
{"id":"c2","code":0,"text":"success","data":"./python_project/"}
{"id":"c3","code":0,"text":"success","data":"./python_project/main.py"}
{"id":"c4","code":0,"text":"success","data":"./python_project/README.md"}
```