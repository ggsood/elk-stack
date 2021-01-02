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
    -XPOST "localhost:9200/logs/_bulk?pretty&refresh" \
    --data-binary "@logs.json"
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