let year;

function changeYear(functionyear){
    year = functionyear;
    document.querySelector('#yearBtn').innerHTML = year;
}

function drawTable(product){
    document.querySelector('#productBtn').innerHTML = product;
    // d3.json('/endpoint', function(responseData){

    // }
}