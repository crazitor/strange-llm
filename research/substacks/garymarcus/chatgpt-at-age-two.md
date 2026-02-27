---
title: "ChatGPT, at Age Two"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/chatgpt-at-age-two"
---

[](https://substackcdn.com/image/fetch/$s_!Ehc7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6fd0968e-0c30-489c-b90b-878dd377cef5_1343x1003.png)Ezra Klein, in his introduction [to his January 6, 2023 interview with yours truly](https://www.nytimes.com/2023/01/06/podcasts/transcript-ezra-klein-interviews-gary-marcus.html)

ChatGPT blew the world away two years ago this week, and has received more press — and more investment - than anything else in the history of AI. ChatGPT is undeniably fun to play with. The pace of its spread has been incredible, with hundreds of millions of people trying it out.

But a lot of of theories about how ChatGPT would be used in practice have fizzled out. Remember how ChatGPT was gonna take over web search and wipe out Google? Two years later Google’s search share hasn’t diminished all that much. High school kids are still using ChatGPT to write term papers, but a lot of Fortune 500 companies are somewhat underwhelmed by the real world results they are getting. 

There has been a ton of experimentation, but relatively few well-documented success stories, and some fairly negative stories like [a recent one at Business Insider on GPT-powered CoPilot](https://www.businessinsider.com/microsoft-ai-artificial-intelligence-bet-doubts-marc-benioff-satya-nadella-2024-11), headlined “Microsoft is betting big on AI. Company insiders have serious doubts”, quoting a source there as saying “I really feel like I'm living in a group delusion here at Microsoft … [the company touts that] AI is going to revolutionize everything … but the support isn't there for AI to do 75% of what Microsoft claims it'll do.”

As long time readers will know, I commented somewhat negatively on ChatGPT, in this Substack, within days of its release, and soon thereafter in a January 2023 podcast with Ezra Klein. Klein, to his credit, was one of the first in the major media to recognize out loud that all was not entirely roses.

It is instructive to rewind to that moment, asking whether the initial problems of ChatGPT have been resolved, after two years of allegedly exponential progress. (The [whole interview is worth rereading](https://www.nytimes.com/2023/01/06/podcasts/transcript-ezra-klein-interviews-gary-marcus.html), in fact.)

§

As already noted, [the podcast ](https://www.nytimes.com/2023/01/06/opinion/ezra-klein-podcast-gary-marcus.html) revolved in part around ChatGPT’s tendency to create bullshit. 

_Ezra Klein: … And what unnerved me a bit about ChatGPT was the sense that we are going to drive the cost of bullshit to zero when we have not driven the cost of truthful or accurate or knowledge advancing information lower at all. And I’m curious how you see that concern._

_Gary Marcus: It’s exactly right. These systems have no conception of truth. Sometimes they land on it and sometimes they don’t, but they’re all fundamentally bullshitting in the sense that they’re just saying stuff that other people have said and trying to maximize the probability of that. It’s just auto complete, and auto complete just gives you bullshit._

(Ernest Davis and I had emphasized the same earlier, [in a 2020 essay](https://www.technologyreview.com/2020/08/22/1007539/gpt3-openai-language-generator-artificial-intelligence-ai-opinion/), characterizing ChatGPT’s predecessor GPT-3 as a “fluent spouter of bullshit”.)

§

The very next day, foreshadowing so much of what was to come, Nate Labenz [wrote a scathing, wildly popular thread on X that excoriated the episde at great length](https://x.com/labenz/status/1611724185709027328?s=61), ultimately garnering nearly 700,000 views and a thousand likes. His thread began “As an AI obsessive and long-time @ezraklein fan, I was excited to see yesterday's podcast with @GaryMarcus. … Unfortunately, as I listened, my excitement gave way to frustration, and I felt compelled to write my first-ever megathread. … there are so many inaccuracies in this interview”. 

The crux was to go after quotes like these

> ChatGPT's output "has no real relationship to the truth." 

and

> "everything it produces sounds plausible, but it doesn't always know the connections between the things that it's putting together" 

In a longer passage I said 

> You can’t say at the beginning of a ChatGPT session and expect it to work, “please only say true statements in what follows.” It just won’t be able to respect that. It doesn’t really understand what you mean by say only true things. And it cannot constrain itself to only say true things.

Labenz tried to paint these criticisms as archaic and out of touch, writing that 

> [Marcus’] knowledge of LLMs performance & behavior is two generations out of date. His claims were accurate in 2020, maybe 2021, but not now.

Labenz – and the countless venture capitalists and big tech companies that invested hundreds of billions in improving ChatGPT – projected that hallucinations and stupid errors of misunderstanding would soon recede. 

They didn’t.

§

In fact, by Fall of 2023, people were starting to acknowledge that hallucinations were a real problem. 

But powerful people continued to express endless optimism that hallucinations would soon disappear. For example, in September 2023 Microsoft Board Member/LinkedIn Founder Reid Hoffman told Time Magazine:

> And there’s a whole bunch of very good R&D on how to massively reduce [hallucinations](https://www.nytimes.com/2023/05/01/business/ai-chatbots-hallucination.html) [AI-generated inaccuracies] and get more factuality. Microsoft has been working on that pretty assiduously from last summer, as has Google. It is a solvable problem. I would bet you any sum of money you can get the hallucinations right down into the line of human-expert rate within months. So I’m not really that worried about that problem overall.

Alas, even today hallucinations (probably better described as confabulations) _still_ haven’t gone away. And not for lack of trying. The industry has tried practically everything, scaling, more scaling, and [RAG](https://garymarcus.substack.com/p/no-rag-is-probably-not-going-to-rescue). [Apple even tried (to little avail) literally putting “do not hallucinate” in its system prompt](https://arstechnica.com/gadgets/2024/08/do-not-hallucinate-testers-find-prompts-meant-to-keep-apple-intelligence-on-the-rails/). 

_None_ of this has eliminated the problem.

§

Here’s a typical example someone shared with me this morning, a[ long dialog on film reviews](https://bsky.app/profile/valoisdubins.bsky.social/post/3lbyqffqu2s2o) with ChatGPT, from someone with the pseudonym Valois Dubins.

It opens with Dubins asking ChatGPT (latest, 2024 edition) to write a negative review of the film _Wicked_.

[](https://substackcdn.com/image/fetch/$s_!pFjx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1619a935-3901-4bdd-81fb-16a705ed8dfc_859x866.png)

But the whole thing was made-up:

[](https://substackcdn.com/image/fetch/$s_!B323!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71c83b46-0bfe-4466-94e8-7b949cd6ee82_878x630.png)

A trustworthy AI, not having seen the film, would have declined the mission, and not just made things up. But not ChatGPT, which never hesitated. Its tendency to generate bullshit is as strong as ever. 

§

Things got worse, much worse from there. The film subsequently libeled a critic named Mark Kermode, [describing a “career misstep” that never happened and was entirely fabricated](https://bsky.app/profile/valoisdubins.bsky.social/post/3lbyq7kha622o), and claiming (again completely invented) that the critic “has since acknowledged & reflected on the irony of reviewing a movie he hadn’t seen, using the experience as a lesson in the importance of genuine engagement with art”. 

Dubois continued “Shocked to learn of this sordid skeleton in the Kermodian closet, I asked for a link to the review. Upon which ChatGPT apologised, confessed it didn't exist.” 

None of what ChatGPT had said was real; bullshit had been layered on bullshit. [Same as it ever was](https://genius.com/Talking-heads-once-in-a-lifetime-lyrics). 

§

The last two years have been filled with tech titans and influencers touting “exponential progress” and assuring us—with zero proof, and no principled argument whatsoever—that hallucinations would go away. Instead, hallucinations are still a regular occurrence. (Promises that they will soon disappear haven’t gone away either. Fixes will surely come [Real Soon Now](https://www.urbandictionary.com/define.php?term=real+soon+now), as Jerry Pournelle used to say.) They may have declined, but they certainly haven’t vanished. (The fact that humans hallucinate when they are sleep-deprived or on drugs is no excuse.)

The reality is this. Two years on, on the most important question of all – factuality and reliability — we are still pretty much where we were when ChatGPT first came out: wishing and hoping. RAG, scaling, and system problems haven’t eradicated the inherent tendency of LLMs to hallucinate. 

Commercial progress has been halting precisely because the tech simply isn’t reliable. 

Yet hundreds of billions more have been invested on further speculation that scaling would somehow magically cure problems that actually appear to be inherent with the technology.

How long do we need to keep up the charade? 

§

At the end of the Ezra Klein interview, I called for a massive investment in new approaches to AI. I still think that is the way to go. 

[Share](https://garymarcus.substack.com/p/chatgpt-at-age-two?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** knows that ChatGPT helps some people with brainstorming, writing and coding, but wishes the field of AI would turns its attention to more reliable tools._
