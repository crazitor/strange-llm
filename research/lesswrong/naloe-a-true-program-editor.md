---
title: "Naloe: A True Program Editor"
author: "TristanTrim"
date: "2026-02-25"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/ccqHbHccuTeDmWsTA/naloe-a-true-program-editor"
score: 7
votes: 5
---

When I was younger and ever so slightly more idealistic I dreamed of making a programming editor that didn't suck. I was going to call it "Naloe" and provide many bacronyms to explain the name. In the nature of young idealistic programmers, I allowed the scope of the idea to creep horribly out of control. But I still love many of those ideas. 

In responding to [Is Building Good Note-Taking Software an AGI-Complete Problem?](https://www.lesswrong.com/posts/34J5qzxjyWr3Tu47L/is-building-good-note-taking-software-an-agi-complete#), I started typing out some of those ideas and it became so long I decided to post it as a stand alone post, so without further ado here is a list of ideas about Naloe, the first true program editor:

1.  Programs are running processes. The text code is the thing that bootstraps the program into running, but it is not the program. As such, no (good) program editors exist today, and programmers are forced to work with text editors or integrated development environments to modify dead text that becomes a program. Bret Victor has a lot of related ideas, especially inspiring is "[Stop Drawing Dead Fish](https://www.youtube.com/watch?v=ZfytHvgHybA)", although it is obviously, as with Naloe, wildly ambitious and idealistic.
2.  Question: Since the code is not the proper representation of a program, what is the proper representation? Answer: There is no proper representation. The program is coordinated transistor states. Anything you see is necessarily an abstract symbolic representation created to help you understand and control the dance of those transistors. These representations, in Naloe, are called "guises" and a programmer feel free and capable of switching guises on the fly to perform different operations understanding and altering programs.
3.  This makes a clear distinction surrounding "booting", "recovery", and "running" programs. If a program is thought of as something launched from an executable or interpreted from code, then it is natural to think only of editing the program code, but once editing the running program becomes a part of programming, this creates a problem? How is the program supposed to start up again if it is terminated? The answer is that Naloe should focus on making the lifecycle of a program explicit. Programs are living and have living "recovery plans" as a part of themselves.
    1.  These "recovery plans" should be explicit and should be informed by the guise the programmer used to create the program they are now working with.
    2.  Alterations to a running program must explicitly modify or leave the recovery plan unchanged. This is true whether it is a programmer or other program modifying the running program.
    3.  A programmer should never lose a data structure they valued because the program they were working with crashed. This is true whether the programmer values that data because it took their computer time to make, took them time to make, recorded unrecoverable past states of reality, or just cause they think that data is cute and they want to keep it around.
4.  Any guise can be put on any aspect of any program. It is up to programmers to determine which guises are appropriate for what programs and structures.
5.  With no preconceptions on what guises are appropriate, understanding a program would be the same as reverse engineering it. So we might speak of tags and views.
    1.  A view is a program that coordinates guises giving a programmer a view into some aspect of some particular program or kind of program.
    2.  A tag is something attached to or referencing another part of a programs structure. Tags may be added by programmers, like comments, to inform programmers or views how which guises might be useful for examining programs or their data structures.
6.  Tags, views, and guises are all themselves programs, and as such should be worked with using tags, views, and guises.
7.  Programs run differently depending on how closely you're looking at them. They run slower. Hooks put in to feed guises have a cost. This is explicit.
    1.  As with everything in Naloe, increasing and decreasing the amount of hooks should be possible dynamically.
8.  The interface is the most important program. The interface responsiveness should be sacrificed for another program only when the programmer explicitly requests it.
9.  Since data can be viewed with different guises in cohesive views, all user applications could be views within Naloe, and as such, could be modified and worked with in the same ways accessible when working with any other program.
10.  Programs do not exist on a single computer. What computers and hardware a programmer and their programs have access to, and where and how those programs are running, should also be represented and controllable with guises.