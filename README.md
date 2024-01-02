

[![Python application test with Github Actions](https://github.com/yangxu21/ML_summary/actions/workflows/main.yml/badge.svg)](https://github.com/yangxu21/ML_summary/actions/workflows/main.yml)


# ML_summary
K_means


# To call microservice
```bash
curl -X 'POST' \
  'https://laughing-xylophone-4jj9j677x9542j766-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

# Build container

'docker build .'
'docker image ls'

# Run container

'docker run -p 127.0.0.1:8080:8080 d883dbf16b04'

# Invoke POST request

run 'invoke.sh'