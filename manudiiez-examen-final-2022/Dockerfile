FROM python:3

RUN git clone repositorio

WORKDIR repositorio

RUN pip install -r requirements.txt

CMD ["python3", "-m", "unittest"]