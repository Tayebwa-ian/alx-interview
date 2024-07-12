#!/usr/bin/node

// fetch and use data from Star wars API
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const resource = url + process.argv.slice(2)[0];
request(resource, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const content = JSON.parse(body);
    const cast = content.characters;
    for (let i = 0; i < cast.length; i++) {
      request(cast[i], (er, resp, body2) => {
        if (er) {
          console.log('Error: can not fetch a character');
        } else {
          const cont = JSON.parse(body2);
          console.log(cont.name);
        }
      });
    }
  }
});
