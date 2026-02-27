---
title: "Opening for a summer student"
author: "Scott Aaronson"
date: "Mon, 06 Oct 2008"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=362"
---

I'm seeking a talented student for summer of 2009, to work with me in developing and experimenting with a new open-source web application. I'm open to students from anywhere, though MIT students will receive special consideration for funding reasons.

The web app -- tentatively called "Worldview Manager" -- is intended to help people ferret out hidden contradictions in their worldviews. Think of a kindly, patient teacher in a philosophy seminar who never directly accuses students of irrationality, but instead uses Socratic questioning to help them clarify their own beliefs.

The idea is extremely simple (as of course it has to be, if this app is to attract any significant number of users). The user selects a topic from a list, which might include the following at the beginning:

Climate Change  
The Singularity  
Libertarianism  
Computational Complexity  
Interpretation of Quantum Mechanics  
Quantum Computing  
Gay Rights  
Israel  
Gifted Education  
Foundations of Mathematics  
Strong AI and Philosophy of Mind  
Utilitarian Ethics  
Animal Rights  
Art and Aesthetics

Users will also be able to contribute their own topic files. (The above list is biased toward those topics about which I feel like I could write a topic file myself.)

After choosing a topic, the user will be presented with a sequence of statements, one at a time and in a random order. For example, if the topic is Foundations of Mathematics, the statements might include the following:

> Math is a cultural construct.  
>  Math privileges male, linear thinking over female, intuitive thinking.  
>  The Continuum Hypothesis is either true or false, even if humans will never know which.  
>  There's a sense in which integers, real numbers, and other mathematical objects "existed" before humans were around to name them, and will continue to exist after humans are gone.

The user can indicate her level of agreement with each statement by dragging the cursor.

Now the topic file, in addition to the statements themselves, will also contain lists of pairs or sometimes triples of statements that appear (at least to the writer of the topic file) to be in "tension" with one another. From time to time, the program will search the user's previous responses for beliefs that appear to be in tension, point out the tension, and give the user the opportunity to adjust one or more beliefs accordingly. For example, the user might get a message like the following:

> You indicated substantial agreement with the statement
> 
> _If a scientific consensus on climate change existed, then society would have to act accordingly._
> 
> and also substantial agreement with the statement
> 
> _The so-called "consensus" on climate change simply reflects scientists' liberal beliefs, and therefore does not necessitate action._
> 
> These views would seem to be in tension with each other. Would you like to adjust your belief in one or both statements accordingly?

That's about all there is to it. No Bayesianism, no advanced math of any kind (or at least none that the user sees).

As you may have gathered, the writing of topic files is not a "value-neutral" activity: the choice of statements, and of which statements are in tension with which other ones, will necessarily reflect the writer's interests and biases. This seems completely unavoidable to me. The goal, however, will be to adhere as closely as is practical to Wikipedia's [NPOV](http://en.wikipedia.org/wiki/Wikipedia:Neutral_point_of_view) standard. And thus, for example, any well-written topic file ought to admit "multiple equilibria"; that is, multiple points of view that are genuinely different from one another but all more-or-less internally consistent.

The student's responsibilities for this project will be as follows:

  * Write, debug, and document the web app. This sounds straightforward, but it'll be important to get the details right. I'm not even sure which development tools would be best--e.g., whether we should use Java or JavaScript, do all computation on the server side, etc.--and will rely on you to make implementation decisions.
  * Write topic files. I can create many of the files myself, but it would be great if you could pitch in with your own ideas.
  * Help run experiments with real users.
  * Help write up a paper about the project.



If there's time, we could also add more advanced functionality to Worldview Manager. Your own ideas are more than welcome, but here are a few possibilities:

  * Present statements to the user in a non-random order that more rapidly uncovers tensions.
  * Allow users to register for accounts, and save their "worldviews" to work on later.
  * Give users the ability to compare worldviews against their friends', with large disagreements flagged for special consideration.
  * Give users the ability to use a local search or backtrack algorithm to decrease the total "tension" in their worldviews, while changing their stated beliefs by the minimum possible amount.
  * Enable adaptive follow-up questions. That is, once two beliefs in tension have been uncovered, the user can be queried more specifically on how she wants to resolve the apparent contradiction.



I'm looking for someone smart, curious, enthusiastic, and hard-working, who has experience with the development of web applications (a work sample is requested). Grad students, undergrads, high school students, nursery school students … it's what you can do that interests me.

I expect the internship to last about three months, but am flexible with dates. Note that in the year or so since I started at MIT, I've already worked with six undergraduate students, and three of these interactions have led or will lead to published papers.

If you're interested, send a cover letter, cv, and link to a work sample to aaronson at csail mit edu. If you want to tell me why the Worldview Manager idea is idiotic and misguided, use the comments section as usual.

**Update (10/15):** In a somewhat related spirit, Eric Schwitzgebel at UC Riverside points me to a [study](http://moral.wjh.harvard.edu/eric1/test/testN.html) that he and a colleague are conducting, on whether professional philosophers respond differently than laypeople to ethical dilemmas. _Shtetl-Optimized_ readers are encouraged to participate.
