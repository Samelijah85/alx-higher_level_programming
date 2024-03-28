#!/bin/bash
# Displays all HTTP methods accepted by the server for the specified URL
curl -sI "$1" | awk '/^Allow:/ { gsub("Allow: ", ""); print }'
