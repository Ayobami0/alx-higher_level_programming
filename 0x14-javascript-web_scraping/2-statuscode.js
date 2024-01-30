#!/usr/bin/node

const request = require('request');
const { argv } = request('node:process');

request.get(argv[2]).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
