all: deploy

deploy: 
	aws cloudformation deploy \
	--template-file CargoTrackingSystem.yaml \
	--stack-name CargoTrackingSystem \
	--capabilities CAPABILITY_IAM

.PHONY: deploy
