setup:
	python -m venv ~/.click-cli
	. ~/.click-cli/bin/activate

install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py

test:
	python -m pytest -vv --cov=app test_hello.py
