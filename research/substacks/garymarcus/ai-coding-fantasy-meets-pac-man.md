---
title: "AI Coding Fantasy meets Pac-Man"
author: "Gary Marcus"
date: ""
source: "substack_garymarcus"
url: "https://garymarcus.substack.com/p/ai-coding-fantasy-meets-pac-man"
---

Last week[ I dissected Kevin Roose’s claims that neophytes would soon be able to build the software of their dreams without knowing how to write a line of code](https://garymarcus.substack.com/p/decoding-and-debunking-hard-forks), and also criticized Roose (and his Hard Fork sidekick Casey Newton) for drinking Anthropic’s “code-will-all-be-written by machines” hyperbole. 

Anthropic’s CEO Dario Amodei obviously failed to read my rebuttal. A few days ago he triumphantly claimed (without evidence) that [nearly all code would be written by AI within the next year](https://x.com/slow_developer/status/1899430284350616025?s=61):

[](https://substackcdn.com/image/fetch/$s_!0OhA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2a19fea-ccf9-43ba-b87b-e755b36ad11e_1363x1361.png)

§

I am kicking myself now for going too easy on both. I think most or all of the points I made – about challenges in building and debugging novel systems with sufficient generality- will stand the test of time. 

But, wow, [The Guardian really just went me one better](https://www.theguardian.com/games/2025/mar/11/ai-pac-man-clones-reviewed-grok?CMP=oth_b-aplnews_d-1). 

An enterprising reporter there, Rich Pelley, decided to put all these no-coding knowledge claims to a test. And I don’t mean a _hard_ test – like asking newbies to build a new real-time, networked air traffic control system – I mean an _easy_ test. The reporter asked seven people to build a clone of the 1980 arcade bestseller [Pac-Man](https://en.wikipedia.org/wiki/Pac-Man) – a low resolution, 2D graphics game that absolutely pales in algorithmic complexity compared to almost any modern video game.

[](https://substackcdn.com/image/fetch/$s_!HN3Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f40d7cc-d278-4479-a3e1-99ebabc794e4_224x288.png)

Remember it? Yellow character, controlled by person wanders maze, ghosts chase yellow user character; that’s pretty much it. The entire game play can be [described in a page](https://www.geekslop.com/old-school/2020/the-logic-and-programming-behind-pac-man-all-the-crazy-cool-stuff-you-ever-wanted-to-know-about-how-the-classic-pac-man-game-works-under-the-hood). 

You would _think_ this job (not even asking for variants like extra ghosts would be easy. I don’t want spoil all [the fun](https://www.theguardian.com/games/2025/mar/11/ai-pac-man-clones-reviewed-grok?CMP=oth_b-aplnews_d-1), but … things didn’t go well:

[](https://substackcdn.com/image/fetch/$s_!80Ta!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7352a9f0-c616-4ba9-8db1-c2497177ad34_1718x1550.jpeg)

To be sure, most or all trained coders will (if they are not already) soon use AI as a part of their workflow. As a fantastic, souped-up version of autocomplete, AI coding tools somewhat increase productivity. They can help a coder learn a new API, or maybe even a new programming language. But current AI tools don’t replace an understanding of debugging, nor an understanding of system architecture, nor an understanding of what clients want. And they don’t magically resolve the challenges of maintaining complex code bases over time. In some instances, an overdependence on the new tools will lead beginners to make giant mountains of difficult-to-maintain spaghetti code; security will be an issue as well. The idea that coders (and more generally, software architects) are on their way out is absurd. AI will be a tool to help people write code, just as spell-checkers are a tool to help authors write articles and novel, but AI will not soon replace people who understand how to conceive of, write, and debug code. 

If you can’t get Pac-Man right in 2025 (full original source code to the Atari 2600 version [available on github](https://github.com/DillonDepeel/Pacman-Source-Code)[1](https://garymarcus.substack.com/p/ai-coding-fantasy-meets-pac-man#footnote-1-158921170)), how on earth are you going to build the next high-quality Zelda clone next year?

[Share](https://garymarcus.substack.com/p/ai-coding-fantasy-meets-pac-man?utm_source=substack&utm_medium=email&utm_content=share&action=share)

 _**Gary Marcus** is enjoying this week’s third anniversary of “Deep learning is hitting a wall”, and will write an update if he can find the time._

[1](https://garymarcus.substack.com/p/ai-coding-fantasy-meets-pac-man#footnote-anchor-1-158921170)

The Atari source code is written in 6502 assembly language, one of the first programming languages I ever learned. My guess is that current AI coding tools would struggle to use 6502 well, for multiple reasons, including a lack of high-level libraries, fewer Stack Overflow queries to rely on, and a greater needed for the coding tool to understanding high level architectural concerns that might be side-stepped in higher level languages. (Want to know what coders then had to deal with back then? Check out[ ](https://bogost.com/books/video_computer_system/)_[Racing The Beam.](https://bogost.com/books/video_computer_system/)_)
