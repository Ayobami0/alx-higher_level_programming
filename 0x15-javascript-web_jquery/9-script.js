$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', (resp) => {
  $('DIV#hello').text(resp.hello);
});
