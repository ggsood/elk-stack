# **Finding your feet**
---

Lets start with a simple tutorial covering basics concepts like indexing, search and aggregations.
We will cover more on them in next sections.

Have a running instance of Elasticsearch running, single node cluster will be good to follow along. 

For details on the different installations you can refer this [getting-started-install](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html).

For keeping things simple we will use docker to run the elasticsearch node and later on use docker-compose to have a working ELK Stack.

To start a single-node ES cluster for development or testing

```shell
docker run -p 9200:9200 -p 9300:9300 \
        -e "discovery.type=single-node" \
        docker.elastic.co/elasticsearch/elasticsearch:7.10.1
```

## *Index some documents*

```bash
PUT /customer/_doc/1
{
  "name": "John Doe"
}
```

This request automatically creates the customer index if it doesn’t already exist, adds a new document that has an ID of 1, and stores and indexes the name field.

The new document is available immediately from any node in the cluster. You can retrieve it with a GET request that specifies its document ID.
```bash
GET /customer/_doc/1
```
You can also load documents in bulk by following steps-

1. Download the [accounts.json](https://github.com/elastic/elasticsearch/blob/master/docs/src/test/resources/accounts.json?raw=true) sample data set.
2. Index the account data into the bank index with the following _bulk request:
```bash
## Load the bulk json
curl -H "Content-Type: application/json" \
    -XPOST "localhost:9200/bank/_bulk?pretty&refresh" \
    --data-binary "@accounts.json"

## check the new index with the documents
curl "localhost:9200/_cat/indices?v"
```
The response indicates that 1,000 documents were indexed successfully.

## *Start Searching*
Once you have ingested some data into an Elasticsearch index, you can search it by sending requests to the *_search* endpoint. 
- To access the full suite of search capabilities, you use the Elasticsearch Query DSL to specify the search criteria in the request body. We will discuss more on this in the later sections.
- You can specify the name of the index you want to search in the request URI.

```bash
GET /bank/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
```

Each search request is **self-contained**: meaning Elasticsearch does not maintain any state information across requests, so every request you fire will be a new request all together.

To page through the search hits, specify the from and size parameters in your request.
For example, the following request gets hits 10 through 19:
```bash
GET /bank/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ],
  "from": 10,
  "size": 10
}
```

**Full-Text Search** - the following request only matches addresses that contain the phrase `mill lane` 
```bash
GET /bank/_search
{
  "query": { "match_phrase": { "address": "mill lane" } }
}
```

## *Analytics*

Elasticsearch aggregations enable you to get meta-information about your search results and answer questions like, "How many account holders are in Texas?" or "What’s the average balance of accounts in Tennessee?" 

You can search documents, filter hits, and use aggregations to analyze the results all in one request.
```bash
GET /bank/_search
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state.keyword"
      }
    }
  }
}
```

## **Next Steps**

Now that you’ve set up a cluster, indexed some documents, and run some searches and aggregations, time to dig inside elasticsearch more.
