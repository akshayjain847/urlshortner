FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV SCRIPT_HOME /etc/infracloud

RUN mkdir $SCRIPT_HOME

#install dependencies
ADD requirements.txt $SCRIPT_HOME

RUN pip install -r $SCRIPT_HOME/requirements.txt

# Add other files
COPY . $SCRIPT_HOME/


# Give execution rights on the files
RUN chmod 0644 $SCRIPT_HOME/*

# Run the command on container startup

CMD python $SCRIPT_HOME/manage.py runserver 0.0.0.0:8000