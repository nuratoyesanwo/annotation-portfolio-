# Data Annotation & AI Evaluation Portfolio
**Nurat Oyesanwo** · Lagos, Nigeria · [LinkedIn](#) · [Email](#)

---

## About

I'm a Data Annotator and AI Evaluation Specialist with hands-on experience across computer vision annotation, 3D point cloud segmentation, egocentric video labeling, and RLHF-style AI output evaluation. I have led annotation teams as Team Captain, conducted QA reviews, and built pipelines for multimodal dataset creation.

This repository contains reusable scripts, templates, and documentation from my annotation and AI evaluation work.

---

## Core Specialisations

| Domain | Skills & Tools |
|---|---|
| **Computer Vision** | 2D/3D bounding boxes, panoptic segmentation, semantic segmentation, instance segmentation |
| **3D / LiDAR** | Point cloud segmentation, LiDAR object labeling |
| **Video Annotation** | Egocentric video labeling, temporal action annotation, AI-caption auditing |
| **AI Evaluation** | RLHF-style review, rubric-based output scoring, hallucination detection, NER classification |
| **Team Leadership** | Team Captain, QA Reviewer, error analysis, annotator performance tracking |
| **Platforms** | CVAT · Labelbox · Supervisely · Segment AI · FastLabel |

---

## Repository Structure

```
annotation-portfolio/
│
├── scripts/                   # Python utility scripts
│   ├── coco_to_csv.py         # Convert COCO JSON annotations to CSV
│   ├── bbox_validator.py      # Validate bounding box coordinates
│   └── label_stats.py         # Generate label distribution stats
│
├── guidelines/                # Annotation guideline templates
│   ├── panoptic_seg_guide.md  # Panoptic segmentation conventions
│   ├── video_caption_guide.md # Egocentric video labeling conventions
│   └── ner_classification.md  # NER tagging reference
│
├── qa-templates/              # QA review and error tracking templates
│   ├── error_taxonomy.md      # Error categories: MERGE, OVER, UNDER, FP, MISCLASS
│   ├── qa_checklist.md        # Pre-submission QA checklist
│   └── annotator_tracker.xlsx # Team performance tracker (template)
│
└── resources/                 # Reference materials and notes
    └── annotation_formats.md  # COCO, YOLO, Pascal VOC format cheatsheet
```

---

## Highlighted Work

### Panoptic Segmentation — Japan Ver 1.3.2
- Served as **Team Captain and QA Reviewer**, managing a team of 6 annotators
- Conducted systematic error analysis using a defined taxonomy (MERGE, OVER, UNDER, FP, MISCLASSIFICATION)
- Maintained a multi-sheet Excel tracker for individual annotator performance
- Produced QA reports and manager-facing summaries

### Egocentric Video Labeling — Atlas Capture
- Labeled egocentric video footage for manipulation task datasets
- Applied strict conventions for hand description, spatial anchoring, bimanual annotation, and action lifecycle documentation
- Audited AI-generated captions against project guidelines for correctness and completeness

### Multimodal Visual Reasoning Dataset
- Annotated image-prompt pairs with structured answers and expert chain-of-thought reasoning
- Built task submissions aligned to rubric criteria for factuality, logical flow, and context awareness

---

## Scripts Overview

### `coco_to_csv.py`
Converts a COCO-format JSON annotation file to a flat CSV for easier review and filtering.

```bash
python scripts/coco_to_csv.py --input annotations.json --output labels.csv
```

### `bbox_validator.py`
Checks that all bounding boxes in an annotation file are within image bounds and have valid dimensions.

```bash
python scripts/bbox_validator.py --input annotations.json
```

### `label_stats.py`
Generates a category distribution report from a COCO annotation file — useful for spotting class imbalances before QA.

```bash
python scripts/label_stats.py --input annotations.json
```

---

## QA Error Taxonomy

Used for systematic error analysis in segmentation projects:

| Code | Name | Description |
|---|---|---|
| `MERGE` | Merge error | Two or more distinct instances incorrectly merged into one |
| `OVER` | Over-segmentation | One instance split into multiple segments |
| `UNDER` | Under-segmentation | Segment boundary does not cover the full extent of the instance |
| `FP` | False positive | Region labeled as an object when none is present |
| `MISCLASS` | Misclassification | Instance annotated with the wrong class label |

---

## Annotation Format Reference

Quick reference for common export formats:

- **COCO JSON** — Used by Labelbox, CVAT; supports bounding boxes, segmentation masks, keypoints
- **YOLO TXT** — One `.txt` per image; class index + normalised bbox coordinates
- **Pascal VOC XML** — Per-image XML files; common in older CV pipelines
- **Supervisely JSON** — Platform-native format with rich metadata support

---

## Contact

Open to remote data annotation, AI training, and AI evaluation roles.
Reach me at: **[your email]** · LinkedIn: **[your profile]**
