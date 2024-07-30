FROM python:3.11

LABEL Maintainer_Name="Giuliano Crenna" Maintainer_Email="giulicrenna@gmail.com" 

WORKDIR /app

ENV FLASK_APP app.py
ENV FLASK_ENV development

COPY . .

RUN pip3 install -r requirements.txt


CMD python3 app.py