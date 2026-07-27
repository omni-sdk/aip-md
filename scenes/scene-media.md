# 多媒体处理

## 视频格式转换

```atp
terminal#t1:ffmpeg -i input.avi -c:v libx264 -c:a aac output.mp4
workdir:./videos
timeout:300s
```

```json
{"id":"t1","code":0,"text":"success","data":"conversion completed"}
```

---

## 音频提取

```atp
terminal#t2:ffmpeg -i video.mp4 -vn -acodec mp3 audio.mp3
workdir:./videos
timeout:120s
```

```json
{"id":"t2","code":0,"text":"success","data":"audio extracted"}
```

---

## 图片批量压缩

```atp
terminal#t3:for f in *.png; do convert "$f" -quality 80 "compressed_$f"; done
workdir:./images
timeout:120s
```

```json
{"id":"t3","code":0,"text":"success","data":"12 images compressed"}
```

---

## 视频截图

```atp
terminal#t4:ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumb.jpg
workdir:./videos
```

```json
{"id":"t4","code":0,"text":"success","data":"thumbnail captured"}
```