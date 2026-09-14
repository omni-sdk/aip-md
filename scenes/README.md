# AIP 场景示例

本目录包含 AIP 在各种实际场景中的使用示例。每个文件展示了 AI 生成的 AIP 指令和对应的 AIP 原生返回结果。

## 场景列表

### 基础操作

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-file-crud.md | 文件创建、读取、修改、删除 |
| scene-system-command.md | 系统指令执行（系统信息、进程管理、压缩解压） |
| scene-text-processing.md | 文本处理与日志分析 |
| scene-permission.md | 文件权限与用户管理 |
| scene-env-setup.md | 开发环境配置（Go、Node.js、Python） |

### 系统与平台

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-windows-specific.md | Windows 特有操作（注册表、服务、环境变量） |
| scene-macos.md | macOS 特有操作（Homebrew、Launch 服务） |
| scene-media.md | 多媒体处理（视频转换、音频提取、图片压缩） |
| scene-security.md | 安全与加密（SSH 密钥、证书、文件加密） |

### 网络与远程

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-network.md | 网络诊断、文件下载、DNS 解析 |
| scene-api-integration.md | API 集成与 Webhook 通知 |
| scene-remote-management.md | SSH、FTP 远程设备管理 |
| scene-devops.md | DevOps 自动化（批量部署、健康检查） |

### 开发与运维

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-code-run.md | 代码编译、运行、测试 |
| scene-git.md | Git 提交、推送、分支管理 |
| scene-docker.md | Docker 容器管理 |
| scene-database.md | 数据库备份、导入、查询 |
| scene-cron-backup.md | 定时任务与自动备份 |
| scene-monitor.md | 系统监控（CPU、内存、磁盘、日志） |

### 控制与联动

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-iot-control.md | 物联网设备控制（设备端 AIP 引擎语义设计） |
| scene-smart-home.md | 智能家居联动（设备端 AIP 引擎语义设计） |
| scene-when-condition.md | 条件触发执行（构建→部署、健康检查→重启） |
| scene-error-handling.md | 错误码、超时、条件判断、异步执行 |

### 前瞻场景

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-aip-as-script.md | 指令即脚本，脚本即文档：可执行文档范式 |
| scene-human-ai-draft.md | 人写草稿，AI 补全，共同编辑 |
| scene-replay-audit.md | 每一次操作都可回放、可追溯、可审计 |
| scene-offline-field.md | 无网络、无云端、无 API 的离线部署 |
| scene-device-fleet.md | 不同品牌、不同协议、同一套指令 |
| scene-teach-protocol.md | 用 AIP 教协议思维：五课教学案例 |

### AI 与教学

| 场景文件 | 覆盖内容 |
|---------|---------|
| scene-ai-tool-calling.md | AI 生成指令的完整对话流程 |
| scene-teaching.md | 教学演示场景 |

## 如何使用

1. 打开任意场景文件，查看 AI 生成的 AIP 指令
2. 指令以 `atp` 代码块标注，返回结果以 AIP 原生格式展示
3. 将 AIP 指令发送给 AIP 引擎，即可获得相同的执行结果

## 更多信息

- 完整指令语法: 参见项目根目录的 [README.md](../README.md)
- AI 提示词: 参见 [PROMPT.md](../PROMPT.md)
- 测试报告: 参见 [TEST_REPORT.md](../TEST_REPORT.md)