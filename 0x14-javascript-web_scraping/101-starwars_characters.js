#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;
request.get(url, (_, __, body) => {
  const jBody = JSON.parse(body);
  jBody.characters.forEach(peopleUrl => {
    request.get(peopleUrl, (_, __, body) => {
      console.log(JSON.parse(body).name);
    });
  });
});
