window.addEventListener('load',
  () => {
    $('INPUT#language_code').keypress((event) => {
      if (event.originalEvent.key === 'Enter') {
        const lang = $('INPUT#language_code').val();
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (resp) => {
          $('DIV#hello').text(resp.hello);
        });
      }
    });
    $('INPUT#btn_translate').click(
      () => {
        const lang = $('INPUT#language_code').val();
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (resp) => {
          $('DIV#hello').text(resp.hello);
        });
      }
    );
  });
