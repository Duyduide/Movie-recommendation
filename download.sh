# /bin/bash
mkdir ./data

curl -L -o ./data/data.zip https://www.kaggle.com/api/v1/datasets/download/rounakbanik/the-movies-dataset

unzip ./data/data.zip -d ./data