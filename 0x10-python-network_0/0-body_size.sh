#!/bin/bash
# a script that takes a url and sends a request to url, then displays
# its content
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
