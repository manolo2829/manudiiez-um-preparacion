FROM python:3

RUN git clone linkalrepositorio

WORKDIR /nombredelrepo

RUN pip install -r requirements.txt

CMD ["python3", "-m", "unittest"]