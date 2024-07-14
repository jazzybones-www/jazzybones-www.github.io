# discord requires cups

i used to use gentoo gnu/linux. it was great, i could choose exactly which
programs i wanted on my system and throw away everything else. if i didn't want
bluetooth, i didn't have to install it. inversely, this also meant that if i did
want something like printer drivers, i'd have to manually compile and install it
myself, which could take anywhere from 30 seconds to several hours.

that last part became really annoying when i tried to install discord. the
discord app uses the [electron desktop
framework](<https://en.wikipedia.org/wiki/Electron_(software_framework)>), which
then uses chromium as a backend, which then has a hard dependency on cups, or
the common unix printing system. this means that if you want to install discord
on a unix-based operating system, you have to install printer drivers.

these sorts of chained dependencies create problems all of the time. on march
14, 2014[^git-date], software developer Azer Ko&ccedil;ulu wrote the `left-pad`
npm module. it was just 17 lines of code:

[^git-date]: that's the date of the first commit from
[https://github.com/left-pad/left-pad](https://github.com/left-pad/left-pad)

    module.exports = leftpad;

    function leftpad(str, len, ch) {
      str = String(str);

      var i = -1;

      ch || (ch = ' ');
      len = len - str.length;


      while (++i < len) {
        str = ch + str;
      }

      return str;
    }

this code isn't actually that great, it's doing this weird precalculation in a
loop that could be made more efficient and clean, but i digress. over the years
`left-pad` turned out to be a mildly useful package to some programmers. these
programmers wrote other useful code on top of that, and other programmers still
built further up this tower. eventually, left-pad became a dependency of
thousands of projects and got downloaded over 15 million times.

in addition `left-pad`, Ko&ccedil;ulu had another project called "kik". this
became a problem when [the messaging app of the same
name](https://en.wikipedia.org/wiki/Kik_Messenger) wanted to create an npm
project called "kik". kik the messenger began by kindly asking Ko&ccedil;ulu to
take down the kik npm package. when he refused, they asked npm directly to
remove the kik package. since kik the messenger was a registered trademark
across several countries, npm sided with them and removed the kik package. in
response, Ko&ccedil;ulu deleted all of his packages from npm, including
`left-pad`.

suddenly, many high profile npm packages were broken because they needed a thing
that needed a thing that needed a thing that needed `left-pad`. 24 hours later,
npm forcefully brought back `left-pad` and prevented users from deleting
packages if another one already depended on it.

this seemed like a great policy, until someone made an npm package that depended
on [everything](https://www.npmjs.com/package/everything). for a while, nobody
could delete any npm package.

this just shows that you really have to know what software you're using, either
directly or indirectly, because it all affects you and your users.
