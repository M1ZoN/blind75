#!/bin/bash

cd week2
for x in ./*.py; do
  mkdir "${x%.*}" && mv "$x" "${x%.*}"
done