jb_src=$(shell find -name '*.jb')
jb_out=$(jb_src:.jb=.md)
md_src=$(jb_out) $(shell find -name '*.md')
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
.INTERMEDIATE: $(jb_out)
