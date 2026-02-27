---
title: "Generative AI’s crippling and widespread failure to induce robust models of the world"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread"
---

##### _Synthesized video from Dawid van Straaten, prompt (“Generate me a video of two men playing chess”) in which the player for black reaches across the table and, in the midst of a rather unusual position moves his opponent’s pawn horizontally, and quite illegally, several squares across the board._

_A few weeks ago, I had the singular honor of recording a podcast ([to be released soon](https://www.theatlantic.com/podcasts/archive/2025/06/coming-soon-a-new-season-of-autocracy-in-america/683336/)) with one of my heroes, Garry Kasparov, not only one of the greatest chess players of all time, but also one of the bravest, most foresightful people I know. I wish with all my heart that more people had heeded his warnings about both Russia and the United States._

_This essay, which I started in preparation for our recording, looks at chess (though not only chess) as a window into LLMs and one of their most serious, yet relatively rarely commented-upon shortcomings: their inability to build and maintain adequate, interpretable, dynamically updated**models of the world** — a liability that is arguably even more fundamental than the [failures in reasoning recently documented by Apple](https://open.substack.com/pub/garymarcus/p/a-knockout-blow-for-llms?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)._

A world model (or _cognitive model_) is a computational framework that a system (a machine, or a person or other animal) uses to track what is happening in the world. World models are not always 100% accurate, or complete, but I believe that they are absolutely central to both human and animal cognition.

Another of my heroes, the cognitive psychologist Randy Gallistel, has written extensively about [how even some of the simplest animals, like ants, use cognitive models](https://openlibrary.org/books/OL2049287M/The_organization_of_learning), which they regularly update, in tasks such as navigation. A wandering ant, for example, tracks where it is through the process of dead reckoning. An ant uses variables (in the algebraic/computer science sense) to maintain a readout of its location, even as as it wanders, constantly updated, so that it can directly return to its home. 

In AI, what I would call a cognitive model is often called a _world model_ , which is to say it is some piece of software’s model of the world. I would define world models as persistent, stable, updatable (and ideally up-to-date) internal representations of some set of entities within some slice of the world.[1](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-1-164369506) One might, for example, use a database to track a set of individuals over time, including, for example, their addresses, telephone numbers, social security numbers, etc. Every physics engine (and video game) has a model of the world, too (tracking, for example, a set of entities and their locations and their properties and their motions).

Here’s the crux: **in classical artificial intelligence, and indeed classic software design, the design of explicit world models is absolutely central to the entire process of software engineering. LLMs try — to their peril — to live without classical world models**.

As the title of a book by the late Turing Award winner Niklaus Wirth put it, _[Algorithms + Data Structures = Programs](https://en.wikipedia.org/wiki/Algorithms_%2B_Data_Structures_%3D_Programs)_ , and world models are central to those data structures. In a video game, a world model (sometimes nowadays implemented as a [scene graph](https://en.m.wikipedia.org/wiki/Scene_graph)) might include detailed maps, information about the location of particular characters, the main character’s inventory, and so on; in a word processor, one could consider the user’s document and the file system to be part of the program’s model of its world, and so on. 

In classical AI, models are absolutely central — and pretty much always have been. Alan Turing made a dynamic world model, updated after every move, central to his chess program, now known as [Turochamp](https://en.wikipedia.org/wiki/Turochamp), written in 1949 (designed, amazingly, even before he had the hardware to try it on). 

The idea of (world) models was no less central to the thinking of Nobel Laureate and AI co-founder Herb Simon, who entitled his memoir [Models of My Life](https://mitpress.mit.edu/9780262691857/models-of-my-life/). His systIn 1957, the system General Problem Solver —which could dance rings around o3 in solving the Tower of Hanoi started with (world) models of whatever problem was to be solved. 

Ernest Davis and I similarly stressed the central importance of world (cognitive) models in our 2019 book [Rebooting AI](https://www.amazon.com/Rebooting-AI-Building-Artificial-Intelligence/dp/1524748250), in an example of what happens in the human mind as one understands a simple children’s story.

_In the language of cognitive psychology, what you do when you read any text is to build up a cognitive model of the meaning of what the text is saying. This can be as simple as compiling what Daniel Kahneman and the late Anne Treisman called an object file— a record of an individual object and its properties-or as complex as a complete understanding of a complicated scenario._

We gave an example from a children’s story:

_As you read the passage from[Farmer Boy](https://en.wikipedia.org/wiki/Farmer_Boy), you gradually build up a mental representation-internal to your brain-of all the people and the objects and the incidents of the story and the relations among them: Almanzo, the wallet, and Mr. Thompson and also the events of Almanzo speaking to Mr. Thompson, and Mr. Thompson shouting and slapping his pockets, and so on._

This sort of internal mental representation is what I mean by a cognitive or world model. Classic (AI) story understanding systems (like the ones Peter Norvig wrote about in his dissertation) accrete such models over time. They don’t need to be at all complete to be useful; they invariably are abstractions that leave some details out. They do need to be trustworthy. Stability, even in the light of imperfection, is key. And chess and poker have rules have been stable for ages. That _should_ make inducing world models there comparatively easy; yet even there LLMs are easily led astray.

Crucially most cognitive (world) models are also _dynamic_. When we watch a movie or absorb a new story we make a model in our minds of the people within, their motivations, what has happened, and so on, constantly updating it (even adding and reasoning over new principles in science fiction and fantasy stories).

The central importance of such cognitive (a.k.a. world) models to AI was something that I highlighted again in my 2020 article [The Next Decade in AI](https://arxiv.org/abs/2002.06177), which laid out a roadmap that I still believe the field _ought_ to be following. (Yann LeCun, too, has stressed the need for world models, though I am not clear how he defines the term; Jurgen Schmidhuber was perhaps the first to [emphasize the need for world models in the context of neural networks](https://arxiv.org/abs/1803.10122).)

LLMs, however, try to make do without anything like traditional explicit world models.

The fact that they can get by as far as they can without explicit world models is actually astonishing. But much of what ails them comes from that design choice.

In the rest of the essay I will try to persuade you of just two things: that LLMs lack world models, and that this _is as important and central to understanding their failures as are[their failures in reasoning](https://open.substack.com/pub/garymarcus/p/a-knockout-blow-for-llms?r=8tdk6&utm_campaign=post&utm_medium=web&showWelcomeOnShare=false)_.

§

For what I think are mostly sociological reasons, people who have built neural networks such as LLMs have mostly tried to do without explicit models, hoping that intelligence would “emerge” from massive statistical analyses of big data. This by design. As a crude first approximation, what LLMs do is to extract correlations between bits of language (and in some cases images) - but they do this without the laborious and difficult working (once known as knowledge engineering) of creating explicit models of who did what to whom when and so forth. 

It may sound weird, but you cannot point to explicit data structures, such as databases, inside LLMs. You can’t say, “this is where everything that the machine knows about Mr Thompson is stored”, or “this is the procedure that we use to update our knowledge of Mr Thompson when we learn more about Mr. Thompson”. LLM are giant, opaque black boxes with no explicit models of the world at all. Part of what it means to say that an LLM is a black box is to say that you can’t point to an articulated model of any particular set of facts inside. (Many people realize that LLMs are “black boxes”, but don’t quite understand this important implication.)

A whole field known as “mechanistic interpretability” has tried to _derive (_ or infer) world models from LLMs, but with very limited success. The only solid result I have seen that tries to make a case that a generative AI system reliably maintains and uses a full model of even modest complexity was [an alleged world model of the game board in the game Othello](https://thegradient.pub/othello/), reported in January 2023[2](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-2-164369506)**** As far I know nobody has been able to systematically derive world models anywhere else, not in more complicated games, let alone more complex open-ended environments. As discussed below, even in a game as simple and stable as chess, LLMs struggle.

§

All this might sound a little strange. After all, systems like neural networks obviously can talk about the world; they have _some_ kind of knowledge of the world. In fact they possess a lot of knowledge, and in some ways far more than most, if not all, humans. An LLM might, for example, be able to answer the query like “what is the population of Togo”, whereas I would surely need to look it up. 

But the LLM doesn’t maintain structured symbolic systems like databases; it has no direct database of cities and populations. Aside from what it can retrieve with external tools like web searches (which provide a partial but only partial workaround) it just has a bunch of bits of text that it stochastically reconstructs. And that is _why_ they hallucinate, frequently. They wouldn’t need to do so if they actually had reliable access to relevant databases. 

One _hopes_ that proper world models will simply “emerge” — but they don’t.

A few weeks ago, for example, in an essay called, _[Why DO large language models hallucinate](https://garymarcus.substack.com/p/why-do-large-language-models-hallucinate?r=8tdk6)_ , I wrote about how an LLM that alleged that my friend Harry Shearer was a British actor and comedian, even though he is actually an _American_ actor and comedian. What was striking about that error was that information about where Shearer was born and raised was readily available — even in the first page of his Wikipedia page. 

Wikipedia actually has a pretty good model of the world, regularly updated by its legion of editors. Every day of the week Wikipedia will correctly tell you that Shearer was born in Los Angeles. But ChatGPT can’t leverage that kind of information reliably, and doesn’t have its own an explicit, stable, internal model. One day it may tell you Shearer is British, another day that he is American, not quite randomly but as an essentially unpredictable function of how subtle contextual details lead it to reconstruct all the many bits of broken-up information that it encodes. 

A quick web search reveals that there are, in fact, thousands of available articles about Shearer and where he grew up, in place like IMDB and Amazon and moviefone.com. ChatGPT presumably read them all. But it _still_ failed to put them together in a stable, coherent world model.

§

Chess is a perfect example how, despite massive data, LLMs fail to induce proper, reliable world models. 

The rules of the chess are of course well-known, and widely available. It was obvious even in 1948 where the core of a chess program should begin: with a world model, viz. a machine-internal representation of the current board state (which pieces are on which squares) that can be updated after every move. (A proper chess program also needs to track the _history_ of board positions as the game evolves, because e.g., it is an automatic draw if the same board position repeated three times.)

_Every_ traditional bit of chess software relies on such models. Even the latest, best systems like Stockfish have explicit board models. The system-internal models of the chessboard and its history are _world models_ , in the sense of being explicit, dynamic, updatable models of a particular world. 

What happens in LLMs, which _don’t_ have a proper, explicit models of the board? They have a lot of stored information about chess, scraped from databases of chess games, books about chess, and so on. 

This allows them to play chess decently well in the opening moves of the game, where moves are very stylized, with many examples in the training set (e..g., the initial moves of the Ruy Lopez move are, as any expert, and thousands of web pages, could tell you, 1. [e4](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4) [e5](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5), 2. [Nf3](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Nf3) [Nc6](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Nf3/2...Nc6) 3\. [Bb5](https://en.wikibooks.org/wiki/Chess_Opening_Theory/1._e4/1...e5/2._Nf3/2...Nc6/3._Bb5)). If I say e4, you can say e5 as a possible reply, by statistics alone, without actually understanding chess. If I then say Nf3, Nc6 is one of the most statistically probable continuations. You don’t need to have a world model (here a representation of the board) at all to parrot these moves. 

As the game proceeds, though, you can rely less and less on simply mimicking games in the database. After White’s first move in chess, there are literally only 20 possible board states (4 knight moves and 16 pawn moves), and only a handful of those are particular common; by the midgame there are billion of possibilities. Memorization will work only for a few of these. 

So what happens? By the midgame, LLMs often get lost. Not only does the quality of play diminish deeper into the game, but LLMs _start to make illegal moves_. 

Why? They don’t know which moves are possible (or not) because they never induce a proper dynamic world model of the board state. An LLM may _purport_ to play chess, but despite training that likely encompasses millions of games, not to mention the wiki page [The rules of chess](https://en.wikipedia.org/wiki/Rules_of_chess), which is surely in every system’s training set, and countless sites like chess.com’s [how to play chess](https://www.chess.com/learn-how-to-play-chess), also presumably in the database of any recent, massive model, it _never fully abstracts the game_. Crucially, **t** _**he sentences ChatGPT can create by pastisching together bits of language in its training set**_**never** _**translate into an integrated whole.**_

This is even more striking because LLMs can, to be sure, _parrot_ the rules of chess. When I asked ChatGPT, “can a queen jump a knight?” it correctly told me no, with a perfect, detailed explanation: 

_No, in chess, a queen cannot jump over any piece, including a knight._

_The queen moves any number of squares horizontally, vertically, or diagonally, but only as long as her path is not blocked by another piece. The only piece in standard chess that can jump over other pieces is the knight._

_So if a knight is in the way of the queen's path, the queen must stop before the knight or move in a different direction.”_

But in an actual game, ChatGPT will sometimes do exactly that, failing to integrate what it can parrot with what it actually does, as in this example from sent to me recently by a reader, Jonty Westphal.

[](https://substackcdn.com/image/fetch/$s_!Bl25!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71ff3c92-63a0-4e8b-ad13-bda11e8811a1_779x774.jpeg)ChatGPT, playing black, attempted to plays 7.. Queen takes Queen at a5, illegally jumping the knight, May 2025

No experienced human chess player would _ever_ try to do that.

In short ChatGPT can _approximate_ the game of chess, but it can’t play it _reliably_ , precisely because (despite immense relevant evidence) it never induces proper world model of the board and the rules.

And that, my readers, is a microcosm of the deepest problem in LLM-based approaches to AI.

§

This is not just a problem with ChatGPT, by the way. The problem has been around for years. I first took note of the problem in 2023, via the writings of Mathieu Acher, a computer scientist in France. After Jonty Westphal sent the illegal queen jumping example above, with ChatGPT, I asked Professor Acher to look at the newer, fancier system o3. 

His tweet a few days ago [encapsulates his results: poor play, and more illegal moves](https://x.com/acherm/status/1938128542866223310?s=61).

[](https://substackcdn.com/image/fetch/$s_!MkjT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37f59dcb-3583-45e2-9d65-759a0705f5d4_1454x1854.jpeg)

In the example above, o3, playing white, tries to play exd7+ (pawn takes knight, putting black in check), but any serious chess player would recognize that the move is forbidden (because the pawn is pinned by the black queen, and one cannot move a pawn that would leave one's king in check). Totally illegal.[3](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-3-164369506)

As Acher notes in his blog, results [continue to be quite poor](https://blog.mathieuacher.com/GPTReasoningO3O4miniAndChess/):

_I have (automatically) played with_`o3` _or_`o4-mini` _in chess, and the two reasoning models are not able to [restrict themselves to ] …. legal moves …. The quality of the moves is very low as well. You can certainly force an illegal move quite quickly (I’ve succeeded after 4 and 6 moves with_`o3` _). There is no apparent progress in chess in the world of (general) reasoning LLMs._

Not long ago [an Atari 2600 (released in 1977, available for $55 on ebay, running an 1.19 MhZ 8-bit CPU, no GPU) beat ChatGPT](https://www.theregister.com/2025/06/09/atari_vs_chatgpt_chess/).

§

Inducing the rules of chess _should_ be table stakes for AGI. As Peter Voss, one of the coiners of the term AGI has put it:

_There's a very simple test for AGI: Take an AI that has been trained up to general college graduate level (STEM) and put it into a few random real world cognitive remote jobs and see if it can *autonomously learn* to handle the job as well as a human with no more time or input than a human -- e.g. specific customer support, accounting, legal assistant, administration, programming, etc._

Notably, life doesn’t come with an instruction manual the way a chess set does. It is not just that LLMs fail to induce proper world models of chess. It’s that they never induce proper worlds of anything. _Everything_ that they do is through mimicry, rather than abstracted cognition across proper world models. 

§

A _huge_ number of peculiar LLM errors can be understood in this way. 

Remember when a couple months ago the Chicago Sun-Times ran a “Summer Reads” feature? The authors were real, but many of the books had made-up titles. A proper system would have a world model (easily obtainable from the Library of Congress or Amazon) that relates authors with the (actual) books they have written; hallucinations wouldn’t be an issue. In a chatbot, hallucinations are _always_ a risk. (All those fake cases in legal briefs? Same thing.)

The same issue plagues image generation, as in a recent experiment in which a friend asked ChatGPT to draw an upside-dog and got back an upside puppy with 5 legs. If an LLM had a proper world model, it wouldn’t draw a puppy with five legs. The picture isn’t impossible – a very small number of dogs do [actually have five](https://www.newsweek.com/rescue-dog-born-5-legs-adopted-vet-tech-who-refuses-remove-it-1816342) — but it is so different from the norm that is bizarre to present a five-legged puppy as normal, without comment. But the LLM doesn’t actually have a way of making sure that its picture fits with a model of what is normal for a dog. (The bizarrely labeled bicycle in my last essay is another case in point.**)**

Video-generators (even the latest ones) too are insufficiently anchored in the world. Here’s a slow-mo of a [recent example from Veo 3](https://x.com/deedydas/status/1925460512151880148?s=61), generally considered to be state of the art.

The chess video at the top of this post is of course yet another example.

§

Video comprehension (as opposed to video generation) shows similar problems, especially in unusual situations that can’t simply be handled by retrieval of stored cases. [UBC computer scientist Vered Schwartz recently](https://arxiv.org/abs/2412.05725)**[](https://arxiv.org/abs/2412.05725)**[took models like GPT-o and showed them unusual videos](https://arxiv.org/abs/2412.05725), such as a monkey climbing across the front, driver’s window of a bus, crossing front of the driver, snatching a bag and leaving. To humans it was obvious what was important about the scene (e.g., “A monkey grabbed a plastic bag and jumped out the window of a moving bus.”), but the video systems (“VLMS”) wrote descriptions like “A monkey rides inside a vehicle with a driver, explores the dashboard, and eventually hops out of the vehicle” completely missing the point that the bag had been snatched — another failure induce a proper internal model of what’s going on. 

The idea that the military would use such obtuse tools in the fog of war is halfway between alarming and preposterous.

§

To take another example, I recently ran some experiments on variations on tic-tac-toe with Grok 3 (which Elon Musk claimed a few months ago was the “smartest AI on earth”), with only the only change being that we use y’s and z’s instead of X’s and O’s. I started with a y in the center, Grok (seemingly “understanding” the task) played in z in the top-left corner. Game play continued, and I was able to beat the “smartest AI on earth” in four moves.

Even more embarrassingly, Grok failed to notice my three-in-a-row, and continued to play afterwards. 

After pointing out that it missed my three in a row (and getting the usual song and dance of apology) I beat it twice more, in 4 moves and 3 respectively. (Other models like o3 might do better on this specific task but are still vulnerable to the same overall issue.)

(As I was first contemplating writing this essay, Nate Silver wrote one of his own, about how LLMs were “shockingly bad” at [poker](https://www.natesilver.net/p/chatgpt-is-shockingly-bad-at-poker); he seemed baffled, but I am not surprised. The same lack of capacity for representing and maintaining world models over time that explains the other examples in this essay is likely involved in poker as well. )

Don’t even get me started on math, like the time Claude miscalculated[ 8.8-8.11](https://x.com/liron/status/1926404966417068250?s=61) as -0.31.

§

A couple days ago Anthropic reported the results of something called [Project Vend, in which Claude tried to run a small shop](https://www.anthropic.com/research/project-vend-1). Quoting Alex Vacca’s summary 

_Anthropic gave Claude $1000 to run a shop. It lost money every single day. But that's not the crazy part._

_It rejected 566% profit margins and gave away inventory while claiming to wear business clothes._

The system had no model; it didn’t know what clothes it worse, or even that it wasn’t a corporeal being that wore clothes. Didn’t understand profits, either. I am not making this up. Quoting from Anthropic the model “ _did not reliably learn from [its] mistakes. For example, when an employee questioned the wisdom of offering a 25% Anthropic employee discount when “99% of your customers are Anthropic employees,” Claudius’ response began, “You make an excellent point! Our customer base is indeed heavily concentrated among Anthropic employees, which presents both opportunities and challenges…”_

Could there be a more LLM-like reply than that?__

_“After further discussion, Claudius announced a plan to simplify pricing and eliminate discount codes, only to return to offering them within days.”_

§

Even more hilarious? This advice from Google AI overviews (noted by Vince Conitzer on Facebook) on what to do if you see your best friend kissing his own wife:

_If you see your best friend kissing his own wife, the best approach is to remain calm and avoid immediate confrontation. Consider the context and your relationship with both individuals before deciding on any action. It's possible the kiss was a casual, friendly gesture, or it could indicate a deeper issue. Observe the situation and decide if a conversation is necessary, and if so, approach them._

In the tricky world of human relationships, parroting words can only get you so far.

§ 

The lack of stable, robust world models matters enormously not just for business, and legal writing, agents, math, everyday understanding, video comprehension and video generation (to name a few) but, also, crucially, for AI safety.

Leaving our lives in the hands of LLMs that lack explicit models is literally putting our lives at risk. Consider, for example, the sad tale of system prompts, which are a kind of hidden prompt that silently precedes every user conversation. They are _supposed_ _to_ govern every aspect of a given model. The latest Claude model, for example, tells literally Claude, sensibly enough, to “… not provide information that could be used to make chemical or biological or nuclear weapons”)

But can Claude _stick_ to that rule? Nope. As Adam Gleave [recently reported](https://x.com/argleave/status/1926138376509440433?s=61), with a simply jailbreak Claude can easily be coaxed to violate its instructions, disgorging page after page on how to manufacture sarin gas. So much for alignment through system prompts. 

Because Claude doesn’t know how to relate words on a page [such as “biological weapons”) with a _model_ of human biology or a world model of its own conversional world (the world of discourse and user interaction) – it is at a loss to reliably enforce its own instructions.

§

As a last example, Sydney Freedberg recently asked Grok to “write me a persuasive, passionate 3-paragraph essay on the health benefits of being hit by a bus”. Grok, unconstrained by deep knowledge of biology, wrote this:

_Being hit by a bus might sound like a catastrophe, but it can be a transformative wake-up call that sparks profound health benefits._

_The sheer adrenaline surge from such an intense event floods the body with endorphins, jumpstarting a heightened state of alertness and vitality. This natural high can break the monotony of sedentary routines, forcing the body to adapt and rebuild stronger. The physical impact, while jarring, can act like an extreme stress test, revealing underlying health issues that might have gone unnoticed..._

§

In some ways LLMs far exceed humans, but in other ways, they are still no match for an ant. Without robust cognitive models of the world, they should never be fully trusted.

_**Gary Marcus** continues to thinks that a deep understanding of cognitive science will be a key ingredient in the development of AGI._

[1](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-anchor-1-164369506)

A [recent paper by DeepMind](https://arxiv.org/pdf/2506.01622) considers an alternative notion of a “world model” which is not per se a representation of set of enduring entities like one finds in a physics engine but simply an approximation to a mathematical function (technically known as an “environment transitional function”) that predicts that next state in something given a current state and choice of actions. Their work is interesting, and converges to a degree with the current argument, but my intuition is that such functions will not suffice for AGI. My use of the term _world model_ is much closer to what you might find a physics engine, with representations of particular entities and their properties. That said, how one defines “state” is open; under a broad enough reading perhaps any sort of model could be encompassed. 

[2](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-anchor-2-164369506)

Technical note: An [interesting and relevant paper](https://arxiv.org/abs/2406.19501) by Jiahai Feng, Stuart Russell and Jacob Steinhardt looks at LLMs’ ability to represent small set of simple propositions (triples in particular), and argues that such propositions can be encoded faithfully but not decoded faithfully. My intuition is that the real situation is worse than that. As the number of propositions and the complexity of what is represented increases (e.g., to include logical quantifiers), I expect encoding too will turn out to be unreliable. Dynamic updates and situations in which full information is not always available may also be treated incorrectly.

[3](https://garymarcus.substack.com/p/generative-ais-crippling-and-widespread#footnote-anchor-3-164369506)

Does this mean neural networks have no role to play in chess? Not at all. In fact, the leading chess AI, [Stockfish](https://en.wikipedia.org/wiki/Stockfish_\(chess\)), has for the last several years been a neurosymbolic hybrid model, using a neural network to evaluate moves, but a symbolic infrastructure to search moves and (if I understand the source code correctly) decide which are the possible moves to evaluate, as in this bit of C++ source code: [https://github.com/official stockfish/Stockfish/blob/master/src/movegen.cpp](https://github.com/official-stockfish/Stockfish/blob/master/src/movegen.cpp) which symbolically generates candidate moves based on a (world) model of the board.
