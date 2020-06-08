## ES Templates

``` json
PUT _template/sample
{
  "aliases": {
    "test": {}
  },
  "mappings": {
    "properties": {
      "firstname": {
        "type": "keyword"
      },
      "lastname": {
        "type": "keyword"
      }
    }
  },
  "settings": {
    "number_of_replicas": 1,
    "number_of_shards": 1
  },
  "index_patterns": [
    "sample-*"
  ],
  "order": 0
}
```

`index_patterns` - tells which indices will have this template
`order` - defines which template to use in case of multiple matches

### Dynamic Templates

```json
PUT _template/sample
{
  "aliases": {
    "test": {}
  },
  "mappings": {
    "properties": {
      "firstname": {
        "type": "keyword"
      }
    },
    "dynamic_templates": [ // List of dynamic templates
      {
        "strings_to_keyword": { // name of pattern
          "match_mapping_type": "string", // data field to match
          "unmatch": "*_text", // unmatch a field based on key
          "mapping": {
            "type": "keyword" // mapping for the field
          }
        }
      },
      {
        "long_to_integer": {
          "match_mapping_type": "long",
          "mapping": {
            "type": "integer"
          }
        }
      },
      {
        "strings_to_text": {
          "match_mapping_type": "string",
          "match": "*_text",
          "mapping": {
            "type": "text"
          }
        }
      }
    ]
  },
  "settings": {
    "number_of_replicas": 1,
    "number_of_shards": 1
  },
  "index_patterns": [
    "sample-*"
  ]
}
```