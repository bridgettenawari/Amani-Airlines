const URL = "./flights.json"; // Fetch the arrivals data from flights.json
const tableBody = document.getElementById("arrivals-tbody"); // get the table's body by its id and assign it a variable

// checking the flight's status
function getFlightStatus(status) {
  if (status == "LANDED") {
    return "status-landed";
  } else if (status == "ON TIME") {
    return "status-on-time";
  } else if (status == "DELAYED") {
    return "status-delayed";
  }
}
// fetch data from the json file
fetch(URL)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    // loop through the arrivals data
    data.arrivals.forEach((flight) => {
      const row = document.createElement("tr"); // create a new table row element
      const flightStatus = getFlightStatus(flight.status);
      row.innerHTML = `
        <td>${flight.scheduled_arrival}</td>
        <td>${flight.estimated_arrival}</td>
        <td>${flight.flight_number}</td>
        <td>${flight.from}</td>
        <td>${flight.airline}</td>
        <td>${flight.terminal}</td>
        <td class=${flightStatus}>${flight.status}
        `; // adds data to the row from the fetched json file
      tableBody.appendChild(row); // append data from your new rows to ur html table
    });
  })
  .catch((error) => {
    console.error("Data not fetched", error);
  });
