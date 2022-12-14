FROM  python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY reqs.txt /app/reqs.txt
RUN pip3 install -r reqs.txt

ADD . .
