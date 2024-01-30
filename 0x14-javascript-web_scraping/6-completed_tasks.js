#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request.get(argv[2], (_, __, body) => {
  const taskComplete = {};
  JSON.parse(body).forEach(todo => {
    if (todo.completed === true) {
      if (todo.userId in taskComplete) {
        taskComplete[todo.userId] += 1;
      } else {
        taskComplete[todo.userId] = 1;
      }
    }
  });
  console.log(taskComplete);
});
