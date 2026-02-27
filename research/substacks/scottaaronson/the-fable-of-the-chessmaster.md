---
title: "The Fable of the Chessmaster"
author: "Scott Aaronson"
date: "Sat, 18 Feb 2006"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=56"
---

If a layperson asks you what computational complexity is, you could do worse than to tell the following story, which I learned from Steven Rudich.

A man with a flowing gray beard is standing on a street corner, claiming to be God. A bemused crowd gathers around him. "Prove it!" they taunt.

"Well," says the man,"I can beat anyone at chess."

A game is duly arranged against Kasparov, who happens to be in town. The man with the gray beard wins.

"OK, so you're pretty good at chess," the onlookers concede. "But that still doesn't mean you're God."

"O ye of little faith! As long as I play White, it's not just hard to beat me -- it's mathematically impossible! Play Black over and over, try every possible sequence of moves, and you'll see: I always win."

A nerd pipes up. "But there are more sequences of moves than there are atoms in the universe! Even supposing you beat us every day for a century, we'd still have no idea whether some sequence of moves we hadn't tried yet would lead to your defeat. We'll be long dead before every possibility is examined. So unless you're prepared to grant us immortality, there's no way you can possibly convince us!"

Most of you know the punchline to this story, but for those who don't: the nerd is wrong. By asking a short sequence of randomly-chosen questions, each a followup to the last, the crowd can quickly convince itself, to as high a confidence as it likes, that the man they're interrogating knows a winning strategy for White -- or else expose his lie if he doesn't. The [reason](http://www.cs.sfu.ca/%7Ekabanets/710/w12.ps) was discovered in 1990 by Lund, Fortnow, Karloff, Nisan, and Shamir, and has less to do with chess than with the zeroes of polynomials over finite fields.

There are two lessons I'd like to draw from Rudich's Fable of the Chessmaster.

The first lesson is that computational complexity theory is really, really, really not about computers. Computers play the same role in complexity that clocks, trains, and elevators play in relativity. They're a great way to illustrate the point, they were probably essential for discovering the point, but they're not the point.

The best definition of complexity theory I can think of is that it's quantitative theology: the mathematical study of hypothetical superintelligent beings such as gods. Its concerns include:

  * If a God or gods existed, how could they reveal themselves to mortals? (IP=PSPACE, or MIP=NEXP in the polytheistic case.)


  * Which gods are mightier than which other gods? (PNP vs. PP, SZK vs. QMA, BQPNP vs. NPBQP, etc. etc.)


  * Could a munificent God choose to bestow His omniscience on a mortal? (EXP vs. P/poly.)


  * Can oracles be trusted? (Can oracles be trusted?)



And of course:

  * Could mortals ever become godlike themselves? (P vs. NP, BQP vs. NP.)



Incidentally, it's ironic that some people derisively refer to string theory as "recreational mathematical theology." String theory has to earn the status of mathematical theology -- right now it's merely physics! A good place for string theorists to start their theological training is [this](http://www.arxiv.org/abs/hep-th/0602072) recent paper by Denef and Douglas.

So that was my first lesson. The second lesson is that interaction helps: you can get your message across a lot faster if people are continually challenging you. If the gray-bearded man were just lecturing to a passive audience, rather than being grilled by doubters trying to trap him in a contradiction, then it would take longer than the age of the universe for him to prove his unbeatability at chess. Or rather, we theologians conjecture that it would.

I'm reminded of the power of interaction every time I give a talk. Despite a certain reputation for cheap yuks, I've never been a good speaker. I'm terrible at explaining anything coherently -- that is, in a way that anticipates people's objections. Fortunately, as long as people interrupt me, it doesn't matter much, since I can easily answer the objections once I know what they are. Indeed, not only do interruptions clue me in on what's bugging people -- as in the Fable of the Chessmaster, they also let me prove that I basically know what I'm talking about, even if I can't articulate it in the allotted time!

(In my ideal talk, I would begin by saying "Thank you. Are there any questions?")

For another example, take the sex columnist [Dan Savage](http://www.avclub.com/content/savagelove). Savage has a "philosophy," which consists partly of a refusal to condemn sex acts if they don't harm anyone, and a willingness to condemn them if they do. But if he tried to state his philosophy explicitly, he wouldn't do it justice any more than I just did. So instead he answers questions about used underwear fetishes and masturbating parakeets.

The same goes for comedians, at least the good ones like [Jon Stewart](http://www.comedycentral.com/shows/the_daily_show/index.jhtml). Stewart has an enviably easy job: news happens, he reacts to it. It's like my ideal talk that consists entirely of questions -- except that instead of questions, there's Bush warning about "human-animal hybrids" in his State of the Union address, or Cheney shooting his hunting buddy in the face.

Inspired by such examples, and by my recent positive experience answering [Peter Brooke's question](https://scottaaronson.blog/?p=55), I've decided to open this blog to questions on a regular basis. Email them, post them in the comments section, whatever. I can't promise to take up everything. Try to guess which of the following would have a better chance:

> "Please discuss the relative merits of conference and journal publication in theoretical computer science."  
>  "How could schools be redesigned to improve the sex lives of nerds?"
