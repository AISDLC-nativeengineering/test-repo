# Product Details Module

## Overview
This module handles the display of product details, sizes, and customer reviews based on the requirements given in Jira issue AINA-397.

## Features
- Displays product images, descriptions, and price details.
- Allows users to select product sizes and display availability.
- Shows customer reviews sorted by relevance.

## Code
```python
class ProductPage:
    def __init__(self, product):
        self.product = product

    def load_page(self):
        return {
            "images": self.product["images"],
            "description": self.product["description"],
            "price": self.product["price"]
        }

    def select_size(self, size):
        if size in self.product["available_sizes"]:
            return f"Size {size} is available."
        else:
            return f"Size {size} is not available."

    def load_reviews(self):
        reviews = self.product["reviews"]
        return sorted(reviews, key=lambda x: x["relevance_score"], reverse=True)

# Example product data
product_data = {
    "images": ["image1.jpg", "image2.jpg"],
    "description": "High-quality winter jacket.",
    "price": "$99.99",
    "available_sizes": ["S", "M", "L"],
    "reviews": [
        {"text": "Great jacket!", "rating": 5, "relevance_score": 95},
        {"text": "Good quality but expensive.", "rating": 4, "relevance_score": 85}
    ]
}

page = ProductPage(product_data)
print(page.load_page())
print(page.select_size("M"))
print(page.load_reviews())
```
