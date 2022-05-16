/*
JavaScript code to fetch data from the API then post the result
*/

//defines the variable "visitorCount" by loading in the html files (document) and calling the ID labeled 'visitorCount'
visitorCount = document.getElementById('visitorCount');
//fetchs the API, then
fetch('https://2jvj37mzwj.execute-api.us-east-1.amazonaws.com/Prod/get')
    .then(response => response.json())
    .then(data => (visitorCount.innerHTML = (data)));




