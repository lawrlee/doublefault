FROM python:2.7.13

RUN mkdir /doublefault
WORKDIR /doublefault

RUN apt-get update && apt-get install -y \
    postgresql-client \
    vim \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY . /doublefault/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN curl https://nodejs.org/dist/v6.11.1/node-v6.11.1-linux-x64.tar.xz | tar -C /usr/local --strip-components 1 -Jxv
