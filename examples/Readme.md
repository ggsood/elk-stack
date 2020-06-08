Command to start filebeat

```
filebeat -c `pwd`/filebeat.yaml -e
```

metricbeat setup -e \
  -E output.logstash.enabled=false \
  -E output.elasticsearch.hosts=['https://localhost:9200'] \
  -E output.elasticsearch.username=elastic \
  -E output.elasticsearch.password=RMa8k7nwIzBZZai3jRay \
  -E output.elasticsearch.ssl.verification_mode="none" \
  -E setup.kibana.host=https://localhost:5601 \
  -E setup.kibana.ssl.verification_mode="none"

