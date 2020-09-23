// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
var map;
var service;
var infowindow;

function initMap() {
    var position = new google.maps.LatLng(-33.8665433, 151.1956316);

    map = new google.maps.Map(document.getElementById('map'), {
        center: position,
        zoom: 18,
        styles: [{
            featureType: 'poi.business',
            elementType: 'labels',
            stylers: [{
                visibility: 'off'
            }]
        }]
    });
    // Create the search box and link it to the UI element.
    //const input = document.getElementById(name);
    //const searchBox = new google.maps.places.SearchBox(input);
    //const searchBox = new google.maps.places.SearchBox(idswitch(id));
    //// Bias the SearchBox results towards current map's viewport.
    //map.addListener("bounds_changed", () => {
    //    searchBox.setBounds(map.getBounds());
    //});
    //let markers = [];
    //// Listen for the event fired when the user selects a prediction and retrieve
    //// more details for that place.
    //searchBox.addListener("places_changed", () => {
    //    const places = searchBox.getPlaces();

    //    if (places.length == 0) {
    //        return;
    //    }
    //    // Clear out the old markers.
    //    markers.forEach(marker => {
    //        marker.setMap(null);
    //    });
    //    markers = [];
    //    // For each place, get the icon, name and location.
    //    const bounds = new google.maps.LatLngBounds();
    //    places.forEach(place => {
    //        if (!place.geometry) {
    //            console.log("Returned place contains no geometry");
    //            return;
    //        }
    //        position = place.geometry.location;
    //        //gets location and search criteria and radius
    //        var request = {
    //            location: position,
    //            radius: '5050',
    //            type: ['pizza']

    //        };
    //        //infowindow = new google.maps.InfoWindow();
    //        //var service = new google.maps.places.PlacesService(map);

    //        //service.nearbySearch(request, callback);
    //        // `end`
    //        const icon = {
    //            scaledSize: new google.maps.Size(25, 25)
    //        };
    //        // Create a marker for each place.
    //        markers.push(
    //            new google.maps.Marker({
    //                map,
    //                icon,
    //                title: place.name,
    //                position: place.geometry.location
    //            })
    //        );

    //        if (place.geometry.viewport) {
    //            // Only geocodes have viewport.
    //            bounds.union(place.geometry.viewport);
    //        } else {
    //            bounds.extend(place.geometry.location);
    //        }
    //    });
    //    map.fitBounds(bounds);

    //});
}
function switchmap(lat, lng) {
    var position1 = new google.maps.LatLng(lat, lng);

    map = new google.maps.Map(document.getElementById('map'), {
        center: position1,
        zoom: 18,
        styles: [{
            featureType: 'poi.business',
            elementType: 'labels',
            stylers: [{
                visibility: 'on'
            }]
        }]
    });
    var marker = new google.maps.Marker({
        map: map,
        position: position1

    });
    marker.setMap(map)
}
//function callback(results, status) {
//    if (status == google.maps.places.PlacesServiceStatus.OK) {
//        for (var i = 0; i < results.length; i++) {
//            createMarker(results[i]);
//        }
//    }
//}
//function createMarker(place) {
//    var placeLoc = place.geometry.location;
//    var marker = new google.maps.Marker({
//        map: map,
//        position: place.geometry.location
//    });

//    google.maps.event.addListener(marker, 'click', function () {
//        infowindow.setContent(place.name);
//        infowindow.open(map, this);
//    });
    
//}