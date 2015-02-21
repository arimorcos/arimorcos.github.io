var main = function () {

    $('.showTooltip').tooltipster( {
        animation: 'fall',
        offsetX: 0,
        offsetY: 0,
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
        $(".navAbout > a").toggleClass("animateAboutMeColor");
        $(".navAbout > a > img").toggleClass("animateAboutMe");
    } else if (url.search('posts') > 0) {
        $(".navBlog > a").toggleClass("animateBlogColor");
        $(".navBlog > a > img").toggleClass("animateBlog");
    } else if (url.search('research') > 0 ) {
        $(".navResearch > a").toggleClass("animateResearchColor");
        $(".navResearch > a > img").toggleClass("animateResearch");
    } else if (url.search('contact') > 0 ) {
        $(".navContact > a").toggleClass("animateContactColor");
        $(".navContact > a > img").toggleClass("animateContact");
    }

}

$(document).ready(main);