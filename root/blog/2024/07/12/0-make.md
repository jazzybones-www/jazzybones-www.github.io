# make is magic

i have mixed feelings about shell scripts. on the one hand, they're really,
really powerful. on the other hand, they're really, really slow.

this website is generated pretty much entirely by shell scripts. there's some
python for when i need performance (brand new sentence) like with the room tour,
but the html boilerplate is all added by shell scripts.

there are generally three types of files on this website.

1. static content like images which don't have to be processed at all
1. markdown documents
1. more complex things like the index page of the blog, which is automatically
   generated with a shell script.

since i'm using github pages to host this site, i really don't have to worry
about static content. it sort of _just works_<sup>TM</sup>.

markdown documents are also pretty easy, i just use pandoc to compile to html
and add some html boilerplate using this shell script

```
#!/bin/bash

set -e

if [ $# -lt 2 ] ; then
	echo "usage: $0 [in.md] [out.html]"
	exit 1
fi

TITLE="$(grep '^#' "$1" | head -n1 | sed 's/^# *//')"
cat head.html <(pandoc "$1") tail.html | sed "s/<?title?>/$TITLE/g" > "$2"
```

for the other stuff i created a custom file format called jbfiles. the goal was
basically to have shell scripts embedded in markdown. for example, the index
page of my blog as of now looks like this:

```
# the jazzybones blog

[rss feed](rss.xml)

\$ find blog -mindepth 2 -name '*.md' -or -name '*.jb' | sort -r | ./add-links.sh sed -e 's/blog\///' -e 's/\//-/' -e 's/\//-/' -e 's/\/.*//'
\jb_dependencies: find blog -mindepth 2 -name '*.md'
```

ignore that last line, we'll get to it in a bit.

this is basically markdown, any lines beginning with `\$` get interpreted as
shell scripts, but that's really it. i've made it smart enough to handle some
more complicated markdown stuff, so for example i could put the list of blog
posts in a block quote like this:

```
# the jazzybones blog

[rss feed](rss.xml)

> \$ find blog -mindepth 2 -name '*.md' -or -name '*.jb' | sort -r | ./add-links.sh sed -e 's/blog\///' -e 's/\//-/' -e 's/\//-/' -e 's/\/.*//'
\jb_dependencies: $(shell find blog -mindepth 2 -name '*.md')
```

i feel like the way i'm describing this makes it sound a lot more complicated
than it really is, the script that parses these files is only 16 lines long.

```
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
```

this is a big part of why i love the shell so much, literally every program ever
written for unix is an atomic building block of the shell, and the filesystem is
just baked into the language. like, if we want to run a shell script and get the
result, we can just do that. we don't have to `import os` or process a stream
for the program output, it all just works.

throughout this website there's this idea of using shell scripts to translate
between file formats. i translate between markdown and html, jbfile and
markdown, and so on. this is a perfect use case for a makefile.

i can compile every markdown file to html with just this makefile:

```
md_src=$(shell find -name '*.md')
html_src=$(md_src:.md=.html)

all: $(html_src)

%.html: %.md
	./compile-html.sh $< $@

.PHONY: all # this line isn't technically needed
```

make takes this idea of shell scripts translating filesinto other files and runs
with it. this is just a clean design, if `compile.sh` compiles `file.a` into
`file.b`, i can write this rule to make that happen:

```
file.b: file.a
	./compile.sh
```

then, make will automatically figure out all of your dependencies and avoid
recompiling things when it's not necessary. it does all of this on the fly using
the last modified date of the filesystem as a database. make knows exactly what
it is and what it isn't. it's up to the programmer to figure out how to compile
everything as well as the dependencies of each file, and it's up make to take
that information and compile everything.

this article was inspired by some changes i made to the jazzybones makefile
earlier today.

```
jb_src=$(shell find -name '*.jb')
md_src=$(jb_src:.jb=.md) $(shell find -name '*.md')
md_out=$(md_src:.md=.html)
bb_src=$(shell find -name '*.bb')
bb_out=$(bb_src:.bb=)
autodeps=$(jb_src:=.d) $(bb_src:=.d)

all: $(md_out) $(bb_out)

%.jb.d: %.jb ./make-build-rule.sh
	./make-build-rule.sh $< $*.md $@

%.bb.d: %.bb ./make-build-rule.sh
	./make-build-rule.sh $< $* $@

%.html: %.md head.html tail.html ./compile-html.sh
	./compile-html.sh $< $@

include $(autodeps)

.PHONY: all
```

that `include $(autodeps)` line is where the real magic happens. if we have a
`blog/index.jb` file, then we include `blog/index.jb.d`. as it turns out,
`blog/index.jb.d` doesn't actually exist, so we create it from `blog/index.jb`
using the second rule. then, `blog/index.jb.d` contains a new rule to convert
`blog/index.jb` into `blog/index.md`. `blog/index.md` is then used by the fourth
rule to generate `blog/index.html`.

make just handles all of that. it generates its own rules, discovers the
`blog/index.jb` to `blog/index.md` to `blog/index.html` pipeline, and compiles
everything on its own. the algorithms that it uses to do this aren't that
complicated, but somehow they come together to make this really powerful tool.

coming back to the `\jb_dependencies` thing, this is where that's used. i can
dynamically generate my dependencies within each file so that all of the stuff
about a given resource is in a single place.

make is so cool.
