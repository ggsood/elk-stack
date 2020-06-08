```json
PUT _ingest/pipeline/test-pipeline
{
  "description": "Converts M/F to Male/Female",
  "processors": [
    {
      "remove": {
        "field": "account_number"
      }
    },
    {
      "set": {
        "field": "_source.fullname",
        "value": "{{_source.firstname}} {{_source.lastname}}"
      }
    },
    {
      "convert": {
        "field": "age",
        "type": "string"
      }
    },
    {
      "script": {
        "lang": "painless",
        "source": """
  if(ctx.gender == "M") {
    ctx.gender = "male"
  } else {
    ctx.gender = "female"
  }
"""
      }
    }
  ]
}

POST _reindex
{
  "source": {
    "index": "accounts"
  },
  "dest": {
    "pipeline": "test-pipeline", // pipeline name
    "index": "banking-new"
  }
}

GET banking-new/_search

```