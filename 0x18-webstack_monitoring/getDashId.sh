#!/bin/bash

api_key='8f1548c9c303dbb09181fa8f9e7a2b09'
app_key='d5cfb05df8b6a91cb549cf7b66b7830e929f8954'

curl -X GET "https://api.datadoghq.com/api/v1/dashboard" -H "Content-Type: application/json" -H "DD-API-KEY: ${api_key}" -H "DD-APPLICATION-KEY: ${app_key}"
