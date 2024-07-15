# wish.com twitter

i have [a status page](/status.html) now! the system that makes it work is kind
of goofy.

it begins with the status.jb file. i wrote a bit about how jb files work in a
[previous blog](/blog/2024/07/12/0-make.html), but it's basically just markdown
with built in shell scripting. in this case, we literally just run a single
shell script.

    # jazzybones status updates
    
    \$ ./status.sh
    
    \jb_dependencies: status.sh status.txt

then, `status.sh` will look at the git history of `status.txt` and show all of
my previous statuses.

    #!/bin/sh
    
    git log --pretty=oneline status.txt | awk '{print $1;}' | while read commit ; do
    	git checkout "$commit" ./status.txt > /dev/null 2>&1
    	printf "%s: " "$(git show -s --format=%ad --date iso8601 "$commit")"
    	cat status.txt
    	echo
    done
    
    git checkout HEAD ./status.txt > /dev/null 2>&1

that's all i just think that this system is pretty neat.
