# FOD Detection Assessment — 5-Epoch Baseline

## Summary

The preserved 5-epoch YOLO detector was evaluated on the held-out test split. This is a baseline result; the planned 15-epoch run was not completed and is not used here.

## Test metrics

| Metric | Result |
|---|---:|
| Test images | 5,069 |
| Precision | 0.936 |
| Recall | 0.951 |
| mAP@50 | 0.976 |
| mAP@50–95 | 0.721 |
| AP@75 | 0.885 |
| AP small objects | 0.604 |
| AP medium objects | 0.747 |
| AP large objects | 0.762 |

Evaluation used the checkpoint `runs/fod_yolov8s_gpu_5ep/weights/best.pt`, image size 640, and confidence threshold 0.25 for saved predictions.

## Interpretation

The detector finds most labelled objects and has high performance at IoU 0.50. The lower mAP@50–95 and small-object AP show that localization quality is less reliable at stricter overlap requirements, especially for small debris. This matters for runway use because small, low-contrast objects are likely to be the hardest and most safety-critical cases.

Per-class results are uneven. Examples of weaker classes include Screw (AP@50 0.828), Pen (0.919), and Wrench (0.933), while several common classes exceed 0.99 AP@50. These differences should be reported rather than hidden by the aggregate score.

## Safety threshold reasoning

The saved inference threshold was 0.25 to favour recall during analysis. A runway deployment should select its operating threshold using a validation precision–recall curve and an explicit false-alarm budget. Because a missed object can create a direct safety risk, the initial operating point should favour high recall, with human/operator review or a second-stage tracker reducing nuisance alarms.

## Error-analysis checklist

Review the saved predictions for:

- false positives on shadows, runway markings, reflections, and surface texture;
- missed small objects and low-contrast objects;
- occluded or overlapping debris;
- confusing visually similar classes;
- confidence scores near the selected operating threshold.

Likely improvements are higher-resolution or tiled inference for small debris, more diverse lighting/weather and altitude data, class balancing for rare objects, and hard-negative mining from false alarms.

## Generated artifacts

- Metrics and plots: `runs/test_metrics_5ep_final/`
- COCO-format predictions: `runs/test_metrics_5ep_final/predictions.json`
- Annotated test predictions: `submission/test_predictions_5ep_final/`
- Model checkpoint: `runs/fod_yolov8s_gpu_5ep/weights/best.pt`

The generated directory contains the confusion matrix, normalized confusion matrix, precision/recall/F1 curves, validation examples, and prediction outputs.
