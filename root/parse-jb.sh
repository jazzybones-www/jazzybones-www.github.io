#!/bin/sh

set -e

while IFS= read -r line ; do
	if printf "%s\n" "$line" | grep -Pq '(^|[^\\])\\\$' ; then
		parts="$(printf "%s\n" "$line" | perl -pe 's|(.*?)\\\$(.*)|\1\n\2|')"
		prefix="$(printf "%s\n" "$parts" | head -n1)"
		cmd="$(printf "%s\n" "$parts" | tail -n1)"
		eval "$cmd" | sed "s/^/$prefix/"
	elif printf "%s\n" "$line" | grep -q '^\\jb_dependencies:' ; then
		continue
	else
		printf "%s\n" "$line"
	fi
done
