---
title: "AlphaCode as a dog speaking mediocre English"
author: "Scott Aaronson"
date: "Sun, 06 Feb 2022"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=6288"
---

Tonight, I took the time actually to read DeepMind’s [AlphaCode paper](https://storage.googleapis.com/deepmind-media/AlphaCode/competition_level_code_generation_with_alphacode.pdf), and to work through the example contest problems provided, and understand how I would've solved those problems, and how AlphaCode solved them.

It is absolutely astounding.

Consider, for example, the "n singers" challenge (pages 59-60). To solve this well, you first need to parse a somewhat convoluted English description, discarding the irrelevant fluff about singers, in order to figure out that you're being asked to find a positive integer solution (if it exists) to a linear system whose matrix looks like  
1 2 3 4  
4 1 2 3  
3 4 1 2  
2 3 4 1.  
Next you need to find a trick for solving such a system without Gaussian elimination or the like (I'll leave that as an exercise…). Finally, you need to generate code that implements that trick, correctly handling the wraparound at the edges of the matrix, and breaking and returning "NO" for any of multiple possible reasons why a positive integer solution won't exist. Oh, and also correctly parse the input.

Yes, I realize that AlphaCode generates a million candidate programs for each challenge, then discards the vast majority by checking that they don't work on the example data provided, then _still_ has to use clever tricks to choose from among the thousands of candidates remaining. I realize that it was trained on tens of thousands of contest problems and millions of solutions to those problems. I realize that it "only" solves about a third of the contest problems, making it similar to a mediocre human programmer on these problems. I realize that it works only in the artificial domain of programming contests, where a complete English problem specification and example inputs and outputs are always provided.

Forget all that. Judged against where AI was 20-25 years ago, when I was a student, a dog is now holding meaningful conversations in English. And people are complaining that the dog isn't a very eloquent orator, that it often makes grammatical errors and has to start again, that it took heroic effort to train it, and that it's unclear how much the dog really understands.

It's not obvious how you go from solving programming contest problems to conquering the human race or whatever, but I feel pretty confident that we've now entered a world where "programming" will look different.

**Update:** A colleague of mine points out that one million, the number of candidate programs that AlphaCode needs to generate, could be seen as roughly exponential in the number of lines of the generated programs. If so, this suggests a perspective according to which DeepMind has created almost the exact equivalent, in AI code generation, of a non-fault-tolerant quantum computer that’s nevertheless competitive on some task (as in the quantum supremacy experiments). I.e., it clearly does something highly nontrivial, but the “signal” is still decreasing exponentially with the number of instructions, necessitating an exponential number of repetitions to extract the signal and imposing a limit on the size of the programs you can scale to.
