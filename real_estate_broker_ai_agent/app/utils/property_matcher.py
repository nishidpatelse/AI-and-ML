import json

def load_properties(path="app/sample_data/listings.json"):
    with open(path) as f:
        return json.load(f)

def match_properties(requirements, listings):
    matches = []
    for prop in listings:
        if requirements['property_type'] and requirements['property_type'] != prop['type']:
            continue
        if requirements['pet_friendly'] and requirements['pet_friendly'] != prop['pet_friendly']:
            continue
        if requirements['budget_min'] and prop['price'] < requirements['budget_min']:
            continue
        if requirements['budget_max'] and prop['price'] > requirements['budget_max']:
            continue
        if requirements['facilities']:
            if not all(f in prop['facilities'] for f in requirements['facilities']):
                continue
        matches.append(prop)
    return matches
