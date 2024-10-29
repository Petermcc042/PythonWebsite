Querying Big Query Using Python
========================

This project is designed to show you how to query data from big query

Firstly, you must setup your big 


<h1>Dataset Viewer</h1>

<form id="query-form">
    <label for="query">Enter SQL Query:</label><br>
    <textarea id="query" name="query" rows="4" cols="50"></textarea><br><br>
    <button type="submit">Run Query</button>
</form>

<label for="dataset-select">Choose a dataset:</label>
<select id="dataset-select">
        {% for dataset in datasets %}
        <option value="{{ dataset }}">{{ dataset }}</option>
        {% endfor %}
</select>
<button id="run-button">Run</button>
<div>
        <h2>Dataset</h2>
        <div id="dataset-table"></div>
</div>
<div>
        <h2>Graph</h2>
        <div id="chart-container"></div>
</div>


<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script src="{{ url_for('static', filename='javascript/mixpanel.js') }}"></script>
<style>
.data {
        border-collapse: collapse;
        width: 100%;
}
.data th,
.data td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
}
</style>
       