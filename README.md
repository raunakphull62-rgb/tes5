markdown
# FastAPI Backend

This is a FastAPI backend with authentication and authorization using Supabase and JWT.

## Installation

1. Install the required packages by running `pip install -r requirements.txt`
2. Create a `.env` file with the following environment variables:
   - SUPABASE_URL
   - SUPABASE_ANON_KEY
   - SUPABASE_SERVICE_KEY
   - DB_PASSWORD
   - DB_HOST
3. Run the application by running `uvicorn main:app --host 0.0.0.0 --port 8000`

## API Endpoints

### Users

* `POST /users`: Create a new user
* `GET /users`: Get all users
* `GET /users/{user_id}`: Get a user by ID
* `PUT /users/{user_id}`: Update a user
* `DELETE /users/{user_id}`: Delete a user

### Products

* `POST /products`: Create a new product
* `GET /products`: Get all products
* `GET /products/{product_id}`: Get a product by ID
* `PUT /products/{product_id}`: Update a product
* `DELETE /products/{product_id}`: Delete a product

### Auth

* `POST /login`: Login a user
* `POST /register`: Register a new user
* `GET /me`: Get the current user