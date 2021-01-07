cd /reto_everis
docker-compose stop
docker-compose rm -fv
docker-compose build
docker-compose up -d


echo " se desplego contenedor docker"