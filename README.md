# chef-beta

## Mock server using prism
start mock server on docker compose

```sh
docker compose up -d prism
```

check mock server
```sh
curl http://localhost:4010/hello
{"message":"hello"}
```
