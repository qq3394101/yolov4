from utils.dataloader import YoloDataset

txt = "2007_train.txt"
with open(txt) as f:
    lines = f.readlines()
dataset = YoloDataset(lines, (416, 416), mosaic=False, is_train=True)
for i, data in enumerate(dataset):
    print(data[0].shape)
    print(data[1].shape)
    print(data[1])
    if i == 4:
        break