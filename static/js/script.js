
function drawTable(city){
    document.querySelector('#cityBtn').innerHTML = city;
}

var data = [data.js];

var table = d3.select('#visual')
    .append('table')
    .classed('table', true);

var thead = table.append('thead').append('tr');

var body = table.append('tbody');

var reload = function() {
    console.log("reload() called.");
    redraw();
};

var redraw = function () {
    console.log("redraw() called.");
};

reload();
