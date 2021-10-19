FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install -c rdkit=2021.03
RUN pip install soltrannet==1.0.0

WORKDIR /repo
COPY ./repo
