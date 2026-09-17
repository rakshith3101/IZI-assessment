from pathlib import Path
from ultralytics import YOLO
root=Path(__file__).parents[1]; w=root/'runs/fod_yolov8s_gpu_5ep/weights/best.pt'; m=YOLO(str(w))
m.val(data=str(root/'data/fod_clean/fod.yaml'), split='test', imgsz=640, workers=0, device=0, project=str(root/'runs'), name='test_metrics', plots=True, save_json=True)
m.predict(source=str(root/'data/fod_clean/images/test'), imgsz=640, conf=.25, workers=0, device=0, save=True, save_txt=True, save_conf=True, project=str(root/'submission'), name='test_predictions')
