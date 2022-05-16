#!/bin/bash
if [ -n "$1" ];
then
    curl $1 2>&- | grep body | cut -d "\"" -f 2
else
    echo "No parametr found"
fiй