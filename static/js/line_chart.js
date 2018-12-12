d3.json("/scatter_data",
    function(month_data){
        let layout = {
            title : "Product Line Sales by Month",
            margin : { t : 0}
        };
    Plotly.plot("lineChart", month_data, layout);
    }
);
