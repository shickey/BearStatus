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
  $(events).each(function(index, e) {
    var o = e.obj;
    o.css('left', e.left);
    o.css('width', e.width);
    o.css('top', e.startTime - offset);
    
    var height = e.endTime - e.startTime;
    if (height < 30) {
      offset -= 30 - height;
      height = 30;
    };
    o.css('height', height);
    
  });
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