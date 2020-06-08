#!/bin/bash

## Running as su
echo "elastic - nofile 65535" >> /etc/security/limits.conf
echo "vm.max_map_count = 262144" >> /etc/sysctl.conf && sysctl -p
useradd elastic
sudo su - elastic
curl -O https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.2-linux-x86_64.tar.gz
tar -xzf elasticsearch-7.5.2-linux-x86_64.tar.gz