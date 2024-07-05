#!/bin/bash
# Script to send a GET request to a URL with a header and displays the body
curl -s -X GET -H "X-School-User-Id:98" "$1"
