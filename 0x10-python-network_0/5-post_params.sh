#!/bin/bash
# A script that sends a POST request to the passed URL and displays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
