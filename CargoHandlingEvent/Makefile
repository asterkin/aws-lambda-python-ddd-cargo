all: test deploy

service = $(shell basename `pwd`)
bucket = s3://$(shell echo $(service) | tr '[:upper:]' '[:lower:]')
functions := $(patsubst ./main/%.py, %, $(filter-out ./main/common.py, $(wildcard ./main/*.py)))
archives := $(patsubst %, ./dist/%.zip, $(functions))
common = ./main/common.py ../nahash/main/nahash.py
main := ./main
nahash := ../nahash/main
env = export PYTHONPATH="$(main):$(nahash)";

test:
	$(env) python3 -m unittest discover -p '*_test.py' -s ./test/

build/$(service).yaml: $(archives) $(nahash)/samgen
#Do not understand why I need to copy it here
	$(env) ../nahash/main/samgen $(service) $(basename $(functions)) > build/$(service).yaml

deploy: build/$(service).yaml
	aws s3 sync ./dist/ $(bucket)
	aws cloudformation deploy \
	--template-file build/$(service).yaml \
	--stack-name $(service) \
	--capabilities CAPABILITY_IAM

./dist/%.zip: ./main/%.py $(common)
	mkdir -p build
	rm -f build/*
	cp $< $(common) build/
	zip -j $@ build/*


.PHONY: test
