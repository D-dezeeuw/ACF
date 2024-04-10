FROM python:3.12.2-bullseye

WORKDIR /app

COPY requirements.txt .

RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --upgrade wheel

RUN pip install --no-cache-dir --upgrade -r requirements.txt
# RUN pip install pysqlite3-binary

RUN mkdir /src
COPY src/ ./src
COPY runserver.sh .
COPY wsgi.py .

RUN chmod +x runserver.sh
# RUN chmod +x make_sqlite.sh

CMD bash ./make_sqlite.sh
CMD echo "info making make_sqlite "

EXPOSE 8000

CMD bash ./runserver.sh

