FROM python:3

RUN git clone repositorio

WORKDIR /repositorio

RUN pip install -r requirements

CMD ["python3", "-m", "unittest"]