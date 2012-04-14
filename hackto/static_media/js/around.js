$(document).ready(function() {
    $('#map_canvas').gmap().bind('init', function(ev, map) {
        $('#map_canvas').gmap('addMarker', {'position': $LAT,$LON, 'bounds': true}).click(function() {
            $('#map_canvas').gmap('openInfoWindow', {'content': 'Hello World!'}, this);
        });
    });
});