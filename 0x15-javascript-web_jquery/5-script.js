$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const newItem = $('<li>Item</li>');
    $('ul.my_list').append(newItem);
  });
});
