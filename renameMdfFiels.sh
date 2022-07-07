#!/bin/bash

for d in week1/*/
do
    (cd "$d" && find . -name *.md -exec mv {} ./README.md \;)
done