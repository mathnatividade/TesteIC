from fastapi import FastAPI, Request
import uvicorn
import socket
import os
import requests

app = FastAPI()

@app.get("/status", status_code=200)
def healthcheck():
    return 'http status code 200 ta el'

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
