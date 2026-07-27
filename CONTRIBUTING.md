# 贡献指南 (CONTRIBUTING)

感谢你对 ATP (AI Transfer Protocol) 项目的关注！本文档将帮助你了解如何参与本项目的开发。

## 开发环境

### 基础要求

- Go 1.26+ (必须)
- Git (必须)
- 操作系统: Windows 10+ 或 Linux (Ubuntu 22.04+ 推荐)

### 克隆仓库

```bash
git clone https://github.com/sinmofun/atp.git
cd atp
```

## 本地开发流程

### 1. 创建特性分支

```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/your-bug-fix
```

### 2. 编写代码

- 新增指令：在 `commands/` 目录下创建对应文件
- 平台相关代码：使用 `_windows.go` / `_unix.go` 后缀
- 核心引擎修改：仅限于 `engine/` 目录

### 3. 运行测试

```bash
# 运行所有测试
go test ./...

# 运行指定包的测试
go test ./commands/

# 使用 vet 检查代码
go vet ./...
```

### 4. 编译验证

```bash
# Linux
go build -o atp_ws ./server/atp_ws.go

# Windows
go build -o atp_ws.exe ./server/atp_ws.go
```

### 5. 提交代码

```bash
git add .
git commit -m "feat: add new feature description"
git push origin feature/your-feature-name
```

### 6. 创建 Pull Request

在 GitHub 上从你的分支创建 PR 到 `main` 分支。

## 代码规范

### 文件命名

```
指令文件:     command_name.go
平台实现:     command_name_windows.go / command_name_unix.go
测试文件:     main_command_name_test.go (放在 cmd/ 目录)
```

### 指令注册

每个指令必须包含 `init()` 函数自动注册:

```go
func init() {
    engine.DefaultRegister.Register("command_name", CommandName{})
}
```

### 错误处理

使用 `engine.NewErrorResult()` 返回统一错误:

```go
return engine.NewErrorResult("", "command_name: error description")
```

## 提交规范 (Commit Convention)

### 提交信息格式

```
<type>: <description>
```

### Type 类型

| Type | 说明 |
|------|------|
| `feat` | 新功能 |
| `fix` | 修复 bug |
| `docs` | 文档更新 |
| `test` | 测试相关 |
| `refactor` | 代码重构 |
| `chore` | 构建/工具/依赖更新 |

### 提交示例

```bash
git commit -m "feat: add terminal PTY support for Linux"
git commit -m "fix: resolve ResolveWorkdirPath path parsing issue"
git commit -m "docs: update README with project description"
git commit -m "test: add Windows terminal multidimensional tests"
git commit -m "refactor: extract common exec logic to base"
```

## 测试指南

### 新增指令测试

1. 在 `cmd/` 目录下创建 `main_command_name_test.go`
2. 覆盖基本功能、边界情况、错误处理
3. Linux 和 Windows 下分别测试

### 跨平台测试

```bash
# Linux
go run ./cmd/main_terminal_check.go

# Windows
go run ./cmd/main_terminal_win_1.go
```

## 发布流程

1. 更新 `README.md` 中的版本号
2. 更新 `TEST_REPORT.md` 中的测试数据
3. 创建版本标签: `git tag -a vX.Y.Z -m "release vX.Y.Z"`
4. 推送标签: `git push origin vX.Y.Z`

## 问题反馈

- 提交 Bug: [GitHub Issues](https://github.com/sinmofun/atp/issues)
- 功能建议: 通过 Issue 提交并添加 `enhancement` 标签