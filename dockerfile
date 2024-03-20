FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./api /app/api
COPY ./db /app/db
COPY .env /app/.env
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
EXPOSE 8080
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
