---
title: "What does Meta AI’s Diplomacy-winning Cicero Mean for AI?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/what-does-meta-ais-diplomacy-winning"
---

> “The distinguishing property of humans is to search for and to follow after truth.”
> 
> – Cicero

Cicero the human being (106-43 BC) was a celebrated politician, an orator, and a writer; his historical and philosophical importance is still debated two thousand years later. Cicero the computer program, announced in [an article in Science](https://www.science.org/doi/10.1126/science.ade9097) on November 22, is a powerful AI system that plays Diplomacy; its implications for AI are not yet clear three days later, and may not be for a long time.

Diplomacy, a complex game that requires extensive communication, has been recognized as a challenge for AI for at least [fifty years](http://www.bitsavers.org/pdf/mit/ai/aim/AIM-250.pdf). To win, a player must not only play strategically, but form alliances, negotiate, persuade, threaten, and occasionally deceive. It therefore presents challenges for AI that are go far beyond those faced either by systems that play games like Go and chess or by chatbots that engage in dialog in less complex settings. 

The results themselves are, without question, genuinely impressive. Although the AI is not yet at or near world champion level, the system was able to integrate language with game play, in an online version of blitz Diplomacy, ranking within the top 10% of mixed crowd of professional and amateurs, with play and language use that were natural enough that only one human player suspected it of being a bot. 

Lots of questions arise: How does it work? Does it have implications for other ongoing challenges in AI? Is it, as [Meta AI’s blog](https://ai.facebook.com/blog/cicero-ai-negotiates-persuades-and-cooperates-with-people/) claims, “a breakthrough toward building AI that has mastered the skills” of negotiation, persuasion, and cooperation with people”? How much of an advance is it toward a system that can actually interact intelligently with human beings in real situations? Do we have to worry that Meta has built an AI that can manipulate people to achieve its goal of world domination, as a friend of ours posted, perhaps half-seriously? Are we at some kind of newfound risk given that deception is involved? Meta AI, to its credit, has published the code for Cicero open-source so that the research community can begin to explore these questions.

In AI, it’s always hard to answer questions about implications without first looking at a system’s architecture. As it turns out, the architecture of Cicero differs profoundly from most of what’s been talked about in recent years in AI.

The first thing to realize is that Cicero is a very complex system. Its high-level structure is considerably more complex than systems like AlphaZero, which mastered Go and chess, or GPT-3 which focuses purely on sequences of words. Some of that complexity is immediately apparent in the flowchart; whereas a lot of recent models are something like data-in, action out, with some kind of unified system (say a Transformer) in between, Cicero is heavily prestructured, in advance of any learning or training, with a carefully-designed bespoke architecture that is divided into multiple modules and streams, each with their own specialization.

[](https://substackcdn.com/image/fetch/$s_!4pgs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F3fc424c2-f83e-4bbc-bbd7-ea7e0e854009_936x698.jpeg)

And that’s just the start of the complexity. Many of Cicero’s most important features, in terms of evaluating its overall significance, lie in details buried deep within the article’s [supplementary material](https://www.science.org/doi/suppl/10.1126/science.ade9097/suppl_file/science.ade9097_sm.pdf). Although we aim to spare you most of the detail, it is clear that understanding Cicero properly and answering these questions unavoidably requires a careful analysis. 

## How Cicero plays Diplomacy

The game of Diplomacy consists of a series of turns. In each turn, first all the players communicate privately, one-on-one; they can make secret alliances, negotiate terms, threaten repercussions, and so on. When the discussions are complete, they all privately decide on a move, and they announce their moves simultaneously. (The contest was a “blitz” version of the game, limited to five minutes a move, which favors computers, since the blitz version is presumably less dialogue- and negotiation-intensive than the full version of the game[; in a longer version of the game, humans may still dominate.](https://twitter.com/sir_deenicus/status/1595693780992139270?s=20&t=69KMAB1cRgiEhscj0HN7vQ))

At each move, Cicero must decide who it will talk to, and what it will say, and what move it will make at the end. Each of these decisions depend on the current state of play, including the past history both of play and of communications, and on what other players say to it during the current move.

Making the right decision here can get enormously complicated. If you are playing Diplomacy, what you should do as its next action obviously depends on what the other players are going do. And what they are going to do depends on what they think you are going to do. To make it more complicated, you can (hopefully) gauge what they are going to do by what they say and you can influence what they are going to do by what you say. But the choice of what you are going to say is determined by what you want them to do which circles back to the question of what you are going to do. 

Luckily for the Cicero team, game theory, first developed in the 1930s, and now very powerful, offered a strong starting point. The game theory literature figures prominently in how Cicero chooses its strategy. This was already well developed in Meta AI’s earlier work on a simplified version of Diplomacy that was non-linguistic. That in itself was impressive. But game theory is a theory of actions; it is not at all a theory of language. In the new work, the Cicero team had to combine game-theoretic strategizing with natural language technology that has been developed for purely linguistic tasks, such translation or question answering. Putting all this together into a coordinated whole was extremely challenging. We are frankly impressed that the Meta AI team pulled it off.

It was perhaps inevitable then that the architecture of Cicero during play consists of a collection of highly complex, interacting algorithms. We are not going to attempt to describe it fully here, but we see two key takeaways. The first is that Cicero’s overall architecture Is not something that simply emerged spontaneously from the basic data, but it is rather an exquisitely engineered structure with many moving parts, laboriously worked out by a broad team of different types of AI experts, combining techniques from game theory with probabilistic analysis.

The second takeaway is that Cicero leverages many different kinds of information in making its decisions. These include

· The current state of play in the game.

· The history of all the previous moves and all the previous dialogue

· Knowledge of language patterns, based on a purely linguistic model similar to GPT-3. This gives Cicero some idea of what is a reasonable way to respond to communications from the other players.

· Knowledge of how sentences are related to actions. This gives Cicero some idea of how to tell allies or prospective allies what it is planning to do.

· How much time (in seconds) passes between messages.

Importantly, although Cicero plays against humans, it doesn’t work in precisely the same ways as humans. For example, human players presumably try to categorize the mental state and the social interactions of the other players. “England wants Netherland to support Belgium”, “France thinks that Belgium is moving to Holland”, “If I threaten Germany then they may agree to support Holland or they may form a defensive alliance with Russia”,and so on. Cicero manages to succeed without directly formulating or representing these kinds of thoughts. (To take another example, because of the well-known tendency of LLMs to hallucinate, Cicero sends every proposed message~~~~ through a filter, to remove inappropriate, hallucinatory, or otherwise flawed utterances—a step that is presumably largely unnecessary for humans.)

## How Cicero is trained

Like virtually all other current practical AIs, the construction of Cicero makes substantial use of machine learning technology. The training data had a number of different parts, some of which involve substantial labor to create. The system ultimately relied on four classes of bespoke data, far more variegated than one finds in typical deep learning systems, with a fair amount of hand-constructed data (also rare in the deep learning world):

· A corpus of 125,300 human games played on the online platform (of these 40,400 included dialogue, with a total of 12,900,000 individual messages).

· A large language model that appears to have been trained on billions of words, further fine-tuned on the corpus of game dialogue.

· Thousands of expert-generated annotations, evaluating the quality of messages produced by a preliminary version of Cicero.

· A large collection of synthetic data sets, many of which were hand-constructed, for training various modules. For instance, to train the filter that excludes invalid messages, they created a hand-constructed collection of invalid messages. Another data set trained Cicero out of its propensity to miscount the entities on the board; still another was designed to improve its understanding of negation. A corpus of games of self-play was used for reinforcement learning, and so on.

With that carefully-engineered data all in hand, the system needed to learn what messages in language mean in terms of game actions; it needed to learn, for example, that the sequence of words “Do you want to support Netherlands in Belgium?” means the action marked in the game play as “NTH S BEL”. To do this, Cicero made the assumption that, generally speaking, the sentences in the dialogue between A and B referred to the actions which A and B carried out at the end of the dialogue. (Cleverly, the system looked in the later conversation for claims of dishonesty. If B said to A at some point “You lied to me last turn”, then that indicated that A’s statements to B on the previous turn should not be annotated with A’s actual move.)

Getting all this to work together is amazing.

## Scope and Limits

Cicero is in many ways a marvel; it has achieved by far the deepest and most extensive integration of language and action in a dynamic world of any AI system built to date. It has also succeeded in carrying out complex interactions with humans of a form not previously seen.

But it is also striking in _how_ it does that. Strikingly, and in opposition to much of the Zeitgeist, Cicero relies quite heavily on hand-crafting, both in the data sets, and in the architecture; in this sense it is in many ways more reminiscent of classical “Good Old Fashioned AI” than deep learning systems that tend to be less structured, and less customized to particular problems. There is far more innateness here than we have typically seen in recent AI systems

Also, it is worth noting that some aspects of Cicero use a neurosymbolic approach to AI, such as the association of messages in language with symbolic representation of actions, the built-in (innate) understanding of dialogue structure, the nature of lying as a phenomenon that modifies the significance of utterances, and so forth.

That said, it’s less clear to us how generalizable the particulars of Cicero are.

§

So far as we know, Cicero has been tested only on the single task, the very task that it was carefully crafted to do: playing blitz Diplomacy. It could not be immediately applied to the challenge of, say, customer service or guiding the actions of a domestic robot, or well, almost anything else, really. Even within the world of Diplomacy, the scope is somewhat limited. Human players for example can probably cope well when with an alternative board (the map of Europe as of 1400, say)) or with [slightly revised rules for actions](http://www.diplom.org/Online/variants.html) (e.g. forces that could travel by air rather than just land or sea ). In Cicero, there is no simple way to “present” any such rule or map changes, and its training is very heavily tied bound to the language describing actions specifics of the standard Diplomacy board; how much would carry over is unclear. Our best guess is that if you played Diplomacy with alternative rules, the system would like to have retrained almost from scratch,

And there is no easy way to retrain Cicero. If you wanted to build a version of AlphaZero that plays on a 20x20 Go board, that can be done with very little new human labor, since AlphaZero is trained entirely on self-play. With Cicero, you would have to wait until humans had played 125,000 games to retrain on, before you could get on with the experiment.

None of this suggests an easy road adapting Cicero to other tasks. The critical question that arises, as is so often the case in AI, is, to what extent do the techniques that have been used in Cicero generalize to other situations involving action and social interactions? What aspects of Cicero’s execution architecture, training architecture, or general methodological approach will be useful if we want to build an AI that is useful for some complex interaction with people outside the closed and limited world of Diplomacy? The system is complex enough that we can’t predict this with any great confidence, but as things stand now, the prospects for generalization seem to us to be somewhat limited; the style of work might well be useful in other problems, but it may be that not much of the specifics of the architecture would survive if the system were applied to other problems, such as bidding in games like bridge, , or negotiating a work schedule for a team working on a project, or planning a wedding.

## What does Cicero’s success indicate about AI in general?

Cicero makes extensive use of machine learning, but is hardly a poster child for simply making ever bigger models (so-called “scaling maximalism”), nor for the currently popular view of “end-to-end” machine learning of in which some single general learning algorithm applies across the board, with little internal structure and zero innate knowledge. At execution time, Cicero consists of a complex array of separate hand-crafted modules with complex interactions. At training time, it draws on a wide range of training materials, some built by experts specifically for Cicero, some synthesized in programs hand-crafted by experts.

The same day that Cicero was announced, there was a [friendly debate at the AACL conference](https://aclanthology.org/2022.aacl-main.0.pdf) on the topic "Is there more to NLP [natural language processing] than Deep Learning,” with four distinguished researchers trained some decades ago arguing the affirmative and four brilliant young researchers more recently trained arguing the negative. Cicero is perhaps a reminder that there is indeed a lot more to natural language processing than deep learning.

Our final takeaway? We have known for some time that machine learning is valuable; but too often nowadays ML is a taken as universal solvent—as if the rest of AI was irrelevant—and left to do everything on its own. Cicero may change that calculus. If Cicero is any guide, machine learning may ultimately prove to be even more valuable if it is embedded in highly structured systems, with a fair amount of innate, sometimes neurosymbolic machinery.

[Share](https://garymarcus.substack.com/p/what-does-meta-ais-diplomacy-winning?utm_source=substack&utm_medium=email&utm_content=share&action=share)
