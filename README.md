# Jist-Summarizer

## Configuring the Docker Network
In order for this to successfully communicate with the HTML parser (at least on local host), you must add the `jist-net` docker network.
This can be done by running `docker network create -d bridge jist-net`

The `run.sh` files for both summarizer and HTML parser should contain the param `--network="jist-net"`, which will use this network


## THINGS TO DISCUSS/FIX:
* We potentially need to change our encoding scheme. Currently, the example used from the Huffington post has some special characters (their apostrophes and dashes for example) that end up turning into garbage characters (at least when viewed in the terminal).
* We need to address the problem of preserving some HTML elements from the original text. Do we preserve all line breaks, or only some? Are the line breaks in the AMP article the same as in the desktop version?
* We need to address the issue of things like open quotations. E.g. if there is a two-sentence quote, but only the second sentence is in the digest, then there is a hanging quotation mark
