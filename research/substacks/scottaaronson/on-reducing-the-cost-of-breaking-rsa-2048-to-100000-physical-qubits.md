---
title: "On reducing the cost of breaking RSA-2048 to 100,000 physical qubits"
author: "Scott Aaronson"
date: "Sun, 15 Feb 2026"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=9564"
---

So, a group based in Sydney, Australia has [put out a preprint](https://arxiv.org/abs/2602.11457) with a new estimate of the resource requirements for Shor's algorithm, claiming that if you use LDPC codes rather than the surface code, you should be able to break RSA-2048 with fewer than 100,000 physical qubits, which is an order-of-magnitude improvement over the previous estimate by friend-of-the-blog Craig Gidney. I've now gotten sufficiently many inquiries about it that it's passed the threshold of blog-necessity.

A few quick remarks, and then we can discuss more in the comments section:

  * Yes, this is serious work. The claim seems entirely plausible to me, although it would be an understatement to say that I haven't verified the details. The main worry I'd have is simply that LDPC codes are harder to engineer than the surface code (especially for superconducting qubits, less so for trapped-ion), because you need wildly nonlocal measurements of the error syndromes. Experts (including Gidney himself, if he likes!) should feel free to opine in the comments.  

  * I have no idea by how much this shortens the timeline for breaking RSA-2048 on a quantum computer. A few months? Dunno. I, for one, had already "baked in" the assumption that further improvements were surely possible by using better error-correcting codes. But it's good to figure it out explicitly.  

  * On my Facebook, I mused that it might be time for the QC community to start having a conversation about whether work like this should still be openly published--a concern that my friends in the engineering side of QC have expressed to me. I got strong pushback from cryptographer and longtime friend [Nadia Heninger](https://cseweb.ucsd.edu/~nadiah/), who told me that the crypto community has already had this conversation for decades, and has come down strongly on the side of open publication, albeit with ["responsible disclosure"](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure) waiting periods, which are often 90 days. While the stakes would surely be unusually high with a full break of RSA-2048, Nadia didn't see that the basic principles there were any different. Nadia's arguments updated me in the direction of saying that groups with further improvements to the resource requirements for Shor's algorithm should _probably_ just go ahead and disclose what they've learned, and the crypto community will have their backs as having done what they've learned over the decades was the right thing. Certainly, any advantage that such disclosure would give to hackers, who could take the new Shor circuits and simply submit them to the increasingly powerful QCs that will gradually come online via cloud services, needs to be balanced against the loud, clear, open warning the world will get to migrate faster to quantum-resistant encryption.  

  * I'm told that these days, the biggest practical game is breaking elliptic curve cryptography, _not_ breaking Diffie-Hellman or RSA. Somewhat ironically, elliptic curve crypto is likely to fall to quantum computers a bit _before_ RSA and Diffie-Hellman will fall, because ECC's "better security" (against classical attacks, that is) led people to use 256-bit keys rather than 2,048-bit keys, and Shor's algorithm mostly just cares about the key size.  

  * In the acknowledgments of the paper, I'm thanked for "thoughtful feedback on the title." Indeed, their original title was about "_breaking_ RSA-2048″ with 100,000 physical qubits. When they sent me a draft, I pointed out to them that they need to change it, since journalists would predictably misinterpret it to mean that they'd already done it, rather than simply saying that it _could_ be done.


