FROM tiangolo/uwsgi-nginx-flask:python3.9

# Install requirements
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install --upgrade numpy
RUN pip install pytest

ENV STATIC_URL /static
ENV STATIC_PATH /app/static




