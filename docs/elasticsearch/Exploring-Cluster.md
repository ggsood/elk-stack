###Cluster health

```
GET /_cat/health?v

pattern of how we access data in Elasticsearch. That pattern can be summarized as follows:

<HTTP Verb> /<Index>/<Type>/<ID>
```


cluster health, we either get green, yellow, or red.

Green - everything is good (cluster is fully functional)
Yellow - all data is available but some replicas are not yet allocated (cluster is fully functional)
Red - some data is not available for whatever reason (cluster is partially functional)

*Note: When a cluster is red, it will continue to serve search requests from the available shards but you will likely need to fix it ASAP since there are unassigned shards.*

Elasticsearch uses ***unicast network discovery*** by default to find other nodes on the same machine, it is possible that you could accidentally start up more than one node on your computer and have them all join a single cluster

https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-discovery-zen.html

https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-transport.html

https://www.elastic.co/guide/en/elasticsearch/reference/current/important-settings.html

**Cluster state updates**
The master node is the only node in a cluster that can make changes to the cluster state. The master node processes one cluster state update at a time, applies the required changes and publishes the updated cluster state to all the other nodes in the cluster. Each node receives the publish message, acknowledges it, but does not yet apply it. If the master does not receive acknowledgement from at least discovery.zen.minimum_master_nodes nodes within a certain time (controlled by the discovery.zen.commit_timeout setting and defaults to 30 seconds) the cluster state change is rejected.

Once enough nodes have responded, the cluster state is committed and a message will be sent to all the nodes. The nodes then proceed to apply the new cluster state to their internal state. The master node waits for all nodes to respond, up to a timeout, before going ahead processing the next updates in the queue. The discovery.zen.publish_timeout is set by default to 30 seconds and is measured from the moment the publishing started. Both timeout settings can be changed dynamically through the cluster update settings api.
https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-update-settings.html