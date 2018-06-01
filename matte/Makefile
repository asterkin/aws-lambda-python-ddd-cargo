all: handler test

handler: main/make_handler test/check_cargo.py
	mkdir -p build
	rm -fR build/*
	export PYTHONPATH="./main:./test"; main/make_handler check_cargo > build/lambda_handler.py

test: handler
	export PYTHONPATH="./main:./build:./test"; python3 -m unittest discover -p '*_test.py' -s ./test/

