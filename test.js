var http = require('http'),
    httpProxy = require('http-proxy');
    
// 
// Create a proxy server with custom application logic 
// 
httpProxy.createServer(function (req, res, proxy) {
  // 
  // Put your custom server logic here 
  // 

  console.log("Received proxy request");
  console.dir(req);

  proxy.proxyRequest(req, res, {
    host: 'localhost',
    port: 9000
  });
}).listen(8000);
 
http.createServer(function (req, res) {
  console.log("Received request");
  console.dir(req);
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.write('request successfully proxied: ' + req.url +'\n' + JSON.stringify(req.headers, true, 2));
  res.end();
}).listen(9000);