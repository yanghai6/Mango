from torch.utils.data import DataLoader
import torch


def get_data_loader(model, split=0.8, batch_size=32):
    dataset_len = len(model)
    train_size = int(split * dataset_len)
    val_size = dataset_len - train_size
    train_set, val_set = torch.utils.data.random_split(model, [train_size, val_size])

    return DataLoader(train_set, batch_size=batch_size), DataLoader(
        val_set, batch_size=batch_size
    )
