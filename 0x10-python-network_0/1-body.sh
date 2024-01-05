#!/bin/bash
# Display body
if [[ "$(curl -s -w "%{http_code}\n" -o /tmp/1-body "$1")" = 200 ]]; then
	echo /tmp/1-body
fi
