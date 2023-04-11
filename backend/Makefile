setup_development_db:
	cd db && poetry run alembic upgrade head

setup_test_db:
	sh db/test/import_schema.sh

run_fastapi:
	poetry run uvicorn app.main:app --reload

lint:
	poetry run isort .
	poetry run black .
	poetry run pflake8 .
	poetry run mypy .

clear_cache_files:
	find . | grep -E __pycache__ | xargs rm -rf
	find . | grep -E .pytest_cache | xargs rm -rf
	find . | grep -E .mypy_cache | xargs rm -rf

import_seeds:
	mysql -h ${MYSQL_HOST} -P ${MYSQL_PORT} -u root -p${MYSQL_ROOT_PASSWORD} ${MYSQL_DATABASE} < db/seeds.sql
