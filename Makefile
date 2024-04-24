run_api:
	uvicorn pylibsproject.main:app --reload

run_tests:
	pytest tests/
