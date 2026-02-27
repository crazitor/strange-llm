---
title: "Thanksgiving Special: D-Wave at MIT"
author: "Scott Aaronson"
date: "Thu, 22 Nov 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=291"
---

Some people think I have a vendetta against D-Wave Systems and its questionable quantum computer claims (see [here](https://scottaaronson.blog/?p=198), [here](https://scottaaronson.blog/?p=201), [here](https://scottaaronson.blog/?p=204), [here](https://scottaaronson.blog/?p=206), [here](https://scottaaronson.blog/?p=223), [here](https://scottaaronson.blog/?p=225), [here](https://scottaaronson.blog/?p=239), [here](https://scottaaronson.blog/?p=266), [here](https://scottaaronson.blog/?p=242) for context). But actually, nothing could be further from the truth. I keep trying and trying to change the subject! Wouldn't you all rather hear about [Wolfram](https://scottaaronson.blog/?p=284), I say? Or [unparadoxes](https://scottaaronson.blog/?p=285)? Or my #1 topic du jour, nothing whatsoever?

Apparently you wouldn't. From my inbox to my comments section to the hallway, the masses have spoken, and what they want to know is: _did I attend D-Wave 's presentation at MIT on Monday, and if so what did I think?_

Yes, I attended, in body though not in mind. You see, Monday was _also_ the day of the STOC deadline, so if our guests from D-Wave (Mohammad Amin and Andrew Berkley) were expecting a ferocious skeptic, they instead got a bleary-eyed zombie with visions of MAEXP, P/poly, and 7:59PM EST cavorting in his head.

This meant that Ed Farhi, Isaac Chuang, Peter Shor, and Lorenza Viola had to do most of the questioning. As it turned out, they did a vastly better job than I could have.

As others have [pointed out in stronger terms](http://dwave.wordpress.com/2007/11/09/a-picture-of-the-demo-chip/#comment-16231), I'm not a physicist. (On the other hand, the gentleman linked to in the previous sentence is _not_ correct about my being paid by the NSA to discredit Canadian quantum computing efforts: it's actually the GCHQ and the Mossad.) As such, I can't directly evaluate D-Wave's central claim to have built an adiabatic quantum computer, nor have I ever tried to do so. All I can do is point out the many things D-Wave has said to the press (about NP-complete problems, for example) that I _know_ are false, its history of making dramatic announcements without evidence, and its contemptuous attitude toward scientists who have asked for such evidence. For me, that's more than enough to destroy D-Wave's credibility on the claims I _can 't_ directly evaluate. After all, _the burden of proof is not on me; it 's on them._

However, other people have not been satisfied with this line of argument. "We don't care who the burden the proof is on," they say. "We just care whether D-Wave built an adiabatic quantum computer."

But my physicist colleagues don't suffer from the same argumentative limitations that I do. At the group meeting preceding the talk, Farhi announced that he didn't care what the press releases said, nor did he want to discuss what problems quantum computers can solve (since we academics can figure that out ourselves). Instead he wanted to focus on a single question: is D-Wave's device a quantum computer or not?

What followed was probably the most intense grilling of an invited speaker I've ever seen.

It quickly emerged that D-Wave wants to run a coherent quantum computation for microseconds, even though each of their superconducting qubits will have completely decohered within nanoseconds. Farhi had to ask Amin to repeat this several times, to make sure he'd gotten it right.

Amin's claim was that what looks like total decoherence in the computational basis is irrelevant -- since for adiabatic quantum computation, all that matters is what happens in the basis of energy eigenstates. In particular, Amin claimed to have numerical simulations showing that, if the temperature is smaller than the spectral gap, then one can do adiabatic quantum computation even if the conventional coherence times (the t1 and t2) would manifestly seem to prohibit it.

The physicists questioned Amin relentlessly on this one claim. I think it's fair to say that they emerged curious but severely skeptical, not at all convinced by the calculations Amin provided, and determined to study the issue for themselves.

In other words, this was science as it should be. In contrast to their bosses, Amin and Berkley made a genuine effort to answer questions. They basically admitted that D-Wave's press releases were litanies of hype and exaggeration, but nevertheless _thought_ they had a promising path to a quantum computer. On several occasions, they seemed to be struggling to give an honest answer that would still uphold the company line.

Two other highlights:

  * I asked Amin and Berkley whether they could give any evidence for any sort of speedup over classical simulated annealing. They laughed at this. "It's sixteen qubits!" they said. "_Of course_ you're not going to see a scaling effect with sixteen qubits."I said I understood perfectly well (though I wondered silently whether the dozens of journalists covering D-Wave's demo understood the same). But, I continued, surely you should be able to see a scaling effect by the end of 2008, when your business plan calls for 1024 qubits?"Well, that's what it says in the press release," they said.Forget about the press release, Farhi interjected. How many qubits are you _actually_ going to make?Amin and Berkley shrugged; they said they'd just try to make as many qubits as they could.


  * Even though it hadn't exhibited any sort of speedup, Amin and Berkley steadfastly maintained that their 16-qubit device was indeed a quantum computer. Their evidence was that simulations of its behavior that took quantum mechanics into account gave, they said, a better fit to the data than simulations that didn't. On the other hand, they said they were _not_ able to test directly for the presence of any quantum effect such as entanglement. (They agreed that entanglement was a non-negotiable requirement for quantum computing.)There was a Feynmanesque moment, when Ike Chuang asked Amin and Berkley an experimental question so simple even I understood it. Ike said: if you're indeed seeing quantum effects, then by running your computer at higher and higher temperatures, at some point you should see a transition to classical behavior. Have you tried this simple control experiment?Amin and Berkley said that they hadn't, but that it sounded like a good idea.



For a theorist like me -- accustomed to talks ending with "if there are no questions, then let's thank the speaker again" -- this was exciting, heady stuff. And when it was over, I still had almost three hours until the STOC deadline.

[](http://xkcd.com/54/)
