from pathlib import Path
from ultralytics import YOLO
root=Path(__file__).parents[1]
checkpoint=root/'runs/fod_yolov8s_gpu_5ep/weights/last.pt'
model=YOLO(str(checkpoint) if checkpoint.exists() else 'yolov8s.pt')
model.train(data=str(root/'data/fod_clean/fod.yaml'), imgsz=640, epochs=15, batch=16, patience=5, workers=0, device=0, amp=True, optimizer='AdamW', project=str(root/'runs'), name='fod_yolov8s_gpu_15ep', pretrained=True, resume=checkpoint.exists(), degrees=5, translate=.1, scale=.5, fliplr=.5, hsv_h=.015, hsv_s=.5, hsv_v=.3)
