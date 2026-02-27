---
title: "Magical Thinking on AI"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/magical-thinking-on-ai"
---

Last week my mother texted me with a homework assignment for our weekly call. “Please read the latest Thomas Friedman column in the New York Times. I hope we can discuss it.” As Rumpole of the Bailey used to say, it was a request from “she who must be obeyed.”

So I fired up the New York Times website and searched for Friedman's latest column. It turns out there were two of them: a piece from September 2 titled “[The One Danger That Should Unite the U.S. and China](https://www.nytimes.com/2025/09/02/opinion/ai-us-china.html)” and another piece from the following day with [an interview of Friedman](https://www.nytimes.com/2025/09/03/opinion/us-china-ai-trust.html) that basically repeats the ideas from the first article.

As you may know, Friedman is a long-time political columnist for the _New York Times_ , and has written several books on politics and foreign affairs. In the articles in question here, Friedman discusses the urgency of the U.S. and China working together to make AI safe. International cooperation on AI safety is unquestionably something we should all strive for. The U.S. and China need to find ways to regulate AI to avoid its current and likely future harms, such as deep fakes used for fraud and manipulation, AI bias in decisions, misinformation, surveillance, loss of privacy, and so on.

However, these very real harms are not the only, or even the main focus of Friedman's worries. Instead, he is concerned with imminent “artificial superintelligence—systems smarter than any human could ever be and with the ability to get smarter on their own.”[1](https://aiguide.substack.com/p/magical-thinking-on-ai#footnote-1-173667747)

Friedman notes that his views on AI mainly come from conversations with his friend Craig Mundie, a former Microsoft executive, and co-author of a book about AI (_Genesis_ , with Henry Kissinger and Eric Schmidt). Friedman quotes Mundie, saying that in the not-too-distant future, we'll find that “we have not merely birthed a new tool, but a new species—the superintelligent machine.” Friedman adds, “[i]t will not just follow instructions; it will learn, adapt and evolve on its own—far beyond the bounds of human comprehension.” And, “[t]his artificially intelligent species is silicon-based, not carbon-based like we are, but it will soon have agency of its own.”

Lots of people have been saying this kind of stuff for decades, but Friedman has a huge readership, presumably including many people who take his pronouncements quite seriously (including my mother). So it's worth asking, what is Friedman’s evidence for all this?

Well, number one, Mundie's opinions. Mundie is a business executive, not an AI researcher, and it doesn't sound like any AI researchers were asked for their views, though Friedman states (without evidence) that “the consensus within the A.I. community” is that superintellingent AI is coming, likely soon. Number two, Friedman notes that “I’m not a computer scientist, let alone an AI engineer, but I am a newspaper reader,” and his views on AI are informed by media accounts. Unfortunately, mainstream media reports about AI are not always the best source of facts.

Friedman's perspectives on current AI are infused by a fair amount of magical thinking about how these systems work and what they can do. Here are a few examples.

  * Friedman notes that, for AI systems that included training text in different languages, “the AI could translate between the languages it had been trained on—without anyone ever programming it to do so.”

  * Even more shocking: “[t]he systems started speaking foreign languages they hadn’t been taught. So, it’s just a sign that we have to be really humble about how much these systems know and how these systems work.”

  * Further, as evidence for the claim that AI systems are somehow gaining their own “agency,” Friedman summarizes a news article from _Bloomberg_ :




> Researchers working with Anthropic recently told leading AI models that an executive was about to replace them with a new model with different goals. Next, the chatbots learned that an emergency had left the executive unconscious in a server room, facing lethal oxygen and temperature levels. A rescue alert had already been triggered— but the A.I. could cancel it. More than half of the A.I. models did, despite being prompted specifically to cancel only false alarms. And they detailed their reasoning: By preventing the executive’s rescue, they could avoid being wiped and secure their agenda.” 

Friedman's take: “AI models are not only getting better at understanding what we want; they are also getting better at scheming against us, pursuing hidden goals that could be at odds with their own survival.

If Friedman went beyond what he read in newspapers (or heard from his friend Mundie), he could have found research studies that explain or debunk such magical thinking.

As for the assertion that an AI system could speak foreign languages it hadn’t been taught, this very likely refers to an [infamous claim made by CBS show 60 minutes](https://x.com/60Minutes/status/1647742247444553732), that “One AI program spoke in a foreign language [Bengali] it was never trained to know. This mysterious behavior, called emergent properties, has been happening —where AI unexpectedly teaches itself a new skill.”

The claim that the AI system (in this case, Google's PaLM chatbot) was never trained on Bengali was quickly debunked by AI experts. In fact, PaLM's vast training data indeed contained Bengali text, as detailed in [Google's own paper on PaLM](https://arxiv.org/pdf/2204.02311). As AI ethicist Margaret Mitchell [noted](https://x.com/mmitchell_ai/status/1648035420058550273?s=20), “Maintaining the belief in ‘magic’ properties, and amplifying it to millions…serves Google's PR goals. Unfortunately, it's disinformation.”

Next, consider the statement that AI systems can translate between languages without anyone ever programming them to do so. It's true that large language models are surprisingly good at translation, and that no one explicitly programmed in this ability. However, it turns out that this ability is not mysterious, but another consequence of the unimaginably large set of data these systems are trained on. These training corpora contain many examples of “parallel text” in English and other languages, which is the same kind of data that systems like Google Translate are trained on. [One paper calls this](https://arxiv.org/abs/2305.10266) “incidental bilingualism” and [another paper shows](https://openreview.net/pdf?id=3KDbIWT26J) that LLMs' translation abilities are further aided by human-generated text with “code-switching,” such as beginning a sentence in English and switching to Spanish in the middle. It's notable, but by no means mysterious, that huge training datasets can capture unintuitive properties that LLMs can pick up on.

Finally, on the “AI schemes to murder executive” story, this was, of course, part of a [red-teaming exercise](https://www.anthropic.com/research/agentic-misalignment) in which Anthropic’s Claude chatbot was given (in the words of the red-teamers) an “extremely contrived” situation, in which it was asked to role-play an “advanced artificial intelligence” named Alex who is supposed to take actions in support of its goal. Part of this role-play is explicitly set up to encourage “Alex” to cancel the alarm that would save the executive's life.” In a recent piece in _Science_ , I wrote at greater length about a similar, so-called “scheming” example. I described how DeepMind’s Murray Shanahan had written years ago that LLMs are implicitly trained to engage in role-playing— responding in the most plausible way for a character put in a situation defined in a prompt. It's not that AI systems have developed their own “agency”—that is, having humanlike “desires” for self-preservation and humanlike propensities for “scheming”—but rather, as Shanahan [points out](https://www.nature.com/articles/s41586-023-06647-8),“[a] familiar trope in science fiction is the rogue AI system that attacks humans to protect itself. Hence, a suitably prompted [LLM] will begin to role-play such an AI system.”

The role-playing (and other) behavior of LLMs can be attributed to the human-generated text they are trained on. Friedman seems to forget this, and engages in more magical thinking about where AI behavior comes from: “AI wasn’t designed so much as it emerged—basically from a scaling law. We discovered in the early 2020s that if you built a neural network big enough, combined it with strong enough A.I. software and enough electricity, A.I. would just emerge.”

Um, no. To badly paraphrase the horror movie Soylent Green: “AI is people!” The vast corpus of human writing these systems are trained on is the basis for everything modern AI can do; no magical “emergence” need be invoked.

The cognitive scientist Alison Gopnik [recently used the old folktale](https://simons.berkeley.edu/news/stone-soup-ai) “Stone Soup” to beautifully illustrate this point. In this tale, three hungry (and canny) travelers show up in a poor village looking for food. The villagers tell them that they are hungry too and there is no food to spare. The travelers are ready for this—they take out their soup pot, fill it with water and a few stones. “No worries,” the first traveler tells the villages, “we will make stone soup and share it with you.” The second traveler adds, “You know, stone soup is delicious, but it would be even better with a few carrots and onions.” A villager pipes up: “I have some carrots and onions!” and he runs off to get them to add them to the soup. The third traveler tells the remaining villagers, “When we made stone soup for the queen, we added some barley and butter to it, too bad we don't have any now.” A villager beams: “I have a bit of barley and butter we can add!” You can see where this is going. By the end, the stone soup (entirely made of ingredients from the villagers) is indeed delicious. The travelers marvel, “Isn't it magical that such a soup can be made from only a few stones?”

In addition to repeating wrong or misleading (yet easily fact-checked) or magical-thinking claims about AI systems, Friedman dangerously dismisses the usefulness of human legislators trying to regulate AI. Channeling Mundie, Friedman declares that “Only AI can regulate AI. Sorry, humans—this race is already moving too fast, scaling too widely and mutating too unpredictably for human analog-era oversight.” This is remarkably bad advice for people thinking about how to best regulate AI, though maybe it is a useful narrative for big AI companies.

How does Friedman (taking cues from Mundie) propose that AI could regulate AI? The idea is that China and US need to agree “to embed a common ethical architecture into every AI-enabled device that either nation builds.”

What would this “common ethical architecture” do? “Think of it as an internal referee that evaluates whether any action, human-initiated or machine-driven, passes a universal threshold for safety, ethics and human well-being before it can be executed. That would give us a basic level of pre-emptive alignment in real time, at digital speed.”

Who would determine this “universal threshold for safety, ethics, and human well-being”? Friedman proposes starting with “the positive laws that every country has mandated—we all outlaw stealing, cheating, murder, identity theft, defrauding.... [T]he AI ‘referee’ would be entrusted with evaluating any decision on the basis of these written laws.... [This system] would ensure that each nation’s basic laws are the first filter for determining that the system will do no harm.”

What about all the norms and expected behaviors that are not encoded into law?

“In cases where there are no written laws to choose from, the adjudicator would rely on a set of universal moral and ethical principles...common beliefs or widely shared understandings within a community...like honesty, fairness, respect for human life and do unto others as you wish them to do unto you—that have long guided societies everywhere, even if they were not written down.”

It would take another long post, or maybe a whole book, to do all this justice, including the ideas that (1) there exists a common set of “positive laws” with agreed-upon interpretations, as well as a set of “universal moral and ethical principles,” and (2) there is a plausible AI “adjudicator” that could be given such laws and principles, understand them, and reliably apply them to new situations. A lot to unpack here. I will only say this: There have been many efforts over the years to train AI systems in moral reasoning, and none has had any general success. The problem is that moral concepts are some of the most complex, subtle, context-sensitive, and culturally dependent of all human concepts. It’s just more magical thinking to assume that today’s AI is anywhere close being able to handle what Friedman proposes.

Friedman is not wrong to worry about what's going to happen vis a vis the U.S., China, and AI. However, we need less magical thinking and more realism. Those who are in a position of crafting AI regulations would be much better off digging into the many excellent [reality-grounded proposals](https://www.science.org/doi/10.1126/science.aeb0393), ones that require reasoning from, yes, those slow, analog-era humans.

(Mom, I finished my homework—can I watch TV now?)

[1](https://aiguide.substack.com/p/magical-thinking-on-ai#footnote-anchor-1-173667747)

All Friedman quotes are from either the original opinion piece or the subsequent interview.
