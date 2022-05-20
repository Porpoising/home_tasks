FROM python:3.9-slim

COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY models/checkpoint.h5 /models/checkpoint.h5
COPY src/app.py /src/app.py
COPY src/datagen.py /src/datagen.py
COPY src/load_data.py /src/load_data.py
COPY src/train.py /src/train.py
COPY src/model.py /src/model.py
COPY src/callbacks.py /src/callbacks.py
COPY src/losses.py /src/losses.py
COPY src/request_processing.py /src/request_processing.py

WORKDIR .

CMD ["python3", "/src/app.py"]
