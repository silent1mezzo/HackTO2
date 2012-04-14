$(document).ready(function() {
    var myOptions = {
          zoom: 2,
          maxZoom: 10,
          center: new google.maps.LatLng(38, 15),
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
    map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
});