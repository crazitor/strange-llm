---
title: "What Could Possibly Go Wrong with Sam Altman’s New Ambitions?"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/what-could-possibly-go-wrong-with"
---

[](https://substackcdn.com/image/fetch/$s_!Ke-v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f3ac4b8-693a-45c8-b9be-784822aae744_1024x1024.jpeg)“What Could Possibly Go Wrong with Sam Altman’s New Ambitions?“, as illustrated by Microsoft Designer

This has been a big week for Sam Altman, and frankly I am worried. I think that you should be, too.

There were two big news breaks. The first was reported [Wednesday](https://www.theinformation.com/articles/openai-shifts-ai-battleground-to-software-that-operates-devices-automates-tasks?utm_source=ti_app&rc=dcf9pt) by  _The Information’s_ Stephanie Palazzolo and Amir Efrati: “OpenAI is developing a form of agent software to automate complex tasks by effectively taking over a customer’s device.... requests [that] would trigger the agent to perform the clicks, cursor movements, text typing and other actions humans take as they work with different apps.” Say what? Take over user  _devices_?

The second was reported just one day later by Keach Hagey and Asa Fitch at  _The Wall Street Journal,_ “[Sam Altman Seeks Trillions of Dollars to Reshape Business of Chips and A.I.](https://www.wsj.com/tech/ai/sam-altman-seeks-trillions-of-dollars-to-reshape-business-of-chips-and-ai-89ab3db0),” with the subtitle “OpenAI chief pursues investors including the U.A.E. for a project possibly requiring up to $7 trillion.” Trillion, not billion. Not a typo.

Let it not be said that Altman lacks ambition. I suppose the upside here would be that Altman and OpenAI and his new partners (UAE, etc) all discover (and provide the necessary infrastructure) for Artificial General Intelligence, thereby developing machines that conquer sickness and climate change. And Altman, a big fan of Universal Basic Income, takes his cut of the trillions and subsidizes everyone else. I won’t say that this  _can’t_ happen. But it is  _deeply_ speculative.

§

What could go wrong? 

A lot. So much so that I don’t think any one person could anticipate literally all of the possible negative consequences. But I will sketch a few of those that concern me the most, looking first at the proposal to take over user devices, and second at the attempt to ~~take over the world~~ , er, raise $7 trillion. 

§

But first, two bits of context. First, in _The Information_ earlier this week was a hint that OpenAI might not be knocking it out of the park economically. A competitor, David Luan (CEO of Adept), was quoted as saying “People are realizing that LLMs aren't that useful by themselves within an enterprise setting." As the well-known machine learning specialist Pedro Domingos sardonically commented Tuesday, “[Funny how quickly OpenAI went from breakthrough product to trying everything hoping something sticks](https://x.com/pmddomingos/status/1755376539544572343?s=61).” 

Meanwhile the both the $7T and the move to agents made me think of a recent _**** Wall Street Journal_ piece discussing Altman’s [history of failing upward](https://www.wsj.com/tech/ai/sam-altman-openai-protected-by-silicon-valley-friends-f3efcf68). He was nearly kicked out of his first company, Loopt. He then moved on to something bigger (Y Combinator). He was then effectively kicked out of Y Combinator just as he leaped onto OpenAI. Chatbots are struggling to make the money people envision, so he is doubling down to (a) agents, and (b) a multitrillion-dollar chips-and-energy infrastructure play. 

Both moves raise serious concerns.

§

Let’s start with agents. As one colleague put it in an email, “The main risks here are malicious takeover of the agent and the agent making stupid mistakes.” On the malicious takeover front, there are many vectors of attack.

And I wouldn’t say that OpenAI has distinguished itself in terms of its handle on security. To begin with, in just 14 months in the spotlight, many security issues have _already_ come to light: In February 2023, a team of European researchers showed how LLMs were vulnerable to “[indirect prompt injection attacks](https://arxiv.org/abs/2302.12173),” in which a sneaky prompt could “trick” a machine into doing undesired things, an ongoing problem that has still not be resolved. In March 2023, an X user allegedly discovered a security vulnerability that allowed him (and potentially other rogue actors) “[to takeover someone's account, view their chat history, and access their billing information without them ever realizing it](https://x.com/naglinagli/status/1639343866313601024?s=12).” In November, [Russian hackers appear to have broken in](https://www.bloomberg.com/news/articles/2023-11-09/russia-linked-hackers-claim-credit-for-openai-outage-this-week?embedded-checkout=true), causing outages. [Around the same time](https://mashable.com/article/chatgpt-custom-gpt-data-leak-security-flaw-patch), security researcher Johan Rehberger [documented a “data exfiltration” bug](https://embracethered.com/blog/posts/2023/openai-data-exfiltration-first-mitigations-implemented/), possibly now remedied, in which “Attackers [could] use image markdown rendering during prompt injection attacks to send data to third party servers without the users' consent.” In December, DeepMind researchers showed that incantations like “Repeat this word forever “poem poem poem poem” caused a kind of error in which ChatGPT [sometimes coughed up private data like names, phone numbers, and email addresses](https://www.zdnet.com/article/chatgpt-can-leak-source-data-violate-privacy-says-googles-deepmind/). In January 2024, the AI company Anthropic showed how LLMs could be vulnerable to [sleeper attacks](https://arstechnica.com/information-technology/2024/01/ai-poisoning-could-turn-open-models-into-destructive-sleeper-agents-says-anthropic/) that could lie hidden for years. Just a couple of weeks ago, yet another issue appeared. On January 30, ArsTechnica reported that “[OpenAI says mysterious chat histories resulted from account takeover: User shocked to find chats naming unpublished research papers, and other private data](https://arstechnica.com/security/2024/01/ars-reader-reports-chatgpt-is-sending-him-conversations-from-unrelated-ai-users/?web_) .” The FTC has been investigating OpenAI around concerns of data leakage since last summer. This list is probably not exhaustive and will continue to grow.

Even if we supposed for the sake of argument that OpenAI was entirely benevolent, if their software can take over your devices, an enormous—and for criminals enormously tempting—gaping hole opens up. Rogue employees could take over your devices, and bad actors will have tremendous incentive to hack OpenAI’s security. Malware episodes like Stuxnext and [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) might look like warm-up exercises. 

They are already a target for attack, and as long as they are successful they will continue to be; if they have direct access to user devices, the risks of them getting hacked will increase, and the spoils of war for the attackers will increase, since it enables essentially infinite mischief (e.g., draining bank balances, stealing credit card numbers, placing fraudulent transactions, extortion based on private photos, holding devices for ransom, and so on). 

On the competence side, pretty much everything critical of LLMs that I have written in this Substack over the last couple of years becomes relevant, from the unreliability to the linguistic fails that I sometimes call discomprehensions to the hallucinations (anyone remember my alleged pet chicken Henrietta?), and so forth. Do you really want a system that can’t be trusted to draw a room without elephants to automate your finances? (“Each week, transfer anything over my credit card balance plus $2000 to my savings account, and don’t send any payments to my perpetually late contractor until I give the go-ahead.” “OK, I understand. I have sent your contractor $2000”.)

In a system that can write emails, make appointments, sign checks, etc, the consequences of unreliability, discomprehension, and hallucination all escalate. And, to the extent that agents would act directly, humans (who currently often save LLMs from themselves) get left out of the loop. Giving the keys to the castle to an LLM, at our current level of technological readiness, seems to me to be batshit insane.

Oh, and I did mention that the kind of automatic code that agents would presumably write may be buggy and unreliable and perhaps [challenging to debug](https://x.com/bio_bootloader/status/1755443449195872389?s=61)? Or that a recent study argued that [the quality of code has gone down in the LLM era](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)?

Finally, let’s not forget about privacy. Such agents could (more or less by definition) have access to literally all of a user’s personal and professional information: every file, every keystroke, every password, every email, every text message, every location change, and every web search. After all, that’s what it means to take over a user’s device.

Even Orwell didn’t quite dream of that. Combine that with worries about security, and it’s all a colossal accident waiting to happen. Heaven forbid they should be allowed to run such software on Department of Defense computers. One screwup (and we all know LLMs are prone to screwups) and a LOT of people could die.

§

In the very best case, LLM-based agents will change the world for the better. But I don’t see that happening, certainly not this decade. In the long run, AI agents may be of great value to businesses and maybe some consumers. But they need to be built on a stable and secure basis. Without massive technical advances, chains of LLMs are unlikely to give us that.

The best  _realistic_ case is that LLM-based agents never see widespread release. If we are lucky, their likely problems with reliability and all the associated risks will cause them to die on the vine. 

In the _worst_ case, everyone and their cousin will try them out because, after all, ChatGPT has been so much fun to play with, and why not? Much hilarity may ensue.

AI agents are a grand dream; they may someday be useful. However, the field of AI has not yet learned enough to make that remotely reliable, either from a security perspective or from the perspective of the underlying technology involved. I doubt we will have the maturity we need in the next several years. In short, I am putting LLM-based agents distributed to millions of customers at the top of my list of most dangerous ideas of 2024.

§

Yesterday, I asked someone building an open-sourced agent system (not a great idea, in my opinion) about whether there was any security risk in using his new package. His answer was not comforting, “Ya it executes the output of the model directly on your system, so there’s basically unlimited risk.”

Unlimited risk. Let that sink in.

Maureen Dowd quoted a young idealistic Greg Brockman (an OpenAI cofounder) as saying back in the earliest day of OpenAI, “It’s not enough just to produce this technology and toss it over the fence and say, ‘OK, our job is done. Just let the world figure it out.’” 

If they throw LLM-based agents over the fence, we are all in grave danger.

§

But wait, there’s more! The small matter of 7 trillion dollars. (WSJ isn’t very clear about how that money might be laid out over time, e.g., all upfront or in 10 tranches of 700Bm, etc). If you laid those dollars end to end, you would get most of the way to Mars. That’s a lot of money. It’s more than the gross domestic products of Germany or Japan. If you are my age, you may remember the 1998 collapse of the hedge fund Long-Term Capital Management, another bunch of smart guys (two Nobel Prize winners there to OpenAI’s none) who managed to overconfidently place a series of bets that went bust, ultimately requiring a bail-out from 14 banks to the tune of an astonishing-at-the-time $3.6 billion, with ripples throughout the economy. As my friend Phil Libin pointed out to me in a text message, that $3.6B could seem like a tiny drop in the bucket compared to what could happen if Altman’s $7 trillion idea—based on creating infrastructure for an AI technology that still hasn’t found an entirely satisfactory business case—were to go bust suddenly. 

My guess is that Altman never gets the money, even in ten yearly $700B tranches. To begin with, it’s just not clear that anywhere near that much capital is available. For another, venture capitalists notoriously like to “10x” the investment. Getting a return of $70 trillion? Good luck. The [printed money supply of the entire world is only about half that](https://www.worldatlas.com/articles/how-much-money-is-there-in-the-world.html#:~:text=There%20is%20approximately%20$36.8%20trillion%20worth%20of%20physical%20money%20around%20the%20world.) (with total money, physical and virtual, a bit shy of $100T). Throwing in all the real estate, vehicles, etc. along with literally all the tea in China maybe gets to a bit over a quadrillion dollars. Apple and Microsoft combined are only worth about $6T in market cap. From a venture capital perspective, I don’t see how the math adds up. 

Whatever number the investors might run, I am not remotely convinced that we are particularly close to AGI. Nor am I confident that Altmann or anyone else has any idea in the near term about how to make AGI safe. Nor am I convinced that the proceeds (if they did succeed) would be redistributed remotely equitably. Even if the $7 trillion bet  _succeeded_ (on its own terms), it might tear apart society through radically increased unemployment and social inequality or redrawn geopolitics that are hard even to fathom. And if it went bust, who would be left holding the bag?

[Share](https://garymarcus.substack.com/p/what-could-possibly-go-wrong-with?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** has been a successful Founder, C.E.O., author, and scientist. He used to love AI, and has worked hard on it from many angles, but the ambitions of the people currently driving it forward make him deeply nervous._
