#!/bin/sh

git log --pretty=oneline status.txt | awk '{print $1;}' | while read commit ; do
	git checkout "$commit" ./status.txt > /dev/null 2>&1
	printf "%s: " "$(git show -s --format=%ad --date iso8601 "$commit")"
	cat status.txt
	echo
done

git checkout HEAD ./status.txt > /dev/null 2>&1
