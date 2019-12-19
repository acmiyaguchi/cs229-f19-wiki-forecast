FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y gcc g++

# install the app
WORKDIR /app
ADD . /app

# install trmf from the external packages, ensure the submodule is initialized
RUN conda install -y --file requirements.txt
RUN pip install -e external/exp-trmf-nips16/python

RUN pip install pandas pyarrow
