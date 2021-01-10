### Disaster scenarios

- CCR provides a way to automatically synchronize indices from your primary cluster to a secondary remote cluster that can serve as a hot backup. 
- If the primary cluster fails, the secondary cluster can take over. 
- You can also use CCR to create secondary clusters to serve read requests in geo-proximity to your users.


Cross-cluster replication is **active-passive**. 
The index on the primary cluster is the active leader index and handles all write requests. *Indices replicated to secondary clusters are read-only followers.*