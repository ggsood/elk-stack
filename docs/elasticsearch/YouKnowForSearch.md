# ***You Know, for Search***

Elasticsearch is an open-source search engine built on top of Apache Lucene, a fulltext search-engine library.
But Lucene is just a library. To leverage its power, you need to work in Java and need to integrate Lucene directly with your application.
Lucene is very complex and this approach is time and resource consuming.

Elasticsearch, written in Java  uses Lucene internally for all of its indexing and searching, it aims to make full-text search easy by hiding the complexities of
Lucene behind a simple, coherent, RESTful API. However Elasticsearch is more then "just" full-text search.

It can also be described as follows:
- A distributed near real-time document store where every field is indexed and searchable.
- A distributed search engine with real-time analytics
- Capable of scaling to hundreds of servers and petabytes of structured and unstructured data

Moreover it packages up all this functionality into a standalone server that any application can talk to via a simple **RESTful API**, using any webclient or just cli.

## RESTful API with JSON over HTTP

All languages can communicate with Elasticsearch over port 9200 using a RESTful API, accessible with your favorite web client or just curl command.

A request to Elasticsearch consists of the same parts as any HTTP request:

`curl -X<VERB> '<PROTOCOL>://<HOST>/<PATH>?<QUERY_STRING>' -d '<BODY>'`

where

`VERB`: The appropriate HTTP method or verb: GET, POST, PUT, HEAD, or DELETE.

`PROTOCOL`: Either http or https 

`HOST`: The hostname of any node in your Elasticsearch cluster, or localhost for a node on your local machine.

`PORT`: The port running the Elasticsearch HTTP service, which defaults to 9200.

`QUERY_STRING`:  Any optional query-string parameters 

`BODY`: A JSON-encoded request body

Example - to count the number of documents in the cluster
```bash
curl -XGET 'http://localhost:9200/_count?pretty' -d '
{
    "query": {
        "match_all": {}
    }
}'
```

## **Document Oriented**

Elasticsearch is document oriented, meaning that it stores entire objects or documents.

It not only stores them, but also indexes the contents of each document in order to
make them searchable. 

In Elasticsearch, you index, search, sort, and filter documents — not rows of columnar data.

Elasticsearch uses JavaScript Object Notation, or **JSON**, as the serialization format for
documents.

JSON serialization is supported by most programming languages, and
has become the standard format used by the NoSQL movement.


## **Finding your feet**

Lets start with a simple tutorial covering basics concepts like indexing, search and aggregations.
We will cover more on them in next sections.

Have a running instance of Elasticsearch running, single node cluster will be good, for details you can refer this [link](https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started-install.html).


### *Index some documents*

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
curl -H "Content-Type: application/json" -XPOST "localhost:9200/bank/_bulk?pretty&refresh" --data-binary "@accounts.json"
curl "localhost:9200/_cat/indices?v"
```
The response indicates that 1,000 documents were indexed successfully.

### *Start Searching*
Once you have ingested some data into an Elasticsearch index, you can search it by sending requests to the *_search* endpoint. 
- To access the full suite of search capabilities, you use the Elasticsearch Query DSL to specify the search criteria in the request body. 
- You specify the name of the index you want to search in the request URI.

```bash
GET /bank/_search
{
  "query": { "match_all": {} },
  "sort": [
    { "account_number": "asc" }
  ]
}
```

Each search request is **self-contained**: Elasticsearch does not maintain any state information across requests. 

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

### *Analytics*

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

Now that you’ve set up a cluster, indexed some documents, and run some searches and aggregations, time to dig inside elasticsearch more in the next sections.