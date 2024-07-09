# bitburner's memory model

i've been playing way too much bitburner recently. anyways, every bitburner
script has a memory footprint, which is entirely determined by the functions
that the script uses. for example, the `hackAnalyzePercent()` function uses 1 GB
of memory, so any script that uses it uses at least 1 GB of memory.

the memory footprint is _not_ influenced by the length of the script, so even if
my script is 100 MB of javascript, it's still going to use the same amount of
memory as a 100 byte script.

this makes sense, we're dealing with mostly plain text so it's really hard to
actually use a non-negligible amount of memory without intentionally writing
inefficient code.

this model of growth analysis comes up pretty often. mant times a function is
dominated by the runtime of a single step, so the effective runtime is different
from the actual runtime.

anyways i've been playing way too much bitburner so i only have a minute to
finish this article to continue my streak. i'll continue "tomorrow".
