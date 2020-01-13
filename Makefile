# Makefile
# Author: Samuel Hornsey

# function to deploy
LAMBDA=lambda-au-prod-leftovers-01

# lint
lint:
	pylint main.py

# Run tests
test: lint
	export API_KEY='DUMMY_KEY' && python -m unittest test.py

clean:
	rm -rf /tmp/package && rm /tmp/function.zip

# build the project
build:
	/bin/bash bin/build.sh

# deploy the project
deploy: build
	/bin/bash bin/deploy.sh $(LAMBDA)