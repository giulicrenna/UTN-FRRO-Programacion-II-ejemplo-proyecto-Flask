FROM python:3.11

LABEL Maintainer_Name="Giuliano Crenna" Maintainer_Email="giulicrenna@gmail.com" 

WORKDIR /

ENV FLASK_APP app.py
ENV FLASK_ENV development

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir app
WORKDIR /app

COPY . .

CMD python3 app.py