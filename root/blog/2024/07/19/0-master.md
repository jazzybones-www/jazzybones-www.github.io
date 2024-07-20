# the jazzybones word: master

## cw: mentions of slavery

from [man 7 pty](https://www.man7.org/linux/man-pages/man7/pty.7.html):

> A pseudoterminal (sometimes abbreviated "pty") is a pair of virtual character
> devices that provide a bidirectional communication channel.  One end of the
> channel is called the **master**; the other end is called the **slave**.

the use of the term "master" in code is a controversial topic. the most
prominent example is probably with [github changing the default branch name from
master to main](https://github.com/github/renaming). on the one hand, using the
word "slave" to describe something like a terminal in 2024 just feels icky. on
the other hand, changing all of our existing systems and documentation would
take a lot of effort for a bunch of "sjw liberal propaganda".

in the case of git, this whole debate is kind of stupid. there are no "slave"
branches in git, the term "master" is used in the same sense as the word "master
copy", as in the original copy from which other copies are derived. the master
copy of an album, for example, would be the original tape from which the vinyl
disk is pressed. it's not like there's any pressure for educational institutions
to rename their "master's degrees".

sometimes there are technical reasons to avoid the word master. [rfc
1035](https://datatracker.ietf.org/doc/html/rfc1035) defines various technical
aspects of the dns, including (on page 33), "master" files. this term sucks for
two reasons. first, master files can also be used to store caches, which are
definitively not master copies of data. second, "master file" could refer to a
bunch of different file formats in a bunch of different areas of computing, so
to disambiguate all of these you'd have to say specifically "dns master file".

for these reasons, people usually call them "zone files". "dns master file" is
then specifically refers to the master data that a server is reading from, as
opposed to a dns cache file, although people often just say "zone files" to all
of these things[^cloudflare].

[^cloudflare]: at least [cloudflare
does](https://www.cloudflare.com/learning/dns/dns-records/), and they have some
pretty smart network engineers.

the most egregious case i've ever come across is the pseudoterminal example from
the beginning of this article. master/slave terminology in this case is
atrocious. first of all, this isn't a case where "master copy" is confused with
"master/slave", this is explicitly about slavery, it's right there in the manual
and all of the code examples.

secondly, this isn't even a good term. master/slave terminals form a
_bidirectional_ communication channel, the difference between them is that the
master end faces the user, and the slave end faces the program. the "user end"
and "program end" would have been much better names from a purely technical
standpoint, regardless of any political connotations. the master terminal does
have some special controls over the slave terminal, but not many. the master
terminal can stop the program running on a slave terminal through an interrupt,
just like how a user can stop a program.

somehow, everybody in this debate is stupid. yes, words have a lot of power, and
we should try to get rid of references to slavery wherever possible, but the
uses of the word "master" that people get mad about are usually not in reference
to slavery. at the same time, people who use the word "master" with an explicit
reference to slavery almost always have some better word that they could be
using instead. like, somehow the socially aware people are getting language
wrong while the technically minded people are getting technical stuff wrong.

there's a reasonable middle ground where "master copies" are fine,
"master/slave" relationships are dumb for purely technical reasons, all mentions
of slavery are removed, and everybody is happy. let's just do that.
