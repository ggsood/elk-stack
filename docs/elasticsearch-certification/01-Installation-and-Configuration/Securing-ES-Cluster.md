## Securing the Elastic Search cluster

Without the Security plugin, Elasticsearch is susceptible to unauthorized use by nefarious actors. To secure Elasticsearch properly, you must use Elasticsearch Security to encrypt the various networks and enforce granular, role-based user access control. I encourage you to follow along on the Linux Academy Cloud Playground servers as we demonstrate how to:

- Generate a CA with the certutil tool
- Generate node certificates
- Add certificate passwords to the Elasticsearch keystore
- Encrypt the transport network
- Set built-in user passwords
- Encrypt the HTTP network
- Configure Kibana to work with a secured Elasticsearch cluster

## Generating certificates for each Nodes

```sh
/home/elastic/elasticsearch/bin/elasticsearch-certutil ca --out config/certs/ca --pass elastic

## master, data and node-1 nodes using the same CA
/home/elastic/elasticsearch/bin/elasticsearch-certutil cert --ca config/certs/ca --ca-pass elastic --name node-1 --out config/certs/node-1 --pass elastic
```

!!! note
    certificates generated are relative to the elasticsearch installation directory, which in our case in /home/elastic/elasticsearch, so conf dir is the one present here.

## TODO: Full host verification with IP and Hostname, also the format of certificates is PKCS#12, try with PEM too

```
cd /home/elastic/elasticsearch

echo "elastic" | ./bin/elasticsearch-keystore add --stdin xpack.security.transport.ssl.keystore.secure_password
echo "elastic" | ./bin/elasticsearch-keystore add --stdin xpack.security.transport.ssl.truststore.secure_password
echo "elastic" | ./bin/elasticsearch-keystore add --stdin xpack.security.http.ssl.keystore.secure_password
echo "elastic" | ./bin/elasticsearch-keystore add --stdin xpack.security.http.ssl.truststore.secure_password

```

### New ES Files

```yml
cluster.name: cluster-1
node.name: master-1
node.attr.zone: 1
network.host: [_local_, _site_]
cluster.initial_master_nodes: ["master-1"]
node:
  master: true
  data: false
  ingest: false
xpack.security:
  enabled: true
  transport:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/master-1
      truststore:
        path: certs/master-1
  http:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/master-1
      truststore:
        path: certs/master-1

## data-1 node
cluster.name: cluster-1
node.name: data-1
node.attr.zone: 1
node.attr.temp: hot
network.host: [_local_, _site_]
discovery.seed_hosts: ["172.31.30.103"]
cluster.initial_master_nodes: ["master-1"]
node:
  master: false
  data: true
  ingest: false
xpack.security:
  enabled: true
  transport:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/data-1
      truststore:
        path: certs/data-1
  http:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/data-1
      truststore:
        path: certs/data-1

## data-2 node
cluster.name: cluster-1
node.name: data-2
node.attr.zone: 2
node.attr.temp: warm
network.host: [_local_, _site_]
discovery.seed_hosts: ["172.31.30.103"]
cluster.initial_master_nodes: ["master-1"]
node:
  master: false
  data: true
  ingest: false
xpack.security:
  enabled: true
  transport:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/data-2
      truststore:
        path: certs/data-2
  http:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/data-2
      truststore:
        path: certs/data-2

## cluster-2 node-1
cluster.name: cluster-2
node.name: node-1
node.attr.zone: 1
network.host: [_local_, _site_]
cluster.initial_master_nodes: ["node-1"]
node:
  master: true
  data: true
  ingest: true
xpack.security:
  enabled: true
  transport:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/node-1
      truststore:
        path: certs/node-1
  http:
    ssl:
      enabled: true
      verification_mode: certificate
      keystore:
        path: certs/node-1
      truststore:
        path: certs/node-1

```

### Restart commands
```pkill -F pid && ./bin/elasticsearch -d -p pid```

### setup passwords 

```sh
./bin/elasticsearch-setup-passwords interactive

# change in kibana yaml with username and password
```