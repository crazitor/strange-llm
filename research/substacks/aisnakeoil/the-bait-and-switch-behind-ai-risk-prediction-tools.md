---
title: "The bait and switch behind AI risk prediction tools"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/the-bait-and-switch-behind-ai-risk"
---

Toronto recently used an AI tool to predict when a public beach will be safe. It went [horribly awry](https://www.theinformation.com/articles/when-artificial-intelligence-isnt-smarter?rc=aidfin). 

The developer claimed the tool achieved over 90% accuracy in predicting when beaches would be safe to swim in. But the tool did much worse: on a majority of the days when the water was in fact unsafe, beaches remained open based on the tool’s assessments. It was less accurate than the previous method of simply testing the water for bacteria each day.

We do not find this surprising. In fact, we consider this to be the default state of affairs when an AI risk prediction tool is deployed. 

The Toronto tool involved an elementary performance evaluation failure—city officials never checked the performance of the deployed model over the summer—but much more subtle failures are possible. Perhaps the model is generally accurate but occasionally misses even extremely high bacteria levels. Or it works well on most beaches but totally fails on one particular beach. It's not realistic to expect non-experts to be able to comprehensively evaluate a model. Unless the customer of an AI risk prediction tool has internal experts, they’re buying the tool on faith. And if they do have their own experts, it’s usually easier to build the tool in-house!

When officials were questioned about the tool's efficacy, they deflected the questions by saying that the tool was never used on its own—a human always made the final decision. But they did not answer questions about how often the human decision-makers overrode the tool's recommendation. 

This is also a familiar pattern. AI vendors often use a bait-and-switch when it comes to human oversight. Vendors sell these tools based on the promise of full automation and elimination of jobs, but when concerns are raised about bias, catastrophic failure, or other well-known limitations of AI, they retreat to the fine print which says that the [tool shouldn't be used on its own](https://doaj.org/article/97ff6743ea7a44a5ade2a04fd2c57a3c). Their promises lead to over-automation—AI tools are used for tasks far beyond their capabilities.

Here are three other stories of similar failures of risk prediction models.

### **Epic’s sepsis prediction debacle**

[Epic](https://www.epic.com/about) is a large healthcare software company. It stores health data for over 300 million patients. In 2017, Epic released a sepsis prediction model. Over the next few years, it was deployed in hundreds of hospitals across the U.S. However, a [2021 study](https://pubmed.ncbi.nlm.nih.gov/34152373/) from researchers at the University of Michigan found that Epic’s model vastly underperformed compared to the developer’s claims. 

The tool's inputs included information about whether a patient was given antibiotics. But if a patient is given antibiotics, they have [already been diagnosed with sepsis](https://www.statnews.com/2021/09/27/epic-sepsis-algorithm-antibiotics-model/)—making the tool’s prediction useless. These cases were still counted as successes when the developer evaluated the tool, leading to exaggerated claims about how well it performed. This is an example of [data leakage](https://reproducible.cs.princeton.edu/), a common error in building AI tools.

In a 2021 [response](https://www.epic.com/epic/post/for-clinicians-by-clinicians-our-take-on-predictive-models), Epic tried to deflect criticism by claiming that their AI tools are not used on their own: "The robust clinical workflows and processes that surround these tools are what give the tools purpose and allow for improved outcomes". But the opposite was true: [88%](https://www.jwatch.org/na53777/2021/09/07/epics-sepsis-model-not-ready-prime-time) of the tool’s alerts were false alarms, further increasing the workload on healthcare workers. A year later, Epic [stopped selling](https://www.statnews.com/2022/10/24/epic-overhaul-of-a-flawed-algorithm/) its one-size-fits-all sepsis prediction model.

### **Dutch childcare benefits scandal**

In 2013, the Netherlands deployed an algorithm to detect welfare fraud by people receiving childcare benefits. The algorithm found statistical correlations in the data, but these correlations were used to make serious accusations of guilt—without any other evidence. 

The algorithm was used to wrongly accuse [30,000 parents](https://caribischnetwerk.ntr.nl/2021/02/01/veel-caribische-nederlanders-slachtoffer-toeslagenaffaire/). It sent many into financial and mental ruin. People accused by the algorithm were often asked to pay back [hundreds of thousands of euros](https://www.vice.com/en/article/jgq35d/how-a-discriminatory-algorithm-wrongly-accused-thousands-of-families-of-fraud). In many cases, the accusation resulted from [incorrect data about people](https://autoriteitpersoonsgegevens-nl.translate.goog/nl/nieuws/boete-belastingdienst-voor-zwarte-lijst-fsv?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp)—but they had no way to find out.

Shockingly, one of the inputs to the algorithm was whether someone had dual nationality; simply having a Turkish, Moroccan, or Eastern European nationality would make a person more likely to be [flagged as a fraudster](https://autoriteitpersoonsgegevens-nl.translate.goog/nl/nieuws/boete-belastingdienst-voor-zwarte-lijst-fsv?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp). 

Worse, those accused had no recourse. Before the algorithm was developed, each case used to be [reviewed by humans](https://www.vice.com/en/article/jgq35d/how-a-discriminatory-algorithm-wrongly-accused-thousands-of-families-of-fraud). After its deployment, no human was in the loop to override the algorithm’s flawed decisions.

Despite these issues, the algorithm was used for over 6 years. 

In the fallout over the algorithm’s use, [the Prime Minister and his entire cabinet resigned](https://www.politico.eu/article/dutch-scandal-serves-as-a-warning-for-europe-over-risks-of-using-algorithms/). Tax authorities that deployed the algorithm had to pay a EUR 3.7 million fine for the lapses that occurred during the model’s creation. This was the [largest such fine](https://autoriteitpersoonsgegevens-nl.translate.goog/nl/nieuws/boete-belastingdienst-voor-zwarte-lijst-fsv?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=wapp) imposed in the country. 

This serves as a cautionary example of over-automation: an untested algorithm was deployed without any oversight and caused massive financial and emotional harm to people for 6 years before it was disbanded.

### **Family separation in Allegheny county**

In 2016, Allegheny county in Pennsylvania adopted the Allegheny Family Screening Tool (AFST) to predict which children are at risk of maltreatment. AFST is used to decide which families should be investigated by social workers. In these investigations, social workers can forcibly remove children from their families and place them in foster care, [even if there are no allegations of abuse](https://www.wired.com/story/excerpt-from-automating-inequality/)—only poverty-based neglect.

Two years later, it was [discovered](https://proceedings.mlr.press/v81/chouldechova18a/chouldechova18a.pdf) that AFST suffered from data leakage, leading to exaggerated claims about its performance. In addition, the tool was [systematically biased](https://dl.acm.org/doi/pdf/10.1145/3491102.3501831) against Black families. When questioned, the creators trotted out the familiar defense that the [final decision is always made by a human decision-maker](https://www.wesa.fm/politics-government/2022-04-29/an-algorithm-that-screens-for-child-neglect-in-allegheny-county-raises-concerns).

There are many other examples of AI being particularly ill-suited for risk prediction; in an [upcoming paper](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4238015), we look at 8 consequential examples and find that they are all prone to failure in similar ways. Without scrutiny, all such tools are suspect.

Of course, when companies are asked to share their models for scrutiny, they throw their hands up with cries of "trade secret"—this happened with Epic, [Northpointe](https://hdsr.mitpress.mit.edu/pub/hzwo7ax4/release/3) (the company that makes the [infamous recidivism prediction tool, COMPAS](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)), and many other firms that sell such tools.

The takeaway is clear: the onus should be on the company selling the AI tool to proactively justify its validity. Without such evidence, we should treat any risk assessment tool as suspect. And that includes most tools on the market today. 

**Further reading**

  * History never repeats itself, but it does often rhyme. In Michigan, an algorithm was used to detect unemployment fraud from 2013-2015. The state [incorrectly collected USD 21 million from residents](https://www.theatlantic.com/technology/archive/2020/06/michigan-unemployment-fraud-automation/612721/). In another fraud detection scandal, the Australian government stole [AUD 721 million from its citizens](https://www.vice.com/en/article/y3zkgb/the-story-of-how-the-australian-government-screwed-its-most-vulnerable-people-v27n3) from 2016-2020. Citizens were accused of welfare fraud using an algorithm; this is often called the “robodebt” scandal. 

  * J. Khadijah Abdurahman offers an [incisive and gut-wrenching take on family separation](https://logicmag.io/home/birthing-predictions-of-premature-death/) and the role of AI tools—including AFST—in amplifying its harms.

  * In her book _[Automating Inequality](https://us.macmillan.com/books/9781250074317/automatinginequality)_ , Virginia Eubanks dives into AFST and how it penalizes poverty. An excerpt of the chapter on AFST was [published in WIRED](https://www.wired.com/story/excerpt-from-automating-inequality/).

  * Madeleine Clare Elish and Elizabeth Anne Watkins study another sepsis prediction algorithm—[Sepsis Watch](https://datasociety.net/wp-content/uploads/2020/09/Repairing-Innovation-DataSociety-20200930-1.pdf)—that was deployed at Duke University. They document the painstaking work needed by clinicians to incorporate the model into their hospital-specific workflows and social context. This was aided by the fact that the tool was developed in-house, in contrast to the usual portrayal of AI tools as plug-and-play.

  * Elish also develops the concept of [moral crumple zones](https://doaj.org/article/97ff6743ea7a44a5ade2a04fd2c57a3c): blaming incorrect decisions taken using automated systems on human operators without asking if they can provide reasonable oversight. 

  * Ben Green argues that [human oversight is overrated](https://www.sciencedirect.com/science/article/pii/S0267364922000292): it legitimizes faulty tools, provides a false sense of security, and cannot address the fundamental issues with algorithms.

  * [Deb Raji et al.](https://dl.acm.org/doi/10.1145/3531146.3533158) offer a taxonomy of the different kinds of failures that have occurred in real-world AI systems beyond risk prediction.




_The ideas in this post were developed during a[research project](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4238015) with [Angelina Wang](https://angelina-wang.github.io/) and [Solon Barocas](http://solon.barocas.org/). [Link](https://www.nicepng.com/maxp/u2t4y3w7e6i1o0o0/) to cover image source._
