# AITP 如何支持跨平台？

## 问题

AITP 在 Linux 和 Windows 上的行为是否一致？

## 解答

AITP 的指令格式在 Linux 和 Windows 上是完全一致的，但底层实现不同：
- Linux: 使用 PTY 伪终端，支持交互式命令和后台进程
- Windows: 使用临时 BAT 脚本执行，功能等价

指令语法是统一的，但执行的命令语法需要根据平台编写。例如 `ping` 命令在 Linux 和 Windows 上的参数不同：
- Linux: `ping -c 4 8.8.8.8`
- Windows: `ping -n 4 8.8.8.8`