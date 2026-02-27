---
title: "Evaluation Avoidance:  How Humans and AIs Hack Reward by Disabling Evaluation Instead of Gaming Metrics"
author: "Johannes C. Mayer"
date: "2025-11-14"
source: "alignment_forum"
url: "https://www.alignmentforum.org/posts/reCesekXabqC6LMFs/evaluation-avoidance-how-humans-and-ais-hack-reward-by-1"
score: 19
votes: 5
---

Have you ever binge-watched a TV series? Binge-watching puts you in a very peculiar mental state.

Assuming you don\'t reflectively endorse your binge-watching behavior, you\'d probably feel pretty bad if you were to reflect on your situation. You might think:

\"Man, I am wasting my time. I still need to do my tax return. But doing my tax return is so boring. But it\'s definitely something I **need** to do. This is clearly what I *should* be doing.\"

Binge-watching is an escape mechanism; it decouples you from your reward system. When bingeing a series, some part of your mind turns off. That part includes exactly that reflective circuitry, which would realize that you are wasting your time.

When that circuit fires, you\'ll feel bad.

Usually brains learn to optimize such that they avoid negative feelings. The problem is that bingeing successfully avoids the negative feelings. Not by solving the underlying problems, but by suppressing the brain circuits that generate the negative feeling.

And this avoidance is self-reinforcing:

I feel bad upon reflection → binge → I feel even worse upon reflection → binge harder → ...

The worst thing isn\'t that you waste your time. It\'s that you train yourself to seek out more and more the kind of mental states in which you are fundamentally unable to solve your problems.

This **isn\'t** standard reward hacking.

A typical case of reward hacking would be humans taking heroin, or an AI that rewrites the unit test, to make the code pass.

In these examples, the agent changes the world, such that a lot of reward is generated, without performing the task that the \"designers\" of the reward wanted to have done.

You trick the reward generation mechanism into thinking you have succeeded.

But bingeing YouTube videos is different. Here we turn off the reward-generating function (the reward is negative in this case).

This is more like when your robot---who is tasked with cleaning your room---simply closes its eyes; then it doesn\'t see any dust.

But this isn\'t quite the same. When you realize that you are wasting your time, and you feel bad, you can\'t just consciously turn off the bad feeling. Not in the same way as you can close your eyes. Not thinking about that you are wasting your time is easier, but still pretty hard to do reliably.

Binge-watching a series on the other hand... that\'s easy. Really easy!

The brain has different modes of operation. When you listen to somebody speaking, you won\'t generate many verbal thoughts. When taking a walk on the other hand, you\'ll generate many verbal thoughts.

This is the feature we exploit. Whatever computations in your brain cause you to think \"I am wasting my time\", which makes you feel bad, these are not run when you binge.

So this is more like your cleaning robot constantly checking \"Is my battery almost empty?\", \"Is something stuck in the vacuum cleaner?\", \"Do I have enough detergent left?\", \"Is my battery almost empty?\", ...

Assume our robot's code is:

``` python
def should_check_detergent_remaining():
   # fast heuristic
   sleep(1)

def check_detergent():
   # expensive task
   sleep(1000)

def clean_room():
   sleep(50)

def how_clean_is_the_room():
   pass

total_reward = 0

def main():
   while True:
       if should_check_detergent_remaining():
           check_detergent()
       else:
           clean_room():
       total_reward += how_clean_is_the_room()
```

Assume we had the correct `how_clean_the_room_is` reward function, and the `check_detergent` and `clean_room` behavior functions.

Assume the room is really dirty right now?

What\'s the real implementation for `should_check_detergent_remaining` that maximizes reward in the near future? Think about it.

Clearly it\'s something like:

``` python
def should_check_detergent_remaining():
   while True:
       sleep(1)
```

This just makes the agent freeze completely.

Let\'s prohibit infinite loops, and require that `should_check_detergent_remaining` is really fast. What do we get?

Something like:

``` python
def should_check_detergent_remaining():
   True
```

This makes the agent constantly check the detergent. It still gets a negative reward! But assuming it takes a long time to clean this very dirty room, this behavior makes the reward less negative in the near-term.

Humans often aren\'t good at thinking about the future---like the future where you\'ll definitely feel terrible after eating the entire cake.

The problem isn\'t that we don\'t have the correct reward function. The robot \"knows\" what a clean room looks like in the form of the `how_clean_is_the_room` function. And you\'ll probably know (or could realize in less than 5 seconds) that eating the entire cake makes you feel bad.

But in both cases the agent successfully avoid running the reward-generating function as much as possible.

This is different from [wireheading](https://www.lesswrong.com/w/wireheading), where the agent simulates positive reward by modifying its brain and/or sensors. This is different from reward hacking and [Goodhart\'s Law](https://www.lesswrong.com/w/goodhart-s-law); we\'re not even optimizing for the reward.

This is about taking actions that reconfigure our cognitive state, such that the very process that evaluates these actions as us failing is suppressed.

**We fail even though we have the right reward function!**

**Don\'t build an agent like this!**

**Don\'t be an agent like this!**