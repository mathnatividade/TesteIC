from fastapi import FastAPI
from datetime import datetime
import uvicorn
import socket
import os
import pytz

app = FastAPI()

@app.get("/status", status_code=200)
def status(): 
    hostname = socket.gethostname()
    ip = socket.gethostbyname(socket.gethostname())
    IST = pytz.timezone('America/Sao_Paulo') 
    datetime_ist = datetime.now(IST) 
    acesstime = datetime_ist.strftime('%A, %B %d, %Y %H:%M:%S')
    return {"name": hostname, "ip": ip}

    #"code": 200, "time":acesstime

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
