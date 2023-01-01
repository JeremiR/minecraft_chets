$(document).ready(function(){
    $('legend').each(function(index){
        $(this).replaceWith('<h3>' + $ (this).text() + '</h3>');
    });
});
var requiredFlag = ' * ';
var codicinalFlag = ' ** ';
var requiredKey = $('input.required : first') .next('span') .text();
var codicinalKey = $('input.codicinal : first') .next('span') .text();
