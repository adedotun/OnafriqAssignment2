from auth import AuthenticationPage
from booking import BookingPage

# Main execution
auth_page = AuthenticationPage()
token = auth_page.authenticate()
print(f"Authenticated Token: {token}")

booking_page = BookingPage()
booking = booking_page.create_booking(token)
print(f"Created Booking: {booking}")

booking_id = booking['bookingid']

retrieved_booking = booking_page.get_booking(booking_id)
print(f"Retrieved Booking: {retrieved_booking}")

updated_booking = booking_page.update_booking(booking_id, token)
print(f"Updated Booking: {updated_booking}")
