#!/bin/bash
# Print methods
curl -s -sI "$1" | sed -n 's/^Allow: //p'
