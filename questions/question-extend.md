# 如何扩展 AITP？

## 问题

我想为 AITP 添加自定义指令，该怎么做？

## 解答

AITP 的指令系统支持热插拔，新增指令只需实现 Command 接口并注册即可：

```go
type LightCommand struct{}

func (c LightCommand) Execute(params *engine.Params) *engine.Result {
    action := params.MainParam
    name := params.Get("name")
    return engine.NewResult("", fmt.Sprintf("%s light %s", name, action))
}

func init() {
    engine.DefaultRegister.Register("light", LightCommand{})
}
```

添加后即可使用：
```atp
light#l1:ON
name:living_room
```