FROM python:3.9-slim

COPY requirements.txt /requirements.txt
RUN apt-get update && apt-get install -y python3-opencv
RUN pip3 install -r requirements.txt

COPY src/ /src/
#COPY runserver.sh /runserver.sh
#
#ENV PORT = 8000

WORKDIR .

#RUN chmod +x /runserver.sh
#
#CMD ["/runserver.sh"]

CMD ["python3", "/src/figure_determinator.py"]
