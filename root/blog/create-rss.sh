#!/bin/sh

set -e

olddir="$(pwd)"
cd "$(dirname "$0")"

printmonths() {
	echo "Jan"
	echo "Feb"
	echo "Mar"
	echo "Apr"
	echo "May"
	echo "Jun"
	echo "Jul"
	echo "Aug"
	echo "Sep"
	echo "Oct"
	echo "Nov"
	echo "Dec"
}

find -name '*.md' | sort -r | head -n 50 | while IFS= read -r md ; do
	title="$(grep '^# ' "$md" | head -n1 | sed 's/^# *//')"
	link="$(printf "%s\n" "$md" | sed 's/md$/html/' | sed 's/^\./https:\/\/jazzybones-www.github.io\/blog/')"
	guid="$link"
	pubDate="$(git log --follow --format=%ad --date rfc $md | tail -n1)"
	echo "<item>"
	echo "<title>$title</title>"
	echo "<link>$link</link>"
	echo "<guid>$guid</guid>"
	echo "<pubDate>$pubDate</pubDate>"
	echo "</item>"
done

echo "$html_docs"

cd "$olddir"
