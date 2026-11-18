# Fashion attribute extraction: data splits and masking code

Code and data splits accompanying the paper "Lightweight Multimodal Deep Learning for Fine-Grained Fashion Attribute Extraction Using Gated Fusion with Label Leakage Mitigation".

## Files

| File | Description |
|---|---|
| `masking.py` | Keyword dictionary (`ATTR_KEYWORDS`), category map (`ATTR_CATEGORY_MAP`) and `mask_text()`, the exact code used for label-leakage masking. |
| `notebook.ipynb` | Notebook for data preparation, training and evaluation. |
| `train_split.csv`, `val_split.csv`, `test_split.csv` | Stratified splits (by category, seed 42, 70/15/15): 22,185 / 4,754 / 4,754 items. |

## Split columns

`image`, `brand`, `category`, `color`, `pattern`, `material`, `sleeve_type`, `fit`, `neck_type`, `heel_type`, `toe_style`, `sole_type`, `gender`, `occasion`, `closure_type`

Only `category` is a native field of the source dataset. The other twelve attribute labels were derived by the authors using rule-based extraction, followed by manual verification on a representative sample. The raw product descriptions are not redistributed.

## Masking

```python
from masking import mask_text
mask_text("Women casual white printed cotton t-shirt round neck slim fit short sleeve", "T-Shirt")
# -> "[GENDER] [OCCASION] [COLOR] [PATTERN] [MATERIAL] t-shirt [NECK] [FIT] [SLEEVE]"
```

## Running the notebook

1. Obtain the images from the original public dataset and place them in a folder named `images_final/`.
2. Set `DATA_DIR` in the first cells to the folder containing the CSV files and `images_final/`.
3. Models: ConvNeXt-Tiny (`timm`, `convnext_tiny.in12k_ft_in1k`) and DeBERTa-v3 Small with scalar gated fusion.

## Notes

- Only the data-preparation cells were re-executed for this release. The ablation cells were not re-run for it.
- Images are not included in this repository.
