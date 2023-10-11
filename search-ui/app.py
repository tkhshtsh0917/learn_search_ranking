import os

import pandas as pd
import streamlit as st
from elasticsearch import Elasticsearch

from es_query import (
    generate_query_to_search_with_default,
    generate_query_to_search_with_mlr,
)


st.set_page_config(layout="wide")

search_engine_url = os.environ["ELASTICSEARCH_HOSTS"]
search_engine = Elasticsearch(search_engine_url)

keywords = st.text_input(label="Please input search keywords.", value="")

if not keywords:
    st.stop()

default_query = generate_query_to_search_with_default(keywords, size=20)
default_result = search_engine.search(index="simple_wiki", **default_query)["hits"]["hits"]

mlr_query = generate_query_to_search_with_mlr(keywords, size=20)
mlr_result = search_engine.search(index="simple_wiki", **mlr_query)["hits"]["hits"]

default_col, mlr_col = st.columns(2)

with default_col:
    st.header("default")
    st.table(
        pd.DataFrame(
            {
                "title": [h["_source"]["title"] for h in default_result],
                "score": [h["_score"] for h in default_result],
            }
        )
    )

with mlr_col:
    st.header("ranking model")
    st.table(
        pd.DataFrame(
            {
                "title": [h["_source"]["title"] for h in mlr_result],
                "score": [h["_score"] for h in mlr_result],
            }
        )
    )
