---
title: "Generative AI as Shakespearean tragedy"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/generative-ai-as-shakespearean-tragedy"
---

[](https://substackcdn.com/image/fetch/$s_!smEH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8d2a331-e5d2-4601-bf5c-3ca8b3d629d3_987x1026.jpeg)“hubris and the tragedy of generative AI“

You may have read yesterday’s [New York Times report](https://www.nytimes.com/2024/04/06/technology/tech-giants-harvest-data-artificial-intelligence.html) by Cade Metz and others on how many of the biggest AI companies have been cutting ethical corners in a race to gather as much data as possible (“OpenAI, Google and Meta ignored corporate policies, altered their own rules and discussed skirting copyright law as they sought online information to train their newest artificial intelligence systems”). 

All this happened upon the realization that their systems simply cannot succeed without even more data than the internet-scale data they have already been trained on. 

Maybe the starkest image there is OpenAI’s then-president Greg Brockman personally working on lining up YouTube videos to download and transcribe—very likely knowing that he was entering a legal grey area—yet desperate to feed the beast. If it all falls apart, either for legal reasons or technical reasons, that image may linger. 

Both the _Times_ and _Wall Street Journal_ also covered the current race to synthetic data. I had foreseen all of this — both the data guzzling and the need for synthetic data — in my 2018 paper [Deep Learning: A Critical Appraisal](https://arxiv.org/abs/1801.00631). As Jason Pontin concisely put it in an opinion essay in WIRED, maybe the only mainstream outlet to take note at the time, the thrust of my critique was that Deep Learning was “[Brittle, Greedy, Opaque, and Shallow”. ](https://www.wired.com/story/greedy-brittle-opaque-and-shallow-the-downsides-to-deep-learning/)

Fast forward six years, and those problems are _exactly_ what is ailing GenAI today: the brittleness (a term for unreliability); the greed for data that is causing the desperation that the Times described; the opacity (uninterpretability) that makes debugging, fairness, and engineering so hard; and the shallowness, meaning that generalizations are never complete.

What makes all this tragic is that many of us have tried so hard to warn the field that we would wind up here, and people like LeCun (who haughtily declared that my 2018 critique was “mostly wrong”, moments after it posted) have been routinely dismissive, both of my critiques (often co-authored with Ernest Davis) and others, such as concerns about AI and bias and social injustice, rightfully and repeatedly raised by researchers such as Latanya Sweeney, Timnit Gebru, Kate Crawford, Abeba Birhane, and Margaret Mitchell.

In my own case, it feels as if literally everything I have been warning about is finally coming home to roost:

  * 2001: [𝗛𝗮𝗹𝗹𝘂𝗰𝗶𝗻𝗮𝘁𝗶𝗼𝗻𝘀](https://mitpress.mit.edu/9780262632683/the-algebraic-mind/), and core problems with 𝗮𝗯𝘀𝘁𝗿𝗮𝗰𝘁𝗶𝗼𝗻 𝗮𝗻𝗱 𝗿𝗲𝗮𝘀𝗼𝗻𝗶𝗻𝗴.

  * 2014: (w Ernest Davis) [𝗧𝗵𝗲 𝗲𝗰𝗵𝗼 𝗰𝗵𝗮𝗺𝗯𝗲𝗿 𝗲𝗳𝗳𝗲𝗰𝘁](https://www.nytimes.com/2014/04/07/opinion/eight-no-nine-problems-with-big-data.html) that threatens to contaminate the web. 

  * 2015 (w Ernest Davis) The [need for research focus on 𝗰𝗼𝗺𝗺𝗼𝗻 𝘀𝗲𝗻𝘀𝗲 and 𝗽𝗵𝘆𝘀𝗶𝗰𝗮𝗹 𝗿𝗲𝗮𝘀𝗼𝗻𝗶𝗻𝗴.](https://dl.acm.org/doi/pdf/10.1145/2701413)

  * 2016: [𝗘𝗱𝗴𝗲 𝗰𝗮𝘀𝗲𝘀 as the undoing of driverless cars](https://www.edge.org/conversation/gary_marcus-is-big-data-taking-us-closer-to-the-deeper-questions-in-artificial).

  * 2018: [𝗕𝗿𝗶𝘁𝘁𝗹𝗲𝗻𝗲𝘀𝘀/𝘂𝗻𝗿𝗲𝗹𝗶𝗮𝗯𝗶𝗹𝗶𝘁𝘆 and 𝗣𝗼𝘁𝗲𝗻𝘁𝗶𝗮𝗹 𝗽𝗹𝗮𝘁𝗲𝗮𝘂𝘀](https://arxiv.org/abs/1801.00631) because of problems with abstraction and reasoning etc.

  * 2018: The [𝗱𝗮𝘁𝗮-𝗴𝘂𝘇𝘇𝗹𝗶𝗻𝗴](https://arxiv.org/abs/1801.00631), leading to the desperate need for data that the NYT just reported, along with obscene corner-cutting and rampant copyright issues.

  * 2019/2020: The way in which[ 𝗟𝗟𝗠s](https://x.com/GaryMarcus/status/1221178444769161217) inherited all of the above liabilities from prior deep learning architectures.

  * 2022: [𝗟𝗟𝗠-𝗱𝗿𝗶𝘃𝗲𝗻 𝗽𝗼𝗹𝗹𝘂𝘁𝗶𝗼𝗻 𝗼𝗳 𝘁𝗵𝗲 𝗲𝗰𝗼𝘀𝗽𝗵𝗲𝗿𝗲](https://garymarcus.substack.com/p/ais-jurassic-park-moment) threatening trust and democracy.




It’s all happening now. Every single point was originally ignored or dismissed (often most vocally by LeCun, who for example called my initial characterization of reasoning failures in LLM’s a “rear-guard action”).

Not one of these problems has been adequately addressed.

Today we are left with two things:

• an intellectual monoculture — with no alternative approach that is nearly as well-funded.

• a pile of unreliable systems that are unlikely to live up to the hype.

Only with a more open-minded field can we hope to make progress. 

We must invest heavily in alternative approaches and stop funding a losing hand to the infinite degree, crowding everything out. 

[Share](https://garymarcus.substack.com/p/generative-ai-as-shakespearean-tragedy?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** desperately hopes the field of AI will again start to welcome fresh ideas._

_._
