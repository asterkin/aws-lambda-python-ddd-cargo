all: deploy

service = $(shell basename `pwd`)
bucket = $(shell echo $(service) | tr '[:upper:]' '[:lower:]')
functions := $(patsubst ./main/%.py, %, $(filter-out ./main/$(service).py, $(wildcard ./main/*.py)))
archives := $(patsubst %, ./dist/%.zip, $(functions))
common = ./main/$(service).py $(wildcard ../nahash/main/*.py) $(wildcard ./main/lib/*.py)
main := ./main
nahash := ../nahash/main
env = export PYTHONPATH="$(main):$(nahash)";

test:
	$(env) python3 -m unittest discover -p '*_test.py' -s ./test/

sam: test build/$(service)-package.yaml

build/$(service).yaml: $(archives) $(nahash)/samgen
	$(env) ../nahash/main/samgen $(service) $(basename $(functions)) > build/$(service).yaml

build/$(service)-package.yaml: build/$(service).yaml
	aws cloudformation package --template-file build/$(service).yaml --s3-bucket $(bucket) --output-template-file build/$(service)-package.yaml

deploy: sam
	aws cloudformation deploy \
	--template-file build/$(service)-package.yaml \
	--stack-name $(service) \
	--capabilities CAPABILITY_IAM

./dist/%.zip: ./main/%.py $(common)
	mkdir -p dist
	mkdir -p build
	rm -f build/*
	cp $< $(common) build/
	zip -j $@ build/*

clean:
	rm -f build/*
	rm -f dist/*
	
.PHONY: test clean
