tar -xzf /vagrant/install/elasticsearch-7.8.0-linux-x86_64.tar.gz -C /home/vagrant
cp /vagrant/install/elasticsearch.yml /home/vagrant/elasticsearch-7.8.0/config/elasticsearch.yml
cp /vagrant/install/jvm.options /home/vagrant/elasticsearch-7.8.0/config/jvm.options