$(document).ready(function(){
    $('legend').each(function(index){
        $(this).replaceWith('<h3>' + $ (this).text() + '</h3>');
    });
});
var rquiredFlag = ' * ';
var codicinalFlag = ' ** ';

