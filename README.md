# First time 
## Create virtualenv
python3 -m venv async-demo-venv

# Run 
# Activate virtualenv
source async-demo-venv/bin/activate

# Run redis server
redis-server

# Run worker 
python -m worker 

# Run script 
python -m demo

