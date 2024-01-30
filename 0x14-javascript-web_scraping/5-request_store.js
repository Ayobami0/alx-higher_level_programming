#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2]).pipe(fs.createWriteStream(argv[3], { encoding: 'utf-8' }));
