FROM python:3.12.2-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .
COPY runserver.sh .
COPY wsgi.py .

RUN chmod +x runserver.sh

EXPOSE 8000

ENTRYPOINT ["./runserver.sh"]
