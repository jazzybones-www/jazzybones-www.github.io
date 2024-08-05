# the dbound working group

let's play a game. i'm going to name pairs of domains, and you have to figure
out if they are owned by the same person/company, or different people/companies.

## level 1

> facebook.com, google.com

pretty easy. facebook and google are two separate companies with different
websites.

> google.com, www.google.com

also easy, both domains are clearly owned by google.

## level 2

> google.co.uk, bbc.co.uk

at first glance it might look like both domains are "owned" by .co.uk, but
they're really owned by two different people.

## level 3

> google.com, google.co.uk

even though both domains have completely different suffixes, they're both owned
by google.

## level 4

> jazzybones-www.github.io, bitburner-official.github.io

this is really weird because both domains are _hosted_ by github, but their
contents are _controlled_ by different people, so it really depends on what
exactly you're talking about.

## what now?

this turns out to be a really important but difficult question for computers to
solve. you can't just count the dots in the website because there are secondary
domain names that are used as suffixes for a lot of domains. you can't just
create a list of top level domains operated by registrars and use that, because
anybody can create their own "effective tld".

i can't find a specific date, but it seems like around 2007 mozilla created the
[public suffix list](https://publicsuffix.org/) to address at least some of
these problems. basically, it's a big list of suffixes, including ones created
by private actors. github.io is on that list, as is co.uk.

the list is biased towards distinguishing domains, so you'll never recognize
that google.com and google.co.uk are owned by the same person with just the list
(although you will be able to recognize that google.com and www.google.com are).

this is a decent solution, but it's not great that this backbone of internet
security is run by a few random unpaid volunteers. it'd be nice if we could have
some distributed system that was secure and which handled all of these weird
case.

thus, the [dbound working group](https://datatracker.ietf.org/wg/dbound/about/)
was formed. a bunch of nerds just meeting up in bars around the world trying to
figure out how to solve this damn problem.

> seriously though, so many of the messages on their mailing list were just
> planning which bar to have a meeting in. i guess this is just how internet
> standards get made.

they very quickly realized that this problem was a lot harder than expected. a
few people submitted proposals, some documents were made clarifying the exact
problem they were trying to solve, and...

nothing came of it. there were like three proposals and the five people active
in the mailing list couldn't agree on which one to go with, so in 2017 they
basically agreed that the public suffixes list was fine and disbanded the group.
now we have no distributed system for determining dns boundaries. everything is
done by a few random volunteers.

that's not great. like, they couldn't just pick a proposal and go with it, so
now we're stuck with a worse outcome for everybody. i personally would have gone
with [John Levine's
proposal](https://datatracker.ietf.org/doc/html/draft-deccio-dbound-organizational-domain-policy-03),
because it feels like a distributed public suffix list and doesn't try to do
anything too fancy, but i wasn't part of this mailing list.

the weird thing is that everybody had a common goal, they all wanted some
distributed way to distinguish domain names, but they couldn't agree on the
little details, so the larger goal remained unachieved. it'd be really nice if
we could all just agree on the things that we agree on and not bicker over the
details, but that's really never happening.
