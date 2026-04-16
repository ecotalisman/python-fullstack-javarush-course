const http = require('http');

// Creating the HTTP server
const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello from Node.js!');
});

// Listening on port 3000
server.listen(3000, '0.0.0.0', () => {
  console.log('Server running on port 3000');
});