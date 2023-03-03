/* jshint esversion: 11 */

/**
 * Automatically close messages after time
 */
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);