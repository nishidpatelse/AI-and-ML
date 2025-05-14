
import requests
from bs4 import BeautifulSoup

def run_seo_audit(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, "html.parser")
    return {
        "title": soup.title.string if soup.title else "Missing",
        "meta_description": soup.find("meta", attrs={"name": "description"}),
        "h1_tags": [h1.get_text() for h1 in soup.find_all("h1")],
        "images_missing_alt": [img['src'] for img in soup.find_all("img") if not img.get("alt")]
    }
