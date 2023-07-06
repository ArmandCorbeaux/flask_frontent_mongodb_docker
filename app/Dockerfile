FROM ubuntu
WORKDIR /
COPY .env .
COPY app.py .
COPY requirements.txt .
RUN mkdir -p templates
COPY templates/* ./templates
RUN apt update && apt upgrade -y && apt install python3-venv python3-pip -y
RUN python3 -m venv .venv
ENV PATH=".venv/bin:$PATH"
#RUN . .venv/bin/activate
#RUN .venv/bin/pip3 install Flask pymongo python-dotenv
RUN pip3 install -r requirements.txt
RUN export FLASK_APP=app
EXPOSE 5000
#CMD . .venv/bin/activate && exec .venv/bin/python3 app.py
CMD ["flask","run"]