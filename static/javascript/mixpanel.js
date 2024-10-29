$(document).ready(function() {
    $('#run-button').click(function() {
        const selectedDataset = $('#dataset-select').val();
        $.post('/get_data', { dataset: selectedDataset }, function(response) {
            $('#dataset-table').html(response.table_html);
            $('#chart-container').html(response.graph_html);
        });
    });
});
