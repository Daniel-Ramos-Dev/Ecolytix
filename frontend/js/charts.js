let rtChart;

    const rtCtx = document.getElementById('rtChart');

    rtChart = new Chart(rtCtx, {
        type: 'line',
        data: {
            labels: rtLabels,
            datasets: [{
                label: 'Air Quality',
                data: rtData,
                tension: 0.3
            }]
        },
        options: {
            responsive: true
        }
    });

    const histCtx = document.getElementById('histChart');

    histChart = new Chart(histCtx, {
        type: 'bar',
        data: {
            labels: ['GOOD', 'MODERATE', 'POOR'],
            datasets: [{
                label: 'Occurrences',
                data: [0, 0, 0]
            }]
        },
        options: {
            responsive: true
        }
    });


function updateCharts(aqi, status) {

    const time = new Date().toLocaleTimeString();

    rtLabels.push(time);
    rtData.push(aqi);

    if (rtLabels.length > 15) {
        rtLabels.shift();
        rtData.shift();
    }

    rtChart.update();

    if (statusCounter[status] !== undefined) {
        statusCounter[status]++;
    }

    histChart.data.datasets[0].data = [
        statusCounter.GOOD,
        statusCounter.MODERATE,
        statusCounter.POOR
    ];

    histChart.update();
}