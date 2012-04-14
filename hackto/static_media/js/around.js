$(document).ready(function() {
    $('#map_canvas').gmap().bind('init', function(ev, map) {
        $('#map_canvas').gmap('addMarker', {'position': '57.7973333,12.0502107', 'bounds': true}).click(function() {
            $('#map_canvas').gmap('openInfoWindow', {'content': 'Hello World!'}, this);
        });
    });
});