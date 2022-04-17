# README #

payments_recovery

### What is this repository for? ###

* warrant_recovery is a scheduled-run python application. Used for updating MOCK records missing
  payment data from associated records in mockpoepleSoft.
* Version 1.0

### How do I get set up? ###

* This application has an associated control-m job that can be used to interface with scheduled-runs.
* Located on helenatto0017 /data/project/PROD/in/python
* Logs located at /logs/applications/python
* Deployment instructions: Contact Trevor Osborne trevoroborne1989@gmail.com to deploy and 
						   provide him the following instructions...
	- Create a requirements.txt file to zip into the project that contains all dependencies of the python application
	- Placed zip of the project in the /tmp folder. It's payments_recovery.zip [payments_recovery.zip]
	- Unzip into /data/project/in/python and give it gatekeeper permissions like the other directories in the location
	- Create a Python virtual environment and install dependencies with the following commands in the /python/payments_recovery working directory
      /usr/local/bin/python3.9 -m venv ./venv
	- source ./venv/bin/activate
	- pip install -r requirements.txt
	- deactivate
	- Move script warrant_recovery.sh [payments_recovery.sh] to /data/project/PROD/in/script and chmod 775 it

### Who do I talk to? ###

* Trevor Osborne - Applications Developer - trevorosborne1989@gmail.com - (760) 473-6713