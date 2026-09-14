# 指令即脚本，脚本即文档

> AIP 文件不是"AI 的方言"，而是一种人类和机器都能读、都能写、都能改的可执行文档。
> 它可以进 Git、可以 Code Review、可以当运维手册、也可以直接被 `run` 执行。

---

## 场景：新同事入职

HR 发来一份 `init-dev-env.cmd`：

```atp
make#step1:./workspace/
make#step2:./workspace/config/
make#step3:./workspace/config/app.yaml
text@c1:
server:
  port: 8080
  host: 0.0.0.0
c1
make#step4:./workspace/logs/
append#step5:./workspace/config/env.sh
text@c2:
export APP_ENV=development
export APP_PORT=8080
c2
terminal#step6:bash ./workspace/config/env.sh
```

新同事把它当运维手册读，Human 也能看懂每一步在做什么。

AI 则直接执行：

```atp
run#r1:./init-dev-env.cmd
```

```text
id:r1
code:20
text:success
data@d1:
make#step1 -> ./workspace/ (code:20)
make#step2 -> ./workspace/config/ (code:20)
make#step3 -> ./workspace/config/app.yaml (code:20)
make#step4 -> ./workspace/logs/ (code:20)
append#step5 -> ./workspace/config/env.sh (code:20)
terminal#step6 -> exit 0 (code:20)
d1
```

---

## 为什么这很独特

- **Shell 脚本**：人类友好，但 AI 生成容易出错（引号、转义、平台差异）
- **Ansible Playbook**：结构化好，但 YAML 冗长，且需要装 Python 环境和 Ansible
- **AIP 指令文件**：人机共用一套语法，可读、可写、可执行、可 diff、可审计

它进版本库之后，`git diff` 会告诉你"某一次部署到底做了什么"，而不是甩给你一个黑盒的 `deploy.sh`。