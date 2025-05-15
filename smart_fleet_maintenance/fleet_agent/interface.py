import json
from fleet_agent.maintenance import service_due_message

def load_vehicles(filepath="data/vehicles.json"):
    with open(filepath, "r") as f:
        return json.load(f)

def find_vehicle_by_id(vehicles, vehicle_id):
    for v in vehicles:
        if v['id'] == vehicle_id:
            return v
    return None

def start_cli():
    print("Welcome to Smart Fleet Maintenance Assistant!")
    vehicles = load_vehicles()
    print(f"Loaded {len(vehicles)} vehicles.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nEnter vehicle ID to check maintenance (e.g., truck_1): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        vehicle = find_vehicle_by_id(vehicles, user_input)
        if not vehicle:
            print("Vehicle not found. Try again.")
            continue
        
        msg = service_due_message(vehicle)
        print(f"Maintenance status for {vehicle['id']}: {msg}")
