
# First time 
## Create virtualenv
`python3 -m venv async-demo-venv`

## Install redis 
https://redis.io/docs/install/install-redis/install-redis-on-mac-os/

# Run 
## Activate virtualenv
`source async-demo-venv/bin/activate`

## Install requirements 
`pip install -r requirements.txt`

## (tab 1) Run redis server
`redis-server`

## (tab 2) Run worker 
`python -m worker`

## (tab 3) Run script 
`python -m demo --do_async=true`

`python -m demo --do_async=false`

