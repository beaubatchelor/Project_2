var width = parseInt(d3.select("#visual").style("width"));
var height = width/1.618


console.log(width)


const myMap = L.map("map", {
    center: [41.5868, -93.6250],
    zoom: 2
  });
  
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: 'sk.eyJ1Ijoibmljb2RlbXVzbWQiLCJhIjoiY2pvbHF1YXRtMGNnMDN3bGU1aXZhZGNxMSJ9.GZ8z8dSMhaJJgyG7v8ur6A'
}).addTo(myMap);

const data = 'data.js'

console.log(data)

