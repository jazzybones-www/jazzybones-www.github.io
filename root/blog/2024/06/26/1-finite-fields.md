# jb crypto part 2: finite fields

[read part 1 here](/blog/2024/06/23/0-algebra.md)

in the last installment of jb crypto i talked about group theory and explained
the exact mathematical definition of the integers. i also hinted at the fact
that we made a slight assumption during our derivation.

before i explain the assumption, let's go over the derivation again. from the
definition of a ring, we know that we must have 0 and 1. we also must have
addition, so 1+1 must equal something, which we call 2. 1+2 must equal something
else (3), 1+3=4, 1+4=5, and so on all the way to infinity. every number must
have a negative counterpart, so that gets us the negative numbers.

the assumption here is that adding 1 always gets us a new number. if we wanted
to, we could just declare that 5+1=0. this is called "modulo 6 arithmetic", or
"mod 6 arithmetic", since 0=5=1=6. this would also imply that 1=7, 2=8, and so
on. to convert a real number to a mod 6 number, we just divide that number by 6
and take the remainder. for example, 8/6 = 1R2, so 8=2. to do modulo arithmetic,
we can just do regular arithmetic and apply this conversion to our
result[^mod-equiv-proof].

modulo arithmetic has some interesting implications. in a ring, every value must
have an additive inverse, but there are no negative numbers in modulo
arithmetic. in the regular integers, 1+(-1) = 0, but we don't have -1. instead,
we divide -1/6 to get -1R5, which shows that -1=5 and 1+5=0[^no-idea-readable].

mod 6 arithmetic does form a valid ring, but it doesn't form a valid field. in
mod 6 arithmetic, 2 has no multiplicative inverse. 2\*0=0, 2\*1=2, 2\*2=4,
2\*3=0, 2\*4=2, and 2\*5=4. the problem comes from the fact that 2 is a factor
of 6, and can therefore "dodge" the number 1 with repeated addition. every
composite number has a factor which can dodge the number 1, so modulo arithmetic
with a composite number must always create at least one element without a
multiplicative inverse. therefore, modulo arithmetic over a composite number
will never form a valid field. prime numbers, which have no factors other than 1
and themselves, however, will always work[^prime-field-proof].

it is possible to have some finite fields with a composite number of elements,
but i'll leave that for some other day because i'm a sleeppilled restmaxxer who
wants to hit the hay and doze off.

[^mod-equiv-proof]: a ring is a set with two operations: addition and
    multiplication. let's start with addition.

    recall from jb crypto part 1 that 5+4 is equivalent to
    (1+1+1+1+1)+(1+1+1+1), which is equivalent to 1+1+1+1+1+1+1+1. our
    definition of mod 6 arithmetic states that 5+1=0, so this calculation "wraps
    around" so to speak from 5 back to 0 whenever we hit a 6. this also means
    that groups of 6 1s in a row cancel each other out, which is equivalent to
    subtracting 6. this means that addition under modulo arithmetic is
    equivalent to integer addition where we subtract 6 over and over again until
    we get a valid number. repeated subtraction is just division, so this
    conversion factor works with addition.

    the proof from jb crypto part 1 that multiplication is equivalent to
    repeated addition also works here, and since the conversion factor works
    with addition, it must also work with multiplication.

[^no-idea-readable]: i have no idea if any of this is readable, i'm super tired
    as i'm writing this

[^prime-field-proof]: this is most obvious with an example, let's say mod 7
    arithmetic. in mod 7 arithmetic, there are 7 numbers. let's find the
    multiples of some other number, say 3, under mod 7 arithmetic. we start with
    0. 0+3=3.  3+3=6. 6+3=2.  2+3=5.  5+3=1. 1+3=4. 4+3=0.  note that every time
    we add 3, we jump from one number to another. also note that this cycle will
    definitely get back to 0 after at most 7 iterations, since 3\*7 = 3\*7 =
    7+7+7 = 0+0+0 = 0.  also note that for every number, there is exactly one
    number that leads to it. for example, since 5+3=1, there is no other number
    where x+3=1. in other words, 1-3=5, and only 5.

    this basically shows that this cycle will start and end at 0. it won't get
    caught in an infinite loop somewhere, and we won't see the same number
    twice, unless we've gone back to 0 and are repeating the loop again.

    the length of this cycle is the smallest number x, such that 3*x is a
    multiple of 7. in other words, it's LCM(3, 7)/3. by definition, LCM(x, y) is
    the smallest number with both x and y as a factor. LCM(x, y) can be
    calculated with the formula x\*y/GCF(x, y). i really don't know a decent
    proof of this expression that uses only the concepts that i've introduced so
    far and which is rigorous enough for the standards of this series, so i'll
    leave that as an exercise for the reader.

    anyways, we want to show that for all primes p and all integers n where
    0<n<p, LCM(n, p)/n=p. this means that LCM(n, p)=n\*p, n\*p/GCF(n, p)=n\*p,
    and GCF(n, p)=1. 

    again, i don't know a rigorous way to prove that this statement holds true
    for all primes and doesn't hold true for all composites without introducing
    prime factorization. don't get me wrong, i would 100% write out a proof of
    that, but i'd have to put it in a footnote, and pandoc doesn't like nested
    footnotes. maybe i'll write a follow up article later showing that these two
    statements are true. anyways, this is an exercise for the reader as well.
