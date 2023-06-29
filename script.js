function calculateDistance(userLatitude, userLongitude, latitude, longitude) {
  // Convert latitude and longitude to radians
  var userLatRad = userLatitude * Math.PI / 180;
  var userLonRad = userLongitude * Math.PI / 180;
  var latRad = latitude * Math.PI / 180;
  var lonRad = longitude * Math.PI / 180;

  // Earth's radius in kilometers
  var radius = 6371;

  // Calculate the differences between coordinates
  var diffLat = latRad - userLatRad;
  var diffLon = lonRad - userLonRad;

  // Apply Haversine formula
  var a = Math.sin(diffLat / 2) * Math.sin(diffLat / 2) +
    Math.cos(userLatRad) * Math.cos(latRad) *
    Math.sin(diffLon / 2) * Math.sin(diffLon / 2);

  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  var distance = radius * c;

  // Round the distance to two decimal places
  return distance.toFixed(2);
}

function fetchAndProcessCSV() {
  var userLatitude = parseFloat(document.getElementById("latitudeInput").value);
  var userLongitude = parseFloat(document.getElementById("longitudeInput").value);

  if (isNaN(userLatitude) || isNaN(userLongitude)) {
    alert("Please enter valid latitude and longitude values.");
    return;
  }

  var csvUrl = 'https://raw.githubusercontent.com/kotha070/Thesis/main/output.csv';

  Papa.parse(csvUrl, {
    download: true,
    header: true,
    complete: function(results) {
      var rows = results.data;
      var spreadsheetData = [];

      rows.forEach(function(row, index) {
        var latitude = parseFloat(row.latitude);
        var longitude = parseFloat(row.longitude);

        if (!isNaN(latitude) && !isNaN(longitude)) {
          var distance = calculateDistance(userLatitude, userLongitude, latitude, longitude);
          spreadsheetData.push({
            "IP": row.ip,
            "Country": row.country_name,
            "State/Province": row.state_prov,
            "Latitude": row.latitude,
            "Longitude": row.longitude,
            "Distance": distance
          });
        }
      });

      spreadsheetData.sort(function(a, b) {
        return a.Distance - b.Distance;
      });

      var outputTable = document.createElement("table");
      outputTable.setAttribute("border", "1");

      var outputHeaderRow = document.createElement("tr");
      for (var key in spreadsheetData[0]) {
        var outputHeaderCell = document.createElement("th");
        outputHeaderCell.textContent = key;
        outputHeaderRow.appendChild(outputHeaderCell);
      }
      outputTable.appendChild(outputHeaderRow);

      var rowCount = Math.min(spreadsheetData.length, 20);
      for (var i = 0; i < rowCount; i++) {
        var rowData = spreadsheetData[i];
        var outputRow = document.createElement("tr");
        for (var key in rowData) {
          var outputCell = document.createElement("td");
          outputCell.textContent = rowData[key];
          outputRow.appendChild(outputCell);
        }
        outputTable.appendChild(outputRow);
      }

      var outputDiv = document.getElementById("output");
      outputDiv.innerHTML = ""; // Clear previous contents
      outputDiv.appendChild(outputTable);
    }
  });
}

function checkProxy() {
  // Get user input values
  var ipAddress = document.getElementById('ipAddress').value;
  var portNumber = document.getElementById('portNumber').value;

  // Create a new XMLHttpRequest object
  var xhr = new XMLHttpRequest();

  // Prepare the request
  xhr.open('GET', 'http://' + ipAddress + ':' + portNumber, true);

  // Set up the event handler for the request
  xhr.onload = function() {
    if (xhr.status === 200) {
      updateProxyStatus('Proxy Status: Connected');
    } else {
      updateProxyStatus('Proxy Status: Closed');
    }
  };

  // Send the request
  xhr.send();
}

function updateProxyStatus(status) {
  // Update the proxy status element
  var proxyStatusElement = document.getElementById('proxyStatus');
  proxyStatusElement.textContent = status;
}


function updateProxyStatus(status) {
  // Update the proxy status element
  var proxyStatusElement = document.getElementById('proxyStatus');
  proxyStatusElement.textContent = status;
}


document.getElementById("taskSelect").addEventListener("change", function() {
  var task1Div = document.getElementById("task1");
  var task2Div = document.getElementById("task2");
  var selectedTask = document.getElementById("taskSelect").value;

  task1Div.style.display = selectedTask === "1" ? "block" : "none";
  task2Div.style.display = selectedTask === "2" ? "block" : "none";
});