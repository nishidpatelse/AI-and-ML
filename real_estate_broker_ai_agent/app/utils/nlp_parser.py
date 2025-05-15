import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_requirements(text: str) -> dict:
    doc = nlp(text.lower())
    requirements = {
        "location": None,
        "budget_min": None,
        "budget_max": None,
        "property_type": None,
        "size": None,
        "bhk": None,
        "facilities": [],
        "pet_friendly": None
    }

    price_match = re.search(r'\$?(\d{4,7})\s*(to|-|–)\s*\$?(\d{4,7})', text)
    if price_match:
        requirements['budget_min'] = int(price_match.group(1))
        requirements['budget_max'] = int(price_match.group(3))

    if 'apartment' in text: requirements['property_type'] = 'apartment'
    if 'villa' in text: requirements['property_type'] = 'villa'
    if 'studio' in text: requirements['property_type'] = 'studio'

    if 'pet' in text:
        requirements['pet_friendly'] = 'yes' if 'friendly' in text else 'no'

    if 'gym' in text: requirements['facilities'].append('gym')
    if 'pool' in text: requirements['facilities'].append('pool')
    if 'parking' in text: requirements['facilities'].append('parking')

    return requirements
