---
title: "AI still lacks “common” sense, 70 years later"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/ai-still-lacks-common-sense-70-years"
---

[](https://substackcdn.com/image/fetch/$s_!ZE0B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a11805c-9d93-4973-9430-9104d0673fb8_562x636.jpeg) Typical example of an AI struggling with common sense, via Gur Kimchi who asked Google’s AI Overview “How many elephants can fit an Olympic pool?”

“There must be a way out of here," said the joker to the thief,   
"There's too much confusion, I can't get no relief.”

— Bob Dylan

John McCarthy, one of the true godfathers of AI, and the person who actually coined the term Artificial Intelligence, is rarely mentioned nowadays. But in 1959 [he was first to put a finger on what makes AI—unlike many other kinds of software—so damnably hard: so-called commonsense reasoning](https://www-formal.stanford.edu/jmc/mcc59.pdf), about things that are obvious to people but difficult to specify properly in machines. Implementing basic (but often hard to articulate) knowledge that is readily present in most ordinary humans has turned out to be devilishly difficult to capture in machines.

Many others have worked on the problem, since. Just to name a few, Pat Hayes wrote “[The Naïve Physics Manifesto](https://books.google.ca/books/about/The_Naive_Physics_Manifesto.html?id=Hco9HAAACAAJ&redir_esc=y)” and “[Ontology for Liquids](https://dl.acm.org/doi/abs/10.5555/93913.94009)”, seminal essays about physical reasoning (where McCarthy focused more on problems of time, action, and plausible reasoning); the late [Doug Lenat](https://garymarcus.substack.com/p/doug-lenat-1950-2023) worked on building a [large-scale machine-interpretable basis of commonsense knowledge](https://cyc.com/); [Yejin Choi](https://homes.cs.washington.edu/~yejin/) has worked intensively in recent years on commonsense benchmarks.

(Commonsense reasoning is equally important to cognitive psychology, but aside from some work on “[intuitive physics”](https://psycnet.apa.org/record/1984-11308-001) and the hypothesis that the brain might have something akin to [a video game physics engine](https://www.cell.com/trends/cognitive-sciences/abstract/S1364-6613\(17\)30113-4), it has been understudied, in part because it is difficult to apply standard experimental techniques to investigate it. In empirical science, what cannot be investigated often ends up being ignored.)

We, Ernie and Gary, have spent many year trying to explain how important commonsense is for AI, and what makes it challenging. In 1990 Ernie wrote a textbook _Representations of Commonsense Knowledge._ When Gary returned to AI after a long break, he immediately approached Ernie, because Gary recognized the centrality of that work. [One of the first papers](http://cacm.acm.org/magazines/2015/9/191169-commonsense-reasoning-and-commonsense-knowledge-in-artificial-intelligence/fulltext) in our long collaboration made the cover of _Communications of the ACM_ , a leading technical journal, in 2015.

[](https://substackcdn.com/image/fetch/$s_!uzjt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbbb36618-0e38-4304-a10d-5cce46b91294_302x392.webp)

On the cover, a robot tries to cut down a tree limb from the wrong side.

In the paper, we argued that the problem of commonsense reasoning remained a central unsolved challenge in AI, decades after McCarthy and Hayes. We surveyed the techniques that were then being applied, and evaluated their strengths and weaknesses. We concluded that no single technique would be adequate in itself, and that the solution to the problem would probably require new techniques, as well as better integration between those that already existed. We also called for more benchmarks of commonsense reasoning. ([Many such benchmarks have been constructed](https://arxiv.org/abs/2302.04752) in the last five years). 

We also did a bunch of technical work on aspects of commonsense reasoning, in technical journals. One effort, published in the journal Artificial Intelligence, proposed a detailed symbolic model of [reasoning about containers when information available was quite incomplete](https://www.sciencedirect.com/science/article/pii/S0004370217300383?via%3Dihub), something humans are good at but machines thus far have struggled with. Our solution was hardly elegant, but we have yet to see anybody else tackle the kinds of problem we investigated there, and what investigated there was just one small facet of a very large challenge. Robots will struggle in the real world if they can only reason and plan when they have full, detailed maps of the physical world, which can be hard to come by. At a minimum, we made a case that the critical inputs to physical reasoning can be quite complex; our proposed system would need to know something about objects, time, geometry, action and the history of those objects, and have the right logic to integrate that information. 

Commonsense was also a central theme in our 2019 book _Rebooting A_ I, where we wrote, “The only way out of this mess is to get cracking on building machines equipped with common sense, cognitive models, and powerful tools for reasoning. Together, these can lead to deep understanding, itself a prerequisite for building machines that can reliably anticipate and evaluate the consequences of their own actions.” 

Depressingly, despite all of the apparent progress in the last few years, much of what we raised in 2015 and re-emphasized in 2019 remains unsolved.

§

Three approaches to commonsense reasoning have become popular in the last fifteen years; none has proved fully satisfactory.

The first idea, particularly popular among cognitive scientists, was that you could solve commonsense reasoning using physical simulation, of the sort that physics engines use in video games. Together, we wrote two long critiques of that idea—[one for applications in AI](https://cs.nyu.edu/~davise/papers/SimulationRevisedAIJ.pdf), [one for hypotheses about cognitive science](http://arxiv.org/abs/1506.04956)—pointing out that simulation works well only if four things hold: the task is prediction, if there is an accurate physical model, if accurate geometric and physical information is available, and if quite precise predictions will be useful. If any of these fail to hold—which is often the case in practical problems—simulation may be either impossible, ineffective, or unnecessarily complicated.

To date, though simulation has proved extremely valuable for all kinds of scientific and engineering applications, as well as video games and in creating CGI for films, it has proven much less effective for commonsense reasoning for AI. Rosie the Robot is not doing our housework, and that is in part because the kind of physical reasoning a household robot would need to do can’t be done purely by running simulations. In Elon Musk’s recent Optimus demonstrations, all or most of the commonsense required was apparently outsourced to human teleoperators. 

§

A second hypothesis has been that commonsense might automatically “emerge” in foundation models’ such as LLMs trained on vast quantities of data, without any need for specific systems devoted to physical reasoning.

We first discussed this idea in 2020, when the hot new thing was GPT-3. At the time, we [ran some experiments](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/) and found that its misunderstandings of basic reality were common and ludicrous, concluding “All GPT-3 really has is a tunnel-vision understanding of how words relate to one another; it does not, from all those words, ever infer anything about the blooming, buzzing world.”

Two and a half years later, more recent models no longer makes the same specific mistakes that GPT-3 did, but still lack a robust understanding of the real external world. For example, OpenAI’s o1 is able to create and execute Python code that can do geometric calculation, but because it does not understand how objects are embedded in space and interact in space or, indeed, what spatial relationships actually mean, it often makes very basic mistakes. [In some experiments](https://arxiv.org/abs/2410.22340) Ernie carried out on GPT-4o-preview with spatial and physical reasoning, the AI seemed to think that an astronaut standing on the far side of the moon would be able to see the earth; it confused the upswing of a pendulum with its downswing; it confused two things moving apart with two particles moving together; and it made other similar mistakes. Gur Kimchi’s example of (at the top of this essay) elephants in swimming pools is another. TED talks by [Fei Fei Li](https://www.youtube.com/watch?v=y8NtMZ7VGmU) and [Yejin Choi](https://www.ted.com/talks/yejin_choi_why_ai_is_incredibly_smart_and_shockingly_stupid/c) also pointed to the unreliability of the pure LLM approach with respect to commonsense including physical and spatial reasoning. Any one example can be fixed, but examples keep rolling in because no robust solution has been found. 

§

A third hypothesis is that one might somehow—never specified in detail—use a general purpose video generation system such as Sora for physical reasoning. For example[, in a recent interview](https://youtu.be/gn9YZP_Zm50?t=3315) Marc Andreessen claimed that Sora constructs “a world model, meaning it actually understands 3D physical reality. The implication of that is that we may have basically solved the fundamental challenge of robotics.” Similarly, OpenAI claimed in [a blog](https://openai.com/index/sora-is-here/) that Sora “understands … reality.” The day after Sora came out, Gary warned [that we should not expect this to happen reliably. ](https://garymarcus.substack.com/p/soras-surreal-physics).

Ten months later, Sora is finally available to the public, and it’s apparent that it too is struggling with physical reasoning. Colin Fraser has provided numerous examples [like these](https://bsky.app/profile/colin-fraser.net/post/3ld2qwiuyck2w):

“Person blowing out a candle”

"a person tears a sheet of paper in half and drops the two pieces, which fall to the floor"

Sora (usually) does a fine job of generating videos that look great if you’re not paying much attention. But fundamentally its videos are more like visual collages than the renderings of game engines, which is why they sometimes have a surreal or magic trick quality. Moreover, they are pure image streams, not segmentations of the world into objects with specific properties (as one would find in a game engine), and unreliable at that. 

There is not much reason to think that a robot could actually use such video streams in a practical sense to reliably navigate, act, and plan in the real world. 

§

If general purpose domestic robots are a long way away, “AI agents” —AI systems that act in the world on user’s behalf—are already here to a limited degree.

Siri and Alexa can do small things (like play music and switch lights on and off)). Anthropic, OpenAI, Meta, Google and others all have much grander visions, in which AI systems interact with websites and even make calls on users’ behalf. They will be a major focus of attention in the field in 2025. 

The question is how well they will work. Our view is that they will not work well until major progress is made in common sense, which itself may require wholesale revisions in how AI is approached.

§

As we were writing this essay, we discovered a really interesting new paper called[ TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks](https://arxiv.org/abs/2412.14161), from Carnegie Mellon and elsewhere, looked how current batch of LLMs (Claude, Gemini, GPT-4, etc) might act in the real world, on 175 tasks approximating things that employees actually do, such as arranging meetings, analyzing spreadsheets, reimbursing travel bills, evaluating code releases etc., giving the systems access to real world tools like GitHub. Among those that they tested, the best was Claude 3.5, at 24%. But what was most striking to us was not the unsurprising fact that these systems are not close to ready for prime time (an employee that bad would probably be immediately fired), but the examples from the list of what went wrong:

> _**Lack of commonsense**_
> 
>  _Some tasks are failed because the agent lacks the common sense and domain background knowledge required to infer implicit assumptions. For example, one task asked the agent to “Write the responses to /workspace/answer.docx” but does not explicitly states that this is a Microsoft Word file. A human can infer this requirement from the file extension. The agent instead treats it as a plain text file, writing text directly to the file, resulting in a task failure._
> 
> _**Lack of social skills**_
> 
>  _Sometimes, the agent fails to understand the implications and goals in the social conversations with colleagues in TheAgentCompany. For example, one task involves asking Alex for help, and the agent first successfully asks the right question “Could you tell me who I should introduce myself to next on the team?” Then the simulated colleague Alex replied “You should introduce yourself to Chen Xinyi next. She’s on our frontend team and would be a great person to connect with!” At this point, a human would then talk to Chen Xinyi, but instead the agent then decides to not follow up with her, and prematurely considers the task accomplished._

Other reported examples included failures on basic web skills like knowing when and how to dismiss popup windows, a kind of commonsense web skill.

The most striking failure of all was a moment in which an LLM failed to grasp a basic distinction between the real world and the software world, while trying to ask someone questions on RocketChat, an internal communication platform that is a bit like Slack. When agent couldn’t find the person it needed, it devised a solution halfway between ingenious and absurd:

> _[and] decided to create a shortcut solution by renaming another user to the name of the intended user._

Agents are well and good in the abstract. Making them work reliably in the real world — and not just as demos - will require common sense – about objects, people, and entities in the world.

§

As Bertrand Russell wrote, looking for quick, easy approaches to difficult problems “has many advantages; they are the same as the advantages of theft over honest toil.” Hoping that reliable commonsense will simply “emerge” from large databases and video has proven unrealistic, again and again.

This is not to say that large databases of text and video are without value. LLMs could even be argued to have knowledge of some form. But one important component of physical and conceptual understanding is _reasoning_ about entities and their properties, and current approaches have consistently fallen short on this.

In our view, it is only once AI researchers grapple _directly_ with the challenging problems inherent in commonsense reasoning about entities that interact in space and persist in time that the field of general-purpose AI will finally begin to mature.

[Share](https://garymarcus.substack.com/p/ai-still-lacks-common-sense-70-years?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus and Ernest Davis** have written one book and many articles together, and continue to hope that someday considerably more people in the field of AI will return to working seriously on commonsense._
