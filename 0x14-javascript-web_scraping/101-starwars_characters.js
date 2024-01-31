#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

(function fetchPeople (page) {
  const url = `https://swapi-api.alx-tools.com/api/people/?page=${page}`;
  request.get(url, (_, __, body) => {
    const jBody = JSON.parse(body);
    jBody.results.filter((people) => {
      return people.films.includes(
        `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`
      );
    }).forEach(people => {
      console.log(people.name);
    });
    if (jBody.next !== null) {
      fetchPeople(++page);
    }
  });
})(1);
