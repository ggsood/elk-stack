## Loading Dummy Data


Dummy data can be fetched from the below locations

1. Accounts - 
   https://raw.githubusercontent.com/linuxacademy/content-elastic-certification/master/sample_data/accounts.json
2. Logs - https://raw.githubusercontent.com/linuxacademy/content-elastic-certification/master/sample_data/logs.json
3. shakespeare - https://raw.githubusercontent.com/linuxacademy/content-elastic-certification/master/sample_data/shakespeare.json


Sample commands to load the data, using curl
```
curl -k -u elastic:RMa8k7nwIzBZZai3jRay https://localhost:9200/accounts/_bulk\?pretty -H "Content-Type: application/x-ndjson" --data-binary @accounts.json >files.log

curl -k -u elastic:RMa8k7nwIzBZZai3jRay https://localhost:9200/logs/_bulk\?pretty -H "Content-Type: application/x-ndjson" --data-binary @logs.json  >files.log

curl -k -u elastic:RMa8k7nwIzBZZai3jRay https://localhost:9200/shakespeare/_bulk\?pretty -H "Content-Type: application/x-ndjson" --data-binary @shakespeare.json >files.log

```

for f in xa*
do
curl -k -u elastic:RMa8k7nwIzBZZai3jRay https://localhost:9200/logs/_bulk\?pretty -H "Content-Type: application/x-ndjson" --data-binary @$f
done

splitting a file `split -10000 shakespeare.json shake`