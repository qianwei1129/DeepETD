# DeepETD

<!-- Language Selector -->
<p align="center">
  <a href="#english">English</a> | 
  <a href="#chinese">中文</a>
</p>

---

<div id="english">

# DeepETD: Deep Learning for Endogenous Metabolite-Target Protein Interaction Prediction

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 Overview
DeepETD is a deep learning model designed to predict interactions between endogenous metabolites and target proteins. This tool can accelerate drug discovery and metabolic pathway analysis by identifying potential protein targets for metabolites.

## ✨ Features
- Multi-modal data integration (disease, phenotype, structural information)
- Handling of imbalanced datasets with positive sample weighting
- Efficient training with early stopping
- Top-k prediction export for downstream analysis

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AIDDHao/DeepETD
   cd DeepETD
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Project Structure
```
DeepETD/
├── train.py              # Training script
├── predict.py            # Prediction script
├── requirements.txt      # Python dependencies
├── Data/                 # Data directory
│   ├── disease_list.json
│   ├── phenotype.json
│   ├── pos_datasets.json
│   ├── neg_datasets.json
│   └── predict_datasets.json
├── models/               # Model architecture
├── utils/                # Utility functions
└── README.md
```

## 🚀 Quick Start

### 1) Training the Model
Train the DeepETD model with your dataset:
```bash
python train.py \
  --disease_json ../Data/disease_list.json \
  --phenotype_json ../Data/phenotype.json \
  --positive_json ../Data/pos_datasets.json \
  --negative_json ../Data/neg_datasets.json \
  --predict_json ../Data/predict_datasets.json \
  --model_out best_model.pth \
  --epochs 20 \
  --patience 10 \
  --pos_weight 3.0
```

### 2) Making Predictions
Use the trained model to predict metabolite-protein interactions:
```bash
python predict.py \
  --disease_json ../Data/disease_list.json \
  --phenotype_json ../Data/phenotype.json \
  --positive_json ../Data/pos_datasets.json \
  --negative_json ../Data/neg_datasets.json \
  --predict_json ../Data/predict_datasets.json \
  --checkpoint best_model.pth \
  --out predictions.json
```

## ⚙️ Parameters

### Training Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--disease_json` | str | Required | Path to disease data JSON |
| `--phenotype_json` | str | Required | Path to phenotype data JSON |
| `--positive_json` | str | Required | Path to positive samples JSON |
| `--negative_json` | str | Required | Path to negative samples JSON |
| `--predict_json` | str | Required | Path to prediction dataset JSON |
| `--model_out` | str | `best_model.pth` | Output model checkpoint path |
| `--epochs` | int | `20` | Maximum training epochs |
| `--patience` | int | `10` | Early stopping patience |
| `--pos_weight` | float | `3.0` | Weight for positive samples in loss |

### Prediction Parameters
| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--checkpoint` | str | Required | Path to trained model checkpoint |
| `--out` | str | `predictions.json` | Output predictions file path |

## 📊 Output Format

### Training Output
- Model checkpoint file (`.pth`)
- Training logs with loss and metrics

### Prediction Output
JSON file containing predictions with the following structure:
```json
{
  "compound_id": [
    {"protein": "P12345", "score": 0.95},
    {"protein": "Q67890", "score": 0.87},
    ...
  ],
  ...
}
```
Top-20 proteins are returned for each compound.

## 📝 Technical Notes

### Model Architecture
- The model outputs raw logits
- Uses `BCEWithLogitsLoss` during training (more numerically stable)
- Applies `sigmoid` activation only for metrics and predictions

### Data Processing
- Vocabulary sizes are dynamically determined from fitted label encoders
- Handles empty modality lists by falling back to index 0
- Supports custom `<UNK>` token configuration if needed

### Performance Tips
- Adjust `--pos_weight` based on your dataset imbalance
- Monitor validation loss for optimal early stopping
- Use GPU acceleration for faster training (if available)

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact
For questions and support, please open an issue on GitHub.

## 🙏 Acknowledgments
- Thanks to all contributors and users
- Built with PyTorch and scientific Python ecosystem

---

</div>

<div id="chinese">

# DeepETD: 内源性代谢物-靶蛋白相互作用预测深度学习模型

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-ee4c2c.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📋 概述
DeepETD 是一个深度学习模型，专门用于预测内源性代谢物与靶蛋白之间的相互作用。该工具可通过识别代谢物的潜在蛋白靶点，加速药物发现和代谢通路分析。

## ✨ 功能特点
- 多模态数据整合（疾病、表型、结构信息）
- 处理不平衡数据集，支持正样本加权
- 带有早停机制的高效训练
- 支持 top-k 预测结果导出，便于下游分析

## 📥 安装

### 环境要求
- Python 3.8 或更高版本
- pip 包管理器

### 逐步安装指南
1. 克隆仓库：
   ```bash
   git clone https://github.com/AIDDHao/DeepETD
   cd DeepETD
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 📁 项目结构
```
DeepETD/
├── train.py              # 训练脚本
├── predict.py            # 预测脚本
├── requirements.txt      # Python依赖包
├── Data/                 # 数据目录
│   ├── disease_list.json
│   ├── phenotype.json
│   ├── pos_datasets.json
│   ├── neg_datasets.json
│   └── predict_datasets.json
├── models/               # 模型架构
├── utils/                # 工具函数
└── README.md
```

## 🚀 快速开始

### 1) 训练模型
使用您的数据集训练 DeepETD 模型：
```bash
python train.py \
  --disease_json ../Data/disease_list.json \
  --phenotype_json ../Data/phenotype.json \
  --positive_json ../Data/pos_datasets.json \
  --negative_json ../Data/neg_datasets.json \
  --predict_json ../Data/predict_datasets.json \
  --model_out best_model.pth \
  --epochs 20 \
  --patience 10 \
  --pos_weight 3.0
```

### 2) 进行预测
使用训练好的模型预测代谢物-蛋白质相互作用：
```bash
python predict.py \
  --disease_json ../Data/disease_list.json \
  --phenotype_json ../Data/phenotype.json \
  --positive_json ../Data/pos_datasets.json \
  --negative_json ../Data/neg_datasets.json \
  --predict_json ../Data/predict_datasets.json \
  --checkpoint best_model.pth \
  --out predictions.json
```

## ⚙️ 参数说明

### 训练参数
| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--disease_json` | str | 必需 | 疾病数据JSON文件路径 |
| `--phenotype_json` | str | 必需 | 表型数据JSON文件路径 |
| `--positive_json` | str | 必需 | 正样本数据JSON文件路径 |
| `--negative_json` | str | 必需 | 负样本数据JSON文件路径 |
| `--predict_json` | str | 必需 | 预测数据集JSON文件路径 |
| `--model_out` | str | `best_model.pth` | 模型检查点输出路径 |
| `--epochs` | int | `20` | 最大训练轮数 |
| `--patience` | int | `10` | 早停耐心值 |
| `--pos_weight` | float | `3.0` | 损失函数中正样本权重 |

### 预测参数
| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `--checkpoint` | str | 必需 | 训练好的模型检查点路径 |
| `--out` | str | `predictions.json` | 预测结果输出文件路径 |

## 📊 输出格式

### 训练输出
- 模型检查点文件（`.pth`格式）
- 包含损失和指标的训练日志

### 预测输出
JSON格式的预测结果，结构如下：
```json
{
  "化合物ID": [
    {"protein": "P12345", "score": 0.95},
    {"protein": "Q67890", "score": 0.87},
    ...
  ],
  ...
}
```
每个化合物返回前20个得分最高的蛋白质。

## 📝 技术说明

### 模型架构
- 模型输出原始 logits
- 训练时使用 `BCEWithLogitsLoss`（数值更稳定）
- 仅在计算指标和预测时应用 `sigmoid` 激活函数

### 数据处理
- 词汇表大小根据拟合的标签编码器动态确定
- 处理空模态列表时回退到索引 0
- 支持自定义 `<UNK>` 标记配置

### 性能优化建议
- 根据数据集不平衡程度调整 `--pos_weight` 参数
- 监控验证损失以优化早停策略
- 如有可用GPU，可加速训练过程

## 🤝 贡献指南
欢迎贡献代码！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建功能分支 (`git checkout -b feature/新功能`)
3. 提交更改 (`git commit -m '添加新功能'`)
4. 推送分支 (`git push origin feature/新功能`)
5. 打开 Pull Request

## 📄 许可证
本项目采用 MIT 许可证 - 详情请见 [LICENSE](LICENSE) 文件。

## 📧 联系方式
如有问题或需要支持，请在 GitHub 上提交 issue。

## 🙏 致谢
- 感谢所有贡献者和用户
- 基于 PyTorch 和科学 Python 生态系统构建

---

</div>

<p align="center">
  <sub>最后更新: 2026年 | 版本: 1.0.0</sub>
</p>

<!-- Back to top links -->
<p align="center">
  <a href="#english">↑ 返回英文版</a> • 
  <a href="#chinese">↑ 返回中文版</a> • 
  <a href="#top">↑ 返回顶部</a>
</p>
```

