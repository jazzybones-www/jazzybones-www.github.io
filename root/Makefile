jb_src=$(shell find -name '*.jb')
md_src=$(jb_src:.jb=.md) $(shell find -name '*.md')
md_out=$(md_src:.md=.html)
bb_src=$(shell find -name '*.bb')
bb_out=$(bb_src:.bb=)
autodeps=$(jb_src:=.d) $(bb_src:=.d)

all: $(md_out) $(bb_out)

%.md: %.jb parse-jb.sh
	./parse-jb.sh < $< > $@

%.jb.d: %.jb
	./make-build-rule.sh $< $*.md $@

%.bb.d: %.bb
	./make-build-rule.sh $< $* $@

%.html: %.md head.html tail.html ./compile-html.sh
	./compile-html.sh $< $@

include $(autodeps)

.PHONY: all
