var main = function () {

    $('.showTooltip').tooltipster( {
        animation: 'fall',
        offsetX: 0,
        offsetY: 2,
        touchDevices: false,
        onlyOne: true,
        theme: 'tooltipster-default'
        });


    changeAnimation();

};

function changeAnimation() {

    // Get current url
    var url = window.location.href;

    // Process which class
    if (url.search('about') > 0) {
        $('.navAbout > a > img').toggleClass("animateAboutMe");
    } else if (url.search('contact') > 0) {
        $('.navBlog > a > img').toggleClass("animateBlog");
    } else if (url.search('research') > 0 ) {
        $('.navResearch > a > img').toggleClass("animateResearch");
    }

}

$(document).ready(main);