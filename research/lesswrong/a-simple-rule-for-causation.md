---
title: "A simple rule for causation"
author: "Vivek Hebbar"
date: "2026-02-24"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/KTasQyRBzz6FTB4BL/a-simple-rule-for-causation"
score: 37
votes: 17
---

Here's a simple heuristic about causal inference:

*   If we find even a single thing X which is related[^6xxvrqvijcv] to A but independent of B, we can conclude that A is **not** causally upstream of B.
*   Therefore, if everything related to A is also related to B, we can become moderately confident that A is causally upstream of B.  We can have a higher confidence if we measure lots of things and the causal graph is likely to be complicated (with most variables having many causes and effects).

For example, consider the claim "rain causes me to carry an umbrella":

*   It should be impossible to think of a thing that is correlated with rain that isn't also correlated with me carrying an umbrella.[^sobv6n7bkp8]
*   Whereas it should be possible to find things that are correlated with umbrella-carrying but not rain.  For example, my level of laziness on a given day might be negatively correlated with carrying an umbrella even if my laziness isn't correlated with rain.

The rule has some exceptions which I discuss in the last section.

Derivation of the rule
----------------------

Suppose A and B are related (non-independent).  We want to distinguish the following three possibilities:

*   A causes B
*   B causes A
*   neither causes the other (there is only common cause)

Now suppose we want to distinguish these using purely observational data.  In particular, we can look at the joint distribution of {A, B, X} for a variety of additional variables X.

Specifically, we are going to look at the conditional dependency relationships between the three variables.  This consists of six questions:

*   are A and B independent?
*   are B and C independent?
*   are A and C independent?
*   are A and B independent conditional on C?
*   are B and C independent conditional on A?
*   are A and C independent conditional on B?

If we require that A and B are related and C is related to at least one of the other two, then it will turn out that there are only 6 possible answers to this set of questions.  Either all of the dependencies will exist (1 option) or exactly one will be independent (5 options, since we already assumed A and B are related).[^qqzsd3mxfo]

Here is the table of which dependency structures are compatible with each of the three causal hypotheses for A and B:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e2ded1f82b931eefed8b46a3a007db402691a67eeb4c39e7.png)

There is no possible value of the conditional dependencies between {A, B, C} that can rule out "common cause only".  However, each of the other two hypotheses can be falsified by a single observation.

The only way to gain high confidence in the hypothesis "A causes B" is to look hard for cases where C is related to A but not to B.  If A does not cause B, we'd expect to eventually find such a case, so not finding one is usually strong evidence of causation.

The counterexample is always a case where C is either:

*   a cause of A which is unrelated to B
*   or an effect of such a cause

In the next section, I'll derive the table by giving a causal diagram for every "allowed" cell.  Then I'll talk about two practical exceptions to the central claim.

A visual derivation of the table
--------------------------------

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/d9cf8bdd817b7ad6041fcbc52512494cc4fc95d125df2cea.png)

**Exceptions**
--------------

**Exception 1: "coincidences" and control systems**[^bpx8xubs9ug]

In general, a causal graph can tell you when two variables *must* be independent, but it cannot rule out two variables being independent "by coincidence" when the causal graph says that they shouldn't be independent.  

If the content of the causal relationships is randomly chosen from a continuous option space, then such coincidences have probability zero.  However, in intentionally designed control systems, it is possible for causal paths to cancel out.

For example, consider a thermostat.  The output voltage of the thermostat at time $t$ surely has a causal effect on the temperature in the room at time $t+1$.  However, if the thermostat functions perfectly, it might statistically appear as if the output voltage is not causally upstream of the future room temperature.  Let's work through the example with a causal graph:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/a875923e71f3c9eb47ff456b890912912a99722c270a2fb2.png)

A causal model of our thermostat

Now let's apply our rule.  We want to verify that **A** is causally upstream of **B**.  Since **X** is related to **A**, it should also be related to **B**.  However, if the thermostat works well, **X** and **B** will in fact be independent!  The temperature at time $t+1$ ("B") will depend only on the thermostat set point and not on the temperature at time $t$ ("X") -- that's what it means for the thermostat to work well!  

The graph says that **X** has two causal paths to **B** (the direct blue arrow and the orange path through the thermostat), but these will cancel out by design of the thermostat.

This designed cancellation would be a probability-zero coincidence for a randomly generated system.

**Exception 2: No measurable causes of A except for common causes with B**

These two diagrams cannot be observationally distinguished:

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/d8a416a2fc72831e6039aa7281ce0f5f7ee3420aa3cf163a.png)

The culprit is that A has no causes except the one shared with B.  

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/1fd0a9f593d6deca9a8d460847352092cc17a506dd198a45.png)

If we instead had this diagram, we could rule out "A causes B" by measuring that D is related to A while being independent of B.

If D is not measurable for some reason, we could instead measure variables downstream of D that are unrelated to B and C.  But if there is some systematic reason that no such variables are measurable, our rule will incorrectly conclude that A causes B.

*Thanks to Thomas Kwa for pointing out the control systems exception, and for encouraging me to write this post.  Thanks to Lukas Finnveden for useful feedback.*

[^6xxvrqvijcv]: Throughout this post I will use "related" as an exact synonym for "not independent", as a way of simplifying the language. 

[^sobv6n7bkp8]: I actually mean "not independent" but I think the sentence is easier to read with "correlated". 

[^qqzsd3mxfo]: I'm assuming here that variables are only independent if the structure of the causal graph requires them to be independent.  Exceptions to this are discussed in the final section. 

[^bpx8xubs9ug]: Thanks to Thomas Kwa for pointing out the control systems exception, and for encouraging me to write this post :)