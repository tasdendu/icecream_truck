# Icecream Truck

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

### API Endpoints
1. `localhost:8000/api/v1/trucks/` List of icecream trucks
2. `localhost:8000/api/v1/items/` Inventory list from all the trucks
3. `localhost:8000/api/v1/orders/` List of customers order
