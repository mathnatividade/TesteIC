from fastapi import FastAPI
import uvicorn
import socket
import os

app = FastAPI()

@app.get("/status", status_code=200)
def healthcheck():
    iphost = socket.gethostbyname(socket.gethostname())
    hname = socket.gethostname()
    return {"Name":hname, "System IP":iphost, "HTTP status code":200}

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
