#!/bin/bash
# Send json as POST
curl -s -X POST -H 'Content-Type: application/json' -d "@$2" "$1"
