
import os
import requests

SHOPIFY_API_KEY = os.getenv('SHOPIFY_API_KEY')
SHOPIFY_API_PASSWORD = os.getenv('SHOPIFY_API_PASSWORD')
SHOPIFY_STORE_NAME = os.getenv('SHOPIFY_STORE_NAME')

def update_product_seo(product_id, title, description):
    url = f"https://{SHOPIFY_API_KEY}:{SHOPIFY_API_PASSWORD}@{SHOPIFY_STORE_NAME}.myshopify.com/admin/api/2021-10/products/{product_id}.json"
    payload = {
        "product": {
            "id": product_id,
            "title": title,
            "body_html": description
        }
    }
    response = requests.put(url, json=payload)
    return response.json()
