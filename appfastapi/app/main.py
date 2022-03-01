from fastapi import FastAPI, Response, status
import uvicorn
import socket
import os

app = FastAPI()

@app.get("/status", status_code=200)
def status(response: Response):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(socket.gethostname())
    #response.status_code = status.HTTP
    print(status)
    return {"name": hostname, "ip": ip}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
