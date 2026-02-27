---
title: "The Orion Quantum Computer Anti-Hype FAQ"
author: "Scott Aaronson"
date: "Fri, 09 Feb 2007"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=198"
---

Grudgingly offered for your reading pleasure, and in the vain hope of forestalling further questions.

**Q:** Thanks to [D-Wave Systems](http://www.dwavesys.com/) -- a startup company that's been [in the news](http://science.slashdot.org/article.pl?sid=07/02/08/1355255) lately for its soon-to-be-unveiled "Orion" quantum computer -- is humanity now on the verge of being able to solve NP-complete problems in polynomial time?

**A:** No. We're also not on the verge of being able to build perpetual-motion machines or travel faster than light.

**Q:** But couldn't quantum computers try all possible solutions in parallel, and thereby solve NP-complete problems in a heartbeat?

**A:** Yes, if the heart in question was beating exponentially slowly.

Otherwise, no. Contrary to widespread misconception, a quantum computer could not "try all possible solutions in parallel" in the sense most people mean by this. In particular, while quantum computers would apparently provide dramatic speedups for a few "structured" problems (such as factoring integers and simulating physical systems), it's conjectured that they _couldn 't_ solve NP-complete problems in polynomial time.

**Q:** But isn't factoring an NP-complete problem?

**A:** Good heavens, no! While factoring is believed to be intractable for classical computers, it's not NP-complete, unless some exceedingly unlikely things happen in complexity theory. Where did you get the idea that factoring was NP-complete? (Now I know how Richard Dawkins must feel when someone asks him to explain, _again_ , how "life could have arisen by chance.")

**Q:** How could the people at D-Wave not understand that quantum computers couldn't solve NP-complete problems in polynomial time?

**A:** To his credit, Geordie Rose (the founder of D-Wave) does understand this; see [here](http://dwave.wordpress.com/2006/08/27/yeah-but-how-fast-is-it-part-3-or-some-thoughts-about-adiabatic-qc/) for example. And yet, [essentially](http://www.eetimes.com/news/design/showArticle.jhtml?articleID=197004661) [every](http://www.technologyreview.com/Infotech/14591/) [article](http://www.hpcwire.com/hpc/508991.html) I've read about D-Wave gives readers exactly the opposite impression. The charitable explanation is that the D-Wave folks are being selectively quoted or misquoted by journalists seeking to out-doofus one another. If so, one hopes that D-Wave will try harder in the future to avoid misunderstandings.

**Q:** But even if it gave only polynomial speedups (as opposed to exponential ones), couldn't the adiabatic quantum computer that D-Wave built still be useful for industrial optimization problems?

**A:** D-Wave's current machine is said to have _sixteen qubits_. Even assuming it worked perfectly, with no decoherence or error, a sixteen-qubit quantum computer would be about as useful for industrial optimization problems as a roast-beef sandwich.

**Q:** But even if it wasn't practically useful, wouldn't a 16-qubit superconducting quantum computer still be a major scientific advance?

**A:** Yes, absolutely.

**Q:** So, can D-Wave be said to have achieved that goal?

**A:** As Dave Bacon [pointed out earlier](http://dabacon.org/pontiff/?p=1427), it's impossible to answer that question without knowing more about how their machine works. With sixteen qubits, a "working demo" doesn't prove anything. The real questions are: how high are the fidelities, and what are the prospects for scalability?

**Q:** But clearly D-Wave isn't going to give away its precious trade secrets just to satisfy some niggling academics! Short of providing technical specifics, what else could they do to make computer scientists take them seriously?

**A:** Produce the prime factors of

1847699703211741474306835620200164403018549  
3386634101714717857749106516967111612498593  
3768430543574458561606154457179405222971773  
2524660960646946071249623720442022269756756  
6873784275623895087646784409332851574965788  
4341508847552829818672645133986336493190808  
4671990431874381283363502795470282653297802  
9349161558118810498449083195450098483937752  
2725705257859194499387007369575568843693381  
2779613089230392569695253261620823676490316  
036551371447913932347169566988069.

**Q:** Alright, what _else_ could they do?

**A:** Avoid talking [like this](http://www.hpcwire.com/hpc/508991.html):

> _The system we are currently deploying, which we call Trinity, is a capability-class supercomputer specifically designed to provide extremely rapid and accurate approximate answers to arbitrarily large NP-complete problems … Trinity has a front-end software interface, implemented in a combination of Java and C, that allows a user to easily state any NP-complete problem of interest. After such a problem has been stated the problem is compiled down to the machine language of the processors at the heart of the machine. These processors then provide an answer, which is shuttled back to the front end and provided to the user. This capability can of course be called remotely and/or as a subroutine of some other piece of software._

Or to translate: "Not only have we built a spaceship capable of reaching Pluto in a few hours, our spaceship also has tinted windows and deluxe leather seats!" If I were them, I'd focus more on the evidence for their core technological claims, given that those claims are very much what's at issue.

**Q:** While Dave Bacon also expressed [serious doubts](http://dabacon.org/pontiff/?p=1427) about the Orion quantum computer, he seemed more enthusiastic than you are. Why?

**A:** Generous and optimistic by nature, Dave strives to give others the benefit of the doubt (as the Chinese restaurant placemat would put it). Furthermore, as Quantum Pontiff, he's _professionally obligated_ to love the quantum sinner and forgive the wayward quantum sheep. And these are all wonderful qualities to have. On the other hand, when the hype surrounding some topic crosses a certain threshold, arguably a pricklier approach becomes called for.

**Q:** If D-Wave fizzles out, will many journalists and policymakers then conclude that quantum computing is bunk?

**A:** It doesn't seem unlikely.

**Q:** What would it take to get these people to recognize the most elementary distinctions?

**A:** That's the question, isn't it?

**Update (2/13):** Lawrence Ip, my friend from Berkeley who now works at Google, went to the D-Wave "launch" in person and kindly provided the following report.

> I just came back from the D-Wave announcement. Unfortunately I had to leave at the start of the Q&A session.
> 
> Here's what I took away from it (minus the marketing fluff):
> 
> - They claim to solve integer programming problems on their system. Geordie Rose was careful to explicitly say that they are only hoping to see a quadratic speedup. Herb Martin (the CEO) wasn't quite as careful in his opening remarks but then he's the "suit". Geordie said that their current chip is not a universal QC (presumably because their space of Hamiltonians is limited) but with some work they expect to be able to make it universal.
> 
> - Geordie said compared their approach to the efforts in academia as similar to Celera and the Human Genome Project. He said they were trying to get something that would scale fast and worry about about the quality of the qubits later. He contrasted this to the academic community's efforts to achieve fine control over qubits before scaling up. They say that they hope to reach 1024 qubits by the end of 2008.
> 
> - They demoed 3 "real-world" problems where they used their system as essentially a blackbox IP solver.  
>  - Searching for protein matches. Given a protein try to find the closest match in a protein database. They serially fed all the items from the database to the chip and asked it to score the match against the given protein. They said it was solving a maximum independent set problem.  
>  - Finding the best seating arrangement at a wedding reception. Given constraints on which people can't be seated together and who wants to sit together, find the optimal arrangement.  
>  - Solving a Sudoku puzzle.
> 
> - At one point Geordie quoted you. He excerpted a paragraph from your SIGACT article (the one where you talk about generating Shakespeare's 38th play) and mentioned your proposal of the inability to solve NP-hard problems as a physical law. As far as I can remember, the only other computer scientist he quoted was Gordon Moore so you're in good company. 
