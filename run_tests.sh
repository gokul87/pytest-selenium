#!/bin/bash
# Start the docker containers
sudo docker-compose up&
sleep(10)

#Execute python tests
pytest -v -s tests

#Shutdown docker after test
sudo docker-compose down