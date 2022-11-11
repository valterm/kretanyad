FROM python:3.9 
WORKDIR .
ADD . .
RUN pip install -r ./requirements.txt 
CMD ["python", "./main.py"] 