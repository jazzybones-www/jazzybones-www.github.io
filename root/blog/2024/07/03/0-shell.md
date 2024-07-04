# the shell is slow

here's a little shell script.

```
#!/bin/sh

while read LINE ; do
	python3 parse_line.py "$LINE"
done < "$1"
```

this script reads a file line by line and runs a python script to process each
one. i'll be using this python script to test this program.

```
#!/usr/bin/env python3

import sys

if len(sys.argv) >= 2:
    print(sys.argv[1])
```

this basically turns our shell script into a worse `cat` command. i'll be
testing this script on this text file:

```
there was a boy
a very strange enchanted boy
they say he wandered very far
very far, over land and sea
```

here's what i got

```
$ time ./script.sh nature-boy.txt
there was a boy
a very strange enchanted boy
they say he wandered very far
very far, over land and sea

real	0m0.056s
user	0m0.046s
sys	0m0.010s
$ time cat nature-boy.txt
there was a boy
a very strange enchanted boy
they say he wandered very far
very far, over land and sea

real	0m0.001s
user	0m0.001s
sys	0m0.000s
```

this script is really slow. when i run this script, i can see the individual
lines printing one by one. sure it's unfair to compare a shell script running a
python program to a highly optimized c program, but 15ms just to print out a
line of text is really slow. so where does that processing time go?

to understand what's happening here, we have to understand what the shell is.
every line of a shell script is a command, and every command is a program.
somewhere on my computer, there is an executable file called `python3`; for me
it's at `/usr/bin/python3`. every time i run a python program, my operating
system has to process that entire file and load it into memory. then, the python
interpreter has to do the same thing with my code before running it. this entire
process takes quite a bit of time, and happens before my code even begins to do
anything useful. this is called a cold-start, and can add a lot of latency to
your programs.

the problem with shell scripts is that we have a lot of cold starts. in this one
program, we have to load the entire python interpreter for every line of our
text file. if this program was written entirely in python, we'd load it once and
be done with it.

optimizing for the shell is weird. your runtime is pretty much entirely driven
by these cold starts, so you have to optimize for the number of commands run
first. this means that you have to pack as much logic into each individual
command as possible. that's pretty neat.
