### Number of primary shards for an index is fixed

- Number of primary shards in an index is fixed at the time that an **index is created**, 
- number of **replica shards can be changed at any time**, without interrupting indexing or query operations.

### Best practice 

- ***Aim to keep the average shard size between a few GB*** and a few tens of GB. For use cases with time-based data, it is common to see shards in the 20GB to 40GB range.
- **Avoid the gazillion shards problem**. The number of shards a node can hold is proportional to the available heap space. As a general rule, **the number of shards per GB of heap space should be less than 20**.

implying if i give 1g of jvm heap, max no. of shards should be >20 
