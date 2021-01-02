For clearing the certification do the following questions:

1. Establish a ES cluster with specific requirements and
   1. 3 nodes - 1 master, 1 data and 1 ingest, with each node having zone, temp and region attributes
   2. 3 nodes - 3 master + data + ingest, with custom attributes
   3. 3 nodes - 1 master + 2 data nodes, with custom attributes

2. Secure the ES cluster 
   1. 1 nodes cluster, with Encryption over transport and client (http)
   2. 3 nodes cluster, with E2E encryption
   3. Verification mode full, certificate and none
      1. Steps to generate certificates using elasticsearch-cert util command.


3. Configure RBAC access to the cluster and
   1. Create custom roles showing different capabilities for the users.