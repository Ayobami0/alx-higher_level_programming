$('DIV#toggle_header').on('click', () => {
  $('header').addClass((_, currentClass) => {
    $('header').removeClass(currentClass).addClass(currentClass === 'red' ? 'green' : 'red');
  }
  );
});
