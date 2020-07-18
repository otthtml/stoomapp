FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8085

ENTRYPOINT ["python3"]
CMD ["application.py"]
