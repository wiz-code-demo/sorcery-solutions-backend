FROM registry.os.test.wiz.io/python:3

WORKDIR /code

COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt --upgrade --no-cache-dir

COPY *.py /code/

ENTRYPOINT ["fastapi", "run", "main.py", "--port", "8000"]
