```sh
## Reading
GET sample-1/_search


## updating method 1
POST sample-1/_update/PVLQxHYB1GqVHCy3GPXV
{
  "doc":  {
    "lastname": "sood",
    "middleinitial": "K"
  }
}


## updating method 2
POST sample-1/_update/PVLQxHYB1GqVHCy3GPXV
{
  "script":  {
    "lang": "painless",
    "source": "ctx._source.remove('middleinitial')"
  }
}


## Deleting
DELETE sample-1/_doc/PVLQxHYB1GqVHCy3GPXV

## Cleanup

DELETE sample-1
```

## Sample Datasets

```
curl -LO https://github.com/linuxacademy/content-elastic-certified-engineer/raw/master/sample_data/accounts.json

# incase of logs.json remove the _type field in the metadata of the json document.
curl -LO https://github.com/linuxacademy/content-elastic-certified-engineer/raw/master/sample_data/logs.json

curl -LO https://github.com/linuxacademy/content-elastic-certified-engineer/raw/master/sample_data/shakespeare.json
```

### *submit the data*
```
curl -H "Content-Type: application/x-ndjson" \
    -XPOST "localhost:9200/bank/_bulk?pretty&refresh" \
    --data-binary "@accounts.json"
```
!!! note
    split  -l 10000 logs.json # incase u get circuit breaking exception
    for f in xa*; do
    curl -H "Content-Type: application/x-ndjson" \
        -XPOST "localhost:9200/logs/_bulk?pretty&refresh" \
        --data-binary @$f > logs_bulk.json
    done


## add alias
```sh
## Aliases
GET bank/_alias

POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "shakespeare",
        "alias": "henry",
        "filter": {
          "term": {
            "play_name": "Henry IV"
          }
        }
      }
    }
  ]
}

GET henry/_search
```

## Index Template
PUT  _template/logs
{
  "aliases": {
    "logs_sample": {}
  },
  "mappings": {
    "properties": {
      "field_1": {
        "type": "keyword"
      }
    }
  },
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 1
  },
  "index_patterns": ["logs-*"]
}


### Reindex indices with remote hosts

```sh
GET _search
{
  "query": {
    "match_all": {}
  }
}

GET _cat/indices

# reindex from a host
POST _reindex
{
  "source": {
    "remote": {
      "host": "https://172.31.30.103:9200",
      "username": "elastic",
      "password": "elastic"
    },
    "index": "bank"
  },
  "dest": {
    "index": "bank"
  }
}

POST _reindex
{
  "source": {
    "remote": {
      "host": "https://172.31.30.103:9200",
      "username": "elastic",
      "password": "elastic"
    },
    "index": "bank",
    "query": {
      "term": {
        "gender.keyword": {
          "value": "F"
        }
      }
    }
  },
  "dest": {
    "index": "accounts_ladies"
  },
  "script": {
    "lang": "painless",
    "source": "ctx._source.remove('gender')"
  }
}

GET accounts_female/_search

GET accounts_ladies/_search

GET bank/_search

GET bank/_search
{
  "query": {
"term": {
      "gender.keyword": {
        "value": "F"
      }
    }
  }
}

POST bank/_update_by_query
{
  "script": {
    "lang": "painless",
    "source": """
      ctx._source.balance+=ctx._source.balance*0.03;
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
```

## Ingest Pipelines

```sh
PUT _ingest/pipeline/test_pipeline
{
  "description": "Changes to bank index",
  "version": 1,
  "processors": [
    {
      "remove": {
        "field": "account_number"
      }
    },
    {
      "set": {
        "field": "_source.fullname",
        # mustache  syntax here
        "value": "{{_source.firstname}} {{_source.lastname}}" 
      }
    },
    {
      "convert": {
        "field": "_source.age",
        "type": "string"
      }
    },
    {
      "script": {
        "lang": "painless",
        "source": """
        # painless works separately here
        if(ctx.gender == "M") {
          ctx.gender = "male"
        } else if (ctx.gender == "F") {
          ctx.gender = "female"
        }
"""
      }
    }
  ]
}
```