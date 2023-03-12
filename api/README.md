# chef-api
## setup
load environment variables
```sh
brew install direnv
direnv allow . # load .envrc, then load .env
```

install poetry and depencencies
```sh
curl -sSL https://install.python-poetry.org | python3 - --version 1.4.0
poetry install
```

setup databases
```sh
docker compose up -d db
make setup_development_db
make setup_test_db
```


## migration
```sh
cd db

# generate a migraiton version according to app/models.py
poetry run alembic revision --autogenerate -m "<message>"

# migrate to database
poetry run alembic upgrade head

cd ..

# also reflesh test database
make setup_test_db
```
