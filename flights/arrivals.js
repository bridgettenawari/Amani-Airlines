const URL = "./flights.json"; // Fetch the arrivals data from flights.json
const table = document.getElementById("arrivals-table"); // get the table by its id and assign it a variable

// fetch data from the json file
fetch(URL)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    // loop through the arrivals data
    data.arrivals.forEach((flight) => {
      const row = document.createElement("tr"); // create a new table row element
      row.innerHTML = `
            <td>${flight.date}</td>
            <td>${flight.flight_number}</td>
            <td>${flight.from}</td>
            <td>${flight.airline}</td>
            <td>${flight.take_off}</td>
            <td>${flight.scheduled_arrival}</td>
            <td>${flight.estimated_arrival}</td>
            <td>${flight.terminal}</td>
            `; // adds data to the row from the fetched json file
      table.appendChild(row); // append data from your new rows to ur html table
    });
  })
  .catch((error) => {
    console.error("Data not fetched", error);
  });
