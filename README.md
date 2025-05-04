# EX01 Developing a Simple Webserver
## Date:04\05\2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
Name: A PRANEYA
Register No: 212224110045
```

```
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
```

## OUTPUT:
![Screenshot 2025-05-04 144932](https://github.com/user-attachments/assets/01c13317-3408-4cca-8188-a74a1a8bb1a8)

![Screenshot 2025-05-04 145207](https://github.com/user-attachments/assets/79e31dd3-b8f3-48a4-8616-693f59876ba2)

## RESULT:
The program for implementing simple webserver is executed successfully.
