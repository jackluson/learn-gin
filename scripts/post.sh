curl --header "Content-Type: application/x-www-form-urlencoded" \
  --request POST \
  --data 'names[second]=tianou&names[chicago]=akeji"' \
  http://localhost:8088/post


# curl -d '{"ids":{"chicago":123,"boston":245}}' -H "Content-Type: application/x-www-form-urlencoded" -X POST 'http://localhost:8088/post?ids\[a\]=123&ids\[b\]=456&ids\[c\]=789'

