FROM python:3.9-slim-bullseye

ENV VIRTUAL_ENV=./venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python3 -m venv /opt/venv
RUN pip install -r ./requirements.txt 
CMD ["python", "./main.py"] 