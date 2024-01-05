#!/bin/bash
# Print methods
curl -sI "$1" | sed -n 's/^Allow: //p'
