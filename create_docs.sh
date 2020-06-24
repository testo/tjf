#!/usr/bin/env bash
if [ ! -f "openapi-generator-cli.jar" ]; then
wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/4.3.1/openapi-generator-cli-4.3.1.jar -O openapi-generator-cli.jar
fi
java -jar openapi-generator-cli.jar generate \
  -i api/testoApi.yaml \
  -g html \
  -o docs/
