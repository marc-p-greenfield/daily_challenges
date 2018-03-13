#!/usr/bin/env bash

curl https://truveris.github.io/jobs/ > a.html
echo marc.p.greenfield@gmail.com > b.txt
cat a.html b.txt | openssl sha256
