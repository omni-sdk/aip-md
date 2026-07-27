# 数据科学家

## 角色描述
数据科学家负责数据分析、模型训练、数据处理和可视化。

## 常用指令

### 运行 Python 脚本

```atp
terminal#t1:python3 analysis.py --input data.csv --output result.json
workdir:./project
timeout:300s
```

```json
{"id":"t1","code":0,"text":"success","data":"analysis completed, result saved to result.json"}
```

### 安装依赖

```atp
terminal#t2:pip install numpy pandas matplotlib scikit-learn
timeout:120s
```

```json
{"id":"t2","code":0,"text":"success","data":"4 packages installed"}
```

### 数据处理

```atp
terminal#t3:python3 -c "import pandas as pd; df = pd.read_csv('data.csv'); print(df.describe())"
workdir:./data
```

```json
{"id":"t3","code":0,"text":"success","data":"count  1000.0\nmean   45.6\nstd    12.3"}
```

### 训练模型

```atp
terminal#t4:python3 train.py --epochs 50 --batch-size 32 --output model.pkl
workdir:./project
timeout:600s
```

```json
{"id":"t4","code":0,"text":"success","data":"model trained, accuracy: 94.2%"}
```

### 下载数据集

```atp
fetch#f1:https://dataset.example.com/large-dataset.zip
save:./data/dataset.zip
```

```json
{"id":"f1","code":0,"text":"success","data":"./data/dataset.zip"}
```