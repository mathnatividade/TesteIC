from fastapi import FastAPI, Request
from typing import Optional
import uvicorn
import socket
import os
import requests

app = FastAPI()

@app.get("/teste2", status_code=200)
def healthcheck():
    httpcode = requests.get('http://localhost/teste2')
    iphost = socket.gethostbyname(socket.gethostname())
    return {"System IP": iphost, "HTTP code": httpcode.status_code}


@app.get("/teste")
def read_root():
    iphost = socket.gethostbyname(socket.gethostname())
    return {"Ip do sistema": iphost}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/status", status_code=200)
def healthcheck():
    return "http status code 200"
#    appcoderesponse = requests.get("/status")
#   return {"Http code:", status_code}


@app.get("/clientip")
def client_data(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    return {"client_host": client_host, "client_port": client_port}

# @app.get("/")
# def homescore():
#    return 'ok'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
