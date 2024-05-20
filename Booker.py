import requests
import json

base_url = "https://restful-booker.herokuapp.com"


def authenticate():
    url = f"{base_url}/auth"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['token']


def create_booking():
    url = f"{base_url}/booking"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "firstname": "Adedotun",
        "lastname": "Ogunwuyi",
        "totalprice": 1200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-05-21",
            "checkout": "2024-05-30"
        },
        "additionalneeds": "Dinner"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()


def get_booking(booking_id):
    url = f"{base_url}/booking/{booking_id}"
    response = requests.get(url)
    return response.json()


def update_booking(booking_id, token):
    url = f"{base_url}/booking/{booking_id}"
    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={token}"
    }
    payload = {
        "firstname": "Adedotun",
        "lastname": "Ogunwuyi",
        "totalprice": 1200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-05-21",
            "checkout": "2024-05-25"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url, headers=headers, data=json.dumps(payload))
    return response.json()


# Main execution
token = authenticate()
print(f"Authenticated Token: {token}")

booking = create_booking()
print(f"Created Booking: {booking}")

booking_id = booking['bookingid']

retrieved_booking = get_booking(booking_id)
print(f"Retrieved Booking: {retrieved_booking}")

updated_booking = update_booking(booking_id, token)
print(f"Updated Booking: {updated_booking}")
