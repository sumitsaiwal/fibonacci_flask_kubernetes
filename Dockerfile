# Using official python runtime base image
FROM python:3.7-stretch as base

#metadata
LABEL Name="Fibnocci_Flask"
LABEL Version="1.0"

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

#Tester
FROM base
RUN mkdir /p_app
WORKDIR /p_app
RUN pip install pytest pylint
COPY . /p_app
RUN find . -iname "*.py" | xargs pylint --msg-template='{path}:{line}:{column}: {msg_id}: {msg} ({symbol})'; exit 0
#https://docs.pytest.org/en/latest/goodpractices.html#tests-outside-application-code
RUN python -m pytest tests/unit tests/integration

#Application
FROM base
WORKDIR /app
COPY app /app

# Make port 80 available for publish
EXPOSE 8080

# Heathcheck, Let's use kubernetes liveness probe
#HEALTHCHECK CMD curl --fail http://localhost:8080/calculate_fibonacci?n=1 || exit 1

# Define our entrypoint to be run when launching the container, args can be appended
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
