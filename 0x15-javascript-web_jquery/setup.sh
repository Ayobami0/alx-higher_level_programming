#!/usr/bin/bash
# Creates all the required files
for n in {0..9}; do
	touch "$n-script.js" "test_htmls/$n-main.html"
done
