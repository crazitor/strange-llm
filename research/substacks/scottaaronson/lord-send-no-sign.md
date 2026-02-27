---
title: "Lord, send no sign"
author: "Scott Aaronson"
date: "Mon, 27 Feb 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=60"
---

Lars Johansson asks me to comment on a [press release](http://www.news.uiuc.edu/news/06/0222quantum.html) entitled "Quantum computer solves problem, without running." Alright, what have we got this time?

> CHAMPAIGN, Ill. -- By combining quantum computation and quantum interrogation, scientists at the University of Illinois at Urbana-Champaign have found an exotic way of determining an answer to an algorithm -- without ever running the algorithm.
> 
> Using an optical-based quantum computer, a research team led by physicist Paul Kwiat has presented the first demonstration of "counterfactual computation," inferring information about an answer, even though the computer did not run.

Readers, my sole ambition in life, outside the purely personal, is to prevent stuff like this from being spouted.

I'm serious. You see, I have no "philosophy" to offer the world, no unifying theory, no startling new idea. All I have is a long howl of rage, which admittedly tends to take the form of STOC/FOCS papers. But if you read those papers, you'll see that almost every one of them was born when I came across some specific claim and said, "No. Dammit. No. That can't possibly be right."

Look -- if you tell a layperson that a computer has solved a problem without ever having been switched on, then not only have you not explained anything, you haven't even asserted anything. All you've done is pose a question: namely, "what's the catch?"

In this case, the catch is simple. Say you've got two programs, Dif and Doof, running in the Windows taskbar. Dif is performing some enormous calculation, while Doof (being a Doof) is doing nothing. If Dif's calculation returns any answer other than 5, then Dif closes Doof. You come back to your computer and find that Doof is still running. Even though Doof didn't calculate anything, and even though Dif never did anything to Doof, you can immediately conclude -- from Doof alone -- that the answer you wanted was 5. Mindblowing! Unbelievable!

Now let Dif and Doof run, not in different windows, but in different branches of the wavefunction -- that is, in quantum superposition. And instead of Dif using an operating system to close Doof, have Dif's branch of the wavefunction interfere destructively with Doof's branch, thereby preventing Doof's branch from being observed. That's the idea of counterfactual quantum computing.

I suppose this is "mysterious," in the same way that a dog claiming to hate doggie-treats would be mysterious. In the former case, the mystery is quantum mechanics. In the latter case, the mystery is a talking dog.

Having said that, the [original paper](http://arxiv.org/abs/quant-ph/9907007) by Jozsa and Mitchison is actually lovely and well worth reading. It proves some nontrivial results about limits of counterfactual computing, and it also gives a good introduction to the Vaidman bomb (which I think of as a precursor to Grover's algorithm).

I'll end with the clearest account of counterfactual computing I've seen, courtesy of one Homer J. Simpson.

> Dear Lord, the gods have been good to me. As an offering, I present these milk and cookies. If you wish me to eat them instead, please give me no sign whatsoever.
> 
> …
> 
> Thy will be done (munch munch munch).

Update (3/1): Paul Kwiat has written in to the comments section with some helpful clarifications.
