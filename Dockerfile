FROM python:3.9

COPY . /

WORKDIR /

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]