# Low Tide Event Finder
A script for parsing a location's tide data from www.tide-forecast.com to find upcoming daylight low tide events for tide pool exploration

## Requirements
The following development environment is recommended:
- [Python 3.11](https://www.python.org/downloads/release/python-3116/)
- A Python virtual environment with the dependencies listed in [requirements.txt](requirements.txt)

## Installation
**NOTE: These installation steps are for Unix systems, Windows install steps are slightly different** (e.g. "\\" instead of "/" in paths, slight differences in Python paths, etc.) Please let me know if steps for Windows are needed.
### Install Python 3.11
Follow the instructions from [python.org](www.python.org) based on your system.

### Clone this project
* Change directory (cd) into the directory where you want to clone this project. This example will clone the directory into the `/home/pi` (~) directory.
        
        cd ~
        git clone https://github.com/jhthompson12/low-tide-finder.git
* Then cd into the project directory
        
        cd low-tide-finder


### Create a Python Virtual Environment for this project
* Use your base Python 3.11 executable to create a virtual environment names `.venv`
        
        python3.11 -m venv .venv

* Install the required packages

        ./.venv/bin/pip install -r requirements.txt
 
## Run the Script
From the `low-tide-finder` directory run the script using the previously configured virtual environment:

        ./.venv/bin/python low_tide_grabber.py