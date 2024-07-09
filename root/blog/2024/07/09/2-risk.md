# the mathematically best bitburner stock market strategy

i'm still addicted to bitburner. anyways, bitburner has a stock market. there
are stocks which you can buy and sell (you can also hold a short position, but
i didn't feel like writing code for that). there's also a forecasting system
that tells you the probability of a given stock's value increasing within a
single tick.

so we've got all of these stocks and their corresponding price forcasts. somehow
we have to distribute our money between each of these stocks to maximize the
expected value of the next tick.

we might try putting the same amount of money into every stock. let's say we
have 10 billion dollars to distribute among 10 stocks, we'd just invest 1
billion into each stock.

we might take some of the money from the worst performing stock and transfer it
to the best performing stock. this will obviously get us a better expected
value, since we're getting rid of a small value in the average and replacing it
with a big value.

we might keep doing this continuously. in the end we find that the
mathematically best strategy is just to yolo on a single stock r/wallstreetbets
style.

there are two reasons why real hedge funds don't actually do this:

1. real hedge funds don't have perfect forecasts like we do
2. it increases risk

if we go all in on a single stock, and that one stock has a 20% chance of
failing, then our entire firm has a 20% chance of failing. if we instead go 20%
in on 5 different socks and each one has an independent 50% chance of failing,
then our entire firm has only a 3.125% chance of failing.

i'm still running the yolo code, it's easier to write and i really don't know
enough statistics to make it better.
