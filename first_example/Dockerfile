FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN pip3 install apache-airflow

RUN pip3 install pandas virtualenv pytrends

RUN airflow db init
RUN airflow users create  --username admin  --role Admin --email qq@qq.com --firstname Peter  --lastname Parker  --password admin

COPY dags /root/airflow/dags

CMD airflow standalone



