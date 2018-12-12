// var tableData = cityData;

var salesRevenue = d3.select("#salesRevenue");
var margin = d3.select("#Margin");

function drawTable(city) {
  salesRevenue.html("");
  margin.html("");
console.log('hi')
  cityInfo.forEach((dataRow) => {
    if(dataRow.City === city){
      let values = [];
      for(let info in dataRow["Lines with Sales"][0]){
        values.push(dataRow["Lines with Sales"][0][info]);
      }
      console.log(values)
      salesRevenue.selectAll('td')
        .data(values)
        .enter()
        .append('td')
        .text(function (d) {
          return d
        })
    }});

    // var row = tbody.append("tr");

  //   Object.values(dataRow).forEach((val) => {
  //     var cell = row.append("td");
  //       cell.text(val);
  //     }
  //   );
  // });
}

// function handleClick() {

//   d3.event.preventDefault();

//   var date = d3.select("#datetime").property("value");
//   let filteredData = tableData;

//   if (city) {

//     filteredData = filteredData.filter(row => row.datetime === date);
//   }

//   buildTable(filteredData);
// }

// d3.selectAll("#filter-btn").on("click", handleClick);

// buildTable(tableData);