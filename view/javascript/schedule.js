$(function() {
  var columns = []
  var lastEventEnding = null;
  
  var events = $('.schedule-event').map(function(index, o) {
    o = $(o);
    return {
      obj: o,
      startTime: o.data('startTime'),
      endTime: o.data('endTime')
    };
  });
  
  events = events.sort(function(e1,e2) {
    if (e1.startTime < e2.startTime) return -1;
    if (e1.startTime > e2.startTime) return 1;
    if (e1.endTime < e2.endTime) return -1;
    if (e1.endTime > e2.endTime) return 1;
    return 0;
  }).get();
  
  $(events).each(function(index,e) {
    
    if (lastEventEnding !== null && e.startTime >= lastEventEnding) {
      packEvents(columns);
      columns = [];
      lastEventEnding = null;
    };
    
    var placed = false;
    for (var i = 0; i < columns.length; ++i) {
      var col = columns[i];
      if (!eventsOverlap( col[col.length-1], e)) {
        col.push(e);
        placed = true;
        break;
      };
    }
    
    if (!placed) {
      columns.push([e]);
    };
    
    if (lastEventEnding === null || e.endTime > lastEventEnding) {
      lastEventEnding = e.endTime;
    }
  });
  
  if (columns.length > 0) {
    packEvents(columns);
  };
  
  layoutEvents(events);  
});

function layoutEvents(events) {
  var offset = $(events)[0].startTime;
  var all_offset = offset;
  var left_offset = 0;
  var right_offset = 0;
  var mq = window.matchMedia( "(max-width: 768px)" );    // see if on xs screen (mobile)
  $(events).each(function(index, e) {
    var o = e.obj;
    var height = e.endTime - e.startTime;
    o.css('left', e.left);
    o.css('width', e.width);

    if (e.width == "100%") {
      o.css('top', (e.startTime - offset));
      all_offset = offset;

      // make sure blocks are at least 30px tall
      if (height < 30) {
        offset -= 30 - height;
        height = 30;
      };
    }

    // if there are two collumns, the offsets for each collumn have to be calculated separately
    else if (e.width == "50%") {

      // left collumn
      if (e.left == "0%") {
        o.css('top', (e.startTime - all_offset - left_offset));
        // if on mobile, lunch blocks should be at least 45px tall
        if (mq.matches && height < 45) {
          left_offset -= 45 - height;
          height = 45;
        }
        // make sure blocks are at least 30px tall, even if on desktop
        else if (height < 30) {
          left_offset -= 30 - height;
          height = 30;
        };
      };

      // right collumn
      if (e.left == "50%") {
        o.css('top', (e.startTime - all_offset - right_offset));
        // if on mobile, lunch blocks should be at least 45px tall
        if (mq.matches && height < 45) {
          right_offset -= 45 - height;
          height = 45;
        }
        // make sure blocks are at least 30px tall, even if on desktop
        else if (height < 30) {
          right_offset -= 30 - height;
          height = 30;
        };
      };

    offset = all_offset + Math.min(left_offset, right_offset);  // determine which collumn is taller for all blocks below

    };

    o.css('height', height);
  });
  // Set height of container element
  var lastEvent = $(events)[events.length-1].obj;
  var containerHeight = lastEvent.position().top + lastEvent.height();
  $('#schedule-container').css('height', containerHeight);
}

function packEvents(columns) {
  var n = columns.length;
  for (var i = 0; i < n; i++) {
    var col = columns[i];
    for (var j = 0; j < col.length; j++) {
      var e = col[j];
      e.left = (i / n)*100 + '%';
      e.width = 100 / n + '%';
    };
  };
}

function eventsOverlap(eventA, eventB) {
  return eventA.endTime > eventB.startTime && eventA.startTime < eventB.endTime;
}

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