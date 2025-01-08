import wandb
from ultralytics import YOLO

# Disable Weights & Biases (wandb) if not used
wandb.init(mode='disabled')

# Initialize the YOLOv11 model
model = YOLO('yolo11n.pt')  # Ensure 'yolo11n.pt' is available

# Train the model
results = model.train(
    data='data.yaml',
    epochs=50,
    imgsz=640,
    save=True,
    device='cpu',     
)
