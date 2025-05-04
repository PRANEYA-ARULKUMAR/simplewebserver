from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
  <title>Simple webserver</title>
  <style>
  .layers{
    display:flex;
  }
  .layer{
    margin-right:100px;
    margin-left:15px;
    flex-wrap: wrap;
    height:150px;
    width:650px;
  }
  body{
    background-color:#FAF1E6;
  }
  h2{
    text-align: center;
    text-decoration: underline;
  }
  p{
    font-size: 1.2em;
    font-weight: bold;
    text-decoration: underline;
  }
  .txt{
    background-color: #E4EFE7;
    margin-left:10px;
    padding:15px;
    border:2px solid black;
    display:inline-block;
  }
  </style>
</head>
<body>

  <h2>List of Protocols</h2>
  <div class='txt'>
  <h4 >Name: A Praneya</h4>
  <h4 >Register No: 212224110045</h4>
  </div>
  <div class='layers'>
  <div class="layer">
    <p>Application Layer</p>
    <ul>
      <li>HTTP,HTTPS</li>
      <li>FTP</li>
      <li>SMTP</li>
      <li>DNS</li>
      <li>Telnet</li>
    </ul>
  </div>

  <div class="layer">
    <p> Transport Layer</p>
    <ul>
      <li>TCP</li>
      <li>UDP </li>
    </ul>
  </div>

  <div class="layer">
    <p>Internet Layer</p>
    <ul>
      <li>IPv4 and IPv6</li>
      <li>ARP</li>
    </ul>
  </div>

  <div class="layer">
    <p>Link Layer</p>
    <ul>
      <li>Ethernet</li>
      <li>Wi-Fi</li>
      <li>MAC</li>
    </ul>
  </div>
  </div>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()