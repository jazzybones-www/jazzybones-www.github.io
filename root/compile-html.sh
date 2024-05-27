#!/bin/bash

if [ $# -lt 2 ] ; then
	echo "usage: $0 [in.md] [out.html]"
	exit 1
fi

cat head.html <(cmark -t html "$1") tail.html > "$2"
