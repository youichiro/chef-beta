# chef-api
## Setup
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

setup local databases
```sh
docker compose up -d db
make setup_development_db
```

run fastapi server
```sh
make run_fastapi
```

## Testing
run test in parallel
```sh
make test
```


## Migration
```sh
# go to alembic.ini directory
cd db

# generate a new migraiton version according to model definitions
poetry run alembic revision --autogenerate -m "<version comment>"

# migrate to database
poetry run alembic upgrade head

# show history
poetry run alembic history

cd ..

# reflesh test database
make setup_test_db
```

## Dependency management
```sh
# add to main group
poerty add xxx

# add to dev group
poetry add --group dev xxx

# add to test group
poerty add --group test xxx
```
