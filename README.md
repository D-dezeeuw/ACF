# ACF - Aggregated Content Filter

A content filter that aggregates content from multiple sources and offers it through 
a vector database and a REST API.

#### Stack used
 - python
 - uvicorn                [ wsgi server ]
 - fastAPI                [ api framework ]
 - slowAPI                [ traffic limiter ]
 - httpx                  [ async routing ]
 - logging                [ logging of events ]
 - sentence_transformers  [ embedding ]