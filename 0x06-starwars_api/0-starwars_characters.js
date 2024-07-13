#!/usr/bin/node

// fetch and use data from Star wars API
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const resource = url + process.argv.slice(2)[0];

function fetchUrl (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, resp, body) => {
      if (err) {
        console.log('Error: can not fetch a character');
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function getCast (resource) {
  const body = await fetchUrl(resource);
  const urls = JSON.parse(body).characters;
  try {
    const results = await Promise.all(urls.map(url => fetchUrl(url)));
    results.forEach((result, index) => {
      const character = JSON.parse(result);
      console.log(character.name);
    });
  } catch (err) {
    console.error(err);
  }
}

getCast(resource);
