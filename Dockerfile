FROM django:1.9-python2

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["/usr/local/bin/gunicorn", "hackathon.wsgi:application", "-w 2", "-b", ":8000"]
