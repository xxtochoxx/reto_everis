FROM python:3.6
LABEL maintainer="Humberto Melendez Fernandez"
HEALTHCHECK --interval=50s --timeout=5s \ CMD curl -f http://localhost/ || exit 1
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
