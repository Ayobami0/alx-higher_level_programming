$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (resp) => {
  resp.results.forEach(movie => {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  });
});
