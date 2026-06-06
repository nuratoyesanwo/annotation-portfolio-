# QA Error Taxonomy

Used for systematic error analysis in segmentation and annotation QA reviews.

---

## Error Categories

### MERGE
**Definition:** Two or more distinct instances are incorrectly combined into a single segment or annotation.

**Example:** Two adjacent pedestrians annotated as one person instance.

**How to flag:** Note both instance IDs that were merged. Record in the tracker under the annotator's name with error type `MERGE`.

---

### OVER (Over-segmentation)
**Definition:** A single instance is split into multiple separate segments or annotations.

**Example:** One car annotated as two separate objects (front half and back half).

**How to flag:** Note the image ID, the incorrectly split annotations, and the correct expected count.

---

### UNDER (Under-segmentation)
**Definition:** The annotation boundary does not cover the full extent of the object — the mask or bounding box is too small.

**Example:** A bounding box that clips the top of a person's head or excludes part of a vehicle.

**How to flag:** Record image ID, annotation ID, and estimate the percentage of the object missed.

---

### FP (False Positive)
**Definition:** An annotation is placed on a region where no valid object is present.

**Example:** A region of road texture annotated as a road marking.

**How to flag:** Record image ID and annotation ID. Note the class that was falsely applied.

---

### MISCLASS (Misclassification)
**Definition:** An object is correctly detected and segmented, but assigned the wrong class label.

**Example:** A utility pole annotated as `tree` instead of `pole`.

**How to flag:** Record image ID, annotation ID, the incorrect class assigned, and the correct class.

---

## Tracker Columns

When logging errors in the performance tracker, use these columns:

| Column | Description |
|---|---|
| `image_id` | Unique image identifier |
| `annotation_id` | ID of the affected annotation |
| `annotator` | Name of the annotator responsible |
| `error_type` | One of: MERGE, OVER, UNDER, FP, MISCLASS |
| `severity` | Low / Medium / High |
| `notes` | Brief description of the specific issue |
| `resolved` | Yes / No |

---

## Severity Guide

- **Low** — Minor boundary imprecision; does not affect downstream model training significantly
- **Medium** — Incorrect class or significant boundary error; may affect training quality
- **High** — Missing instance, large-scale merge, or systematic pattern across multiple images
