const https = require('https');
const port = process.env.PORT || 8000;
const fs = require('fs');

const options = {
  key: fs.readFileSync('privatekey.key'),
  cert: fs.readFileSync('certificate.crt')
};

https.createServer(options, function(client_req, client_res) {
  console.log('Received Request: ' + client_req.url);

  var proxy = https.get(client_req.url, function (res) {
    res.pipe(client_res, {
      end: true
    });
  });

  client_req.pipe(proxy, {
    end: true
  });
}).listen(port, function() {
  console.log("Listening on  *:" + port);
});