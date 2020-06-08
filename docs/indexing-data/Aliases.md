## ES Aliases

```json
POST _aliases
{
  "actions": [
    {
      "add": {
        "index": "sample-1",
        "alias": "dummy"
      }
    }
  ]
}

```

- `POST` API as this will update the index alias 

```<logstash-{now/d}-000001>```