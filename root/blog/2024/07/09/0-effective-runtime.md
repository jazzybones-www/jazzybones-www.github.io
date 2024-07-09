# effective complexity

i wrote [the last blog post](/blog/2024/07/07/0-memory.html) at 11:59 pm but i
didn't want to break my streak of writing every day so i've decided to split it
into two parts. maybe this is cheating, but i don't really care. it's my website
i can do whatever i want with it.

anyways check out this code

```
for item1 in array:
	llm_output := run_llm(item1)
	for item2 in array:
		process_llm_output(llm_output, item2)
```

let's say that the `run_llm` and `process_llm_output` functions both run in O(1)
time. what's the runtime of this code?

well the obvious answer is O(n\^2). `process_llm_output` is run n\^2 times and
`run_llm` is run n times. the runtime converges to the slowest step, so this
code takes O(n\^2) to finish.

let's look a bit deeper into these functions. the `run_llm` function calls the
openai api to generate tokens with their chatgpt model, a process which takes
several seconds to complete. the `process_llm_output` runs entirely on the local
machine and finishes in nanoseconds.

this array would need to be quintillions of items long before you'd even notice
that this function takes O(n\^2) time. even if the `process_llm_output` function
is run more times, the `run_llm` function is just so much slower that it really
doesn't matter.

this sort of thing to me is the biggest difference between computer science and
software development. you can't figure out from a purely mathematical/computer
science perspective that this code effectively runs in O(n) time, you need to
have some knowledge about llms and the fact that they're just about the slowest
thing that you could possibly do on a computer in 2024.

anyways, that's all. back to bitburner.
