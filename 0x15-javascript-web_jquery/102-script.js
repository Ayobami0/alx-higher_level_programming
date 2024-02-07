window.addEventListener('load',
  () => {
    $('INPUT#btn_translate').click(
      () => {
        const lang = $('INPUT#language_code').val();
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (resp) => {
          $('DIV#hello').text(resp.hello);
        });
      }
    );
  });
