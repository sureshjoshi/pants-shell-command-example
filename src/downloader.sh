#! /bin/sh

url=$(head -n 1 manifest.txt)
curl -O "$url"
