aws dynamodb put-item \
  --table-name customers \
  --item '{
    "id": {"N": "27"},
    "authid": {"S": "6543"},
    "firstname": {"Prim": "Rose"}
    "lastname": {"S": "Doe"}
  }'
