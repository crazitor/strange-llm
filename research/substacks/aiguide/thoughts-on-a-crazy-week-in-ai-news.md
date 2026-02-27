---
title: "Thoughts on a Crazy Week in AI News"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/thoughts-on-a-crazy-week-in-ai-news"
---

This last week I intended to keep my head down and finish a paper related to the [Abstraction and Reasoning Corpus](https://aiguide.substack.com/p/why-the-abstraction-and-reasoning)—I’ll write about that paper here soon. But like everyone else interested in AI, I got hopelessly distracted by the week’s crazy news onslaught. And I’m not talking about the Trump indictment.  
  
The topic of the week was what, exactly, we should be worried about with respect to recent progress in systems like ChatGPT and GPT-4. The discussion was a head-spinning potpourri of prosaic ethical concerns blended with anxious hype, with a dash of apocalyptic doom. Here’s some of what happened, and some thoughts.   
  
**1\. The Senator  
**  
The week of AI weirdness began for me with Connecticut Senator Chris Murphy, a politician I have long admired and follow on Twitter. Not one to usually opine about AI, he had obviously seen something that really disturbed him. He [tweeted](https://twitter.com/ChrisMurphyCT/status/1640186536825061376), “ChatGPT taught itself to do advanced chemistry. It wasn’t built into the model. Nobody programmed it to learn complicated chemistry. It decided to teach itself, then made its knowledge available to anyone who asked. Something is coming. We aren’t ready.”  
  
My mind reeled at Murphy’s seeming lack of understanding of what actually happened with ChatGPT. ChatGPT doesn’t “teach itself” or “decide to teach itself.” There is no intentional agent inside of the chatbot that decides to do anything. The system is designed to create a statistical model of the text in its training data. Moreover, saying that “advanced chemistry” wasn’t built into the model isn’t at all correct; lots of text related to chemistry was part of its training data.  
  
My finger raced of its own accord to the “reply” button. I [tweeted](https://twitter.com/MelMitchell1/status/1640342924486643712), “Senator, I’m an AI researcher. Your description of ChatGPT is dangerously misinformed. Every sentence is incorrect. I hope you will learn more about how this system actually works, how it was trained, and what it’s limitations are.”  
  
I wish I had worded this more politely (not to mention spelled “its” correctly), but...Twitter.   
  
To my astonishment, my reply ended up garnering more “likes” than anything I’ve ever tweeted before, as well as an avalanche of replies, both strongly supportive and whatever the polar opposite of “strongly supportive” is. Several other AI researchers replied as well, in a similar vein to my reply, including, prominently, the computer scientist and policy expert [Suresh Venkatasubramanian](https://twitter.com/geomblog).

The Twitter exchange was picked up by several media outlets, including _[The Daily Beast](https://www.thedailybeast.com/senator-chris-murphys-chatgpt-tweet-is-proof-lawmakers-arent-ready-for-the-ai-boom)_ and _[Venture Beat](https://venturebeat.com/ai/sen-murphys-tweets-on-chatgpt-spark-backlash-from-former-white-house-ai-policy-advisor/)_. Murphy was angry, responding over several tweets, “I get it—it’s easy and fun to terminology shame policymakers on tech.” “Of course I know that AI doesn’t ‘learn’ or ‘teach itself’ like a human. I’m using shorthand. And I’m not talking about AI going rogue and destroying humanity.” and “The intent is to bully policymakers away from regulating new technology by ridiculing us when we don’t use the terms the industry uses.”   
  
This made me feel terrible, and somewhat angry. I and the other people who responded to Murphy’s original tweet did so because we were alarmed by an important political leader communicating fear-mongering and false claims about AI to his one-million-plus followers. And accusing the people who responded of “bullying” him “away from regulating new technologies” is so strange and ironic, given that many of those who criticized his tweet (including me) are strongly in favor of the kind of transparency and accountability from tech companies that Murphy is pushing for.  
  
**2\. “The Letter”  
**  
The day after the Chris Murphy Twitter episode, I heard about “the letter.” The [Future of Life Institute](https://futureoflife.org/), which has long been associated with the idea that “superintelligent” AI could present an “existential risk” to humanity, put out an [open letter](https://futureoflife.org/open-letter/pause-giant-ai-experiments/) calling for a six-month pause on training AI systems “more powerful than GPT-4.” The letter (which people on Twitter referred to as “the letter,” quotation marks included) has, as of now, been signed by nearly 3,000 people, including many well-known people in AI and tech. The letter asserts that “recent months have seen AI labs locked in an out-of-control race to develop and deploy ever more powerful digital minds that no one—not even their creators—can understand, predict, or reliably control.” The letter also states, as though it were an accepted fact, that “Contemporary AI systems are now becoming human-competitive at general tasks,” and warns of dangers ranging from machines flooding information channels with disinformation, automating away all jobs, and outsmarting and replacing all humans, who would then lose control of civilization.  
  
I agreed with some aspects of the letter, such as the statement that “AI research and development should be refocused on making today’s powerful, state-of-the-art systems more accurate, safe, interpretable, transparent, robust, aligned, trustworthy, and loyal” (though the “loyal” bit stood out to me as a touch of anthropomorphic creepiness). But the mix of reasonableness and breathless hype was too much for me, and I didn’t sign. As one example of what bothered me, the claim that “Contemporary AI systems are now becoming human-competitive at general tasks” cited a non-peer-reviewed arXiv preprint written by Microsoft researchers (hardly unbiased sources) about the capabilities of GPT-4. The experiments described in the paper are unreproducible and un-probe-able, since researchers outside Microsoft or OpenAI don’t have access to either the version of GPT-4 that was tested, or data used to train it. Even if the the results are robust, [they are hard to interpret in general](https://venturebeat.com/ai/why-exams-intended-for-humans-might-not-be-good-benchmarks-for-gpt-4/).

So, I can’t accept this article as a valid reference for such a huge claim. I don’t want to fan the flames of AI hype, and it seemed that signing the letter might help to do just that.  
  
Not surprisingly, there was a huge debate on social media about the letter, with various people supporting and attacking it. The response that I most resonated with was titled “[Statement from the listed authors of Stochastic Parrots on the ‘pause’ letter”](https://www.dair-institute.org/blog/letter-statement-March2023). Here are some excerpts from that statement:   


> “Such language [from “the letter”] that inflates the capabilities of automated systems and anthropomorphizes them, as we note in Stochastic Parrots, deceives people into thinking that there is a sentient being behind the synthetic media. This not only lures people into uncritically trusting the outputs of systems like ChatGPT, but also misattributes agency. Accountability properly lies not with the artifacts but with their builders.”

> “What we need is regulation that enforces transparency. Not only should it always be clear when we are encountering synthetic media, but organizations building these systems should also be required to document and disclose the training data and model architectures. The onus of creating tools that are safe to use should be on the companies that build and deploy generative systems, which means that builders of these systems should be made accountable for the outputs produced by their products.”

**3\. Time Magazine Gives a Platform to Extreme AI Doomerism  
**  
I and others worried that “the letter” would fan the flames of AI hype. It didn’t take long after the letter was published—one day, to be exact—for an [opinion piece](https://time.com/6266923/ai-eliezer-yudkowsky-open-letter-not-enough/) to appear in the online version of _Time_ Magazine, entitled “Pausing AI Developments Isn’t Enough. We Need to Shut it All Down”. The author, Eliezer Yudkowsky, proclaimed:   


> “Many researchers steeped in these issues, including myself, expect that the most likely result of building a superhumanly smart AI, under anything remotely like the current circumstances, is that literally everyone on Earth will die.”  
> 

  
Flames fanned!  
  
Yudkowsky goes further, pushing on the unnamed “many researchers” rhetoric:

> “Many researchers working on these systems think that we’re plunging toward a catastrophe, with more of them daring to say it in private than in public.”

and therefore he recommends:

> “Shut down all the large GPU clusters (the large computer farms where the most powerful AIs are refined). Shut down all the large training runs. Put a ceiling on how much computing power anyone is allowed to use in training an AI system, and move it downward over the coming years to compensate for more efficient training algorithms. No exceptions for governments and militaries. Make immediate multinational agreements to prevent the prohibited activities from moving elsewhere. Track all GPUs sold. If intelligence says that a country outside the agreement is building a GPU cluster, be less scared of a shooting conflict between nations than of the moratorium being violated; be willing to destroy a rogue datacenter by airstrike.”

For context, Yudkowsky has long been a well-known proponent of “AI doomerism”—someone who has been pushing the “Superintelligent AI will kill us all” narrative for decades—so his opinions didn’t come as a surprise to people in the field. However, the huge platform of _Time_ Magazine, _Time_ ’s description of Yudkowsky as “a founder of the field [of AGI],” and the juxtaposition of “the letter” signed by tech luminaries with this more extreme piece is a perfect storm of AI hype.  
  
One of the worst parts of this whole saga was when Fox News correspondent Peter Doocy asked about Yudkowsky’s warnings at [a White House press conference](https://www.youtube.com/watch?v=dSmJuVsgIE8). Doocy noted that “an expert from the Machine Intelligence Research Institute” (an organization founded by Yudkowsky) “says that if there is not an indefinite pause on AI development, literally everyone on Earth will die” and asked Press Secretary Karine Jean-Pierre if she would agree that “this does not sound good”. Jean-Pierre responded—unfortunately quite roboticly and unhelpfully—that there is a “comprehensive process in place” by which the federal government is dealing with AI risk, but she doesn’t have anything else to share.  
  
More flames are fanned!

**4\. What** _**Should**_**We Be Worried About?  
**  
Among all this fanning of flames, what is it that we should actually be worried about with respect to AI?  
  
AI systems have been and will be really useful for many applications, and in thinking about them, we have to trade off the potential benefits and harms. To do so, we need a better understanding of what these potential benefits and harms can be.   
  
As for the potential harms, some things are clear. Large, pre-trained AI systems (such as GPT-4 or Dall-E) encode racial, gender, and other biases picked up from their training data, and, when deployed in the real world, can magnify these biases. These systems are astoundingly good at generating and processing text, but they are unreliable and cannot be trusted to generate truthful information. They can be used by humans to mass-produce disinformation. The large companies that control and profit from these systems are often not transparent about the architecture of the systems, the data they have been trained on, how they are safeguarding the outputs, and other details that are important for understanding the systems’ limitations and immediate risks.   
  
Moreover, we humans are continually at risk of over-anthropomorphizing and over-trusting these systems, attributing agency to them when none is there (e.g., see Chris Murphy’s controversial tweet discussed above). The fact that systems like ChatGPT [anthropomorphize themselves](https://twitter.com/mpshanahan/status/1626631198628773912) by using “I” pronouns and talking about their feelings doesn’t help the situation. And the glib use by researchers of ill-defined hype-y terms such as “Artificial General Intelligence” does not serve the public (or even the research community) in making sense of what these systems can and cannot do.  
  
But what about the more apocalyptic warnings, ranging from “the letter” warning us that AI’s “powerful digital minds” might replace humans, to Yudkowsky’s certainty that “superintelligent” AI is going to kill us all? By calling these claims “flame fanning” or “fear-mongering,” am I putting my head in the sand, like the asteroid-deniers in the movie “Don’t Look Up”?  
  
These questions aren’t simple, but to answer them, we need more clarity about the terms used in the debates. I believe that referring to today’s AI as “powerful digital minds” is a serious overstatement that will mislead the public. The notion of “superintelligence” is still hotly debated. Even before the latest wave of AI progress and hype, Stuart Russell wrote a [New York Times OpEd](https://www.nytimes.com/2019/10/08/opinion/artificial-intelligence.html) that warned of existential risk of superintelligent AI. I wrote a [responding OpEd](https://www.nytimes.com/2019/10/31/opinion/superintelligent-artificial-intelligence.html) questioning the whole premise. I still stand by my arguments, but I think that the only way to resolve the debate is to gain a better scientific understanding of what intelligence is, and [what diverse forms it can take](https://arxiv.org/abs/2210.13966).   
  
It’s notable that one common narrative around today’s AI is that it is impossible for humans to understand how AI systems work. Yudkowsky describes these systems as “composed of giant inscrutable arrays of fractional numbers,” and notes that given “how little insight we have into these systems’ internals, _we do not actually know_ ” if they are self-aware or sentient. While there is lots we don’t understand about systems like ChatGPT or GPT-4, there is a lot we _do_ understand—e.g., enough to know that they are certainly not sentient for any useful meaning of the word—and scientists are making progress all the time in understanding them better. The “unexplainable” narrative gives rise to fear, and [it has been argued](https://www.latimes.com/business/technology/story/2023-03-31/column-afraid-of-ai-the-startups-selling-it-want-you-to-be) that, to a degree, public fear of AI is actually useful for the tech companies selling it, since the flip-side of the fear is the belief that these systems are truly powerful and big companies would be foolish not to adopt them.   
  
Ultimately, to figure out what we really need to worry about, we need better AI literacy among the general public and especially policy-makers. We need better transparency on how these large AI systems work, how they are trained, and how they are evaluated. We need independent evaluation, rather than relying on the unreproducible, “just trust us” results in technical reports from companies that profit from these technologies. We need new approaches to the scientific understanding of such models and [government support for such research](https://www.ai.gov/wp-content/uploads/2023/01/NAIRR-TF-Final-Report-2023.pdf).   
  
Indeed, as some have argued, we need a [“Manhattan Project of intense research](https://twitter.com/yudapearl/status/1641978456513867776)” on AI’s abilities, limitations, trustworthiness, and interpretability, where the investigation and results are open to anyone. What would be a [good name](https://twitter.com/Grady_Booch/status/1641982478994010114) for such a project? Is the name “Open AI” taken?

* * *
