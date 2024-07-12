#!/bin/sh

set -e

while IFS= read -r file ; do
	info="$(printf "%s\n" "$file" | "${@}")"
	title="$(head -n1 "$file" | sed 's/^# *//')"
	uri="$(printf "/%s\n" "$file" | sed 's/\(.*\)\..*/\1.html/')"
	printf "[%s](%s) - %s\n" "$title" "$uri" "$info"
	echo
done
