const http = require("http");

/**
 * Docker Health Check Script
 * This script checks if the application is running and responding on the specified port.
 */

const options = {
  host: "localhost",
  port: 5000,
  timeout: 2000,
  path: "/",
};

const request = http.request(options, (res) => {
  console.log(`STATUS: ${res.statusCode}`);

  if (res.statusCode === 200) {
    process.exit(0);
  } else {
    process.exit(1);
  }
});

request.on("error", (err) => {
  console.error(`Error: ${err.message}`);
  process.exit(1);
});

request.end();
