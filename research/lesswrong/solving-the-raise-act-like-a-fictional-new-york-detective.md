---
title: "Solving The RAISE Act Like a (fictional) New York Detective"
author: "Josephine Schwab"
date: "2026-02-24"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/DniEo2DWXjkt46ihF/solving-the-raise-act-like-a-fictional-new-york-detective"
score: 3
votes: 3
---

*The RAISE Act Still Lacks A Meaningful Third-Party Assessment Regime*
----------------------------------------------------------------------

I’m a big fan of the current New York-based mystery-comedy drama *Only Murders in the Building* – particularly of the character Detective Donna Williams. I thought I might apply the detective's singular crime-solving methodology to my analysis of [New York’s RAISE Act](https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A09449&term=2025&Summary=Y&Text=Y), a fine example of which can be witnessed here:  
  
[https://www.youtube.com/watch?v=hC7q0-5DxPs&t=97s](https://www.youtube.com/watch?v=hC7q0-5DxPs&t=97s)   
  
This post argues for the RAISE Act to be amended to include a mandatory independent assessment regime, and suggests how that regime should be structured. But, before we begin to apply Det. William's methodology, let’s make sure that we are all up to speed.

A09449 – [New York's Responsible AI Safety and Education Act](https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A09449&term=2025&Summary=Y&Text=Y) – is widely [discussed](https://www.findarticles.com/new-york-passes-raise-act-on-ai-safety-into-law) as imposing independent oversight on frontier AI developers, but it does not do that.

In fact, third-party involvement of AI model assessments is left almost entirely to developer discretion. As it stands, the RAISE Act's transparency provisions require large frontier developers to publish *their own* frontier AI framework – including documented protocols for managing catastrophic risk – and to report critical safety incidents in a timely fashion to an Office within the Department of Financial Services (DFS), which currently lacks the necessary expertise. 

These provisions are somewhat meaningful, I suppose, but the Act's treatment of third-party assessment amounts to little: frontier developers must describe, within their own framework*,* how they use third parties to assess catastrophic risk and the effectiveness of mitigations. That is a transparency requirement – the Act does not mandate independent assessment.   
  
So it follows that the Act does not specify what form third-party independent assessment might take, or who is qualified to conduct them, and does it not require that any output from these assessments be shared with regulators. Whether a developer uses rigorous independent evaluators, or cursory tick-box consultants, the statutory requirement is satisfied identically. This is an enormous gap which represents the central structural weakness of the Act.

True, RAISE makes non-compliance with a developer's own frontier AI framework a violation but, writing this from a European’s perspective, this is a recurring legislative weakness typical of an economy dependent on a less constrained form of capitalism. It creates an obvious and perverse incentive: that developers who design conservative frameworks will be more able to satisfy the statute while providing no meaningful safety assurance. Unfortunately, the compliance mechanism will reward frameworks that minimise the risk of non-compliance findings – rather than design that actually minimises catastrophic risk.

Independent third-party assessment is the standard corrective in safety-critical industries precisely because this incentive structure is well understood. Aviation, nuclear engineering, and pharmaceuticals all require external verification, not because regulators distrust developers, but because they recognise that internal teams face pressures – whether commercial, reputational, or organisational – that lead to unreliable self-certification when the stakes are high. There is no principled reason frontier AI should be treated differently, but considerable reason to think the stakes here are higher.

Historically, the US has had to learn this the hard way. When the FAA progressively delegated airworthiness certification to Boeing's own employees, commercial pressure to certify the [737 MAX](https://en.wikipedia.org/wiki/Boeing_737_MAX_groundings) without requiring new pilot training contributed to failed scrutiny of a flawed control system, and 346 people died across two crashes before the issue with manufacturer self-certification was confronted. When internal studies by the health science tech company, Merck, indicated elevated cardiovascular risk in [Vioxx](https://www.newscientist.com/article/dn6918-up-to-140000-heart-attacks-linked-to-vioxx), which was a popular prescription anti-inflammatory, inadequate independent post-market surveillance meant these findings went unsurfaced and the drug remained on the market for years, with excess deaths estimated in the tens of thousands. And when accountant Arthur Andersen audited energy company [Enron](https://en.wikipedia.org/wiki/Enron_scandal) while simultaneously consulting for it, the commercial relationship produced exactly the structural bias that auditor independence requirements exist to prevent. In each case, the failure was the same: internal teams faced pressure to avoid findings that would be costly to act on, continuing without meaningful independent verification. The AI safety community is not asking legislators to accept an unfamiliar regulatory logic, but to accept a logic that every other high-stakes industry has already learned the necessity of.

Getting back to Detective Williams, a robust independent assessment regime needs to address four questions: who is conducting the assessment (*the who*), what is being assessed (*the how*), what happens to the results (*the why*), and when the assessments must occur (*the why now*).

> Charles:   *G-Get the… the what and the what?*
> 
> Det. Williams:   *See, why would you say what? I never said what. There’s no what. It’s “**the who, the how, the why, and the why now”**. Make the case.*

So, without further ado, let's solve RAISE.

### ***The who.***

Allowing developers to choose their own assessors, even with conflict-of-interest carve-outs, will reproduce the same structural biases that have produced serious failures in other sectors, as mentioned above. For example, a developer that pays an assessor and retains discretion over future engagements has significant leverage over findings. An accreditation regime – in which an independent body certifies assessors as meeting defined competence and independence criteria – is the standard solution.

The RAISE Act already establishes an Office within the DFS with rulemaking authority; that Office could be tasked with developing accreditation criteria in consultation with bodies that have more relevant technical expertise, including NIST and federal AI safety bodies, where they exist. Developer-chosen assessors might be permitted on a transitional basis while that infrastructure is being built, potentially with something like an 18 month statutory sunset built-in.

### ***The how. ***

A detective who only checks whether the suspect's alibi is internally consistent has not solved the case, they have only verified a story. Compliance-only auditing does the same thing. *The how* needs to cover four distinct assessment categories, not just whether the developer did what it said it would do:

First, compliance audits – which means verifying that a developer is actually implementing what its own framework describes.

Second, capability replication – which means independently verifying that the developer's evaluations of its own model's capabilities are accurate and not cherry-picked, or gamed.

Third, adversarial testing of mitigations – which means verifying that safeguards designed to prevent catastrophic misuse hold under adversarial pressure, not just in benign evaluation conditions.

Fourth, framework adequacy assessment – which means evaluating whether the framework itself is designed to manage the risks it claims to address, rather than merely creating compliance with whatever the developer chooses to commit itself to.

The last of these is arguably the most important, and also the hardest to operationalise because there is currently no authoritative standard. Therefore, minimum adequacy criteria would need to be established through rulemaking, but the statutory requirement for such an assessment needs to precede that rulemaking, rather than wait for it.

### ***The why. ***

This covers what happens to the findings, and why they need to reach someone with both the expertise and authority, to act on them. Confidentiality agreements that could potentially seal third-party assessment results from the regulators would achieve the same outcome as a solved crime that never reaches the chief prosecutor: findings that exist on paper but cannot drive enforcement. Disclosure obligations are what give the whole exercise its purpose. So, confidentiality agreements between developers and assessors should not be permitted to prevent regulatory access to findings.

### ***The why now. ***

Assessment triggers oriented entirely around deployment miss the pre-training window, where some risks are better prevented than detected. A pre-training assessment requirement, which could be triggered at defined compute thresholds, could allow assessors to flag whether a proposed training run is likely to produce capabilities that the developer's existing framework is not designed to manage. 

Beyond that, periodic post-deployment review is also essential. Catastrophic risk can potentially emerge from use patterns which are not foreseeable at deployment, and quarterly internal reporting to the Office cannot be treated as a substitute for external verification. Assessments should also be triggered automatically by critical safety incidents, within a defined window.

### RAISE Act's "catastrophic risk"

One further gap is worth noting. The Act's catastrophic risk definition (§1420(3)(a)) focuses on capabilities – CBRN uplift, autonomous harmful conduct, control evasion – or it defines 50 deaths or $1 billion in property damage from a single incident. This is deliberately narrow, and excludes diffuse systemic harms that may not cross the single-incident threshold, but nonetheless represent serious societal harms. These could potentially involve large-scale fraud enabled by frontier models, disinformation infrastructure, economic displacement, or other harms.

Independent assessors operating under this definition have no mandate to assess those risks, even where they are clearly foreseeable. Whether the enforcement regime for systemic harms belongs in the same statutory track is a legitimate design question, but an assessment regime should, at minimum, be able to surface them. These are matters the Office could determine via rulemaking.

### To summarise.

None of the above is technically complex to draft – mandatory assessment categories can be specified, assessor accreditation can follow a standard template from financial regulation, and disclosure obligations are well-precedented – the harder political question is whether New York's legislature is willing to impose requirements that meaningfully constrain developer discretion, rather than allowing developers to describe how they constrain themselves. 

Sadly, the RAISE Act in its current form largely does the latter. That may be defensible as a first step toward building a transparency infrastructure, but it is not defensible as an adequate response to catastrophic risk.

**Back to** ***Only Murders...*** I ask you, would Detective Williams accept a case file that described how the suspect planned to monitor themselves? Would she close an investigation because the alibi was, at least, internally consistent? Would she hand jurisdiction to the institution with the little relevant expertise and call it a day? The RAISE Act, in its current form, does all three.

*The who* is unaccredited, *the how* is self-referential, *the why* goes nowhere enforceable, and *the why now* arrives too late. The mystery here is not whether frontier AI poses catastrophic risk (the legislature has already answered) it is why, having identified the threat, RAISE has yet to build the investigative architecture capable of meeting it. New York has written the premise, but it has not yet written the case.

[*Josephine Schwab*](https://www.linkedin.com/in/jreschwab) *is a Research Associate with the Arcadia Impact AI Safety Governance Taskforce, a former Senior Research Fellow (European Security) with the European Institute of Policy Research and Human Rights, former Veritas Forecasting Research Fellow with The Midas Project, UK parliamentary reporter and international justice news writer, and author of “Diplomacy in the Age of AGI”, featured by Futures4Europe, the European Commission’s foresight community platform.*

Photo by [Michael Discenza](https://unsplash.com/@mdisc?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/landscape-photo-of-new-york-empire-state-building-5omwAMDxmkU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)