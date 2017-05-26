function get_chart() {
    $.ajax({
        type: "GET",
        url: '/build_mapchart',
        cache: false,
        data: {
            type: $('input[name="type"]').val(),
            style: $('input[name="style"]').val(),
            year: $('input[name="year"]').val(),
            percentage: $('#percentage').is(':checked')
        },
        success: function(data) {
            draw(data.result)
        }
    });
    return false;
}

function draw(chart_data) {
    google.charts.load('current', {'packages':['geochart']});
    google.charts.setOnLoadCallback(function() {drawChart(chart_data)});
    function drawChart(chart_data) {
        var data = google.visualization.arrayToDataTable(chart_data);

        var options = {
            backgroundColor: '#ffffff',
            defaultColor: '#e5e5e5',
            colorAxis: {colors: ['#9bffab', '#005f25']}
        };

        var chart = new google.visualization.GeoChart(document.getElementById('regions_div'));

        chart.draw(data, options);
}
    document.getElementById('regions_div').style.display = "block";
}