---
title: "Vibe Coding is a System Design Interview"
author: "Brendan Long"
date: "2026-02-27"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/j8836xXSMDJTGgFQD/vibe-coding-is-a-system-design-interview"
score: 12
votes: 2
---

I've been working on two fairly large vibe-coded apps, and my process has converged on:

1.  Write a GitHub issue
2.  (If complicated enough) tell an agent to make a plan and then update the issue
3.  Have another agent read the issue and implement it

As the features get more complicated, I spend more and more time on step (1), and I'm finding that just taking the time to write a detailed enough issue is 90% of the work (and if I have a problem, going back and writing a much more detailed issue usually fixes it). The thing I realized this morning is that writing these issues and working through the plans is very similar to participating in a system design interview: You don't need to implement anything, but you do need to have a good high-level design, and think through all of the edge cases and tradeoffs.

The fun part compared to a normal system design interview is that you don't have to worry about impressing a coding agent, so it's perfectly fine to [just ramble](https://github.com/brendanlong/lion-reader/issues/641) as you think of edge cases and details that need to be handled. Also unlike a real system design interview, you're free to pick reasonable tradeoffs instead of designing everything to support a trillion concurrent users[^b3bsbgp3a8r].

System design interviews have traditionally been the hardest part of interviewing for senior+ software engineer jobs, so it feels meaningful that this is the only hard part left in coding for some domains. I'm curious to see what will happen to the current generation of junior engineers, freed from having to actually implement anything and able to focus purely on system design from the beginning. Maybe they'll grow really fast?

[^b3bsbgp3a8r]: Ironically, AI agents also mean this might be something you do have to design for in some cases now.