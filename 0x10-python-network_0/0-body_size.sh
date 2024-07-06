#!/bin/bash
# A Bash script that takes in a URL and sends a request to it
curl -sl "$1" | wc -c
