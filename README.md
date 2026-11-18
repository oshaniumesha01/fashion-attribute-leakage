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

The split files are our modified version of the Kaggle dataset: the original dataset has four fields (image, description, display name, category), and we added the attribute columns above.

Only `category` is a native field of the source dataset. The other twelve attribute labels were derived by the authors using rule-based extraction, followed by manual verification on a representative sample. The raw product descriptions are not redistributed.

## Masking

```python
from masking import mask_text
mask_text("Women casual white printed cotton t-shirt round neck slim fit short sleeve")
# -> "[GENDER] [OCCASION] [COLOR] [PATTERN] [MATERIAL] t-shirt [NECK] [FIT] [SLEEVE]"
```

## Reproducing the splits and the masking

The notebook was run on a processed file (`Research final dataset.csv`) that combines the Kaggle product text with our derived attribute labels. That file is not redistributed, because it contains the raw product descriptions. The released split files are the labelled item lists derived from it.

1. Download the Kaggle dataset "Fashion Product Images and Text Dataset" (https://www.kaggle.com/datasets/nirmalsankalana/fashion-product-text-images-dataset; derived from Param Aggarwal's Fashion Product Images Dataset). It provides the images and the product text (`data.csv`).
2. Join `train_split.csv`, `val_split.csv` and `test_split.csv` with the Kaggle `data.csv` on the `image` column to recover the product text for each item.
3. Apply `mask_text()` from `masking.py` to the text, as in the notebook.
4. `notebook.ipynb` documents the full pipeline (model definitions, training, evaluation). Its config cell expects the processed CSV described above, so it needs the join in step 2 first.

Models: ConvNeXt-Tiny (`timm`, `convnext_tiny.in12k_ft_in1k`) and DeBERTa-v3 Small with scalar gated fusion.

## Notes

- Reported results were produced with the original training run. The released notebook is a cleaned version of that code; only its data-preparation cells were re-executed for this release.
- Images are not included in this repository.
