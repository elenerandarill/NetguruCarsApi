FROM python
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /djangoRestApp
WORKDIR /djangoRestApp
RUN python "CarsApi - project/manage.py" migrate
CMD python "CarsApi - project/manage.py" runserver 0.0.0.0:8000