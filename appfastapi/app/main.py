from fastapi import FastAPI
import uvicorn
import socket
import os

app = FastAPI()

@app.get("/status", status_code=200)
def healthcheck():
    return 'http status code 200 ta el'

# @app.get("/")
# def homescore():
#    return 'ok'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('PORT')))
