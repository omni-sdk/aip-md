# API 集成与 Webhook

## 调用天气 API

```atp
fetch#f1:https://api.openweathermap.org/data/2.5/weather?q=Beijing&appid=YOUR_KEY
```

```json
{"id":"f1","code":0,"text":"success","data":"{\"weather\":[{\"main\":\"Clear\"}],\"main\":{\"temp\":28.5}}"}
```

---

## 发送 Webhook 通知

```atp
fetch#f2:https://hooks.slack.com/services/T00/B00/xxx
method:post
payload@p2:
{"text":"Deployment completed successfully"}
p2
```

```json
{"id":"f2","code":0,"text":"success","data":"ok"}
```

---

## 获取 GitHub 仓库信息

```atp
fetch#f3:https://api.github.com/repos/sinmofun/atp
header@h3:
Accept:application/vnd.github.v3+json
h3
```

```json
{"id":"f3","code":0,"text":"success","data":"{\"name\":\"atp\",\"stargazers_count\":0,\"language\":\"Go\"}"}
```

---

## 发送邮件

```atp
terminal#t1:echo "Build completed" | mail -s "CI Notification" admin@example.com
```

```json
{"id":"t1","code":0,"text":"success","data":"email sent"}
```