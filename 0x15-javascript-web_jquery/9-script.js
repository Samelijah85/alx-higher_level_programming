$(document).ready(function () {
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    const helloTranslation = data.hello;
    $('DIV#hello').text(helloTranslation);
  });
});
