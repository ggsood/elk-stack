# Reindex
``` json
POST _reindex
{
  "source": {
    "index": "bank",
    "query": {
      "term": {
        "gender.keyword": {
          "value": "M"
        }
      }
    }
  },
  "dest": {
    "index": "bank-male"
  }
}
```



# update by query
```json
GET bank/_search 

POST bank/_update_by_query
{
  "script": {
    "lang": "painless",
    "source": """
      ctx._source.balance += ctx._source.balance*0.03;
      if (ctx._source.transactions == null) {
        ctx._source.transactions = 1;
      } else {
        ctx._source.transactions++;
      }
    """
  },
  "query": {
    "term": {
      "gender.keyword": "F"
    }
  }
}

GET bank/_doc/13
```