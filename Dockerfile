FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

WORKDIR /tmp

RUN apt-get -y update

RUN apt-get install --no-install-recommends -y bash \
    build-essential \
    zip \
    git \
    curl \
    wget \
    ca-certificates \
    gcc \
    libpq-dev

RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash

RUN apt-get clean
RUN rm -rf /var/lib/apt/lists 

RUN chmod 1777 /tmp
RUN rm -rf /tmp

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=$PYTHONPATH:/app

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -U pyopenssl cryptography
