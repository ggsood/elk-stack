# Elasticsearch Basic Concepts and Terms
---

## Near Real Time
Elasticsearch is a near-realtime search platform. What this means is there is a **slight latency** (normally one second) from the time you index a document until the time it becomes searchable.

### Cluster
- A cluster is a collection of one or more nodes (servers) that together holds your entire data and provides federated indexing and search capabilities across all nodes. 
- A cluster is identified by a unique name which by default is "elasticsearch". This name is important because a node can only be part of a cluster if the node is set up to join the cluster by its name.

- Make sure that you don’t reuse the same cluster names in different environments, otherwise you might end up with nodes joining the wrong cluster.

  - For instance you could use logging-dev, logging-stage, and logging-prod for the development, staging, and production clusters.

### Node

- A node is a single server that is part of your cluster, stores your data, and participates in the cluster’s indexing and search capabilities. 
  - Just like a cluster, a node is identified by a name which by default is a random Universally Unique IDentifier (UUID) that is assigned to the node at startup. 
  - You can define any node name you want if you do not want the default. 
  - This name is important for administration purposes where you want to identify which servers in your network correspond to which nodes in your Elasticsearch cluster.

*A node can be configured to join a specific cluster by the cluster name. By default, each node is set up to join a cluster named elasticsearch which means that if you start up a number of nodes on your network and—assuming they can discover each other—they will all automatically form and join a single cluster named elasticsearch.*

### Index

An index is a collection of documents that have somewhat similar characteristics.
An index is identified by a name (that must be all lowercase) and this name is used to refer to the index when performing indexing, search, update, and delete operations against the documents in it.

### Type - Depreceated
A type used to be a logical category/partition of your index to allow you to store different types of documents in the same index, e.g. one type for users, another type for blog posts.

**Reason -** fields that have the same name in different mapping types are backed by the same Lucene field internally.
This can lead to frustration when, for example, you want deleted to be a date field in one type and a boolean field in another type in the same index.
On top of that, storing different entities that have few or no fields in common in the same index leads to sparse data and interferes with Lucene’s ability to compress documents efficiently.

Alternatives- 
1. index per document type
This approach has two benefits:

Data is more likely to be dense and so benefit from compression techniques used in Lucene.
The term statistics used for scoring in full text search are more likely to be accurate because all documents in the same index represent a single entity.

2. custom type

```
PUT twitter
{
  "mappings": {
    "_doc": {
      "properties": {
        "type": { "type": "keyword" }, 
        "name": { "type": "text" },
        "user_name": { "type": "keyword" },
        "email": { "type": "keyword" },
        "content": { "type": "text" },
        "tweeted_at": { "type": "date" }
      }
    }
  }
}

The explicit type field takes the place of the implicit _type field.
Based on your search
"filter": {
    "match": {
        "type": "tweet"  or "type": "user"
    }
}
```

Refer - https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html

### Document -
- A document is a basic unit of information that can be indexed.
- This document is expressed in JSON (JavaScript Object Notation) which is a ubiquitous internet data interchange format.

### Shards and Replicas -
*Subdivide your index into multiple pieces called shards.*

When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.

Sharding is important for two primary reasons:

1. It allows you to horizontally split/scale your content volume
2. It allows you to distribute and parallelize operations across shards (potentially on multiple nodes) thus increasing performance/throughput.

*Elasticsearch allows you to make one or more copies of your index’s shards into what are called replica shards, or replicas for short.*

Replication is important for two primary reasons:

1. It provides high availability in case a shard/node fails. For this reason, it is important to note that a replica shard is never allocated on the same node as the original/primary shard that it was copied from.
2. It allows you to scale out your search volume/throughput since searches can be executed on all replicas in parallel.

The number of shards and replicas can be defined per index at the time the index is created.
After the index is created, you may also change the number of replicas dynamically anytime.

**You can change the number of shards for an existing index using the _shrink and _split APIs, however this is not a trivial task and pre-planning for the correct number of shards is the optimal approach.**

*Each Elasticsearch shard is a Lucene index. There is a maximum number of documents you can have in a single Lucene index. As of LUCENE-5843, the limit is 2,147,483,519 (= Integer.MAX_VALUE - 128) documents. You can monitor shard sizes using the _cat/shards API.*