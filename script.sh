#!/bin/bash

cd week1
for x in ./*.py; do
  mkdir "${x%.*}" && mv "$x" "${x%.*}"
done