run:
	uvicorn main:app --reload

freeze:
	pip freeze > requirements.txt

setup:
	pip install -r requirements.txt

test:
	python -m unittest