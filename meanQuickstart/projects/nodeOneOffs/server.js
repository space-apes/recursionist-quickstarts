var http = require('http');
console.log('server.js: test')
http.createServer(function (req, res) {
			res.writeHead(200, {'Content-Type': 'text/plain'});
			res.end('Hello World!');
		}).listen(80); 

