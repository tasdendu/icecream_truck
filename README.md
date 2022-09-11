# Icecream Truck
#### API Endpoints
1. POST `localhost:8000/api/v1/customers/token/login/` Login with below parameters
    ```json
    {
        "email": "customer@test.com",
        "password": "Test@123"
    }
    ```
2. `localhost:8000/api/v1/trucks/` List of icecream trucks
3. `localhost:8000/api/v1/items/` Inventory list from all the trucks
4. GET `localhost:8000/api/v1/orders/` List of orders
5. POST `localhost:8000/api/v1/orders/` Place order with below parameters
    ```json
    {
        "line_items": {
            "item": 1,
            "quantity": 1
        }
    }
    ```

```zsh
git clone https://github.com/tashi_179/icecream_truck.git
cd icecream_truck
```

Create a virtual environment to install dependencies in and activate it:
Using `venv`
```zsh
python -m venv env
source env/bin/activate
```

Then run the following command to install the dependencies:
```zsh
pip install -r requirements.txt
```

Run seed file to populate dummy data
```zsh
bash migrate_and_seed.sh
python manage.py runserver
```
To run the test suite:
```zsh
python manage.py test
```