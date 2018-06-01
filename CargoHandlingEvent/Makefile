all: deploy

service = $(shell basename `pwd`)
bucket = mattea-cts
prefix = $(shell echo $(service) | tr '[:upper:]' '[:lower:]')
functions := $(patsubst ./main/%.py, %, $(filter-out ./main/$(service).py, $(wildcard ./main/*.py)))
archives := $(patsubst %, ./dist/%.zip, $(functions))
common = ./main/$(service).py $(wildcard ../mattea/main/mattea/*.py) $(wildcard ./main/lib/*.py)
main := ./main
mattea := ../mattea/main
env = export PYTHONPATH="$(main):$(mattea)";

test:
	$(env) python3 -m unittest discover -p '*_test.py' -s ./test/

sam: test build/$(service)-package.yaml

build/$(service).yaml: $(archives) $(mattea)/samgen
	$(env) ../mattea/main/samgen $(service) $(basename $(functions)) > build/$(service).yaml

build/$(service)-package.yaml: build/$(service).yaml
	aws cloudformation package --template-file build/$(service).yaml --s3-bucket $(bucket) --s3-prefix $(prefix) --output-template-file build/$(service)-package.yaml

deploy: sam
	aws cloudformation deploy \
	--template-file build/$(service)-package.yaml \
	--stack-name $(service) \
	--capabilities CAPABILITY_IAM

./dist/%.zip: ./main/%.py $(common)
	mkdir -p dist
	mkdir -p build
	rm -fR build/*
	mkdir build/mattea
	mkdir build/lib
	cp $< build/
	cp ./main/$(service).py build/
	cp ./main/lib/*.py ./build/lib/
	cp $(mattea)/mattea/*.py ./build/mattea/	
	$(env) ../mattea/main/make_handler $(patsubst main/%.py, %, $<) > build/lambda_handler.py
	cd ./build; zip -r ../$@ *; cd -

clean:
	rm -fR build/*
	rm -f dist/*
	
.PHONY: test clean
