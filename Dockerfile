FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /web
COPY app /web
COPY config/req.txt /web/
COPY runapp.sh /web/
RUN rm -r /web/static
RUN pip install -r req.txt

