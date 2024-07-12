#!/bin/bash

set -e

if [ $# -lt 2 ] ; then
	echo "usage: $0 [in.md] [out.html]"
	exit 1
fi

TITLE="$(grep '^#' "$1" | head -n1 | sed 's/^# *//')"
cat head.html <(pandoc "$1") tail.html | sed "s/<?title?>/$TITLE/g" > "$2"
