---
title: "InsanityBench: Cryptic Puzzles as a Probe for Lateral Thinking"
author: "RobinHa"
date: "2026-02-22"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/ZmHGjF8rs5yZMHSmq/insanitybench-cryptic-puzzles-as-a-probe-for-lateral"
score: 44
votes: 25
---

**TLDR:** InsanityBench is a benchmark of handcrafted cryptic puzzles trying to measure creative conceptual leaps as required in, for example, scientific breakthroughs - SOTA models score around 10% - the benchmark is very much in its earliest form and will need to be properly scaled to reduce variance.

* * *

You are given this image and prompted to "solve" it, only left with the title Timely Journey. What are you thinking of?

![](https://www.robinhaselhorst.com/assets/timely-journey-Dpr3eQLw.jpg)

(In case you genuinely wanna try, stop reading for now, [here's the link to the problem](https://www.janestreet.com/puzzles/timely-journey-index/))

The domino stones are **clearly** hinting at 2016 / 4, when they published a different puzzle titled "Long. Journey" which featured coordinates. Just as obvious is that the plant at the top is a Thyme, that you gotta interpret the wooden stone as a Z and there are a bunch of dice showing "ones"; naturally Thyme + Z + ones = Time zones. Of course. And see those pushpins? Yeah, they are pointing at Shift because you have to shift some letters down the line. (It goes on like this but I'll spare you your sanity)

In case it wasn't obvious, I'm being ironic. None of this is obvious - but still weirdly beautiful.

What is InsanityBench
---------------------

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/68127d5fa4be9811b95eee1d756a29bb77a9d283be875ad2.png)

InsanityBench is supposed to be a benchmark encapsulating something we deeply care about (the "insane" leaps of creativity often needed in science), can hardly be gamed (because every task is completely different from another) and is nowhere near saturated yet (the best model scores 15%).

### Insanity and Creativity

When looking through the history of humankind and especially science, there were many keypoints where individuals proposed such controversial ideas that at first glance they would be titled 'insane'. "Productive insanity" seems to be when you can come up with and engage with ideas that at first glance might appear absurd but when viewed from the correct angle, are the simplest explanation - they somehow just fit with every piece of evidence beautifully and suddenly "insanity" is "creativity".

InsanityBench is trying to emulate such insanity, often only providing the problem solver (an LLM) with a story, maybe an image, or a single txt of cryptic numbers. Sometimes no instructions whatsoever except "Solve this very difficult, cryptic puzzle."

What would the answer even **look like**? Is **this** a hint? What if I do **this**? Do these three **coincide** in some noticeable way?

... and once the answer **is** found, looking back at the puzzle seems like worlds apart - everything just somehow fits. This is the beauty InsanityBench is trying to measure, the beauty which allowed scientific progress, and the beauty LLMs struggle with comparatively to other fields.

### Can't be gamed

I know multiple people working at some big players who are great mathematicians and are getting significant salaries just to write and read CoT (this is now slightly outdated), poke at the model and find problems it can't solve (and then "fix" it). I'm not a big fan of this and am not convinced it will scale. But as a result all the major benchmarks are going up, decoupled from the actual rate of progress.

InsanityBench is trying to resist this not only by staying private (except one example task) but also by the nature of the problems themselves: When the input constantly switches to unseen formats, be it poem, short story, entire book, image, Python code, etc., when the answer and the path of getting there never reappear, then "gaming" the dataset seems very difficult to say the least.

A lot of benchmarks in the past year were competitions like IMO & Codeforces, etc.; as someone who did competitive programming himself for some time and competed in CEOI for Germany, the creativity needed in such competitions (by design) is low-dimensional. That is, you can very well study for them and basic pattern matching from (vast) experience will get you very far.

### Nowhere near saturated

As of right now InsanityBench consists of 10 handcrafted tasks made with love and sweat that no one except a few friends, who roughly verified them, know of. Model responses are graded from 0 to 10 and roughly the following holds: 10 for the full correct answer, 5 for a significant part of the solution and 2 for interpreting a subset of hints correctly.

Of the 10 tasks, the best scoring model gets 15%: Gemini 3.1 Pro solves one fully and one partially. Additionally, none of the models even got partial points on any of the tasks grouped as "hard". It should be noted that the tasks are also difficult for humans - but seeing how skilled LLMs are already at intellectual work measured in other benchmarks, this area of prioritizing creativity heavily sticks out. As an estimate, I think an average person could solve the tasks not classified as "hard" in 1 hour or so.

Details and further plan
------------------------

This is an alpha release of this benchmark. For starters, I will scale the tasks up to roughly 25 in the next two months or so. This still might appear low but since automatic verification is impossible and LLM-as-a-judge will ruin the point of adding more tasks, I'm grading the answers manually. It's normally pretty quick but still not worth it to scale beyond 25 as a result. Additionally, coming up with these tasks is difficult and takes substantial time.

The API costs quickly scale up, even with this small amount of tasks, with all the different models. I might contact some of the providers and ask whether they are willing to spare me some API credits. In case you are interested in partially supporting the API costs, reach out. Especially since as of right now, every task per model is only queried once and taken as a representative sample - I would like to increase this up to 4 or so, but this directly 4x's the cost as well.

Lastly, I'm publishing one of the ("easy") tasks without solution. This is the task that already gets solved the most across the board so I'm not too worried about publicizing it. Mostly so people might get a better feeling for what a task might look like (even if every task is wildly different from another). In case you try it by hand and think you arrived at the solution, you can contact me by email and I'll verify it.

[Leaderboard](https://www.robinhaselhorst.com/insanityBench)

[Sample Task](https://www.robinhaselhorst.com/insanityBench/example.txt)