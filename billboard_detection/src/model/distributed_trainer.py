from typing import List
import torch
import torch.distributed as dist
from torch.nn import Module
from torch.utils.data import DataLoader

class DistributedTrainer:
    def __init__(self, model: Module, train_dataset: List, batch_size: int, num_epochs: int):
        self.model = model
        self.train_dataset = train_dataset
        self.batch_size = batch_size
        self.num_epochs = num_epochs
        self.train_loader = DataLoader(train_dataset, batch_size=batch_size)

    def setup(self):
        dist.init_process_group(backend='nccl')
        self.model = self.model.to(dist.get_rank())
        self.model = torch.nn.parallel.DistributedDataParallel(self.model)

    def train(self):
        self.setup()
        for epoch in range(self.num_epochs):
            for batch in self.train_loader:
                self.train_step(batch)

    def train_step(self, batch):
        inputs, targets = batch
        outputs = self.model(inputs)
        loss = self.compute_loss(outputs, targets)
        loss.backward()
        self.optimizer.step()
        self.optimizer.zero_grad()

    def compute_loss(self, outputs, targets):
        return torch.nn.functional.cross_entropy(outputs, targets)

    def cleanup(self):
        dist.destroy_process_group()