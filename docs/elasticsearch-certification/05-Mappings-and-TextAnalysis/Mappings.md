## Define index mappings

```sh
PUT sample-1
{
  "mappings": {
    "properties": {
      "name": {
        "type": "keyword"
      },
      "bio": {
        "type": "text"
      },
      "age": {
        "type": "short"
      },
      "interest_rate": {
        "type": "scaled_float",
        "scaling_factor": 10000
      },
      "geoip": {
        "type": "geo_point"
      },
      "ip":{
        "type": "ip"
      },
      "is_member": {
        "type": "boolean"
      },
      "last_modified": {
        "type": "date"
      }
    }
  }
}
```

## Text Analysis

```sh
PUT sample-1
{
  "mappings": {
    "properties": {
      "name": {
        "type": "keyword"
      },
      "bio": {
        "type": "text"
      },
      "age": {
        "type": "short"
      },
      "interest_rate": {
        "type": "scaled_float",
        "scaling_factor": 10000
      },
      "geoip": {
        "type": "geo_point"
      },
      "ip":{
        "type": "ip"
      },
      "is_member": {
        "type": "boolean"
      },
      "last_modified": {
        "type": "date"
      }
    }
  }
}

GET _cat/indices

GET sample-1

## Text analysis

POST _analyze
{
  "analyzer": "standard",
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

POST _analyze
{
  "analyzer": "english",
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

POST _analyze
{
  "analyzer": "simple",
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

POST _analyze
{
  "analyzer": "whitespace",
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

POST _analyze
{
  "analyzer": "fingerprint",
  "text": "Yes yes, Gödel said this sentence is consistent and."
}

PUT analysis-1
{
  "settings": {
    "analysis": {
      "analyzer": {
        "whitespace_lowecase": {
          "tokenizer": "whitespace",
          "filter": [
            "lowercase"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "whitespace_lowecase"
      }
    }
  }
}

GET analysis-1

PUT analysis-1/_doc/1
{
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

GET analysis-1/_search
{
  "query": {
    "match": {
      "text": "quick"
    }
  }
}

POST analysis-1/_analyze
{
  "analyzer": "whitespace_lowecase",
  "text": "The 3 QUICK Brown-Foxes jumped over the neighor's fence."
}

# custome token filters and char filters
PUT analysis-2
{
  "settings": {
    "analysis": {
      "analyzer": {
        "standard_emoji": {
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "english_stop"
          ],
          "char_filter": ["emoji"],
          "type": "custom"
        }
      },
      "filter": {
        "english_stop":{
          "type": "stop",
          "stopwords": "_english_"
        }
      },
      "char_filter": {
        "emoji": {
          "type": "mapping",
          "mappings": [
            ":) => happy",
            ":( => sad"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "standard_emoji"
      }
    }
  }
}

PUT analysis-2/_doc/2
{
  "text": "The 3 :) Brown-Foxes jumped over the :( neighor's fence."
}

GET analysis-2/_search
{
  "query": {
    "match": {
      "text": "happy"
    }
  }
}


POST analysis-2/_analyze
{
  "analyzer": "standard_emoji",
  "text": "The 3 :) Brown-Foxes jumped over the :( neighor's fence."
}

```

!!! note
    please check custom analyzer with index, index-templates and other shared components

## Multi Field Mappings Nested Arrays

```sh
GET _cat/indices


PUT sample-1/_doc/1
{
  "field_1": "value"
}

GET sample-1/_search
{
  "query": {
    "match": {
      "field_1": "value"
    }
  }
}

PUT sample-3
{
  "mappings": {
    "properties": {
      "field_1": {
        "type": "keyword",
        "fields": {
          "standard": {
            "type": "text"
          },
          "simple": {
            "type": "text",
            "analyzer": "simple"
          },
          "english": {
            "type": "text",
            "analyzer": "english"
          }
        }
      }
    }
  }
}

GET sample-3


## Nested array  of objects

PUT neseted_array-1/_doc/1
{
  "group": "Horizon Members",
  "members": [
    {
      "firstname": "gaurav",
      "lastname": "sood",
      "email": "g@g.com"
    },
    {
      "firstname": "nick",
      "lastname": "tucker",
      "email": "n@n.com"
    }
  ]
}

GET  neseted_array-1

GET neseted_array-1/_search
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "members.firstname.keyword": {
              "value": "gaurav"
            }
          }
        },
        {
          "term": {
            "members.lastname.keyword": {
              "value": "tucker"
            }
          }
        }
      ]
    }
  }
}

PUT neseted_array-2
{
  "mappings": {
    "properties": {
      "members": {
        "type": "nested"
      }
    }
  }
}

PUT neseted_array-2/_doc/1
{
  "group": "Horizon Members",
  "members": [
    {
      "firstname": "gaurav",
      "lastname": "sood",
      "email": "g@g.com"
    },
    {
      "firstname": "nick",
      "lastname": "tucker",
      "email": "n@n.com"
    }
  ]
}


GET neseted_array-2/_search
{
  "query": {
    "nested": {
      "path": "members",
      "query": {
        "bool": {
          "must": [
            {
              "term": {
                "members.firstname.keyword": {
                  "value": "gaurav"
                }
              }
            },
            {
              "term": {
                "members.lastname.keyword": {
                  "value": "sood"
                }
              }
            }
          ]
        }
      },
      "inner_hits": {
        "highlight": {
          "fields": {
            "members.firstname.keyword": {
              
            },
            "members.lastname.keyword": {}
          }
        }
      }
    }
  }
}
```

## Parent child relationship

searching to be covered later, do remember for having this the parent and child doc should be in the same shared and 
have explicit document ids assigned to them. 

This is a performance heavy operation.

```sh
PUT parent_child-1
{
  "mappings": {
    "properties": {
      "qa" :{
        "type": "join",
        "relations": {
          "question": "answer"
        }
      }
    }
  }
}


PUT parent_child-1/_doc/1
{
  "text": "which node type in ES stores data",
  "qa": {
    "name": "question"
  }
}

GET parent_child-1/_doc/1

# route doc 2 in the same shard as doc 1
PUT parent_child-1/_doc/2?routing=1
{
  "text": "data node",
  "qa": {
    "name": "answer",
    "parent": "1"
  }
}

GET parent_child-1/_doc/2
```


