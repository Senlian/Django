window.onload = function () {
    'use strict';
    // var protrait = $('#id_protrait');
    var protrait = document.getElementById('image');
    console.log(protrait)

    // var Cropper = window.Cropper;
    var cropper = new Cropper(protrait, {
        aspectRatio: 1 / 1,
        viewMode: 2
    });

};
