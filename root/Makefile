jb_src=$(shell find -name '*.jb')
md_src=$(subst .jb,.md,$(jb_src)) $(shell find -name '*.md')
md_out=$(subst .md,.html,$(md_src))

all: $(md_out)

%.md: %.jb parse-jb.sh
	./parse-jb.sh < $< > $@

%.html: %.md head.html tail.html ./compile-html.sh
	./compile-html.sh $< $@
