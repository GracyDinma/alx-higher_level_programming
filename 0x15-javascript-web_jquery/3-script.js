// JavaScript script that adds the class red to the <header> element when the user clicks 

$(function () {
  $('DIV#red_header').click(function () {
    $('HEADER').addClass('red');
  });
});
