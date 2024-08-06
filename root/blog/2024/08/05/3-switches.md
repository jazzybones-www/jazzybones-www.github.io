# multiway switches

if you have a really long hallway or staircase, it's often nice to have a light
switch at both ends. that way, you can turn on the lights at one end, walk
across the hall, and turn off the lights at the other end. this is called
[multiway switching](https://en.wikipedia.org/wiki/Multiway_switching).

in a multiway switch, two or more switches control the same output. if the
output is off, then turning any switch will turn it on, and if it's on, turning
any switch will turn it off.

if we have two switches controlling the same output (a case which is confusingly
called a three way switch in the united states), we might set it up so that if
every switch is off, then the light is off.

    switch 1 | switch 2 | light
    off      | off      | off

based on the rule that makes these switches work, turning a single switch on
should turn the light on.

    switch 1 | switch 2 | light
    off      | off      | off
    on       | off      | on
    off      | on       | on

now, if we turn both switches on, the light should actually turn _off_.

    switch 1 | switch 2 | light
    off      | off      | off
    on       | off      | on
    off      | on       | on
    on       | on       | off

it's kind of annoying that "all switches off" and "all switches on" don't
necessarily mean "lights off" or "lights on", but i guess that's just the cost
of using three way switches.

it's also really convenient that we could just create this simple mapping. could
you imagine if there was some sequence of switchings that made it so that "all
switches off" suddenly meant "lights on"? like, if you could just flip switch 1,
then switch 2, then 1 again, then 2 again, and suddenly the light was on even
though all the switches were off. that would make the wiring so much more
difficult. thankfully, we can just wire up this table and the switches will just
work.

but what if it doesn't work at some point? sure we can create a table for two
switches, but what about three? or four? with each new switch there are
infinitely more possible sequences of flips, how can we be absolutely sure that
we can always just wire up a table like this?

we can first notice that every time we flip a switch, the total number of "on"
switches either goes up by one, or down by one. if there are five switches and
two are on, either i flip a switch that's already on, or i flip a switch that's
already off. if i flip a switch that's already off, then the number of on
switches goes up by one, and if i flip a switch that's already on, then the
number of on switches goes down by one.

next, notice that every time we add or subtract 1 to a number, its parity
changes. any even number plus or minus 1 is an odd number, and any odd number
plus or minus one is an even number.

so here's an alternative definition for a multiway switch: count the number of
on switches. if that number is even, then the output should be off. if it's odd,
then the output should be even.

this is equivalent to the first definition, and it shows that there's a
consistent mapping from switch states to output states, which makes the wiring a
lot more easier.

this new definition is also equivalent to
[xor](https://en.wikipedia.org/wiki/Exclusive_or), which is also equivalent to
both addition and subtraction under finite fields of order 2\^n, but i'm getting
off topic.

multiway switches call into question our idea of what a switch even is. to me,
if a switch is up, then the light is on, and if it's down, then the light is off
(some countries do things the other way around, but the idea is that it's at
least consistent). with a multiway switch though, even though a switch is "on",
the output that it controls could be off. the mapping isn't from one switch to
one output, it's from every switch to one output. in this model, the action of
flipping a switch at all is more important than the actual position of the
switch.

from a user experience perspective, it might be better to have buttons instead
of switches. since buttons don't store state like switches do, they take away
focus from the position of the switch and put it towards the action of pressing
a button.

unfortunately, wiring buttons like switches is complicated and expensive. we
might instead have two buttons at each important point, one to turn the lights
on and another to turn them off, but that would still be a lot more expensive
than just some clever wiring.

speaking of which, multiway switches have some really clever wiring. i'm not
going to get into it, because i'm not an electrical engineer, but you should
really [read about it on
wikipedia](https://en.wikipedia.org/wiki/Multiway_switching#Two_locations).
