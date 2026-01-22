FROM python:3.14
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT [ "streamlit", "run", "streamlit_app.py" ]