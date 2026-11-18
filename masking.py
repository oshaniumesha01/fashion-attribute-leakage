"""
Keyword-masking dictionary and category-to-attribute applicability map
used for all results reported in the manuscript.
"""
import re

ATTR_KEYWORDS = {
    'color':   ['black', 'blue', 'brown', 'gold', 'green', 'grey', 'gray', 'orange', 'pink',
                'purple', 'red', 'silver', 'white', 'yellow', 'navy', 'beige', 'cream',
                'maroon', 'olive', 'khaki', 'teal', 'coral', 'turquoise', 'mustard', 'charcoal'],
    'pattern': ['checked', 'check', 'embroidered', 'embroidery', 'floral', 'graphic',
                'polka dot', 'polka-dot', 'printed', 'print', 'solid', 'striped',
                'stripe', 'stripes'],
    'material': ['canvas', 'cotton', 'denim', 'eva', 'fabric', 'fleece', 'leather', 'linen',
                 'lycra', 'metal', 'polyester', 'rayon', 'rubber', 'silk', 'synthetic',
                 'tpr', 'textile', 'wool', 'nylon', 'suede', 'velvet', 'mesh', 'knit'],
    'sleeve':  ['full sleeve', 'half sleeve', 'sleeveless', 'three-quarter sleeve',
                'long sleeve', 'short sleeve', 'short sleeves', 'long sleeves',
                'full sleeves', 'half sleeves', 'mid sleeve'],
    'fit':     ['flared fit', 'loose fit', 'regular fit', 'slim fit', 'straight fit',
                'regular wash', 'slim wash', 'fits regular', 'fits slim',
                'size and fit', 'hem fit', 'hemline fit', 'chest fit', 'front fit',
                'front fitting', 'hem fitting', 'hemline fitting', 'fitting'],
    'neck':    ['boat neck', 'off shoulder', 'round neck', 'square neck', 'turtle neck',
                'v-neck', 'v neck', 'scoop neck', 'mock collar', 'polo neck',
                'polo collar', 'spread collar', 'tipped collar', 'ribbed collar',
                'mandarin collar', 'collar silhouette', 'round neckline',
                'ribbed round neckline', 'neckline'],
    'closure': ['pull-on', 'lace-up', 'slip-on', 'velcro',
                'buckle closure', 'elastic closure', 'clasp closure',
                'zipper closure', 'button closure', 'butterfly clasp',
                'fold over clasp', 'buttoned cuffs', 'buttoned front',
                'buttoned placket', 'buttoned chest', 'buttoned flaps',
                'full buttoned', 'button placket', 'button cuffs',
                'zippered fly', 'zipper fly', 'drawstrings',
                'elasticated waist', 'elasticated waistband',
                'with zippers', 'with buttons', 'zipper and button',
                'gunmetal buckle', 'single button', 'double button',
                'pearlescent white buttons', 'drawstring'],
    'occasion': ['casual', 'formal', 'sports', 'festive', 'party', 'beach',
                 'lounge', 'outdoor', 'wedding', 'daily use'],
    'gender':  ['women', 'woman', 'womens', 'womans', 'lady', 'ladies', 'mens', 'unisex',
                'girls', 'girl', 'boys', 'boy', 'men', 'man', 'mans'],
}


def mask_text(text):
    """Replace attribute keywords with [ATTRIBUTE] placeholders (longest match first)."""
    t = str(text).lower()
    for attr, kws in ATTR_KEYWORDS.items():
        for kw in sorted(kws, key=len, reverse=True):
            t = re.sub(r'\b' + re.escape(kw) + r'\b', f'[{attr.upper()}]', t)
    return t


# Categories for which each category-specific attribute is applicable.
# Attributes not listed here are applicable to all samples.
ATTR_CATEGORY_MAP = {
    'sleeve_type': ['Dresses', 'Innerwear Vests', 'Jackets', 'Kurtas', 'Kurtis',
                    'Night suits', 'Nightdress', 'Shirts', 'Sweaters',
                    'Sweatshirts', 'Tops', 'Tshirts', 'Tunics'],
    'neck_type':   ['Dresses', 'Innerwear Vests', 'Jackets', 'Kurtas', 'Kurtis',
                    'Night suits', 'Nightdress', 'Shirts', 'Sweaters',
                    'Sweatshirts', 'Tops', 'Tshirts', 'Tunics'],
    'fit':         ['Capris', 'Dresses', 'Innerwear Vests', 'Jackets', 'Jeans',
                    'Kurtas', 'Kurtis', 'Leggings', 'Night suits', 'Nightdress',
                    'Shirts', 'Shorts', 'Skirts', 'Sweaters', 'Sweatshirts',
                    'Tops', 'Track Pants', 'Trousers', 'Tshirts', 'Tunics'],
    'heel_type':   ['Casual Shoes', 'Flats', 'Flip Flops', 'Formal Shoes',
                    'Heels', 'Sandals', 'Sports Shoes'],
    'toe_style':   ['Casual Shoes', 'Flats', 'Flip Flops', 'Formal Shoes',
                    'Heels', 'Sandals', 'Sports Shoes'],
    'sole_type':   ['Casual Shoes', 'Flats', 'Flip Flops', 'Formal Shoes',
                    'Heels', 'Sandals', 'Sports Shoes'],
}