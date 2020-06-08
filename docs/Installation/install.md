On CentOS 7 Machine, elastic version 6.2.4 as this installs xpack, in newer versions xpack is installed by default

Install java 

yum install java-1.8.0-openjdk -y

## Going via tar 
1. Start with adding a user elastic,  `sudo useradd elastic`
2. Increase security limits for the elastic user
   In `/etc/security/limits.conf` add `elastic - nofile 65536`
3. Increase Memory Map limits
   In `/etc/sysctl.conf` add `vm.max_map_count = 262144`
   do `sysctl -p` to load system settings
4. Download elasticsearch 
   curl -L -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.2.4.tar.gz
   tar -xzvf 
   test - start elastic and check if its working
   ```
   ./bin/elasticsearch -d -p pid
   less logs/elasticsearch
   kill `cat pid`
   ```
5. Download Kibana
   curl -L -O https://artifacts.elastic.co/downloads/kibana/kibana-6.2.4-linux-x86_64.tar.gz

6. Install x-pack
   curl -L -O https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-6.2.4.zip

    *For Offline installation*
   ./elasticsearch/bin/elasticsearch-plugin install file:///home/elastic/x-pack-6.2.4.zip


7. Securing and Encryption

In master node ~/elasticsearch/config/certs

~/elasticsearch/bin/x-pack/certutil ca
*passowod=a*
~/elasticsearch/bin/x-pack/certutil cert --ca elastic-stack-ca.p12 --name master --dns gsood1c.mylabserver.com --ip 172.31.22.182
~/elasticsearch/bin/x-pack/certutil cert --ca elastic-stack-ca.p12 --name data1 --dns gsood2c.mylabserver.com --ip 172.31.31.49
~/elasticsearch/bin/x-pack/certutil cert --ca elastic-stack-ca.p12 --name data2 --dns gsood3c.mylabserver.com --ip 172.31.22.21

In other nodes copy
scp data1.p12 elastic@172.31.31.49:/home/elastic/
```
~/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
~/elasticsearch/bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password
~/elasticsearch/bin/elasticsearch-keystore add xpack.security.http.ssl.keystore.secure_password
~/elasticsearch/bin/elasticsearch-keystore add xpack.security.http.ssl.truststore.secure_password
```
```
xpack.security.enabled: true
xpack.security.transport.ssl.enabled: true
xpack.security.transport.ssl.verification_mode: full
xpack.security.transport.ssl.keystore.path: certs/master.p12
xpack.security.transport.ssl.truststore.path: certs/master.p12
xpack.security.http.ssl.enabled: true
xpack.security.http.ssl.keystore.path: certs/master.p12
xpack.security.http.ssl.truststore.path: certs/master.p12

## same in other  nodes  with correct keystore
```

In Kibana

~/kibana/bin/kibana-plugin install file:///home/elastic/x-pack-6.2.4.zip