# Jist-Summarizer

## Configuring the Docker Network
In order for this to successfully communicate with the HTML parser (at least on local host), you must add the `jist-net` docker network.
This can be done by running `docker network create -d bridge jist-net`

The `run.sh` files for both summarizer and HTML parser should contain the param `--network="jist-net"`, which will use this network
