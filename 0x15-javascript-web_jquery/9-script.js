// JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr

$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data) {
      $('DIV#hello').append(data.hello);
    }
  });
});
