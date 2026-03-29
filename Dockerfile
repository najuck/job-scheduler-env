FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install pydantic numpy

CMD ["python", "baseline.py"]