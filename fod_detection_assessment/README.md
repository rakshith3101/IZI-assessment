# FOD Detection Assessment

YOLO baseline for the FOD-A airport foreign-object-debris dataset.

Install dependencies, download the Pascal VOC archive from `dataset/README.md`, then run:

```powershell
pip install -r requirements.txt
python scripts/prepare_dataset.py --voc_zip data/download/FOD-A-V2.1-PascalVOC.zip
python scripts/eda.py
python scripts/train.py
python scripts/evaluate.py
```

Outputs are written to `runs/` and `submission/`.
