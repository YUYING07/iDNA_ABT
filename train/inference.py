import torch
from model import iDNA_ABT
import pickle
from main import load_data, model_eval
import torch.nn as nn


def test(CKPT_PATH, path_config_data):
    config = pickle.load(open(path_config_data, 'rb'))
    train_iter, test_iter = load_data(config)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = iDNA_ABT.BERT(config)
    model = model.to(device)
    model.load_state_dict(torch.load(CKPT_PATH))
    criterion = nn.CrossEntropyLoss()
    last_test_metric, last_test_loss, last_test_repres_list, last_test_label_list, \
    last_test_roc_data, last_test_prc_data = model_eval(test_iter, model, criterion, config)
    print('[ACC,\tPrecision,\tSensitivity,\tSpecificity,\tF1,\tAUC,\tMCC]')
    print(last_test_metric.numpy())
    print('*' * 60 + 'The Last Test Over' + '*' * 60)


if __name__ == '__main__':
    CKPT_PATH = "../result/iDNA_ABT_train/ACC[0.7377], iDNA_ABT_train.pt"
    path_config_data = "../result/iDNA_ABT_train/config.pkl"
    test(CKPT_PATH, path_config_data)
