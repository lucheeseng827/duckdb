FROM alpine:3.18.4

# author
LABEL maintainer="Nick Lu"

# set work directory
WORKDIR /app

# install dependencies
RUN  apk add --no-cache  \
    bash  \
    curl  \
    git  \
    jq  \
    openssh  \
    python3  \
    py3-pip  \
    py3-setuptools  \
    py3-wheel \
    # python3-dev \
    && python -m pip install  --upgrade pip --no-cache-dir

# copy requirements.txt first for better cache on later pushes and delete cache
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt --no-cache-dir && \
     rm -rf /var/cache/apk/*

# copy the rest of the app
COPY examples /app

# run entrypoint/commands
CMD [ "bash" ]
