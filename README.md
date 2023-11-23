python3 ./src/youtube/comments/main.py
python3 ./src/youtube/comments/main.py


main.py
my_key.json
Pipfile
Pipfile.lock


#VIDEO_ID="tlcWiP7OLFI&list=PLhBgTdAWkxeCL3bUv6NLGrg2248ryIUAD"
#chanelid="UCvckir3Kq2WThY3k_34ZGNw" blv_AQ_D

channel_id ='UCwBew3PWseCYjLUwrnXqFrw' #huyentammon have 19 video



# eq-data-pipeline

## Install new package

```
pip install pipenv
pipenv install package_name
pipenv install pyyaml
```


## Run docker

```
docker-compose -f docker/docker-compose.yml build

docker-compose -f docker/docker-compose.yml up -d
```


## Run code
```
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j broward_accounts
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j apc_accounts
docker exec -t eq_data_pipeline python -m src.pipeline.getfly.etl -j broward_products
```
```