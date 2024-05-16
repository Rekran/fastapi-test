FROM python:3.11
COPY requirements.txt app/backend/requirements.txt
WORKDIR /app/backend
RUN pip install -r requirements.txt
COPY . /app/backend

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ,"--reload"]