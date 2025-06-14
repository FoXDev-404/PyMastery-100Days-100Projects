# Day39 Flight Deals Project

This project automates the process of searching for the cheapest flights from a specified origin to multiple destinations and notifies you via SMS or WhatsApp when a lower price is found. It uses the Amadeus API for flight data, Google Sheets (via Sheety API) for storing destination and price data, and Twilio for notifications.

---

## Features

- Automatically fetches and updates IATA codes for destinations.
- Searches for the cheapest round-trip flights within a 6-month window.
- Notifies you via SMS or WhatsApp if a cheaper flight is found.
- Updates the lowest price in your Google Sheet.

---

## Requirements

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- Accounts and credentials for:
  - [Amadeus for Developers](https://developers.amadeus.com/)
  - [Twilio](https://www.twilio.com/)
  - [Sheety](https://sheety.co/) (for Google Sheets API access)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/FoXDev-404/PyMastery-100Days-100Projects.git
cd PyMastery-100Days-100Projects/Day31-40/Day39
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:

```bash
pip install requests python-dotenv twilio
```

### 3. Set Up Environment Variables

Create a `.env` file in the project directory with the following content (replace values with your own credentials):

```
SHEETY_ENDPOINT=your_sheety_endpoint
SHEETY_USERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_secret
TWILIO_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
TWILIO_VERIFIED_NUMBER=your_verified_number
TWILIO_WHATSAPP_NUMBER=your_whatsapp_number
```

- **Sheety**: Set up a Google Sheet and connect it to Sheety. The sheet should have columns: `city`, `iataCode`, `lowestPrice`, and `id`.
- **Twilio**: Register your phone number as a verified number for SMS/WhatsApp.
- **Amadeus**: Create an application to get your API key and secret.

### 4. Prepare Your Google Sheet

- The sheet should have at least the following columns: `city`, `iataCode`, `lowestPrice`, and `id`.
- Add your destination cities and initial lowest prices.

### 5. Run the Project

```bash
python main.py
```

- The script will update IATA codes, search for flights, and send notifications if cheaper flights are found.

---

## Customization

- **Origin Airport**: Change the `ORIGIN_CITY_IATA` variable in `main.py` to your preferred departure airport code.
- **Notification Method**: By default, SMS is used. To use WhatsApp, uncomment the relevant line in `main.py`.

---

## Troubleshooting

- **API Rate Limits**: The Amadeus API has rate limits. The script includes delays to avoid hitting these, but you may need to increase them if you see errors.
- **Twilio Sandbox**: For WhatsApp, you must join the Twilio Sandbox and use the sandbox number.
- **Sheety Auth**: Ensure your Sheety credentials are correct and your sheet is accessible.

---

## File Structure

```
Day39/
├── data_manager.py
├── flight_data.py
├── flight_search.py
├── main.py
├── notification_manager.py
├── .env
└── README.md
```

---

## License

This project is for educational purposes. Please do not share your API keys or credentials publicly.

---

## Credits

- [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
- [Amadeus for Developers](https://developers.amadeus.com/)
- [Twilio](https://www.twilio.com/)
- [Sheety](https://sheety.co/)
