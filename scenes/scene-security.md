# 安全与加密

## 生成 SSH 密钥

```atp
terminal#t1:ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
```

```json
{"id":"t1","code":0,"text":"success","data":"SSH key generated"}
```

---

## 查看证书信息

```atp
terminal#t2:openssl x509 -in cert.pem -noout -subject -dates
```

```json
{"id":"t2","code":0,"text":"success","data":"subject=CN=example.com\nnotBefore=Jan 1 2026\nnotAfter=Dec 31 2026"}
```

---

## 文件加密

```atp
terminal#t3:gpg -c --batch --passphrase "secret" ./config.yaml
```

```json
{"id":"t3","code":0,"text":"success","data":"config.yaml.gpg created"}
```

---

## 检查文件完整性

```atp
terminal#t4:sha256sum ./app.exe
```

```json
{"id":"t4","code":0,"text":"success","data":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  ./app.exe"}
```