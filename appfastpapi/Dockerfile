FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#comentario legal

COPY ./app /code/app

# CMD ["uvicorn", "app.main:app",  "--host", "0.0.0.0", "--port", "80"]

CMD ["python", "/code/app/main.py"]
