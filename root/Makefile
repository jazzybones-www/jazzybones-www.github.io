md_src=$(shell find -name '*.md')
md_out=$(subst .md,.html,$(md_src))

all: $(md_out)

%.html: %.md head.html tail.html
	./compile-html.sh $< $@
