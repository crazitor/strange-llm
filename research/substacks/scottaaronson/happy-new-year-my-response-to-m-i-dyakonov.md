---
title: "Happy New Year!  My response to M. I. Dyakonov"
author: "Scott Aaronson"
date: "Wed, 02 Jan 2013"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=1211"
---

A couple weeks ago M. I. Dyakonov, a longtime quantum computing skeptic, published a [new paper](http://arxiv.org/abs/1212.3562) setting out his arguments (maybe "grievances" is a more accurate word) against quantum computing research. Looking for a way to procrastinate from other work I have to do, I decided to offer some thoughts in response.

To me, perhaps the most striking aspect of Dyakonov's paper is what it _doesn 't_ claim. Unlike Leonid Levin, Oded Goldreich, and several other quantum computing skeptics I've engaged, Dyakonov never seriously entertains the possibility of a general principle that would explain why scalable quantum computing is _not_ possible. (Thus, my [$100K prize](https://scottaaronson.blog/?p=902) presumably isn't relevant to him.) He even ridicules discussion of such a principle (see the end of this post). The unwillingness to say that scalable QC _can 't_ work, or to articulate a reason why, saves Dyakonov from the need to explore what else would need to be true about the physical world if scalable QC were impossible. For example, would there then be an efficient algorithm to simulate arbitrary quantum systems on a classical computer--or at least, all quantum systems that can plausibly arise in Nature? Dyakonov need not, and does not, evince any curiosity about such questions. In his game, it's only the quantum computing proponents who are on trial; there's no need for examination of the other side.

That being so, Dyakonov focuses on what he sees as unrealistic assumptions in known versions of the Quantum Fault-Tolerance Theorem, covering well-trodden ground but with some strange twists. He accuses quantum computing researchers of a "widespread belief that the |0〉 and |1〉 states 'in the computational basis' are something absolute, akin to the on/off states of an electrical switch, or of a transistor in a digital computer." He then follows with a somewhat-patronizing discussion of how no continuous quantity can be manipulated perfectly, and how |0〉 and |1〉 are just arbitrary labels whose meanings could change over time due to drift in the preparation and measurement devices. Well, yes, it's obvious that |0〉 and |1〉 don't have absolute meanings, but is it not equally obvious that we can _give_ them meanings, through suitable choices of initial states, gates, and measurement settings? And if the meanings of |0〉 and |1〉 drift over time, due to the imprecision of our devices … well, if the amount of drift is upper-bounded by some sufficiently small constant, then we can regard it as simply yet another source of noise, and apply standard fault-tolerance methods to correct it. If the drift is unbounded, then we do need better devices.

(Fault-tolerance mavens: please use the comments for more detailed discussion! To my inexpert eyes, Dyakonov doesn't seem to engage the _generality_ of the already-known fault-tolerance theorems--a generality traceable to the fact that what powers those results is ultimately just the linearity of quantum mechanics, not some fragile coincidence that one expects to disappear with the slightest change in assumptions. But I'm sure others can say more.)

Anyway, from his discussion of fault-tolerance, Dyakonov concludes only that the possibility of scalable quantum computing in the real world should be considered an open question.

Surprisingly--since many QC skeptics wouldn't be caught dead making such an argument--Dyakonov next turns around and says that, well, OK, fine, even if scalable QCs _can_ be built, they still won't be good for much. Shor's factoring algorithm is irrelevant, since people would simply switch to other public-key cryptosystems that appear secure even against quantum attack. Simulating quantum physics "would be an interesting and useful achievement, but hardly revolutionary, unless we understand this term in some very narrow sense." And what about Grover's algorithm? In an endnote, Dyakonov writes:

Quantum algorithms that provide (with an ideal quantum computer!) only polynomial speed-up compared to digital computing, like the Grover algorithm, became obsolete due to the polynomial slow-down imposed by error correction.

The above is flat-out mistaken. The slowdown imposed by quantum error-correction is polylogarithmic, not polynomial, so it doesn't come close to wiping out the Grover speedup (or the subexponential speedups that might be achievable, e.g., with the adiabatic algorithm, which Dyakonov doesn't mention).

But disregarding the polylog/polynomial confusion (which recurs elsewhere in the article), and other technical issues about fault-tolerance, up to this point _many quantum computing researchers could happily agree with Dyakonov --and have said similar things many times themselves_. Dyakonov even quotes Dorit Aharonov, one of the discoverers of quantum fault-tolerance, writing, "In a sense, the question of noisy quantum computation is theoretically closed. But a question still ponders our minds: Are the assumptions on the noise correct?"

(And as for QC researchers coming clean about _limitations_ of quantum computers? This is just hearsay, but I'm told there's a QC researcher who actually chose "Quantum computers are not known to be able to solve NP-complete problems in polynomial time" as the tagline for his blog!)

Dyakonov fumes about how popular articles, funding agency reports, and so forth have overhyped progress in quantum computing, leaving the conditions out of theorems and presenting incremental advances as breakthroughs. Here I sadly agree. As readers of  _Shtetl-Optimized_ can hopefully attest, I've seen it as my professional duty to spend part of my life battling cringeworthy quantum computing claims. Every week, it feels like I talk to another journalist who tries to get me to say that this or that QC result will lead to huge practical applications in the near future, since that's what the editor is looking for. And every week I refuse to say it, and try to steer the conversation toward "deeper" scientific questions. Sometimes I succeed and sometimes not, but at least I never hang up the phone feeling dirty.

On the other hand, it would be interesting to know whether, in the history of science, there's _ever_ been a rapidly-developing field, of interest to large numbers of scientists and laypeople alike, that _wasn 't_ surrounded by noxious clouds of exaggeration, incomprehension, and BS. I can imagine that, when Isaac Newton published his _Principia_ , a Cambridge University publicist was there to explain to reporters that the new work proved that the Moon was basically an apple.

But none of that is where Dyakonov loses me. Here's where he does: from the statements

**A) The feasibility of scalable quantum computing in the physical world remains open** _**,** _and

**B) The applications of quantum computing would probably be real but specialized** ,

he somehow, unaided by argument, arrives at the conclusion

**C) Quantum computing is a failed, pathological research program, which will soon die out and be of interest only to sociologists.**

Let me quote from his conclusion at length:

I believe that, in spite of appearances, the quantum computing story is nearing its end, not because somebody proves that it is impossible, but rather because 20 years is a typical lifetime of any big bubble in science, because too many unfounded promises have been made, because people get tired and annoyed by almost daily announcements of new “breakthroughs”, because all the tenure positions in quantum computing are already occupied, and because the proponents are growing older and less zealous, while the younger generation seeks for something new …

In fact, quantum computing is not so much a scientific, as a sociological problem which has expanded out of all proportion due to the US system of funding scientific research (which is now being copied all over the world). While having some positive sides, this system is unstable against spontaneous formation of bubbles and mafia-like structures. It pushes the average researcher to wild exaggerations on the border of fraud and sometimes beyond. Also, it is much easier to understand the workings of the funding system, than the workings of Nature, and these two skills only rarely come together.

The QC story says a lot about human nature, the scientific community, and the society as a whole, so it deserves profound psycho-sociological studies, which should begin right now, while the main actors are still alive and can be questioned.

In case the message isn't yet clear enough, Dyakonov ends by comparing quantum computing to the legend of Nasreddin, who promised the Sultan that he could teach a donkey how to read.

Had he [Nasreddin] the modern degree of sophistication, he could say, first, that there is no theorem forbidding donkeys to read. And, since this does not contradict any known fundamental principles, the failure to achieve this goal would reveal new laws of Nature. So, it is a win-win strategy: either the donkey learns to read, or new laws will be discovered.

Second, he could say that his research may, with some modifications, be generalized to other animals, like goats and sheep, as well as to insects, like ants, gnats, and flies, and this will have a tremendous potential for improving national security: these beasts could easily cross the enemy lines, read the secret plans, and report them back to us.

Dyakonov chose his example carefully. Turnabout: consider the first person who had the idea of domesticating a wild donkey, teaching the beast to _haul people 's stuff on its back_. If you'd never seen a domestic animal before, _that_ idea would sound every bit as insane as donkey literacy. And indeed, it probably took hundreds of years of selective breeding before it worked well.

In general, if there's no general principle saying that X can't work, the truth _might_ be that X can probably never work, but the reasons are too messy to articulate. Or the truth might be that X _can_ work. How can you ever find out, except by, y'know, _science_? Try doing X. If you fail, try to figure out why. If you figure it out, share the lessons with others. Look for an easier related problem Y that you can solve. Think about whether X is impossible; if you could _show_ its impossibility, that might advance human knowledge even more than X itself would have. If the methods you invented for X don't work, see if they work for some other, unrelated problem Z. Congratulations! You've just reinvented quantum computing research. Or really, any kind of research.

But there's something else that bothers me about Dyakonov's donkey story: its _specificity_. Why fixate on teaching a _donkey_ , only a donkey, how to read? Earlier in his article, Dyakonov ridicules the diversity of physical systems that have been considered as qubits--electron spin qubits, nuclear spin qubits, Josephson superconducting qubits, cavity photon qubits, etc.--seeing the long list as symptomatic of some deep pathology in the field. Yet he never notices the tension with his donkey story. Isn't it obvious that, if Nasreddin had been a quantum computing experimentalist, then after failing to get good results with donkeys, he'd simply turn his attention to teaching cows, parrots, snakes, elephants, dolphins, or gorillas how to read? Furthermore, while going through the zoo, Nasreddin might discover that he _could_ teach gorillas how to recognize dozens of pictorial symbols: surely a nice partial result. But maybe he'd have an even better idea: why not _build his own reading machine_? The machine could use a camera to photograph the pages of a book, and a computer chip to decode the letters. If one wanted, the machine could be even be the size and shape of a donkey, and could emit braying sounds. Now, maybe Nasreddin would fail to build this reading machine, but even then, we know today that it would have been a noble failure, like those of Charles Babbage or [Ted Nelson](http://en.wikipedia.org/wiki/Ted_Nelson). Nasreddin would've failed only by being too far ahead of his time.

**Update (Jan. 7):** See [Dyakonov's response to this post](https://scottaaronson.blog/?p=1211#comment-59962), and [my response to his response](https://scottaaronson.blog/?p=1211#comment-59972).
