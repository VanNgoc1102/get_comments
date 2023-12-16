FROM --platform=linux/amd64 python:3.8.12


WORKDIR /app/

RUN apt -y update \
    && apt -y upgrade \
    && apt install -y wget gnupg

RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --system --deploy --ignore-pipfile

COPY . /app/

CMD python3