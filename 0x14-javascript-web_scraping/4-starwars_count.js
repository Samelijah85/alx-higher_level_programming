#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
let count = 0;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;

  films.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes('/18/')) {
        count++;
      }
    });
  });

  console.log(count);
});
