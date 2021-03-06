function refreshAt(hours, minutes, seconds) {
    if (navigator.onLine) {  
        // declare and set variables
        var now = new Date();
        var then = new Date();
        then.setHours(hours);
        then.setMinutes(minutes);
        then.setSeconds(seconds);
        
        // if the time to refresh has passed, reload the page
        if (then.getTime() - now.getTime() <= 0)
        {
            window.location.reload(true);
        }
    }
}

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})