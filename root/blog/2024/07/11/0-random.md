# a really cursed shuffle function

recently, i looked up how to sort an array in javascript. i clicked [the top
result](https://web.archive.org/web/20240710081924/https://www.w3schools.com/js/js_array_sort.asp),
and saw, among other things, this truly awful section.

> ## Sorting an Array in Random Order
> 
> Using a sort function, like explained above, you can sort an [sic] numeric
> array in random order
> 
>     const points = [40, 100, 1, 5, 25, 10];
>     points.sort(function(){return 0.5 - Math.random()});

this is just disgusting. truly revolting stuff. the first problem is that the
comparison function creates is impure. that means that something like this:

    compare(a, b) == compare(a, b)

doesn't always return `true`. i actually have no problem with this, sometimes
you just have to break the rules of a programming interface to get something
done. as long as it works and is easy to work with, it's probably fine.

my biggest problem is that this function doesn't even work. like, one of the
most popular sorting algorithms is
[quicksort](https://en.wikipedia.org/wiki/Quicksort), which looks like this:

    function sort(array):
        pivot = array[0] // this could be any value in the array, but the first one is common
        smaller_values = []
        larger_values = []
	for value in array[1:]:
            if value < pivot:
                smaller_values.append(value)
            else:
                larger_values.append(value)
        return sort(smaller_values) + pivot + sort(larger_values)

this is a really bad quicksort implementation. please don't use it. the idea is
there though, you take some pivot point, separate the smaller values from the
larger values, and sort each individually.

if you try to shuffle this array using the method from earlier, then around half
of the values will be "smaller" than the pivot, and the other half will be
larger. this means that the pivot would almost always go in the middle.

if we use this specific sorting algorithm and use this specific shuffle, then i
know for a fact that the first element of my array will always go around the
middle.

this code is immediately followed by a proper shuffling algorithm, but this code
just reeks of coding by coincidence. like, no smart programmer would ever write
this code, partially because it uses the wrong tool for the job, but mainly
because it just doesn't work. if you write this code, you have to either not
care about the result, or know with 100% certainty that every browser that your
code will run on will handle this properly. the fact that this was included in
the original article at all is wild.

that's all i have to say. please don't use this code.
