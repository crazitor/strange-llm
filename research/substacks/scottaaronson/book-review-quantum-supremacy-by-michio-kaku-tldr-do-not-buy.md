---
title: "Book Review: “Quantum Supremacy” by Michio Kaku (tl;dr DO NOT BUY)"
author: "Scott Aaronson"
date: "Fri, 19 May 2023"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=7321"
---

**Update (June 6):** I wish to clarify that I did not write any of the dialogue for the "Scott Aaronson" character who refutes Michio Kaku's quantum computing hype in [this YouTube video](https://www.youtube.com/watch?v=JEEwDIkQY-Y), which uses an AI recreation of my voice. The writer appears to be physics/math blogger and podcaster Hassaan Saleem; [see his website here](https://hassaansaleem.com/). Luckily, the character and I do share many common views; I'm sure we'd hit it off if we met.

* * *

When I was a teenager, I enjoyed reading _[Hyperspace](https://www.amazon.com/Hyperspace-Scientific-Parallel-Universes-Dimension/dp/0385477058)_ , an early popularization of string theory by the theoretical physicist Michio Kaku. I'm sure I'd have plenty of criticisms if I reread it today, but at the time, I liked it a lot. In the decades since, Kaku has widened his ambit to, well, pretty much everything, regularly churning out popular books with subtitles like "How Science Will Revolutionize the 21st Century" and "How Science Will Shape Human Destiny and Our Daily Lives." He's also appeared on countless TV specials, in many cases to argue that UFOs likely contain extraterrestrial visitors.

Now Kaku has a new bestseller about quantum computing, creatively entitled _[Quantum Supremacy](https://www.amazon.com/Quantum-Supremacy-Computer-Revolution-Everything/dp/0385548362)_. He even [appeared on Joe Rogan](https://ogjre.com/episode/1980-michio-kaku) a couple weeks ago to promote the book, surely reaching an orders-of-magnitude larger audience than I have in two decades of trying to explain quantum computing to non-experts. (Incidentally, to those who've asked why Joe Rogan hasn't invited _me_ on his show to explain quantum computing: I guess you now have an answer of sorts!)

In the spirit, perhaps, of the TikTokkers who eat live cockroaches or whatever to satisfy their viewers, I decided to oblige loyal _Shtetl-Optimized_ fans by buying _Quantum Supremacy_ and reading it. So I can now state with confidence: beating out a crowded field, this is **the worst book about quantum computing,** for some definition of the word "about," that I've ever encountered.

Admittedly, it's not obvious why I'm reviewing the book here at all. Among people who've heard of this blog, I expect that approximately zero would be tempted to buy Kaku's book, at least if they flipped through a few random pages and saw the … _level of care_ that went into them. Conversely, the book's target readers have probably never visited a blog like this one and never will. So what's the use of this post?

Well, as the accidental #1 quantum computing blogger on the planet, I feel a sort of grim obligation here. Who knows, maybe this post will show up in the first page of Google results for Kaku's book, and it will manage to rescue two or three people from the kindergarten of lies.

* * *

Where to begin? Should we just go through _the first chapter_ with a red pen? OK then: on the very first page, Kaku writes,

> Google revealed that their Sycamore quantum computer could solve a mathematical problem in 200 seconds that would take 10,000 years on the world's fastest supercomputer.

No, the "10,000 years" estimate was [quickly falsified](https://scottaaronson.blog/?p=4372), as anyone following the subject knows. I'd be the first to stress that the situation is complicated; compared to the best currently-known classical algorithms, some quantum advantage remains for the Random Circuit Sampling task, depending on how you measure it. But to repeat the "10,000 years" figure at this point, with no qualifications, is actively misleading.

Turning to the second page:

> [Quantum computers] are a new type of computer that can tackle problems that digital computers can never solve, even with an infinite amount of time. For example, digital computers can never accurately calculate how atoms combine to create crucial chemical reactions, especially those that make life possible. Digital computers can only compute on digital tape, consisting of a series of 0s and 1s, which are too crude to describe the delicate waves of electrons dancing deep inside a molecule. For example, when tediously computing the paths taken by a mouse in a maze, a digital computer has to painfully analyze each possible path, one after the other. A quantum computer, however, _simultaneously_ analyzes all possible paths at the same time, with lightning speed.

OK, so here Kaku has already perpetuated two of the most basic, forehead-banging errors about what quantum computers can do. In truth, anything that a QC can calculate, a classical computer can calculate as well, _given exponentially more time_ : for example, by representing the entire wavefunction, all 2n amplitudes, to whatever accuracy is needed. That's why it was understood from the very beginning that quantum computers can't change what's computable, but only how _efficiently_ things can be computed.

And then there's the Misconception of Misconceptions, about how a QC "analyzes all possible paths at the same time"--with no recognition anywhere of the central difficulty, the thing that makes a QC enormously _weaker_ than an exponentially parallel classical computer, but is also the new and interesting part, namely that you only get to see a _single, random outcome_ when you measure, with its probability given by the Born rule. That's the error so common that I warn against it right below the title of my blog.

> [Q]uantum computers are so powerful that, in principle, they could break all known cybercodes.

Nope, that's strongly believed to be false, just like the analogous statement for _classical_ computers. Despite its obvious relevance for business and policy types, the entire field of [post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography)--including the [lattice-based public-key cryptosystems](https://en.wikipedia.org/wiki/Lattice-based_cryptography) that have by now survived 20+ years of efforts to find a quantum algorithm to break them--receives just a single vague mention, on pages 84-85. The possibility of cryptography surviving quantum computers is quickly dismissed because "these new trapdoor functions are not easy to implement." (But they _[have](https://cloud.google.com/blog/products/identity-security/why-google-now-uses-post-quantum-cryptography-for-internal-comms)_ been implemented.)

* * *

There's no attempt, anywhere in this book, to explain how any quantum algorithm actually works, let alone is there a word anywhere about the _limitations_ of quantum algorithms. And yet there's still enough said to be wrong. On page 84, shortly after confusing the concept of a [one-way function](https://en.wikipedia.org/wiki/One-way_function) with that of a [trapdoor function](https://en.wikipedia.org/wiki/Trapdoor_function), Kaku writes:

> Let N represent the number we wish to factorize. For an ordinary digital computer, the amount of time it takes to factorize a number grows exponentially, like t ~ eN, times some unimportant factors.

This is a double howler: first, trial division takes only ~√N time; Kaku has confused N itself with its _number of digits_ , ~log2N. Second, he seems unaware that much better classical factoring algorithms, like the [Number Field Sieve](https://en.wikipedia.org/wiki/General_number_field_sieve), have been known for decades, even though those algorithms play a central role in codebreaking and in any discussion of where the quantum/classical crossover might happen.

* * *

Honestly, though, the errors aren't the worst of it. The majority of the book is not even _worth_ hunting for errors in, because fundamentally, it's _filler_.

First there's page after page breathlessly quoting prestigious-sounding people and organizations--Google's Sundar Pichai, various government agencies, some report by Deloitte--about just how revolutionary they think quantum computing will be. Then there are capsule hagiographies of Babbage and Lovelace, Gödel and Turing, Planck and Einstein, Feynman and Everett.

And then the bulk of the book is actually about stuff _with no direct relation to quantum computing at all_ --the origin of life, climate change, energy generation, cancer, curing aging, etc.--except with ungrounded speculations tacked onto the end of each chapter about how quantum computers will someday revolutionize all of this. Personally, I'd say that

  1. Quantum simulation speeding up progress in biochemistry, high-temperature superconductivity, and the like is at least _plausible_ --though very far from guaranteed, since one has to beat the cleverest classical approaches that can be designed for the same problems (a point that Kaku nowhere grapples with).
  2. The stuff involving optimization, machine learning, and the like is almost entirely wishful thinking.
  3. Not once in the book has Kaku even _mentioned_ the intellectual tools (e.g., looking at actual quantum algorithms like Grover’s algorithm or phase estimation, and their performance on various tasks) that would be needed to distinguish 1 from 2.



* * *

In his acknowledgments section, Kaku simply lists a bunch of famous scientists he's met in his life--Feynman, Witten, Hawking, Penrose, Brian Greene, Lisa Randall, Neil deGrasse Tyson. Not a single living quantum computing researcher is acknowledged, not one.

Recently, I'd been cautiously optimistic that, after decades of overblown headlines about "trying all answers in parallel," "cracking all known codes," etc., the standard for quantum computing popularization was slowly creeping upward. Maybe I was just bowled over by [this recent YouTube video](https://www.youtube.com/watch?v=-UrdExQW0cs) ("How Quantum Computers Break the Internet… Starting Now"), which despite its clickbait title and its slick presentation, miraculously gets essentially everything right, shaming the hypesters by demonstrating just how much better it's possible to do.

Kaku's slapdash "book," and the publicity campaign around it, represents a noxious step backwards. The wonder of it, to me, is Kaku holds a PhD in theoretical physics. And yet the average English major who's written a "what's the deal with quantum computing?" article for some obscure link aggregator site has done a more careful and honest job than Kaku has. That's setting the bar about a millimeter off the floor. I think the difference is, at least the English major knows that they're supposed to _call_ an expert or two, when writing about an enormously complicated subject of which they're completely ignorant.

* * *

**Update:** I’ve now been immersed in the AI safety field for one year, let I wouldn’t consider myself _nearly_ ready to write a book on the subject. My knowledge of related parts of CS, my year studying AI in grad school, and my having created the subject of computational learning theory of quantum states would all be relevant but totally insufficient. And AI safety, for all its importance, has less than quantum computing does in the way of difficult-to-understand concepts and results that basically everyone in the field agrees about. And if I _did_ someday write such a book, I’d be pretty terrified of getting stuff wrong, and would have multiple expert colleagues read drafts.

In case this wasn’t clear enough from my post, Kaku appears to have had zero prior engagement with quantum computing, **and also** to have consulted zero relevant experts who could’ve fixed his misconceptions.
