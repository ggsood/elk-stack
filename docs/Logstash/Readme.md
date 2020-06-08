## Configuring Logstash on an ELK Stack

Pre Requisites
---
- Admin access to ELK Stack
- Logstash installed [refer to helm charts for chart]
- X-Pack enabled

Current Configuration in Ops
---
User - logstash-ingest
Roles - Superadmin

Steps followed
---
Create the following roles to be used by logstash user - logstash-ingest

1. logstash_writer, logstash_reader
```
POST _xpack/security/role/logstash_writer
{
  "cluster": ["manage_index_templates", "monitor"],
  "indices": [
    {
      "names": [ "*" ], 
      "privileges": ["write","delete","create_index"]
    }
  ]
}

POST _xpack/security/role/logstash_reader
{
  "indices": [
    {
      "names": [ "*" ], 
      "privileges": ["read","view_index_metadata"]
    }
  ]
}
```