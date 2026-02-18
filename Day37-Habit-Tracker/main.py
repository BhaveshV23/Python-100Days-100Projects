import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("MY_USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")
ENDPOINT = "https://pixe.la/v1/users"

HEADERS = {"X-USER-TOKEN": TOKEN}
TODAY = datetime.now().strftime("%Y%m%d")

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=ENDPOINT, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# response.raise_for_status()
# print(response.text)

def add_pixel():
    pixel_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    qty = input("How many kilometers did you cycle today? ").strip()
    if not qty.replace(".", "", 1).isdigit():
        print("Invalid input. Please enter a number.")
        return
    pixel_data = {
        "date": TODAY,
        "quantity": qty,
    }
    response = requests.post(url=pixel_endpoint, json=pixel_data, headers=HEADERS)
    response.raise_for_status()
    print(f"Post Result: {response.text}")

def update_pixel():
    update_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
    qty = input("What is the corrected kilometer value? ").strip()
    if not qty.replace(".", "", 1).isdigit():
        print("Invalid input. Please enter a number.")
        return
    new_data = {
        "quantity": qty,
    }
    response = requests.put(url=update_endpoint, json=new_data, headers=HEADERS)
    response.raise_for_status()
    print(f"Update Result: {response.text}")

def delete_pixel():
    delete_endpoint = f"{ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"
    confirm = input(f"Are you sure you want to delete the entry for {TODAY}? (y/n): ")
    if confirm.lower() == 'y':
        response = requests.delete(url=delete_endpoint, headers=HEADERS)
        response.raise_for_status()
        print(f"Delete Result: {response.text}")
    else:
        print("Deletion cancelled.")

if __name__ == "__main__":
    choice = input("What would you like to do? (add/update/delete): ").lower()
    if choice == "add":
        add_pixel()
    elif choice == "update":
        update_pixel()
    elif choice == "delete":
        delete_pixel()
    else:
        print("Invalid choice!")