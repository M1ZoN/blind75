#!/bin/bash

cd $1
for x in ./*.py; do
  mkdir "${x%.*}" && mv "$x" "${x%.*}"
done