#!/bin/bash
# Status code only
curl -s -w "%{http_code}" -o /dev/null "$1"
