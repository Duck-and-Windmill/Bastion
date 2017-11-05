const http = require('http');
const port = process.env.PORT || 8000;

http.createServer(function(client_req, client_res) {
  console.log("Received request");
  console.log('serve: ' + client_req.url);

  try {
    var proxy = http.get(client_req.url, function (res) {
      res.pipe(client_res, {
        end: true
      });
    });

    client_req.pipe(proxy, {
      end: true
    });
  } catch (err) {
      console.error(err)
  }
    
}).listen(port, function(){
  console.log("Listening on *:" + port);
});