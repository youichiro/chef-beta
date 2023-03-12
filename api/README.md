# chef-api
## migration
modify app/models.py

```sh
cd db
poetry run alembic revision --autogenerate -m "<message>"
poetry run alembic upgrade head
```
