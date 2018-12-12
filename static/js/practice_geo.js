// practice geo

var width = parseInt(d3.select("#map").style("width"));
var height = width/2;

console.log(width);
console.log(height);
console.log(cityData.city_list[0].City);

console.log(cityData.city_list[0]['City Location']);



const myMap = L.map("map", {
    center: [41.5868, -93.6250],
    zoom: 3
    
  });
  
  L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: 'sk.eyJ1Ijoibmljb2RlbXVzbWQiLCJhIjoiY2pvbHF1YXRtMGNnMDN3bGU1aXZhZGNxMSJ9.GZ8z8dSMhaJJgyG7v8ur6A'
}).addTo(myMap);


function generateMap(){

    // var width = parseInt(d3.select("#map").style("width"));
    // var height = width/2
    // console.log(width)
    // console.log(height)
    var dropValue = document.getElementById('selected-item').value;
    
    console.log(dropValue);
    //console.log(lineTypes);
    
    let cityIndex = ['Los Angeles', 'Austin', 'San Francisco', 'Colorado Springs', 'Washington',
                                    'Miami', 'Chicago', 'Boston', 'New York', 'Dallas', 'Houston',]

    let lineIndex = ['Accessories', 'City Skirts', 'City Trousers', 'Dresses', 'Jackets', 'Outer Wear', 
                            'Outerwear', 'Overcoats', 'Shirt Waist', 'Sweat T-Shirts', 'Sweaters', 'Trousers' ]
    
    var radiusList = [];
            
        for (i = 0; i < lineIndex.length; i++) {
            
            if (lineIndex[i] === dropValue) {
                for(j = 0; j < cityIndex.length; j++) {
                    var radius = cityData.city_list[j]['Lines with Quantity'][0][dropValue]
                    if (radius > 40000) {
                        radius = 40000
                    }
                    radiusList.push( {
                        'City': cityIndex[j],
                        'location': cityData.city_list[j]['City Location'],
                        'radius': radius*10
                    });


                    
                }
                
            }

            
        }

        for(i=0; i<radiusList.length; i++) {
            L.circle(radiusList[i].location, {
                fillOpacity: 0.75,
                color: 'red',
                fillColor: 'red',
                radius: radiusList[i].radius
            }).addTo(myMap)
        }
        for (i=0; i< radiusList.length; i++){
            console.log(`City: ${radiusList[i].City}, Location: ${radiusList[i].location}, Radius: ${radiusList[i].radius}`)
        }
}     
