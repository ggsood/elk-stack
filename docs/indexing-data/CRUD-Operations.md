## CRUD Operations on a ES Index

```json
# create an index
PUT sample
{
  "settings": {
    "number_of_replicas": 1,
    "number_of_shards": 1
  }
}

# Create some data into the index
PUT sample/_doc/1
{
  "firstname": "gaurav",
  "lastname": "sood"
}

# Read the data from the index
GET sample/_doc/1

# Update the data in the index
POST sample/_update/1
{
  "doc": {
    "middlename": "kumar"
  }
}

# or using scripted painless
POST sample/_update/1
{
  "script": {
    "lang": "painless",
    "source": "ctx._source.remove('middlename')"
  }
}

# DELETE doc and index
DELETE sample-1/_doc/1

DELETE sample-1
```

From this understanding about APIs,
- PUT operation is used to create a new objects
- POST operation is used to update the objects