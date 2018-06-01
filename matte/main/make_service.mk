all: deploy

service = $(shell basename `pwd`)
prefix = $(shell echo $(service) | tr '[:upper:]' '[:lower:]')
functions := $(patsubst ./main/%.py, %, $(filter-out ./main/$(service).py, $(wildcard ./main/*.py)))
archives := $(patsubst %, ./dist/%.zip, $(functions))
common = ./main/$(service).py $(wildcard ../matte/main/matte/*.py) $(wildcard ./main/lib/*.py)
main := ./main
matte := ../matte/main
env = export PYTHONPATH="$(main):$(matte)";

test:
	$(env) python3 -m unittest discover -p '*_test.py' -s ./test/

sam: test build/$(service)-package.yaml

build/$(service).yaml: $(archives) $(matte)/make_sam_template
	$(env) ../matte/main/make_sam_template $(service) $(basename $(functions)) > build/$(service).yaml

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
	mkdir build/matte
	mkdir build/lib
	cp $< build/
	cp ./main/$(service).py build/
	cp ./main/lib/*.py ./build/lib/ 2>/dev/null || :
	cp $(matte)/matte/*.py ./build/matte/	
	$(env) ../matte/main/make_handler $(patsubst main/%.py, %, $<) > build/lambda_handler.py
	cd ./build; zip -r ../$@ *; cd -

clean:
	rm -fR build/*
	rm -f dist/*
	
.PHONY: test clean
