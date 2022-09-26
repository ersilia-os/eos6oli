FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install soltrannet==1.0.0

WORKDIR /repo
COPY ./repo
