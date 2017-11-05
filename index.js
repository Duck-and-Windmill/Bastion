const http = require('http');
const port = process.env.PORT || 8000;

http.createServer(onRequest).listen(port);
console.log("Running on port: " + port);

function onRequest(client_req, client_res) {
  console.log("Received request");
  console.log('serve: ' + client_req.url);

  //console.dir(client_req);

  var options = {
    hostname: 'www.google.com',
    port: 80,
    path: client_req.url,
    method: 'GET'
  };

  var proxy = http.request(options, function (res) {
    res.pipe(client_res, {
      end: true
    });
  });

  client_req.pipe(proxy, {
    end: true
  });
}