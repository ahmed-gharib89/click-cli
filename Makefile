setup:
	python -m venv ~/.click-cli
	. ~/.click-cli/bin/activate

install:
	python -m pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C,E1120 hello.py

test:
	coverage run -m pytest -vv --cov=hello test_hello.py
	coverage report
	coverage xml
