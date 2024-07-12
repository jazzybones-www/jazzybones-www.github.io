#!/bin/sh

set -e

in_file="$1"
out_file="$2"
rule_file="$3"

deps_cmd="$(grep '^\\jb_dependencies:' "$in_file" | perl -pe 's|^.*?:||')"
deps="$(eval "$deps_cmd" | tr '\n' ' ')"

cat > $rule_file << --EOF--
$out_file: $in_file $deps
	./parse-jb.sh < \$< > \$@
	rm $rule_file
--EOF--
