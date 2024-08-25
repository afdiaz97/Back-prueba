# pull official base image
FROM python:3.12

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get -y dist-upgrade
RUN pip install --upgrade pip
RUN apt-get install -y netcat-openbsd

COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./entrypoint.sh .

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh" ] 

CMD ["run"]

