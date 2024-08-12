
FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install pipenv

RUN pipenv install

EXPOSE 8501

CMD ["pipenv", "run", "streamlit","run", "main.py"]