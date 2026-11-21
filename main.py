import csv
import json
import os
from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import dijkstra, get_path
from algorithms.tsp import tsp
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "data", "parcels.csv")
GRAPH_FILE = os.path.join(BASE_DIR, "data", "graph.json")
VEHICLE_CAPACITY = 20
DEPOT = "Depot"
def load_parcels():
    parcels = []
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Deadline"] = int(row["Deadline"])
            row["Weight"] = int(row["Weight"])
            row["Value"] = int(row["Value"])
            parcels.append(row)
    return parcels
def load_graph():
    with open(GRAPH_FILE, "r") as file:
        return json.load(file)
def display_parcels(parcels):
    for parcel in parcels:
        print(
            f"{parcel['Parcel_ID']} | "
            f"Deadline: {parcel['Deadline']} | "
            f"Priority: {parcel['Priority']} | "
            f"Weight: {parcel['Weight']} kg | "
            f"Value: {parcel['Value']} | "
            f"Destination: {parcel['Destination']}"
        )
def main():
    print("=" * 55)
    print("             MINI COURIER PLANNER")
    print("=" * 55)
    parcels = load_parcels()
    print("\n1. TOTAL PARCELS:", len(parcels))
    sorted_parcels = merge_sort(parcels)
    print("\n2. SORTED PARCELS")
    display_parcels(sorted_parcels)
    selected, max_value = knapsack(
        sorted_parcels,
        VEHICLE_CAPACITY
    )
    print("\n3. OPTIMAL PACKING PLAN")
    print("Vehicle Capacity:", VEHICLE_CAPACITY, "kg")

    if not selected:
        print("No parcels selected.")
        return
    display_parcels(selected)
    total_weight = sum(p["Weight"] for p in selected)
    print("\nTotal Selected Weight:", total_weight, "kg")
    print("Maximum Parcel Value:", max_value)
    graph = load_graph()
    print("\n4. DELIVERY GRAPH LOADED")
    print("Total Locations:", len(graph))
    if DEPOT not in graph:
        raise ValueError("Depot is missing from graph.json")
    destinations = list(dict.fromkeys(
        p["Destination"] for p in selected
    ))
    for destination in destinations:
        if destination not in graph:
            raise ValueError(
                f"{destination} is missing from graph.json"
            )
    print("\n5. DIJKSTRA SHORTEST PATHS")
    distances, previous = dijkstra(graph, DEPOT)
    for destination in destinations:
        path = get_path(previous, DEPOT, destination)
        if not path:
            raise ValueError(
                f"No path available to {destination}"
            )
        print(
            f"{DEPOT} -> {destination}: "
            f"{' -> '.join(path)} | "
            f"Distance: {distances[destination]} km"
        )
    print("\n6. DELIVERY ROUTE OPTIMIZATION")
    route, total_distance = tsp(
        graph,
        DEPOT,
        destinations
    )
    print("Delivery Route:")
    print(" -> ".join(route))
    print("Total Route Distance:", total_distance, "km")
    print("\n" + "=" * 55)
    print("          COURIER PLANNING COMPLETED")
    print("=" * 55)
if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError, KeyError) as error:
        print("\nERROR:", error)

