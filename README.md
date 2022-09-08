# Icecream Truck

```sh
git clone https://github.com/tashi_179/icecream_truck.git
cd icecream_truck
```

Create a virtual environment to install dependencies in and activate it:

```sh
conda create --name truck_env django
conda activate truck_env
```

Run seed file to populate dummy data
```sh
(truck_env)$ python seeds.py
(truck_env)$ python manage.py runserver
```

### API Endpoints
1. `http://127.0.0.1:8000/api/v1/trucks/` List of icecream trucks
2. `http://127.0.0.1:8000/api/v1/items/` Inventory list from all the trucks
3. `http://127.0.0.1:8000/api/v1/orders/` List of customers order
