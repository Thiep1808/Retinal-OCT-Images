import torch
import torch.nn as nn

from torch.optim import Adam
from dataset import MyDataset
from torch.utils.data import DataLoader
from utils import train_step, val_step, test_step, load_checkpoint, save_checkpoint, Confusion_Matrix
from model import Model
from torch.utils.tensorboard import SummaryWriter

def main():

    # Create tensorboard file to keep track process training
    import albumentations as A
    from albumentations.pytorch import ToTensorV2

    writer = SummaryWriter(f'/home/grasp/Grasp_simulation/pythonProject1/Retinal_OCT_Images/chech_point')
    step = 0
    iteration = 0

    train_transform = A.Compose(
        [A.RandomCrop(width=400, height=400, p=0.5),
         A.Resize(width=512, height=512),
         A.HorizontalFlip(p=0.5),
         A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0),
         ToTensorV2(),
         ],
    )
    test_transform = A.Compose(
        [A.Resize(width=512, height=512),
         A.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255.0),
         ToTensorV2(),
         ],
    )

    class_labels = ['Normal', 'AMD', 'DME']
    epochs = 200
    batch_size = 4
    num_workers = 4
    lr = 0.001
    weigh_decay = 2e-5
    device = 'cuda'

    # Setup data and split data
    root = '/home/grasp/Downloads/Macular Dataset-Heidelberg/Dataset_3x50_Final'
    train_dataset = MyDataset(root, 'train', train_transform)
    test_dataset = MyDataset(root, 'test', test_transform)
    train_dataloader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=False,
    )

    test_dataloader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=False,
    )

    # Setup all necessary of model
    model = Model().to(device)

    optimizer = Adam(model.parameters(), lr=lr, weight_decay=weigh_decay)
    loss_fn = nn.CrossEntropyLoss()

    for epoch in range(epochs):


        print(f'Epoch: {epoch + 1}')

        # Training process
        train_loss, train_acc, iteration = train_step(model, train_dataloader, loss_fn, optimizer, device, writer, iteration)
        print(f'Train loss: {train_loss:.4f} | Train accuracy: {train_acc * 100:.2f}%')

        # Validation process
        val_loss, val_acc, y_preds_tensor = val_step(model, test_dataloader, loss_fn, device)
        test_targets = torch.Tensor([target for _, target in test_dataset])
        Confusion_Matrix(class_labels, y_preds_tensor, test_targets, epoch)
        # Print information
        print(f'Validation loss: {val_loss:.4f} | Validation accuracy: {val_acc * 100:.2f}%')

        writer.add_scalar(f'Validation Loss', val_loss, global_step=step)
        writer.add_scalar(f'Validation Accuracy', val_acc, global_step=step)
        step += 1
        # Sve model each 5 epochs
        if (epoch + 1) % 5 == 0:
            save_checkpoint(model, optimizer, epoch, f"/home/ana/Study/New/check_point3/model_checkpoint_{epoch}.pt")
        print('--------------------------------------------------------------------')

    # Final testing process
    test_loss, test_acc, y_preds_tensor = test_step(model, test_dataloader, loss_fn, device)
    print(f'Test loss: {test_loss:.4f} | Test accuracy: {test_acc * 100:.2f}%')
    test_targets = torch.Tensor([target for _, target in test_dataset])
    Confusion_Matrix(class_labels, y_preds_tensor, test_targets)


if __name__ == '__main__':
    main()
