$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    $.each(data.results, function (index, movie) {
      const title = movie.title;
      const listItem = $('<li>').text(title);
      $('UL#list_movies').append(listItem);
    });
  });
});
