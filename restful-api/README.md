# RESTful API

**Representational State Transfer (REST)** is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol -- the HTTP protocol is almost always used. REST is an alternative to other approaches like SOAP (Simple Object Access Protocol) and RPC (Remote Procedure Call).

Here are the key constraints that define a RESTful system:

- **Client-Server Architecture**:
This constraint separates the user interface concerns from the data storage concerns. By separating the user interface from the data storage, we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.
- **Statelessness**:
Each request from a client to a server must contain all the information the server needs to understand and process the request. The server should not store any state about the client session on the server side. This improves visibility, reliability and scalability.
- **Cacheability**:
Responses must defines themselves as cacheable or non-cacheable to prevent clients from reusing stale or inappropriate data in response to further requests. Well managed caching can partially or completely eliminate some client-server interactions, further improving scalability and performance.
- **Uniform Interface**:
The uniform interface simplifies and decouples the architecture, which enables each part to evolve independently. The four guiding principles of the uniform interface are:

   * Identification of resources
   * Manipulation of resources through representations
   * Self-descriptive messages
   * Hypermedia as the engine of application state (HATEOAS), meaning that clients interact with the network application entirely through hypermedia provided dynamically by application server.

- **Layered System**:
A client cannot ordinarily tell wether it is connected directly to the end server or to an intermediary along the way. Intermediary servers can improve system scalability by enabling load balancing and providing shared caches.
- **Code on Demand(optional)**:
Servers can temporarily extend or customize the functionality of a client by transfering executable code. This is the only optional constaint of REST.

## MIME (Multipurpose Internet Mail Extensions)

MIME is a standard that extends the format of email maessages to support.

In the context of REST and web developement, MIME types are used to specify the **format of data** being sent or received between a client and a server. They are also known as **media types** or **content types**.

***Examples of MIME types:***

* text/html for HTML documents.
* application/json for JSON data.
* image/png for PNG images.
* application/xml for XML data.

When a client sends a request to a server, it can specify the MIME type it expects in the response using the `Accept` header. Similarily, when a server responds, it specifies the MIME type of the returned data using the `Content-Type` header. This ensures that both parties understand the format of the data being exchanged.

## HTTP/HTTPS Basics

HTTP (Hypertext Transfer Protocol) and HTTP (HTTP Secure) are the foundation of data comunnication on the web.

**Key Concepts**:

- **HTTP**:
A protocol for transferring data between a client and a server. It is not secure by default.
- **HTTPS**:
A secure version of HTTP that uses encryption (SSL/TLS) to protect data during transfer.
- **HTTP Methods**:

   * `GET`: Retrieve data from the server.
   * `POST`: Send data to the server.
   * `PUT`/`PATCH`: Update existing data on the server.
   * `DELETE`: Remove data from the server.

- **Status Codes**:

| Code Range | Category | Examples |
|------------|----------|----------|
|`1xx`       |Informational |`100 Continue` (the server is ready for the request body)|
|`2xx`       |Success       |`200 OK` (request succeeded), `201 Created` (ressource created)|
|`3xx`       |Redirection   |`301 Moved Permanently` (ressource has moved to new URL)|
|`4xx`       |Client Error  |`400 Bad Request` (invalid request), `404 Not Found` (ressource not found)|
|`5xx`       |Server Error  |`500 Ineternal Server Error` (server encountered an error)|

## What is API Consumption ?

API consumption refers to the process of using an API (Application Programming Interface) to access and interact with a service, system, or database. It involves sending requests to an API endpoint and receiving responses, usually in JSON or XML format.

**API Consumption with Command Line**:

You can interact with API using command-line tools like `curl` or `httpie`.

* **cURL**: A command line tool to send HTTP requests.
* **HTTPie**: A user friendly alternative to cURL.

<ins>**Example**</ins>:

Fetch data from API using `curl`.

```bash
curl https://api.example.com/data
```

Send data using `httpie`.

```bash
http POST https://api.example.com/data name="John" age=30
```

**Hints**:

- The -I flag in curl fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
- With the -X flag, you can specify an HTTP method for your request. For example, -X POST will make a POST request.
- The -d flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
- If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like jq for JSON formatting and highlighting.

**API Consumption with Python**:

Python provides librairy like `requests` to interact with AOIs programmatically.

* `requests` **Library**: Simplifies sending HTTP requests and handling reponses.
* **JSON**: The most common format for API data exchange.

<ins>**Example**</ins>:

Fetch data from an API:
```python
import requests
response = requests.get("https://api.example.com/data")
data = response.json()  # Convert response to Python dictionary
print(data)
```

## API Development with http.server

Python’s built-in http.server module allows you to create a basic HTTP server.

* **HTTP Server**: Handles incoming requests and sends responses.
* **Routing**: Mapping URLs to specific functions.

<ins>**Example**</ins>:

Create a simple server:
```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, World!")

server = HTTPServer(("localhost", 8000), SimpleHandler)
server.serve_forever()
```
Run the server and visit http://localhost:8000 in your browser.

## API Development with Flask

Flask is a lightweight Python framework for building APIs.

* **Routing**: Mapping URLs to functions using decorators.
* **Request Handling**: Accessing data sent by the client.
* **Response Handling**: Sending data back to the client.

<ins>**Example**</ins>:

Create a simple Flask API:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(debug=True)
```
Run the server and visit http://localhost:5000/data.

## API Security & Authentication

Securing APIs ensures that only authorized users can access them.

* **Authentication**: Verifying the identity of a user (e.g., API keys, OAuth).
* **HTTPS**: Encrypting data in transit.
* **Rate Limiting**: Preventing abuse by limiting the number of requests.

<ins>**Example**</ins>:

Add API key authentication in Flask:
```python
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "secret123"

@app.route("/data", methods=["GET"])
def get_data():
    if request.headers.get("X-API-KEY") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"message": "Hello, World!"})

if __name__ == "__main__":
    app.run(debug=True)
```

## API Standards & Documentation with OpenAPI

OpenAPI is a standard for documenting RESTful APIs.

* **OpenAPI Specification**: A machine-readable description of an API.
* **Swagger**: Tools for generating and visualizing OpenAPI documentation.

<ins>**Example**</ins>:

Document a Flask API using flask-swagger-ui:
```python
from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = "/api/docs"
API_URL = "/static/swagger.json"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Sample API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
```

## REST API Conceptual Diagram

The diagram illustrates the flow of a RESTful API:

- **Client**: Sends a request (e.g., browser or app).
- **Web Server**: Routes the request to the API server.
- **API Server**: Processes the request and interacts with the database.
- **Database**: Stores and retrieves data.

**Flow**:

- Client → Web Server: Sends an HTTP/HTTPS request.
- Web Server → API Server: Forwards the request.
- API Server → Database: Fetches or modifies data.
- API Server → Web Server: Returns the processed response.
- Web Server → Client: Sends the final response.

## Why This Matters:

- **APIs are the backbone of modern applications**: They enable communication between different systems (e.g., social media, e-commerce, IoT).
- **Skills in API consumption, development, and security** are essential for building scalable and secure applications.
- **Documentation** ensures APIs are usable and maintainable.