## Questions to practice for Installation and Configuration part

Use CentOS box

1. Given 3 node setup, node-1, node-2, node-3 setup an ES cluster with following requirements
   a. node-1 is dedicated master node
   b. node-2, node-3 are data and ingest node
   c. cross cluster nodes should not be there

2. Given 3 node setup, node-1, node-2, node-3 setup an ES cluster with following requirements
   a. node-1 is dedicated master node
   b. node-2 is data and ingest node
   c. node-3 is data, and ml node

3. Given 3 node setup, node-1, node-2, node-3 setup an ES cluster with following requirements
    a. node-1 is master node, node 2 and 3 are data nodes
    b. security is enabled on each node, transport and client
    c. setup custom password for elastic, kibana and logstash user

4. Given 4 node setup, node 1-4, setup 2 clusters, c1 and c2 
    a. c1, 3 nodes, 1 master+kibana, 2 data
    b. c2, 1 node master+kibana
    c. security is enabled
    d. cross cluster search is working on them

5. Given 3 node setup, node-1, node-2, node-3 setup hot warm architecture with
    a. node-1 being master,
    b. node-2 being hot node and node-3 being warm
    c. allocate indices at each node level

**Points to note here -**
* when designing a cluster always see the system requirements and elasticsearch requirements
  * system requirements: swappiness, file limits, process limit, vm max open files limits
  * elasticsearch requirements: path for logs and data, elastic config file, jvm options file, logging (if required)

### Steps to debug a cluster if not working

1. ssh into the node,  check es is working on the node, perform
   1. check es is running, use `ps aux` or check logs of ES cluster 
   2. curl on private ip of the host, default port is 9200 
2. if es is not running, check the config.yaml and see the properties of the node
   1. do make sure about the nodes attrs, names, cluster name, path etc.
   2. run the es on node, and check logs if all good continue to next, if not check the logs for errors
3. once es is running always check the health of the cluster, and indices, no index should be red or yellow unless stated.
   1. if index is yellow check why, use `explain allocation` api to see why index is not allocated.
   2. also check the index settings it might be the replicas count is more then the number of nodes.