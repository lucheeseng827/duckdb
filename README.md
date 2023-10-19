# DuckDB

Duckdb lab and playground

## Dockerfile lint with hadolint/hadolint-docker

```bash
# this runs hadolint on the Dockerfile
hadolint Dockerfile --ignore DL3013 --ignore DL3018

# this runs the docker image and pipes the Dockerfile to hadolint
docker run --rm -i hadolint/hadolint < Dockerfile
```
