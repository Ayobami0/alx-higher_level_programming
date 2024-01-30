#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request.get(argv[2]).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
