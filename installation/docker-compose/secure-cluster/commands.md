# Create cluster
{
    docker-compose -f create-certs.yml run --rm create_certs
    docker-compose -f elastic-docker-tls.yml up -d
}



## Generate passwords
```
docker exec es01 /bin/bash -c "bin/elasticsearch-setup-passwords \
auto --batch \
-Expack.security.http.ssl.certificate=certificates/es01/es01.crt \
-Expack.security.http.ssl.certificate_authorities=certificates/ca/ca.crt \
-Expack.security.http.ssl.key=certificates/es01/es01.key \
--url https://es01:9200"
```

# Refesh with kibana password
{
    docker-compose stop
    docker-compose -f elastic-docker-tls.yml up -d
}


# Delete cluster
