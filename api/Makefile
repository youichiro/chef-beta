setup_development_db:
	cd db && poetry run alembic upgrade head

setup_test_db:
	sh db/test/import_schema.sh

run_fastapi:
	poetry run uvicorn app.main:app --reload
