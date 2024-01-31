#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request.get(argv[2], (_, __, body) => {
  const ID = 18;
  console.log(JSON.parse(body).results.filter((film) => {
    return film.characters.includes(
      `https://swapi-api.alx-tools.com/api/people/${ID}/`
    );
  }).length);
});
