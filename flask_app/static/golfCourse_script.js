
//  function to show Denver in google maps 
async function initMap() {
    var options = {
        zoom: 12,
        center: { lat: 39.7642, lng: -104.9920 }
    }
    var map = new google.maps.Map(document.getElementById('map'), options);

    var marker = new google.maps.marker()
}

initMap()


let map, service;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 6,
    });
    service = new google.maps.places.PlacesService(map);
}

function searchGolfCourses(e) {
    e.preventDefault();
    var searchValue = document.getElementById("searchInput").value;

    var request = {
        location: map.getCenter(),
        radius: 5000, // 5,000 meters radius (adjust as needed)
        keyword: searchValue,
        type: "golf_course",
    };

    service.nearbySearch(request, callback);
}

function callback(results, status) {
    if (status == google.maps.places.PlacesServiceStatus.OK) {
        var resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        for (var i = 0; i < results.length; i++) {
            var golfCourse = results[i];
            var name = golfCourse.name;
            var address = golfCourse.vicinity;
            var course_index = golfCourse.course_index;
            var slope_index = golfCourse.slope_index;

            var resultItem = document.createElement("div");
            resultItem.innerHTML = "<strong>" + name + "</strong><br>" + address;
            resultsDiv.appendChild(resultItem);
        }
    }
}

window.initMap = initMap;




//  Find Geolocation of user

// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 6,
    });
    infoWindow = new google.maps.InfoWindow();

    const locationButton = document.createElement("button");

    locationButton.textContent = "Pan to Current Location";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
    locationButton.addEventListener("click", () => {
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };

                    infoWindow.setPosition(pos);
                    infoWindow.setContent("Location found.");
                    infoWindow.open(map);
                    map.setCenter(pos);
                },
                () => {
                    handleLocationError(true, infoWindow, map.getCenter());
                }
            );
        } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
    });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
        browserHasGeolocation
            ? "Error: The Geolocation service failed."
            : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
}

window.initMap = initMap;


// ======================================================


/* 
Promises -> An action of an asynchronous operation that will either succeed or fail.
Like the term 'Promise' there is no guarantee the data will be succeed, but it guarantees an attempt is made/fulfilled before continuing the rest of the code.

Promises have 3 statuses:
Pending (Loading/Neutral)
Fulfilled (Success)
Rejected (Failed)

*/


// getCourseData()

// fetch('https://maps.googleapis.com/maps/api/js?key=AIzaSyAmeEbSll2MnTOR7zdIk2tjMmvaVzaq8Bg&libraries=places') // Promise is generated with fetch.
//     .then((res) => { res.json() })                     // .then( ... ) is the next step after fetch is resolved and it succeeded.
//     .then(pokeData => console.log(pokeData))
//     .catch(err => console.log(err))             // .catch( ... ) when an error occurs, catch executes.
async function getCourseData() {
    var response = await fetch('https://maps.googleapis.com/maps/api/js?key=AIzaSyAmeEbSll2MnTOR7zdIk2tjMmvaVzaq8Bg&libraries=places');
    var courseData = await response.json();
    console.log(courseData)
    return courseData;


}

function searchGolfCourse(e) {

    e.preventDefault(); // Prevents the standard action of the form being submitted - instead it executes the script below.

    let searchForm = document.getElementById('searchForm');
    let form = new FormData(searchForm);   // Js way of building a request.form just like in Flask.
    fetch('http://localhost:8000/search_courses', { method: 'POST', body: form }) //Promise is generated with fetch
        .then(res => res.json())    // .then( ... ) is the next step after fetch is resolved and it succeeded. Convert response to JSON.
        .then(searchData => {
            console.log(searchData)
            showCourseData(searchData)
        })
        .catch(err => console.log(err))
}

function showCourseData(courseJSON) {
    let coursePInfo = document.getElementById('courseInfo')
}