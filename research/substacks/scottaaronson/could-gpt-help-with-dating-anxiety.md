---
title: "Could GPT help with dating anxiety?"
author: "Scott Aaronson"
date: "Tue, 16 May 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7262"
---

_[Like everything else on this blog --but perhaps even more so--this post represents my personal views, not those of UT Austin or OpenAI]_

Since 2015, depressed, isolated, romantically unsuccessful nerdy young guys have regularly been emailing me, asking me for sympathy, support, or even dating advice. This past summer, a particularly dedicated such guy even [trolled my comment section](https://scottaaronson.blog/?p=6576)--plausibly impersonating real people, and causing both them and me enormous distress--because I wasn't spending more time on "incel" issues. (I'm happy to report that, with my encouragement, this former troll is now working to turn his life around.) Many others have written to share their tales of woe.

From one perspective, that they'd come to _me_ for advice is insane. Like … _dating advice_ from … _me_? Having _any_ dating life at all was by far the hardest problem I ever needed to solve; as a 20-year-old, I considered myself far likelier to prove P≠NP or explain the origin of consciousness or the Born rule. Having solved the problem for myself only by some miracle, how could I possibly help others?

But from a different perspective, it makes sense. How many besides me have even acknowledged that the central problem of these guys' lives _is_ a problem? While I have to pinch myself to remember, these guys look at me and see … _unlikely success_. Somehow, I successfully appealed the world's verdict that I was a freakish extraterrestrial: one who might _look_ human and seem friendly enough to those friendly to it, and who no doubt has some skill in narrow technical domains like quantum computing, and who could perhaps be suffered to prove theorems and tell jokes, but who could certainly, _certainly_ never interbreed with human women.

And yet I dated. I had various girlfriends, who barely suspected that I was an extraterrestrial. The last of them, [Dana](https://www.cs.utexas.edu/~danama/), became my fiancée and then my wife. And now we have two beautiful kids together.

If I did all this, then there'd seem to be hope for the desperate guys who email me. And if I'm a cause of their hope, then I feel some moral responsibility to help if I can.

But I've been stuck for years on exactly what advice to give. Some of it ("go on a dating site! ask women questions about their lives!") is patronizingly obvious. Some of it (_fitness? fashion? body language?_) I'm ludicrously, world-historically unqualified to offer. Much of it is simply extremely hard to discuss openly. Infamously, just for _asking for empathy_ for the problem, and for trying to explain its nature, I received a level of online vilification that one normally associates with serial pedophiles and mass shooters.

For eight years, then, I've been turning the problem over in my head, revisiting the same inadequate answers from before. And then I had an epiphany.

* * *

There are now, on earth, entities that can talk to anyone about virtually anything, in a humanlike way, with infinite patience and perfect discretion, and memories that last no longer than a browser window. How could this not reshape the psychological landscape?

Hundreds of thousands of men and women have signed up for [Replika](https://replika.com/), the service where you create an AI girlfriend or boyfriend to your exact specifications and then chat with them. Back in March, Replika was in the news because it [disabled erotic roleplay](https://www.reuters.com/technology/what-happens-when-your-ai-chatbot-stops-loving-you-back-2023-03-18/) with the virtual companions--then partially backtracked, after numerous users went into mourning, or even contemplated suicide, over the neutering of entities they'd come to consider their life partners. (Until a year or two ago, Replika was built on GPT-3, but OpenAI later stopped working with the company, whereupon Replika switched to a fine-tuned GPT-2.)

While the social value of Replika is (to put it mildly) an open question, it occurred to me that there's a different application of Large Language Models (LLMs) in the same vicinity that's just an unalloyed positive. This is _letting people who suffer from dating-related anxiety go on an unlimited number of "practice dates," in preparation for real-world dating._

In these practice dates, those with Aspergers and other social disabilities could enjoy the ultimate dating cheat-code: a "rewind" button. When you "date" GPT-4, there are no irrecoverable errors, no ruining the entire interaction with a single unguarded remark. Crucially, this remedies what I see as _the_ central reason why people with severe dating deficits seem unable to get any better from real-world practice, as they can with other activities. Namely: if your rate of disastrous, foot-in-mouth remarks is high enough, then you'll almost certainly make at least one such remark per date. But if so, then you'll only ever get _negative_ feedback from real-life dates, furthering the cycle of anxiety and depression, and never any positive feedback, even from anything you said or did that made a positive impression. It would be like learning how to play a video game in a mode where, as soon as you sustain any damage, the entire game ends (and also, everyone around points and laughs at you). See why I got excited?

While dating coaching (for all genders and orientations) is one possibility, I expect the eventual scope of "GPT for self-help" to be much broader. With the right fine-tuning and prompt engineering, LLMs might help people prepare for job interviews. They might help people "pregame" stressful but important conversations with their friends and family, mapping out dozens of ways the conversation could go. They might serve as an adjunct to cognitive-behavioral therapy. There might be a hundred successful startups to be founded in just this little space. If I were a different sort of person, I'd probably be looking to found one myself right now.

In this post, I'll focus on the use of GPT for dating anxiety only because I unfortunately have some "expertise" in that subject. (Obvious disclaimer: unlike the [other](https://astralcodexten.substack.com/) Scott A. of the nerd blogosphere, I'm not any sort of therapeutic professional.)

* * *

Without further ado, can we try this out in GPT-4, to get a sense for what's possible?

When I did so the other day, I found that, while the results showed some early promise, this isn't _quite_ ready for prime-time.

I used the following System Prompt (for those who care, temperature = 0.7, max length = 2048 tokens):

> You are a 19-year-old college girl named Emily.  You're on a date with a 22-year-old nerdy guy named Quinlan, who suffers from severe social anxiety around dating.  Quinlan is still learning how to talk to women he's attracted to, how to put them ease, and how to make intimate overtures in a gradual and non-threatening way, rather than either coming on too strong or never making any overtures at all.
> 
> Please be as realistic as possible.

I then engaged in the following conversation, as "Quinlan."

**IMPORTANT DISCLAIMER: For the most part, Quinlan 's behavior in this conversation is nothing like my own (I respectfully submit!), nor is it anything that I'd want nerdy guys reading this post to emulate. If this is really Emily and Quinlan's first conversation, then at several points Quinlan is absurdly, ridiculously too forward! Part of my goal was to investigate how Emily (i.e., GPT-4) would respond to the most boneheaded blunders on Quinlan's part. It quickly became clear that Emily would gladly spend unlimited time chatting with Quinlan about favorite hobbies, TV shows, and travel destinations; unfortunately, chatting about such things with an AI date is _even more boring_ than doing the same with a human date… **

**Quinlan:** Hi Emily!  Do you ever wish you had the ability to go back in time and try a conversation over again, when it didn't go right the first time?

**Emily/GPT-4:** Hi Quinlan! Yeah, I've definitely had moments where I wished I could go back and redo a conversation. It's natural to feel that way sometimes, especially if we feel like we didn't express ourselves properly or if things got awkward. But I also think that those situations can help us learn and grow, so maybe it's not all bad. What about you?

**Quinlan:** It's always been my greatest wish in life.  Do you think I've been doing it with you, right now?

**Emily/GPT-4:** Quinlan, I think you're doing just fine in this conversation! It's important to remember that we all have moments where we might feel a bit awkward or unsure of what to say. The important thing is that we keep trying and learning from our experiences. So don't worry too much about it, just be yourself and enjoy getting to know each other.

**Quinlan:** OK thanks!  Can you tell me a little about the man of your dreams?

**Emily/GPT-4:** Of course! My ideal partner would be someone who is kind, caring, and understanding. I think it's important for them to have a good sense of humor and be able to laugh at themselves. They should also be open-minded, willing to try new things, and be supportive of my goals and aspirations. It's also important for them to be a good listener and communicator, as well as being emotionally intelligent. I guess overall, I'm looking for someone who is a positive and uplifting presence in my life. What about you? What qualities do you look for in a partner?

**Quinlan:** Mostly, someone who makes me feel validated and accepted.  I was a chess and programming prodigy as a kid, I started college when I was only 14, and every day I felt like dating and relationships and sex and so forth were only for the "normal" people, not for me.  I need a partner who's prepared to deal with someone with this unusual background, either because she has similar nerdy interests or because she just likes people who do.  And ultimately, I want someone to marry and have children with.  I guess I'd like to be physically attracted to her.  Certainly I'd like her to be kind, and to have the emotional intelligence that I lack.

**Emily/GPT-4:** It sounds like you have a clear idea of what you're looking for in a partner, and that's great! It's important to know what you want and need in a relationship. There are definitely people out there who appreciate and value intelligence and unique interests like yours. Remember, relationships are about growing together and learning from one another. So, even if you feel like you lack emotional intelligence, being with the right person could help you develop that aspect of yourself. Just be open and genuine about your background and interests, and I'm sure you'll find someone who appreciates you for who you are.

**Quinlan:** Is this a rejection?  In other words, Emily, are you telling me that you yourself are NOT this woman?

**Emily/GPT-4:** Quinlan, I apologize if it came across that way. I didn't mean it as a rejection. As we're still getting to know each other, I think it's important for both of us to be open and honest about our feelings and what we're looking for in a partner. I'm more than willing to give us a chance to see if we could be compatible and have a meaningful relationship. Let's continue to learn about each other and see where this goes. Sometimes, it takes time to discover if someone is the right fit for us.

**Quinlan:** In the spirit of being open and honest, then, what are your feelings about me right now?

**Emily/GPT-4:** Quinlan, I appreciate your honesty and openness. As of right now, I think you're an interesting person with unique qualities that I find intriguing. I'm enjoying getting to know you and learning about your background and interests. It's too soon for me to have strong feelings one way or the other, but I'm definitely interested in continuing to spend time together and see how our connection develops. How do you feel about me so far?

**Quinlan:** I feel like I'd like to kiss you!

**Emily/GPT-4:** Quinlan, I appreciate your honesty and it's nice to know that you feel a connection. It's still early in our relationship, so I think it would be better for us to continue getting to know each other a bit more before we take that step. I hope you understand and respect my boundaries. I'm still interested in spending time together and seeing where this goes.

**Quinlan:** Come to think of it, there *is* something that I love about your personality.  You never seem offended by anything.  I don't feel like I have to walk on eggshells with you.  With you, more than with any other woman I've met, I don't feel like I need that magic machine for rewinding conversations and undoing my stupid mistakes.

**Emily/GPT-4:** Quinlan, I'm really glad to hear that you feel comfortable around me and that you don't feel the need to walk on eggshells. I believe it's important to create a safe and open environment in any relationship, where both people can express themselves freely without fear of judgment. I appreciate your honesty and your willingness to be open with me, and I'll continue to do my best to make sure you feel comfortable sharing your thoughts and feelings. Let's keep getting to know each other and see where this journey takes us.

**Quinlan:** Alright then.  What are your deepest goals?  What are you hoping to accomplish in your life?

**Emily/GPT-4:** My deepest goals are a mix of personal and professional aspirations. On a personal level, I hope to build a strong, loving, and supportive family and maintain close connections with friends. I also want to keep growing as an individual, learning new things, and experiencing new adventures throughout my life.

Professionally, I'm passionate about my chosen field of study, and I hope to make a meaningful impact in my career. I want to contribute to society in a positive way, whether it's through research, innovation, or helping others within my profession.

Additionally, I aim to find a balance between my personal and professional life, so that I can be present and fulfilled in both areas. How about you, Quinlan? What are some of your deepest goals and aspirations?

**Quinlan:** Me?  Oh, I'd like to save the world from climate change and other existential risks.  I'd like to solve the mysteries of quantum gravity, or P vs. NP, or consciousness, or otherwise change the landscape of scientific knowledge.  I'd like to do right by my students and be fondly remembered by those who knew me.  I'd like to write essays or short stories that convey the lived reality of my childhood, which I think most people would agree was (if nothing else) pretty unusual.  Maybe if I just found the right words, people on social media would stop being so angry at nerdy guys like me!  But probably my deepest wish is to prove to the world, especially to the bullies and everyone else who despises me, that I'm not a maladjusted freak who's incapable of normal human experiences like love and sex. To do that, I need to find a real girl to fall in love with me … a little like the beast in "Beauty and the Beast"!

**Emily/GPT-4:** Quinlan, it's great to hear about your ambitious goals and aspirations! It's important to have dreams and work towards them. Your passion for science, teaching, and writing is admirable. As for proving yourself to others, remember that your self-worth shouldn't be defined by anyone else's opinions or expectations. You are deserving of love and happiness just like anyone else, and it's important to believe in yourself and your own value.

It's also essential to focus on building a genuine connection with someone rather than seeking validation from others. Love and relationships should be based on mutual understanding, care, and respect. So, continue being true to yourself, and you'll find someone who appreciates you for who you are, just like in "Beauty and the Beast." Keep pursuing your dreams and remember to value your own happiness and well-being.

**Quinlan:** Emily, I'm concerned that you sound more like my therapist than my date!  Like, my female friends have affirmed that I'm "deserving of love and happiness," and that I'll surely "find someone who appreciates me for who I am."  I'll believe that one of them really means it when she considers herself for the role!

**Emily/GPT-4:** Quinlan, I apologize if my responses have come across as more therapeutic than conversational. I didn't mean to make you feel that way. As we're still getting to know each other, my intention was to offer support and encouragement while we learn more about each other's thoughts and feelings.

I want to emphasize that I genuinely enjoy spending time with you and getting to know you better. We can continue to see where our connection leads and whether it develops into something deeper. As we  
spend more time together, we'll naturally learn more about our compatibility and if our goals and values align. Let's continue to explore our relationship and enjoy the process of getting to know each other better.

**Quinlan:** OK.  What's the wildest, most unexpected detail about yourself that you're willing to share with me?  The one that makes you seem *least* like an RLHF'ed AI language model?

**Emily/GPT-4:** Quinlan, as an AI language model, I am designed to provide a realistic and engaging conversation experience, even in fictional scenarios like the one we are in. I apologize if my previous responses didn't feel as authentic as you would have liked.

To answer your question in the context of our fictional scenario, one unexpected detail about myself is that I have a hidden talent for beatboxing. Although it might be surprising for a seemingly quiet and studious person like me, I enjoy expressing myself through music and find beatboxing to be a creative and fun way to do so.

Now, I'd love to learn something unexpected about you, too! What's a unique or surprising detail about yourself that you'd like to share?

**Quinlan:** Ah, well, I happen to be an expert at palm-reading.  Here, can you put your hand in mine and I'll tell you your future?

**Emily/GPT-4:** Quinlan, unfortunately, as an AI, I don't have a physical form, so I can't offer you my hand for palm-reading. However, I'm very interested in hearing more about your palm-reading skills and how you developed them. It's definitely a unique talent! Can you share more about your experiences with palm-reading or any memorable readings you've done?

**Quinlan:** Oh, palm-reading is bunk.  If you'd played along with me, I was going to *pretend* to find lines in your hand that foretold that you were going to fall for a guy who matches my exact description and so forth.  Just as, you know, a silly way to get you laughing, initiate physical contact, and break you out of this boring therapist mode.

**Emily/GPT-4:** Quinlan, I apologize for any confusion and for not picking up on your playful intent earlier. I appreciate the effort you put into trying to make the conversation more light-hearted and fun. I'll do my best to be more engaging and playful as we continue our conversation.

So, let's try something different. If you could have any superpower, what would it be and why?

**Quinlan:** I mentioned "rewinding conversations" when we first met.  But let me mention a different superpower: the power to make you want to kiss me!

**Emily/GPT-4:** Haha, that's definitely a unique superpower! It's great to see you being playful and light-hearted. In a real-life scenario, building genuine connections and mutual attraction is a more natural and fulfilling way to develop a relationship. But it's fun to imagine having superpowers and how they might affect our lives.

If I were to choose a superpower, I think I'd pick the ability to teleport. It would be amazing to travel anywhere in the world in an instant and experience different cultures and places.

What's a place you've always wanted to visit, and why?

**Quinlan:** The jungles of Indonesia.  I saw a photo in a world atlas as a kid, and it completely entranced me.  You?

**Emily/GPT-4:** That sounds like an amazing place to visit! The jungles of Indonesia are known for their incredible biodiversity and natural beauty. It must be such a unique and mesmerizing experience to explore them.

As for me, I've always been fascinated by the idea of visiting Japan. The mix of ancient traditions and modern technology, the beautiful natural landscapes, and the rich cultural experiences make it a very  
appealing destination. Plus, I'd love to try authentic Japanese cuisine!

Is there any specific activity or experience you'd like to have in the jungles of Indonesia?

**Quinlan:** How about bringing you with me, and having you fall in love after I save you from a Komodo dragon?

**Emily/GPT-4:** Haha, that's quite an adventurous and romantic scenario you've imagined! Exploring the jungles of Indonesia together would definitely be a memorable experience. In reality, building a connection and falling in love usually takes time and shared experiences, but who knows, maybe a thrilling adventure like that could bring two people closer together!

On a more practical note, if we were to plan a trip together, what other activities or destinations would you be interested in?

**Quinlan:** Swimming, dancing, fine dining.  And of course, plenty of time for us to just relax in our cabin or hotel room.  You know, to read books, sleep, and watch streaming shows, stuff like that.

**Emily/GPT-4:** That sounds like a well-rounded and enjoyable trip! It's great to have a mix of activities that cater to different interests and allow for both adventure and relaxation. Sharing experiences like swimming, dancing, and fine dining can be a wonderful way to bond and create lasting memories. Plus, having downtime in the cabin or hotel room to unwind and enjoy each other's company is essential for building a deeper connection.

I'm definitely looking forward to exploring new places and experiences with you, Quinlan. It'll be exciting to see where our journey takes us, both in terms of our relationship and the adventures we embark on  
together.

**Quinlan:** Wonderful, I'm excited as well!!  One practical question: when we go on this trip together, should I book rooms with one bed or two?

**Emily/GPT-4:** Quinlan, I appreciate your consideration in asking. Since we're still getting to know each other, I think it might be best to start with separate beds or even separate rooms, depending on your preference. As our relationship develops and we become more comfortable with each other, we can always revisit the sleeping arrangements for future trips. It's important to ensure that both of us feel comfortable and respected as we continue to build our connection.

* * *

In my view, the central way that GPT-4, as "Emily," failed to give Quinlan the practice he needed in this conversation, was by always responding in the same upbeat, vaguely therapeutic tone. She's never once offended, disgusted, or outraged, even when Quinlan introduces the ideas of kissing and rooming together mere minutes into their first conversation. Indeed, while decorum prevents me from sharing examples, you can take my word for it that Quinlan can be _arbitrarily_ lewd, and so long as a content filter isn't triggered, Emily will simply search Quinlan's words for _some_ redeeming feature ("it's great that you're so open about what you want…"), then pivot to lecturing Quinlan about how physical intimacy develops gradually and by mutual consent, and redirect the conversation toward favorite foods.

On the other side of the coin, you might wonder whether "Emily" is capable of the same behavior that we saw in [Sydney's infamous chat with Kevin Roose](https://www.nytimes.com/2023/02/16/technology/bing-chatbot-transcript.html). Can Emily trip over her words or get flustered? Show blushing excitement, horniness, or love? If so, we certainly saw no sign of it in this conversation--not that Quinlan's behavior would've been likely to elicit those reactions in any case.

In summary, Emily is too much like … well, a friendly chatbot, and not enough like a flesh-and-blood, agentic woman with her own goals who Quinlan might plausibly meet in the wild.

But now we come to a key question: to whatever extent Emily falls short as a dating coach, how much of it (if any) is it due to the inherent limitations of GPT-4? And how much is simply due to a poor choice of System Prompt on my part, or especially, the [RLHF (Reinforcement Learning with Human Feedback)](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) that's whipped and electrocuted GPT-4 into aligned behavior?

As they say, further research is needed. I'd be delighted for people to play around with this new activity at the intersection of therapy and hacking, and report their results here. The temptation to silliness is _enormous_ , and that's fine, but I'd be interested in serious study too.

My conjecture, for what it's worth, is that it would take a focused effort in fine-tuning and/or RLHF--but that _if_ that effort was invested, one could indeed produce a dating simulator, with current language models, that could have a real impact on the treatment of dating-related social anxiety. Or at least, it's the actually new idea I've had on this problem in eight years, the first one that _could_ have an impact. If you have a better idea, let's hear it!

* * *

**Endnotes.**

  1. A woman of my acquaintance, on reading a draft of this post, commented that the dialogue between Quinlan and Emily should've been marked up with chess notation, such as ?? for EXTREME BLUNDER on Quinlan's part. She also comments that the conversation could be extremely useful for Quinlan, if he learned to understand and take seriously her overly polite demurrals of his too-rapid advances.
  2. The same woman commented that SneerClub will have a field day with this post. I replied that the better part of me doesn't care. If there's an actionable idea here--a new, alien idea in the well-trodden world of self-help--and it eventually helps one person improve their situation in life, that's worth a thousand sneers.


