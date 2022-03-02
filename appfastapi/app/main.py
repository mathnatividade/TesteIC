from fastapi import FastAPI, Response, status
import uvicorn
import socket
import os
import asyncio
from random import randint

app = FastAPI()

@app.get("/status", status_code=200)
async def statusapp(response: Response):
    timeout = randint(30, 50)
    await asyncio.sleep(timeout/1000)
    if timeout > 42: 
        response.status_code = status.HTTP_404_NOT_FOUND    
        return timeout
    hostname = socket.gethostname()
    ip = socket.gethostbyname(socket.gethostname())
    return {"name": hostname, "ip": ip, "timeout" : timeout}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
