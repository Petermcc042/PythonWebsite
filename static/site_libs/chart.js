const chartCanvas = document.getElementById('chartCanvas');
let myChart;

async function updateChart() {
    const tableId = document.getElementById('table-select').value;
    const xColumn = document.getElementById('x-select').value;
    const yColumn = document.getElementById('y-select').value;
    const chartType = document.getElementById('chart-type-select').value;

    const response = await fetch('/plot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ table_id: tableId, x_column: xColumn, y_column: yColumn, chart_type: chartType })
    });
    const { chart_data } = await response.json();

    if (myChart) myChart.destroy();
    myChart = new Chart(chartCanvas, chart_data);
}
