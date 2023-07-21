FROM debian:bookworm

WORKDIR /app
COPY .env .
COPY app.py .

RUN mkdir -p templates
COPY templates/* ./templates

RUN apt update && apt upgrade -y && apt install python3-venv python3-pip -y
RUN python3 -m venv .venv
ENV PATH=".venv/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt
RUN rm requirements.txt

RUN export FLASK_APP=app

EXPOSE 5000
#CMD . .venv/bin/activate && exec .venv/bin/python3 app.py
ENTRYPOINT [".venv/bin/python3"]
CMD ["app.py"]