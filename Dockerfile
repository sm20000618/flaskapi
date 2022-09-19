FROM python:3.8

#defining the present directory

WORKDIR /app

#adding the contents to present directory

ADD . /app/

COPY requirements.txt requirements.txt

#run pip to install the dependencies of the app

RUN pip3 install -r requirements.txt

#define the command to start the container

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]