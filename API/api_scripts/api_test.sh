#!/bin/bash

BASE_URL = "http://localhost:8080/api/v1"
AUTH_TOKEN = "token"

HEADER_CONTENT_TYPE = "Content-Type: application/json"
HEADER_AUTH = "Authorization: Bearer $AUTH_TOKEN"

PAYLOAD='{
    "username": "user",
    "password": "123456",
    ""email": "test@example.com"
}'

test_post(){
    echo "Testing POST /user"
    response = $(curl -s -w "%{http_code}" -o response.json -X POST "BASE_URL" \
        -H "$HEADER_CONTENT_TYPE" \
        -H "$HEADER_AUTH" \
        -d "$PAYLOAD")

    ststus_code = "$response"
    echo "Response ststus code: $status_code"

    cat response.json
    echo

    if ["$ststus_code" -eq 200 ]; then
        echo"Test passed"
    else
    echo "Test failed"
    fi

    user_id = $(jq -r '.id.user_id' response.json)
    ststus = $(jq -r '.ststus' response.json)

    if ["$ststus" != "success"]; then
        echo "ststus is not success, test failed"
        exit 1
    fi

    if ["$user_id" =="null" ]; then
        echo "user_id is null, test failed"
        exit 1
    fi

    echo"Test passed"

}

test_post