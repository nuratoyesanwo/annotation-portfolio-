"""
coco_to_csv.py
Converts a COCO-format JSON annotation file to a flat CSV.
Usage: python coco_to_csv.py --input annotations.json --output labels.csv
"""

import json
import csv
import argparse
from pathlib import Path


def load_coco(path):
    with open(path, "r") as f:
        return json.load(f)


def coco_to_rows(data):
    image_map = {img["id"]: img for img in data.get("images", [])}
    category_map = {cat["id"]: cat["name"] for cat in data.get("categories", [])}

    rows = []
    for ann in data.get("annotations", []):
        img = image_map.get(ann["image_id"], {})
        bbox = ann.get("bbox", [None, None, None, None])
        rows.append({
            "annotation_id": ann["id"],
            "image_id": ann["image_id"],
            "file_name": img.get("file_name", ""),
            "image_width": img.get("width", ""),
            "image_height": img.get("height", ""),
            "category_id": ann["category_id"],
            "category_name": category_map.get(ann["category_id"], "unknown"),
            "bbox_x": bbox[0],
            "bbox_y": bbox[1],
            "bbox_w": bbox[2],
            "bbox_h": bbox[3],
            "area": ann.get("area", ""),
            "iscrowd": ann.get("iscrowd", 0),
        })
    return rows


def write_csv(rows, output_path):
    if not rows:
        print("No annotations found.")
        return
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} rows to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Convert COCO JSON to CSV")
    parser.add_argument("--input", required=True, help="Path to COCO JSON file")
    parser.add_argument("--output", required=True, help="Path for output CSV file")
    args = parser.parse_args()

    data = load_coco(args.input)
    rows = coco_to_rows(data)
    write_csv(rows, args.output)


if __name__ == "__main__":
    main()
