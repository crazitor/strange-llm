---
title: "D-Wave: Still propagating"
author: "Scott Aaronson"
date: "Thu, 05 Apr 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=223"
---

Last night Jason Pontin, the Editor-in-Chief of MIT's _Technology Review_ , published a [hard-hitting article](http://www.technologyreview.com/Infotech/18495/page1/) about D-Wave, the Vancouver startup that claims to have built "the world's first commercial quantum computer." A condensed (and, alas, considerably mangled and dumbed-down) version of his article will appear in Sunday's _New York Times_.

Jason wrote to me a couple weeks ago and said that, while he knew that most journalists had gotten the D-Wave story wrong, he was determined to get it right, and wanted my help in understanding the computer-science issues. He didn't have to ask me twice.

Since I come across as pretty harsh on D-Wave in the article, I think it's worth recalling how we got to this point. When the D-Wave story broke, my first reaction was to give them some benefit of the doubt (as you can see from the mild tone of my ["Orion Anti-Hype FAQ"](https://scottaaronson.blog/?p=198)). So what changed? Well, four things:

  1. I asked Geordie Rose (the founder of D-Wave and sometime commenter on this blog) twice for actual information about the speedup D-Wave claimed to be seeing over classical algorithms, and he never provided any.
  2. Instead of answering my and others' technical questions, D-Wave decided to attack academic science itself. Here's what Herb Martin, the CEO of D-Wave, [told an interviewer from _ITworld_](http://www.itworld.com/Tech/3494/070309nasaquantum/index.html): "Businesses aren't too fascinated about the details of quantum mechanics, but academics have their own axes to grind. I can assure you that our VCs look at us a lot closer than the government looks at the academics who win research grants." The track record of companies that engage in this sort of behavior is not good.
  3. I read article after article claiming that quantum computers can solve NP-complete problems in polynomial time. I reflected on the fact that a single one of these articles will probably reach more people than every quantum complexity paper ever written.
  4. It became clear, both from published interviews and from talking to Jason, that D-Wave was doing essentially nothing to correct journalists' misconceptions about what sorts of problems are believed to be efficiently solvable by quantum computers.



**Update (4/6):** Geordie Rose has [responded to me](http://dwave.wordpress.com/2007/04/06/more-on-the-tr-interview/). A few responses to his response:

  * I apologize for getting the CEO's name wrong. I'd originally written Herb Martin, but then noticed that the [_ITworld_ article](http://www.itworld.com/Tech/3494/070309nasaquantum/index.html) referred to him as "Ed Martin" and therefore changed it. This seems like another case where D-Wave has to work harder to correct journalists' misconceptions!


  * In a discussion with Geordie on my blog, following my Orion Anti-Hype FAQ, I asked:  


> You say you’re seeing a speedup in your experiments — but (1) how big of a speedup, and (2) do you mean compared to the best-known classical algorithms (like simulated annealing), or compared to brute-force search?

Then, in another discussion with Geordie following my [Speaking truth to parallelism](https://scottaaronson.blog/?p=201) post, I asked him again:

> I’m certainly glad that you’re not claiming an exponential speedup. But at least based on the evidence _I_ know about, whether you’re seeing a quadratic speedup — or indeed _any_ asymptotic speedup — is very much open to question. Hence the question I asked you earlier: have you compared the empirical scaling for your adiabatic algorithm to the empirical scaling for the best classical algorithms like simulated annealing? If so, what were the results?



  * Geordie now says that "the only way scaling can be extracted is empirically, and we can’t build big enough systems (yet) to answer scaling questions." Thanks; that's actually extremely helpful to me. I must have gotten a wrong impression from some of D-Wave's previous statements. For example, here's from D-Wave's recently-released "Introduction to Orion" document (which now seems to be available for "premium subscribers" only):  


> Q: Are D-Wave processors quantum computers?  
>  A: Yes. We have determined that quantum effects are being harnessed to accelerate computation in our processors.

And here's from a [comment on Dave Bacon's blog](http://dabacon.org/pontiff/?p=1427#comment-152007) (blog comments seem to be D-Wave's preferred venue for announcing scientific results):

> While the jury is still not in, our studies of these systems seem to indicate that AQCs, in the presence of thermal and spin bath environments, can still provide O(sqrt(N)) scaling even though the central QC system is definitely NOT a “system that’s globally phase coherent over the entire calculation”.



  * The core of Geordie's response is the following paragraph:  


> This is worth emphasizing, because I thought it was obvious, but it turns out alot of people don’t get this. Most of the poorly thought out comments related to what we’re trying to do have come from theoretical computer scientists, who assume that the things they hold dear are likewise treasured by everyone else. Because they worship efficiency, they have assumed that’s the objective of our projects, when I have repeatedly said it’s not.

When I read this to Umesh Vazirani over the phone, he sardonically replied, "it will be interesting to find out what's left of this field after you've removed the notion of efficiency…"


