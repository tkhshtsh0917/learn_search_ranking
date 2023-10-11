#!/usr/bin/env python

import bz2

from elasticsearch import Elasticsearch
from elasticsearch import helpers


def generate_bulk_buffer():
    buf = []
    with bz2.open("simplewiki-202109-pages-with-pageviews-20211001.bz2", "rt") as bz2f:
        for l in bz2f:
            id, title, text, page_views = l.rstrip().split("\t")
            buf.append(
                {
                    "_op_type": "create",
                    "_index": "simple_wiki",
                    "_id": id,
                    "_source": {
                        "title": title,
                        "text": text,
                        "page_views": int(page_views),
                    },
                }
            )

            if 500 <= len(buf):
                yield buf
                buf.clear()

    if buf:
        yield buf


search_engine = Elasticsearch("http://search-engine:9200/")

for buf in generate_bulk_buffer():
    try:
        helpers.bulk(search_engine, buf, refresh="true")

    except Exception:
        pass

search_engine.close()
