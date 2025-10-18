# alx_travel_app_0x02

This is a Django-based application that integrates the Chapa API for payment processing in a travel booking system. The app handles secure payments, booking references, and payment status verification.

## Project Overview

- **Django Framework**: The project uses Django as the backend framework.
- **Chapa API**: Integrated for processing payments and verifying transaction status.
- **Celery**: Used for handling asynchronous background tasks like sending payment confirmation emails.
- **Django REST Framework**: For API endpoints that handle payment initiation and verification.

## Features

- **Booking and Payment Flow**: Allows users to make bookings with secure payment options via Chapa.
- **Chapa Payment Integration**: Initiates payments, verifies payment status, and stores payment details.
- **Background Tasks with Celery**: Sends email confirmations upon successful payments.
- **Swagger Documentation**: The API endpoints are documented with Swagger UI using `drf-yasg`.

## Requirements

- Python 3.9 or later
- Django 5.2+
- Django REST Framework
- Celery
- Redis (for Celery task queue)

## Setup Instructions

### 1. Clone the Repository

````bash
git clone https://github.com/your-username/alx_travel_app_0x02.git
cd alx_travel_app_0x02

2. Create and Activate a Virtual Environment
python3.9 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
CHAPA_SECRET_KEY=your_chapa_secret_key
CHAPA_PUBLIC_KEY=your_chapa_public_key

5. Run Database Migrations
python manage.py migrate

7. Celery Configuration
Install Redis (if not installed):
macOS: brew install redis
Ubuntu: sudo apt install redis-server
Start Redis:
redis-server
In a separate terminal, run the Celery worker:
celery -A alx_travel_app.celery worker --loglevel=info

API Endpoints
1. Initiate Payment

Endpoint: POST /api/payment/initiate/

Description: Initiates the payment process with Chapa.

Request Data:

{
  "booking_reference": "ABC123",
  "amount": 1000.00,
  "email": "user@example.com",
  "phone": "1234567890"
}


Response:

{
  "payment_url": "https://chapa.co/payment/abc123",
  "transaction_id": "txn_12345"
}

2. Verify Payment

Endpoint: GET /api/payment/verify/{transaction_id}/

Description: Verifies the payment status with Chapa.

Response:

{
  "status": "Completed"
}

Task Queue with Celery

Background Task: send_payment_confirmation_email sends a confirmation email once the payment is completed.

Running Celery

Ensure that Redis is running.

In a new terminal window, run:

celery -A alx_travel_app.celery worker --loglevel=info

License

This project is licensed under the MIT License - see the LICENSE
 file for details.


### Key Markdown Elements:

1. **Headings**: `#` for primary headers, `##` for secondary headers, etc.
2. **Code blocks**: Wrapped in triple backticks (```) for commands and JSON examples.
3. **Lists**: Use `-` or `*` for unordered lists, and `1.`, `2.`, etc., for ordered lists.
4. **Links**: `[text](url)` for clickable links.

### How to Use:

- Save this template as `README.md` in your project directory.
- Modify any sections as needed (e.g., replace placeholders like `your-username` and `your_secret_key`).
- When you push your code to GitHub or any other platform that supports Markdown, it will render the `README.md` properly.

Let me know if you need any more modifications!

````
