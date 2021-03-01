var fs = require("fs");
var http = require("http"); 
var os = require("os");
var ip = require("ip");
var startTime;


var server = http.createServer(function(req, res) {
    if (req.url === "/" ) {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type": "text/html"});
            res.end(body);
        });
    }

    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        
        function format(seconds){
            function pad(s){
              return (s < 10 ? '0' : '') + s;
            }
            var days = Math .floor(seconds / (60*60*24));
            var hours = Math.floor(seconds / (60*60));
            var minutes = Math.floor(seconds % (60*60) / 60);
            var seconds = Math.floor(seconds % 60);
          
            return 'Days:'+ pad (days) + ' Hours:' + pad(hours) + ' Minutes: ' + pad(minutes) + ' Seconds: ' + pad(seconds);
          }
          var uptime = process.uptime();
          console.log(format(uptime));
          //https://stackoverflow.com/questions/28705009/how-do-i-get-the-server-uptime-in-node-js
          Totalbytes = os.totalmem();
          Freebytes = os.freemem();
          function formatbytes(bytes){
            myMemory = (bytes / 1048576);
            return myMemory;
          }

        const convertBytes = function(bytes) {
            const sizes = ["Bytes", "KB", "MB", "GB", "TB"]
          
            if (bytes == 0) {
              return "n/a"
            }
          
            const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)))
          
            if (i == 0) {
              return bytes + " " + sizes[i]
            }
          
            return (bytes / Math.pow(1024, i)).toFixed(1) + " " + sizes[i]
          }
          //https://coderrocketfuel.com/article/how-to-convert-bytes-to-kb-mb-gb-or-tb-format-in-node-js

        html=`
        <!DOCTYPE html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${(format(uptime))}</p>
            <p>Total Memory: ${convertBytes(Totalbytes)}</p>
            <p>Free Memory: ${convertBytes(Freebytes)}</p>
            <p>Number of CPUs: ${os.cpus().length / 2}</p>
        </body>
        </html>
        `
        res.writeHead(200, {"Content-Type" : "text/html"});
        res.end(html);
    }

    else {
        res.writeHead(404, {"Content-Type":"text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }

});

server.listen(3000);
console.log("Server listening on port 3000");