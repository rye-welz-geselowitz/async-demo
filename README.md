
# First time 
## Create virtualenv
`python3 -m venv async-demo-venv`

## Install requirements 
`pip install -r requirements.txt`

## Install redis 
https://redis.io/docs/install/install-redis/install-redis-on-mac-os/

# Run 
## Activate virtualenv
`source async-demo-venv/bin/activate`

## Run redis server
`redis-server`

## Run worker 
`python -m worker`

## Run script 
`python -m demo --do_async=true`

`python -m demo --do_async=false`

