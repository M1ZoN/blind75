#!/bin/bash

for d in week2/*/
do
    (cd "$d" && find . -name *.md -exec mv {} ./README.md \;)
done