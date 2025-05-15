import datetime

# Maintenance rules
OIL_CHANGE_MILES = 5000
TIRE_CHANGE_MILES = 10000

def is_oil_change_due(mileage, last_oil_change):
    return (mileage - last_oil_change) >= OIL_CHANGE_MILES

def is_tire_change_due(mileage, last_tire_change):
    return (mileage - last_tire_change) >= TIRE_CHANGE_MILES

def days_since(date_str):
    last_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    delta = datetime.datetime.now() - last_date
    return delta.days

def service_due_message(vehicle):
    msgs = []
    if is_oil_change_due(vehicle['mileage'], vehicle['last_oil_change']):
        msgs.append("Oil change is due.")
    if is_tire_change_due(vehicle['mileage'], vehicle['last_tire_change']):
        msgs.append("Tire change is due.")
    days_passed = days_since(vehicle['last_service_date'])
    if days_passed > 180:
        msgs.append("General service overdue (more than 6 months since last service).")
    if not msgs:
        msgs.append("No maintenance due right now.")
    return " ".join(msgs)
