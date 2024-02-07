$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', (resp) => {
  $('DIV#character').text(resp.name);
});
