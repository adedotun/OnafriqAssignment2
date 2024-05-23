import requests
import json

class BookingPage:
    base_url = "https://restful-booker.herokuapp.com"

    def create_booking(self, token):
        url = f"{self.base_url}/booking"
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}
        payload = {
            "firstname": "Adedotun",
            "lastname": "Ogunwuyi",
            "totalprice": 1200,
            "depositpaid": True,
            "bookingdates": {"checkin": "2024-05-21", "checkout": "2024-05-30"},
            "additionalneeds": "Dinner"
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.json()

    def get_booking(self, booking_id):
        url = f"{self.base_url}/booking/{booking_id}"
        response = requests.get(url)
        return response.json()

    def update_booking(self, booking_id, token):
        url = f"{self.base_url}/booking/{booking_id}"
        headers = {"Content-Type": "application/json", "Cookie": f"token={token}"}
        payload = {
            "firstname": "Adedotun",
            "lastname": "Ogunwuyi",
            "totalprice": 1200,
            "depositpaid": True,
            "bookingdates": {"checkin": "2024-05-21", "checkout": "2024-05-25"},
            "additionalneeds": "Breakfast"
        }
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        return response.json()
