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

    hideBelowFold();

};

function changeAnimation() {

    // Get current url
    var url = window.location.href;

    // Process which class
    if (url.search('about') > 0) {
        $(".navAbout > a").toggleClass("animateAboutMeColor");
        $(".navAbout > a > img").toggleClass("animateAboutMe");
    } else if (url.search('blog') > 0) {
        $(".navBlog > a").toggleClass("animateBlogColor");
        $(".navBlog > a > img").toggleClass("animateBlog");
    } else if (url.search('research') > 0 ) {
        $(".navResearch > a").toggleClass("animateResearchColor");
        $(".navResearch > a > img").toggleClass("animateResearch");
    } else if (url.search('contact') > 0 ) {
        $(".navContact > a").toggleClass("animateContactColor");
        $(".navContact > a > img").toggleClass("animateContact");
    } else {
        $(".navAbout > a").toggleClass("animateAboutMeColor");
        $(".navAbout > a > img").toggleClass("animateAboutMe");
    }

}

function hideBelowFold() {
    // Get current url
    var url = window.location.href;

    //if (url.slice(url.length-1,url.length) == '/') {
    //    url = url.slice(0,url.length-1);
    //}
    //
    //if ('/blog' == url.slice(url.length-5,url.length) ) {
    //    $('div#breakStart').nextUntil('div#breakEnd').css('display', 'none');
    //    $('div#breakStart').nextUntil('div#breakEnd').hide();
    //}

    if (url.search('blog') > 0 && (url.search('page') > 0 || url.search('tag') > 0) ) {
        $('div#breakStart').nextUntil('div#breakEnd').css('display', 'none');
        $('div#breakStart').nextUntil('div#breakEnd').hide();
    }
}

$(document).ready(main);