const URL = "departures.json"; // Look for the JSON file in the same folder
const tableBody = document.getElementById("departures-tbody"); 

// Function to assign the right CSS class based on status
function getFlightStatus(status) {
  if (status === "ON TIME") {
    return "status-on-time"; // Using the classes from arrivals.css
  } else if (status === "BOARDING") {
    return "status-landed"; // Green color
  } else if (status === "DELAYED") {
    return "status-delayed"; // Red color
  }
  return "";
}

// Fetch the data and build the table
fetch(URL)
  .then((response) => response.json())
  .then((data) => {
    data.departures.forEach((flight) => {
      const row = document.createElement("tr");
      const flightStatus = getFlightStatus(flight.status);
      
      row.innerHTML = `
        <td>${flight.scheduled_departure}</td>
        <td>${flight.estimated_departure}</td>
        <td>${flight.flight_number}</td>
        <td>${flight.destination}</td>
        <td>${flight.gate}</td>
        <td class="${flightStatus}">${flight.status}</td>
      `;
      tableBody.appendChild(row); 
    });
  })
  .catch((error) => {
    console.error("Data not fetched", error);
  });