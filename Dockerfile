# pull official base image
FROM python:3.8.0-alpine

#Add User
RUN adduser -D coapp

# set work directory
WORKDIR /coapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /coapp/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /coapp

RUN chown -R coapp:coapp /coapp

USER coapp

#Port
EXPOSE 5001 8083

#command
CMD ["gunicorn", "-b", "0.0.0.0:5001", "wsgi:app"]
#CMD ["python", "app.py"]