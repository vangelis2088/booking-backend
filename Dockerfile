# Dockerfile
#FROM python:3.7
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#WORKDIR /backend
#COPY requirements.txt /backend/
#RUN pip install -r requirements.txt
#COPY . /backend/

FROM gcr.io/google_appengine/python

# Create a virtualenv for the application dependencies.
# # If you want to use Python 2, use the -p python2.7 flag.
RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH
ENV PYTHONUNBUFFERED=1

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

CMD gunicorn -b :5000 booking.wsgi
# [END docker]