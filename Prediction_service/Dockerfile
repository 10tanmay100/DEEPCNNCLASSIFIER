FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]


# FROM python:3.8
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE $PORT
# CMD gunicorn --workers=1 --bind 0.0.0.0:$PORT app:app