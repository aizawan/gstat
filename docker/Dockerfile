FROM ubuntu:16.04

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
	python3 \
	python3-dev \
	unzip \
	bzip2 \
	sudo \
	git \
	curl \
	software-properties-common \
	&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

RUN pip3 --no-cache-dir install \
         django \
	 django-bootstrap4

ADD src /src
WORKDIR /src

RUN python3 manage.py sqlmigrate cms 0001 && python3 manage.py migrate cms && python3 manage.py migrate

WORKDIR /
ADD run.sh /

EXPOSE 8888
CMD ["./run.sh"]



