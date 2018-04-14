var main = function () {

    changeAnimation();

    hideBelowFold();

    $('.showTooltip').tooltipster( {
        animation: 'fall',
        offsetX: 0,
        offsetY: 0,
        touchDevices: false,
        onlyOne: true,
        theme: 'tooltipster-default'
    });

    //var isMobile = getMobile();
    //rearrangeForMobile(isMobile);

    //$('.contentCard a').attr("target","_blank");

};

function rearrangeForMobile(isMobile) {
    if (isMobile) {
        //$('.postList').removeClass('.completeLeft');
        //$('.postList').addClass('.center-element');
    }
}

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
    } else if (url.search('ml_research') > 0 ) {
        $(".navMLResearch > a").toggleClass("animateMLResearchColor");
        $(".navMLResearch > a > .dnn_im_container > img").toggleClass("animateMLResearch");
    } else if (url.search('neuro_research') > 0 ) {
        $(".navNeuroResearch > a").toggleClass("animateNeuroResearchColor");
        $(".navNeuroResearch > a > img").toggleClass("animateNeuroResearch");
    } else if (url.search('publications') > 0 ) {
        $(".navPubs > a").toggleClass("animatePubsColor");
        $(".navPubs > a > .pub_im_container > .scroll_container").toggleClass("animatePubsExpand");
        $(".navPubs > a > .pub_im_container > .scroll_container > img").toggleClass("animatePubsFlyUp");
        $(".navPubs > a > .pub_im_container > .scroll_short").toggleClass("animatePubsVanish");
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

    //var cropURL = url.substring(0, url.lastIndexOf('/'));

    //if ((cropURL.search('blog') > 0 || cropURL.search('tag') > 0) && cropURL.search('post') == -1) {
    //    $('div#breakStart').nextUntil('div#breakEnd').css('display', 'none');
    //    $('div#breakStart').nextUntil('div#breakEnd').hide();
    //}
    if ($('#postList').length > 0) { // If meta data postList exists
        $('div#breakStart').nextUntil('div#breakEnd').css('display', 'none');
        $('div#breakStart').nextUntil('div#breakEnd').hide();
    }
}

function getMobile() {
    if( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ) {
        var mobile = true;
    } else {
        var mobile = false;
    }
    return mobile;
}

$(document).ready(main);