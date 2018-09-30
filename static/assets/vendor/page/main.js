$(function() {


    "use strict";

    var main = $(".main"),
        about = $(".aboutSection");

    $(".about").click(function() {

        main.animate({
                'height': '0',
                'top': '50vh',
                'padding': '0'
            }, 300)
            .animate({
                'width': '2px',
                'left': '50%'
            }, 900)
            .fadeOut(200, function() {
                about.fadeIn(200);
                about.animate({
                    'width': '100%',
                    'left': '0'
                }, 900);
                about.animate({
                    'min-height': '100vh',
                    'top': '0',
                    'padding-top': '50px',
                    'padding-bottom': '50px'
                }, 300);
            });


    });

    $(".home").click(function() {

        about.animate({
                'min-height': '0',
                'height': '0',
                'top': '50vh',
                'padding': '0'
            }, 300)
            .animate({
                'width': '2px',
                'left': '50%'
            }, 900)
            .fadeOut(200, function() {
                main.fadeIn(200)
                    .animate({
                        'width': '100%',
                        'left': '0'
                    }, 900)
                    .animate({
                        'height': '100vh',
                        'top': '0',
                        'padding-top': '100px',
                        'padding-bottom': '100px'
                    }, 300);
            });
    });
});