window.addEventListener('load',
  () => {
    $('DIV#add_item').on('click', () => {
      $('UL.my_list').append('<li>Item</li>');
    });
    $('DIV#remove_item').on('click', () => {
      $('UL.my_list li:last-of-type').remove();
    });
    $('DIV#clear_list').on('click', () => {
      $('UL.my_list').empty();
    });
  }
);
