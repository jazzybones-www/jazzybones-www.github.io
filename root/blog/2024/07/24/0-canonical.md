# the jazzybones word: canonical

## cw: mentions of scientific racism

if some representation of a thing is "canonical", that means that that
representation is the most obvious, natural one. for example, if i have five
students, say, Alice, Bob, Carol, Dave, and Eve, and i want to assign each one a
student id from 1-5, the canonical solution would just be to assign them
alphabetically; so Alice gets 1, Bob gets 2, Carol gets 3, and so on. there are
120 different ways to do this, but most people solving this problem would
naturally converge to that one solution.

this specific article was inspired by the idea of "percent grade". the steepness
of a hill can be measured as a percentage, where higher percentages are steeper.

for the longest time i thought that percent grade was a canonical problem. the
flattest possible slope, a 0 degree plane, should obviously have a 0% grade.
similarly, the steepest possible slope, a 90 degree wall, should obviously have
a 100% grade. then, everything else can be assigned linearly, so 45 degrees
would be a 50% grade, 30 degrees would be a 33.3% grade, and so on. more
rigorously,

> percent\_grade(theta) = theta / 90 degrees \* 100

then i thought about it a bit more. percent grade might be useful as a tool to
calculate elevation changes. like, if i measure out 100 feet with a [surveyor's
wheel](https://en.wikipedia.org/wiki/Surveyor%27s_wheel) and gain 10 feet of
elevation, then i could reasonably call that a 10% grade, even if the actual
angle isn't exactly 10% of 90 degrees. more rigorously,

> percent\_grade(theta) = sin(theta) \* 100

upon this realization, i looked it up. it turns out that the real formula is

> percent\_grade(theta) = tan(theta) \* 100

the idea is that if i walk 100 feet on a gps at a 10% grade, i'll gain 10 feet
of elevation. if i take my surveyor's wheel with me, i'll actually measure
around 100.499 feet, but since i'm not going perfectly horizontally, i'll only
move 100 feet on a map.

this implies that a 100% grade is actually a 45 degree angle, because every time
you move horizontally, you also have to climb up the same distance. this also
implies that a 90 degree angle is actually an infinity% grade, since you will
never be able to move horizontally by climbing directly up a wall.

all three of these solutions are equally natural, which means that none of them
are canonical. the real definition is almost certainly the most useful for real
surveying work, but the second definition might be useful to runners who want to
know their change in elevation for some running distance, and the first is just
mathematically satisfying[^no-real-world].

[^no-real-world]: this is code for "i can't think of a real world case where
these definition is the most useful".

i'm always surprised by how much room for interpretation there is, even in
"cold, logical" fields like math and topography. the specific way that you
represent a problem, and even the problems that you focus on in the first place,
are highly influenced by so many things outside of the page. everything and
everyone, including mathematicians, exist in the context of all in which we live
that what has come before.

this room for interpretation only grows as we add layers of abstraction and
sources of error. "science" isn't some blob of information that's never wrong
and magically grows over time, it's a laborious, slow, divided process. millions
of scientists create hypotheses, run studies, and debate each other over the
validity over these studies and the proper way to interpret their results for
decades and centuries until they slowly come to a consensus. science has been
wrong before, in [truly awful
ways](https://en.wikipedia.org/wiki/Scientific_racism), even up to WWII.
scientific literacy is really about understanding this process, and knowing when
some claim can be justified from the studies it's based on.
