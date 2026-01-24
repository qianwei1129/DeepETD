import yaml
import json
import pandas as pd
import numpy as np
import torch
from data_loader import get_dataloaders, extract_names_from_text_json, set_seed
from model import InteractionPredictionModel_NoAttention, InteractionPredictionModel


def predict(model, dataloader):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    model.eval()

    scores = []
    with torch.no_grad():
        for inputs, _ in dataloader:
            (cd, cp, cs, pd, pp, ps) = inputs
            cd, cp, cs, pd, pp, ps = cd.to(device), cp.to(device), cs.to(device), pd.to(device), pp.to(device), ps.to(device)
            logits = model(cd, cp, cs, pd, pp, ps)
            probs = torch.sigmoid(logits).cpu().numpy().ravel()
            scores.extend(probs.tolist())
    return np.array(scores)


def save_topk_per_compound(scores, protein_names, compound_names, output_path, topk=20):
    """
    使用pandas的简洁版本
    """
    # 创建DataFrame
    df = pd.DataFrame({
        'Compound': compound_names,
        'Protein': protein_names,
        'Score': scores
    })

    # 按化合物分组，对每个化合物按分数排序
    results = {}

    # 使用groupby处理
    for compound, group in df.groupby('Compound'):
        # 排序并取TopK
        sorted_group = group.sort_values('Score', ascending=False).head(topk)

        results[compound] = {
            "Protein Names": sorted_group['Protein'].tolist(),
            "Prediction Scores": sorted_group['Score'].tolist(),
            "Score Type": "sigmoid_probability"
        }

    # 保存
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=4)

    print(f"已保存 {len(results)} 个化合物的Top{topk}结果到: {output_path}")
    return results


def DeepETD_predict(config_path='predict_config.yaml'):
    """

    :param config_path:
    :return:
    """
    # 加载配置
    with open(config_path, 'r') as f:
        cfg = yaml.safe_load(f)

    # 设置随机种子
    set_seed(cfg['prediction']['seed'])

    # 获取数据加载器
    loaded = get_dataloaders(
        disease_json_path=cfg['data']['disease_json'],
        phenotype_json_path=cfg['data']['phenotype_json'],
        positive_json_path=cfg['data']['positive_json'],
        negative_json_path=cfg['data']['negative_json'],
        text_json_path=cfg['data']['text_json'],
        batch_size=cfg['prediction']['batch_size'],
        val_split=cfg['prediction']['val_split'],
        seed=cfg['prediction']['seed'],
    )

    enc = loaded['encoders']
    model_params = cfg['model']['params'].copy()
    model_params.update({
        'num_diseases': len(enc['disease'].classes_),
        'num_phenotypes': len(enc['phenotype'].classes_),
        'num_subcellular_locations': len(enc['subcellular'].classes_),
    })

    model_class = InteractionPredictionModel if cfg['model']['use_attention'] \
        else InteractionPredictionModel_NoAttention
    model = model_class(**model_params)

    state = torch.load(cfg['model']['checkpoint'], map_location='cpu')
    model.load_state_dict(state)

    protein_names, compound_names = extract_names_from_text_json(cfg['data']['text_json'])

    scores = predict(model, loaded['text'])

    n = min(len(scores), len(protein_names), len(compound_names))
    save_topk_per_compound(
        scores[:n],
        protein_names[:n],
        compound_names[:n],
        cfg['prediction']['output_file'],
        topk=cfg['prediction']['topk']
    )


if __name__ == '__main__':
    DeepETD_predict(config_path='config.yaml')

