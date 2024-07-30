# go's date string format

there are a bunch of ways to display a date. i could write today as
"2024-01-30", "1/30/24", "30/1/24", "january 1, 2024", and so on. each date
format can be described with a date string. in c, and with the unix
[date](https://linux.die.net/man/1/date) command, a date string might look like
"%Y-%m-%d". this basically means "4 digit year-month-date".

in [the go programming language](https://pkg.go.dev/time), date strings look
like this:

> Monday, January 2, 2006, -0700 MST

you literally just write out that one random day, and go will figure out
everything for you.

this is weird to me. like, the format string "2day is: 2006-01-02" would encode
today as "30day is: 2024-07-30". this is super familiar to non programmers,
because it's not programmatic.

this takes so much work to implement properly. you have to be able to
distinguish "2006" from "2 006", which isn't a trivial problem. you also can't
put certain extra data in your date string, so "2day" gets misinterpreted.

there's this spectrum between intuition and programmability, and go is at one of
the very extremes of this spectrum.
