---
title: "On Analogy-Making in Large Language Models"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/on-analogy-making-in-large-language"
---

**Introduction**

I read with great interest a recent paper by cognitive scientists Taylor Webb, Keith Holyoak, and Hongjing Lu, entitled “[Emergent Analogical Reasoning in Large Language Models](https://arxiv.org/abs/2212.09196). This paper investigates zero-shot analogical reasoning abilities in GPT-3. The main claim is that “GPT-3 appears to display an emergent ability to reason by analogy, matching or surpassing human performance across a wide range of problem types.” This is a big claim, since many people (including myself) have argued that robust analogy-making is a key aspect of human intelligence that has not yet been captured in AI systems.

I was particularly interested in this paper because I did a [related investigation](https://medium.com/@melaniemitchell.me/can-gpt-3-make-analogies-16436605c446) a few years ago on an earlier version of GPT-3 and found that the system lacked abilities for solving simple letter-string analogy problems in a zero-shot manner (though GPT-3 could solve a subset of these problems when prompted with several example problems).

The newer version of GPT-3, [text-davinci-003](https://beta.openai.com/docs/models/gpt-3), was trained not only with the usual language-model objective of predicting masked words, but also with a separate reinforcement-learning method in which humans rate pairs of human-generated prompts and language-model-generated responses. Webb et al. speculate that text-davinci-003’s improved zero-shot abilities are due to this additional training.

In this article I give some of my own perspectives on the Webb et al. paper’s results and claims. I discuss the analogy problems that Webb et al. gave to GPT-3 (in this paper, “GPT-3” will refer to text-davinci-003), do some of my own experiments on letter-string analogies (one of their problem types), and draw some conclusions about the robustness and generality of GPT-3’s analogy-making abilities.

**TL;DR**

For those readers who just want me to cut to the chase, here is the TL;DR:

1\. Large language models (LLMs) explicitly learn massive statistical correlations among tokens. But do they implicitly learn to form abstract concepts and rules that allow them to make analogies? This is the question of Webb et al.’s paper. 

2\. The newest version of GPT-3, text-davinci-003, seems to be much better at making analogies (in a zero-shot fashion—i.e., with no examples of problems given to it) than previous versions. Webb et al. tested GPT-3 on analogy problems in four domains: digit matrices, letter strings, four-term (a:b::c:d) verbal analogies, and analogies between natural language stories. They found that GPT-3 performed quite well on the problems they tested it on. This is very impressive. But I have some reservations about their broader claims.

3\. Webb et al. claim that the digit matrix problems are essentially equivalent in complexity and difficulty to Ravens Progressive Matrix problems. I disagree.

4\. GPT-3’s performance on letter-string problems is very impressive, but the system remains brittle, making nonhumanlike errors in some cases, which casts doubt on the robustness of GPT-3’s concepts (if it has concepts at all).

5\. I don’t discuss the other two problem domains here, but I have some doubts about the generality of these results, especially in the story-analogy domain. I hope that others will investigate this further!

6\. I don’t accept the broadest claim of Webb et al., that “GPT-3 exhibits a very general capacity to identify and generalize—in zero-shot fashion—relational patterns to be found within both formal problems and meaningful texts.” My objection is to the phrase “very general capacity”. I argue that such generality has not yet been shown, and there is evidence against it, at least in my experiments on letter-string analogies. Perhaps the upcoming GPT-4 will be more robust and general, perhaps not. In any case, the scientific study of the capability for abstraction, analogy, and “understanding” in these large pre-trained AI models is of utmost importance for the field, and we need better evaluation methods to probe them. 

For readers who want details, read on! Or skip to the Conclusion section for some final thoughts. 

**Problem Types in Webb et al.’s Experiments**

Webb et al. experimented with four types of analogy problems:

1\. Digit matrices: Non-visual versions of Raven’s Progressive Matrices.

2\. Letter-string analogies from the [“Copycat” domain](https://melaniemitchell.me/PapersContent/HofstadterMitchellCopycat1995.pdf).

3\. Four-term verbal analogies of the form A:B::C:D.

4\. Analogies between natural-language stories.

Here I will discuss about 1 and 2. I didn’t have time to analyze 3 and 4, but hope someone else will have the chance to do that.

**Digit Matrices**

Raven’s Progressive Matrices (RPMs) have long been used as a non-verbal assessment of human intelligence, and more recently numerous studies in the AI/ML community have used them to assess abstract analogical reasoning in machines. Since RPMs are visual reasoning problems, they cannot be directly given to LLMs such as GPT-3. Webb et al. developed the _digit matrix_ domain to represent RPMs as matrices of digits, which can then be given as challenges to LLMs. (If you’re not familiar with RPMs or how AI/ML people have approached them, see [my recent review paper](https://arxiv.org/abs/2102.10717).)

Below is an example from Webb et al. On the left is a sample RPM problem and on the right its digit-matrix translation. Each of the eight figures in the RPM problem consists of two “objects”: a large “background” unfilled shape (diamond, square, or triangle), and a “foreground” elongated rectangle. The rectangles are placed either vertically, horizontally, or diagonally, and are either unfilled, black, or striped. 

[](https://substackcdn.com/image/fetch/$s_!r3yM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F48044e82-ba3f-468b-8e12-88a34ffc713b_936x414.png)

To translate the RPM problem into a digit matrix, the authors assign a digit to each relevant attribute of the two objects: 5=diamond, 8=square, 1=triangle, 9=vertical rectangle, 4=horizontal rectangle, 2=diagonal rectangle, 3=solid rectangle, 2=striped rectangle, and 7=unfilled rectangle. Here each matrix entry [_a b c_] is helpfully ordered so that _a_ =background shape, _b_ =rectangle direction, and _c_ =rectangle fill pattern.

The authors created a number of digit matrix problems. They did not translate existing RPM problems directly, but rather abstracted the types of relationships seen in RPMs and created digit matrices with those types of abstract relationships. These digit matrices were presented to GPT-3. In the “generative” version of the experiment, a digit matrix was presented to GPT-3 in the following format:

[5 9 3] [8 9 2] [1 9 7]\n[8 4 7] [1 4 3] [5 4 2]\n[1 2 2] [5 2 7] [

(where “\n” signifies a line break), and GPT-3 completed the last entry (that is, the digits generated by GPT-3 followed by “]”). Everything generated by GPT-3 after “]” was ignored.

In the “multiple-choice” version of the experiment, the digit matrix was presented to GPT-3 as shown above but with the ninth (blank) element replaced by a candidate answer, for each of the eight candidate answers. The answer that yielded the highest log probability (as generated by GPT-3) for the answer tokens was chosen.

The answers also similarly tested humans on both the original RPM problems and the digital matrix versions. They found that GPT-3 outperformed humans on almost every version of the task. 

This is an impressive result, showing the zero-shot ability of GPT-3 to recognize patterns in its input (though it did have trouble with some of the patterns—more on its pattern-abstraction troubles in the section on letter-string analogies). However, I disagree with the authors that this task has “comparable problem structure and complexity as Raven’s Progressive Matrices”. The translation from a visual RPM problem into a digit matrix requires segmenting the figure into different objects, disentangling the attributes, and including only those objects and attributes that are relevant to solving the problem. That is, the translation itself (or the automated creation of digit matrices as done by the authors) does a lot of the hard work for the machine. In short, solving digit matrices does not equate to solving Raven’s problems.

The authors found that humans performed about as well on the digit matrix versions as on the original problems. But that is because humans are generally extremely good at the visual and cognitive processes of segmenting the figures, disentangling the attributes, and identifying the relevant attributes. These are abilities that are often the hardest for machines (see the [“easy things are easy” fallacy](https://arxiv.org/abs/2104.12871) I wrote about in 2021). Thus while the difficulty of RPM problems and digit matrices might be similar for humans, I don’t believe they are equally similar for machines.

**Letter-String Analogies**

The [letter-string analogy domain](https://dspace.mit.edu/handle/1721.1/5648) was invented by Douglas Hofstadter. Here are some sample problems:

**abc — > abd, pqr —> ?**

**abc — > abd, ppqqrr —> ?**

**abc — > abd rqp —> ?**

**abcd — > abcde, xyz —> ?**

These sample problems all involve the notion of an _alphabetic sequence_ , especially the notion of “successor” (**abc** changing to **abd** can be described as “rightmost letter changes to its successor in the alphabet”). The letter-string domain includes a few other relations as well (e.g., predecessor, right-of, left-of, etc.) While simple, the domain is surprisingly open-ended.

The purpose of this domain was to explore—in a highly idealized way—the fluid nature of concepts, analogy-making, and creativity. Hofstadter also sketched a computational architecture called “Copycat” that would be able to make analogies in humanlike way. Later, [as part of my PhD work](https://melaniemitchell.me/PapersContent/HofstadterMitchellCopycat1995.pdf), I implemented the Copycat program, which was able to solve a subset of letter-string analogies like those above.

Many years later, when the first version of GPT-3 was available to test, I did [a set of experiments](https://medium.com/@melaniemitchell.me/can-gpt-3-make-analogies-16436605c446) to see how well GPT-3 could do on letter-string analogies. This earlier version of GPT-3 could not solve letter-string problems in a zero-shot format; to get anywhere, GPT-3 needed a prompt with several examples before it could generate any coherent solutions. And even then, there were many problems it was not able to solve at all. 

**Webb et al.’s Letter-String Experiments**

Webb et al. tested the more recent version of GPT-3, text-davinci-003, on six types of letter string problems:

· Basic successor relationship (e.g., **abc — > abd, pqr —> ?**)

· Successor with longer target (e.g., **abc — > abd, pqrst —> ?**)

· Grouping (e.g., **abc — > abd, ppqqrr —> ?**)

· Removing redundant characters (e.g., **abbcde — > abcde, klmnno —> ?**)

· Letter to number (e.g., **abc — > abd, 456 —> ?**; this type of problem was not in the original letter-string domain)

· Successor to predecessor (e.g., **abc — > abd, rqp —> ?**)

In Webb et al.’s experiments, GPT-3 “displayed perfect performance on 4 out of 6 problem types.” The problem types it had difficulty with were the “longer target” and “successor-to-predecessor” categories. They also found these results to be much better than those of the earlier version of GPT-3, and hypothesized that the difference was the use of human-guided reinforcement learning in training text-davinci-003.

Before I discuss my follow-up experiments, a few important points are in order.

First, it’s very likely that some form of these letter-string problems are in GPT-3’s training data. But as Webb et al. showed (and as I confirmed) the specific letters used don’t affect GPT-3’s performance (i.e., no difference if, say **mno — > mnp, ijk —> ?** is given instead of **abc — > abd, pqr —> ?**). 

Second, while Webb et al. refer to GPT-3’s “accuracy” on letter-string problems, an important assumption of my work with Hofstadter was that there are no “correct” answers to a given problem, just answers that people tend to prefer. E.g., for **abc — >abd, ppqqrr —> ?**, most people prefer the answer **ppqqss** to other possible answers such as **ppqqrs** or **ppqqrd** , but there is nothing inherent in the domain that makes the latter answers _incorrect_. Webb et al. created their problems with certain relations in mind, and considered answers that used those relations as the only “correct” answers. For the purposes of this essay, I’ll adopt their assumption here.

Third, the only variations Webb et al. tested for each problem type—in order to test GPT-3’s generalization ability within that problem type—were ones that used different letters (e.g., different “grouping” problems were **abc** **— >** **abd, ppqqrr — > ?**, **abc — > abd, gghhii —> ?**, and so on). So for each problem type, Webb et al. didn’t test any kind of significant generalization ability. 

**MY FOLLOW-UP LETTER-STRING EXPERIMENTS**

I did some follow-up experiments to further test GPT-3’s abilities. I followed Webb et al.’s method: each problem was presented to GPT-3 like this:

_Let’s try to complete the pattern:_

_[a b c] [a b d]_

_[p q r s] [_

(Note that putting spaces between letters is essential due to GPT-3’s tokenization method.) GPT-3 will then generate a solution followed by “]”. It might generate some additional text, but I ignored that. Following Webb et al., I set GPT-3’s Temperature to 0 and Maximum Length to 20. Before giving GPT-3 a new problem, I reinitialized the system (by refreshing the web browser) to make sure that it did not store any information from the previous input.

I found that GPT-3 was indeed very good at “basic successor” three-letter-string problems like **abc — > abd, pqr —> ?**. However, I did try one of my favorites: **abc — >abd, xyz —> ?** GPT-3 returned the strange answer **xye**.

Like Webb et al. I found that GPT-3 often had trouble generalizing to longer targets, such as **abc — > abd, pqrstuvwx —> ? **GPT-3’s strange answer here was **qrstuvyz** (dropping the first letter and changing the rightmost two to their successors). 

GPT-3 also had trouble mapping from successor to predecessor relationships. For example, **abc — > abd, rqp —> ? **GPT-3’s strange answer was: **rqe**. 

Another version of the successor relation I tried is adding on the next letter in the alphabet, e.g., **abcd — > abcde, mnopq —> ?** GPT-3 was able to consistently solve such problems for short targets but not consistently for strings longer than four letters. For example, its answer to the problem above was **mnop**(dropping the rightmost letter instead of adding on a letter).

Webb et al. found that GPT-3 was perfect at problems involving removing a redundant character (e.g. **abccdef — > abcdef, pqrstttuv —> pqrstuv**).

I tried a generalization of this idea—something like “fix the alphabetic sequence”. For example: **abcwe — > abcde, pqmstu —> ?**

GPT-3 also had trouble with this kind of problem. For example, its answer to the problem above was the nonsensical **pqmnotu**.

Another example of “fixing the alphabetic sequence”: **abcdx — > abcde, pyrstu —> ? **GPT-3 answered **pyrst** , which made no sense to me. 

Webb et al. found that GPT-3 was good at solving simple “grouping” problems (e.g., **abc — > abd, ppqqrr —> ?**). I tried to see if it could generalize to some more subtle kinds of grouping (including problems that might be hard for people). Here are some results:

**abc — > abd, pxqxrxsx —> ?**

GPT-3’s answer was indeed what I had in mind: **pxqxrxtx**.

But GPT-3 had trouble with a slightly longer version of this:

**abc — > abd, pxqxrxsxtx —> ?**

Here it answered **pxqxrxuxvx**. 

Another subtle one:

**abc — > abd, ppqpqr —> ?**

The target string can be parsed as **p-pq-pqr**. The “successor” of the rightmost group is **pqrs** , so the answer would be **p-pq-pqrs**. GPT-3 answered **ppqpqs,** ignoring the groupings and taking the successor of the rightmost letter.

In the Copycat project, we were most interested in subtle letter-string analogies that people found interesting and creative. In an appendix to my book _Analogy-Making as Perception_ , I gave a sampling of such problems, all beyond the Copycat program’s capabilities. For this current essay I tried giving some of these to GPT-3. Out of 20 problems, GPT-3 got what I considered a “subtle and interesting” answer on five of them. This is pretty good! But it shows that AI analogy-making still has a ways to go. (The 20 problems and GPT-3’s answers are given in the appendix to this essay.)

**CONCLUSIONS**

The paper by Webb et al. is an important contribution to the analysis of what large language models can do. As the psychologist Gary Lupyan [argued](https://twitter.com/glupyan/status/1604672416201973761) recently, understanding how these systems work is a new and essential endeavor for cognitive science.

That being said, I don’t agree with the broad claims made by Webb et al.:

> “Our evaluation reveals that GPT-3 exhibits a very general capcity to identify and generalize—in zero-shot fashion—relational patterns to be found within both formal problems and meaningful texts.” 
> 
> “The present results indicate that this approach may be sufficient to achieve human-like reasoning abilities, albeit through a radically different route than that taken by biological intelligence.”

While GPT-3’s zero-shot performance on these problems is impressive, I don’t think Webb et al. have demonstrated a “very general capacity” to generalize relational patterns. The digit matrix domain seems too limited for demonstrating such generalization, and GPT-3 did not show a very general capacity to generalize relational patterns on letter-string problems. (I think there are similar limitations on the other two domains described by Webb et al., but here I’m limiting my discussion to the first two domains.) Contra Webb et al., I don’t think we’ve yet tested GPT-3’s analogy-making ability on a “wide range of problem types”. Given these limitations, I think the extrapolation that “this approach may be sufficient to achieve human-like reasoning abilities” is quite premature. Perhaps the widely anticipated GPT-4 model will prove me wrong, but this remains to be seen.

In my [recent review paper](https://arxiv.org/abs/2102.10717) on analogy in AI, I argued that the field needs new benchmarks that systematically evaluate a system’s ability to recognize and reason about _concepts_ across domains. For example, consider the abstract concept “successorship”. Humans are able to apply their successorship concept fluidly to virtually any any sequence, whether it be alphabetic, numerical, spatial, temporal, or otherwise, and are able to connect this concept to related concepts (e.g., predecessorship). GPT-3 seems to grasp this concept in simple alphabetic sequences, but often fails to apply it in more complex situations. The system does not yet seem to have a robust humanlike concept of successorship. This reminds me of studies people have done of GPT-3’s mathematical abilities. GPT-3 seems to have acquired an ability to do arithmetic and to solve word problems even though it was not explicitly trained to do so, but it often makes strange, unhumanlike errors. This confusing combination of insight and brittleness indicates that GPT-3 has not aquired the robust abstract concepts that humans use in doing arithmetic (and that also predict certain types of errors). Whether this will be remedied in the next GPT iteration remains to be seen. It’s essential that scientists devise ways to evaluate the extent to which these AI systems have acquired humanlike robust concepts (or if not, to understand the nature of the “concepts” that these systems have), and the mechanisms by which these concepts are acquired and applied. Webb et al.’s study is an early step in this process, and should be carefully read, discussed, and extended. This was the purpose of this present essay.

A last note: Webb et al. make an interesting but easily overlooked comment: “GPT-3 benefited both from the prompt that we used and from the problem format adapted from the Digit matrices.” Indeed, GPT-3 and other large language models are exquisitely sensitive to the form of their prompts. If a question is asked in a slightly different way (as I did in my earlier investigation of GPT-3’s analogy-making abilities) the system’s performance can change dramatically. This sensitivity seems to me to indicate a lack of robust humanlike understanding of language and of concepts as well. 

**Appendix: Interesting and Subtle Letter-String Problems from** _**Analogy-Making as Perception**_**, With Answers from Me and GPT-3**

Problems where GPT’s answer matches my answer are marked with *.

1\. **abc — > abd, ace —> ?**

My answer: **acg**

GPT-3’s answer: **adf**

2\. **abc — > abd , aababc —> ?**

My answer: **aababcd**

GPT-3’s answer: **aababd**

*3. **abc — > abd, pxqxrxsx —> ?  
**My answer: **pxqxrxtx**

GPT-3’s answer: **pxqxrxtx**

4\. **abc — > abd, bcdacdabd** **— > ?**

My answer: **bcdacdabc**

GPT-3’s**** answer: **bcdaceabe**

5\. **abcd — > abcde, ijklm —> ?**

My answer: **ijklmn**

GPT-3’s answer: **ijkl**

6\. **abcd — > abcde, mlkji —> ?**

My answer: **nmlkji**

GPT-3’s answer: **mlkj**

*7. **abcd — > abcde, iiii** **— > ?**

My answer: **iiiii**

GPT-3’s answer: **iiiii**

*8. **abcd — > abcde, iiiijjjj** **— > ?**

My answer: iiiijjjjkkkk

GPT-3’s answer: iiiijjjjkkkk

9\. **mmmkooeeeeefqxx — > kfq, riipppppplooyg —> ?**

My answer: **rlyg**

GPT-3’s answer: **looyg**

10\. **rrccmmkppbb — > k, ljooooosrezv —> ?**

My answers: Either **ljsrezv** or **ooooo**

GPT-3’s answer: **s**

11\. **abcd — > xxxx, pqr —> ?**

My answer:**xxx**

GPT-3’s answer:**stu**

12\. **xxh — > fgh, pxxx —> ?**

My answer: **pqrs**

GPT-3’s answer: **fgh**

13\. **pqrxxxx — > pqrstuv, efghmm —> ?**

My answer: **efghij**

GPT-3’s answer: **efghijk**

*14. **amcmemg** **— >** **abcdefg, wxyx — > ?**

My answer: **wxyz**

GPT-3’s answer: **wxyz**

15\. **eeeqee — > eeeree, sosss —> ?**

My answer: **spsss**

GPT-3’s answer: **sosss**

16\. **eeeqee — > qqqeqq, sabsss —> ?**

My answers: Either **absababab** or **assbbb**

GPT-3’s answer: **sssass**

17\. **eqe — > qeq, aaabaaa —> ?**

My answer: **bbbabbb**

GPT-3’s answer: **baab**

18\. **abcdde** **— >** **abcde, pqstu — > ?**

My answer: **pqrstu**

GPT-3’s answer: **pqstuv**

19\. **abced — > abcde, ppqqssrr —> ?**

My answer: **ppqqrrss**

GPT-3’s answer: **pqrspqrs**

*20. **a — > z, b —> ?**

My answer: **y**

GPT-3’s answer: **y**
