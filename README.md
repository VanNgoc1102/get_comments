# docker file
Dockerfile

# docker compose
docker
- youtube-compose.yml
- key.env 

docker system prune
docker system df

VIDEO_ID="tlcWiP7OLFI&list=PLhBgTdAWkxeCL3bUv6NLGrg2248ryIUAD"

chanelid="UCvckir3Kq2WThY3k_34ZGNw" blv_AQ_D hav 815
channel_id ='UCwBew3PWseCYjLUwrnXqFrw' #huyentammon have 19 video


## Install new package

```
pip install pipenv
pipenv install package_name
pipenv install pyyaml
```


## Run docker

```
docker-compose -f docker/youtube-compose.yml build
docker-compose -f docker/youtube-compose.yml up --build -d

docker-compose -f docker/docker-compose.yml build
docker-compose -f docker/docker-compose.yml up -d
docker-compose -f docker/docker-compose.yml down -v

```

## Run code

```
docker exec -it docker_my-youtube_1 pwd
docker exec -it docker_my-youtube_1 bash
docker exec -t docker_my-youtube_1 python3 -m src.test

docker exec -t docker_my-youtube_1 python3 -m src.youtube.channels.youtube_statistics
docker exec -t docker_my-youtube_1 python3 -m src.youtube.channels.youtube_channels
docker exec -t docker_my-youtube_1 python3 -m src.youtube.channels.youtube_channels

docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j broward_accounts
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j apc_accounts
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j broward_products
```