FROM bentoml/model-server:0.11.0-py39
MAINTAINER ersilia

RUN pip install rdkit==2024.3.5
RUN pip install soltrannet==1.0.0

WORKDIR /repo
COPY . /repo
