#!/bin/sh

git log --pretty=oneline status.txt | awk '{print $1;}' | while read commit ; do
	git revert "$commit" status.txt
	cat status.txt
	echo
done

git revert HEAD status.txt
