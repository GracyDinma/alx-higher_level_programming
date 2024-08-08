// A JavaScript script that update <header> to red when user clicks

$(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').css({ color: '#FF0000' });
  });
});
