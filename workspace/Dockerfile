FROM python:3.7

RUN pip install --no-cache-dir matplotlib xgboost scikit-learn elasticsearch~=7.17

WORKDIR /workspace

ADD dataset/simplewiki-202109-pages-with-pageviews-20211001.bz2 .

COPY workspace/ .
COPY es_query.py .
