FROM python:3.12

RUN mkdir /app/
WORKDIR /app/
COPY ./app.py /app/
COPY ./requirements.txt /app/
COPY ./utils/ /app/utils/
COPY ./utils/apiutils/ /app/utils/apiutils/
COPY ./utils/dbutils/ /app/utils/dbutils/
# COPY ./templates/ /app/templates/
COPY ./static/ /app/static/
COPY ./src/ /app/src/
COPY ./router/ /app/router/

EXPOSE 8000
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app:app", "--host","0.0.0.0", "--reload","--port","8000"]