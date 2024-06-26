# math as art

there's this famous program called the [EICAR antivirus test
file](https://en.wikipedia.org/wiki/EICAR_test_file). here it is:

    X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

if you save this as a [.com file](https://en.wikipedia.org/wiki/COM_file) and
run it on MS-DOS, it will print the string "EICAR-STANDARD-ANTIVIRUS-TEST-FILE!"
and exit. many antiviruses will treat this program as a virus and automatically
remove it from your system, which allows people to make sure that their
antivirus is working.

this program is written directly in machine code. if you hooked up a machine to
your CPU to find the exact bytes that were flowing through the pins as you ran
this program, you would see this exact string[^self-modify]. it's also written
using only printable, typeable characters, so if you were stuck on a desert
island with nothing but an ancient IBM PC and a text editor, you could write and
run this program.

[^self-modify]: technically, the program modifies its own code, so you wouldn't
see this exact string, but the idea is still the same.

it's hard to explain how impressive this is. there are 256 possible 8 bit bytes,
but only 95 are actually printable. that means that you can only use 37.1% of
the possible bytes in your program. to put it another way, you _can't_ use 62.9%
of the possible bytes in your program. imagine going to a construction site and
stealing 62.9% of the tools that they use on a daily basis; productivity would
either grind to a halt or slowly dredge along with some hacked together
amalgamation of a toolbox.

the authors of this program basically stole 62.9% of their _own_ tools and still
made something kind of functional.

is this program art? it doesn't feel like art, it was made by a bunch of
engineers working purely analytically to create a program for usage in the real
world. it wasn't exhibited at an art gallery, the people who created it probably
wouldn't consider themselves artists, and the people who appreciate its
creativity probably wouldn't consider themselves art enthusiasts. at the same
time, though, this program is brilliant. it takes two wildly different ideas in
computing (plain text and machine code) and somehow merges them into a single
thing. it feels like this program shouldn't exist, yet it does. it makes you
rethink the limits of data itself. if this program isn't art, i really don't
know what is.

here's an even stranger example. math is made up of a bunch of base components
which come together in interesting ways to make new and interesting stuff.
numbers are not one of these base components.

i wrote a bit about this in [jb crypto part 1](/blog/2024/06/23/0-algebra.html),
but numbers and arithmetic can be broken down into the smaller concepts of a
"set" and many different "group operations". numbers are not the only sets, and
arithmetic are not the only group operations. we can create new sets with new
group operations to find brand new math. [maybe there are only 7 numbers, and
6+1=0](https://en.wikipedia.org/wiki/Finite_field). maybe instead of numbers, we
have [points on an elliptic
curve](https://en.wikipedia.org/wiki/Elliptic_curve#The_group_law). maybe
instead of numbers, we have [rotations and reflections of a regular
polygon](https://en.wikipedia.org/wiki/Dihedral_group), and ABC+BCA != BCA+ABC.

similar to the EICAR test program and to so much other art, group theory makes
me rethink everything i thought i knew about math. group theory isn't some
product of human creativity, though; it existed in the universe before we
discovered it.

art is an expression of human creativity, which is inherently chaotic and
doesn't follow any rules. math feels like it should go completely against that,
but somehow i and many others find artistic beauty in an elegant proof or
interesting way to think about a problem. a good proof is like a magic trick; it
has some ground rules, follows those rules exactly, then shows you something
that feels impossible. if god exists and they created math, then they're they're
the most brilliant artist i've ever witnessed.
