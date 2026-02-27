---
title: "Generative AI companies must publish transparency reports"
author: "Arvind Narayanan & Sayash Kapoor"
date: ""
source: "substack_aisnakeoil"
url: "https://www.normaltech.ai/p/generative-ai-companies-must-publish"
---

How many people have used chatbots for self-diagnosis when they felt sick? For legal or financial advice? How often did they receive incorrect answers?

We don’t know.

How often have generative AI based search engines defamed people, like [falsely accusing a professor of sexual harassment](https://www.washingtonpost.com/technology/2023/04/05/chatgpt-lies/)?

We don’t know.

How often do chatbot users encounter inappropriate outputs reflecting racial, gender, or political biases?

We don’t know.

How many people are using chatbots and text-to-image generators for one of the many prohibited uses such as generating disinformation or child abuse images? How often are they successful at bypassing the tools’ filters? Are companies doing anything to track or enforce violations of their Terms of Service?

We don’t know.

The debate about the harms of AI is happening in a data vacuum.

#### Like social media platforms, generative AI providers must publish transparency reports

Like social media, people use generative AI to generate and consume content, and might be exposed to harmful content in the process. Due to public pressure as well as regulatory requirements, it has become [standard practice](https://www.tspa.org/curriculum/ts-fundamentals/transparency-report/) for social media companies to publish [detailed](https://www.tiktok.com/transparency/en/reports/) [transparency](https://transparencyreport.google.com/?hl=en) [reports](https://transparency.fb.com/policies/community-standards/) that quantify the spread of harmful content on the platform. We think AI companies should do the same.

Specifically, for each category of harmful output, transparency reports must:

  1. Explain how it is defined and how harmful content is detected.

  2. Report how often it was encountered in the reporting period.

  3. If it is the result of a Terms of Service violation, describe the enforcement mechanism and provide an analysis of its effectiveness.

  4. Describe the mitigations implemented to avoid it (e.g., safety filters), and provide an analysis of their effectiveness.




On social media, researchers have some visibility into the spread of harmful content, since much of it is public. But with generative AI, we are completely in the dark. So these transparency measures are urgent.

Transparency reporting is most critical for apps intended to be general-purpose (e.g., ChatGPT) and those intended to be used in a high-risk setting (such as medicine, finance, law, or hiring).

For open-source generative AI, transparency is infeasible since users can run it on their own devices. But we think that even with open-source models, most people will prefer cloud-based versions over locally running ones because of the hardware and expertise required to run them. Those service providers, rather than the developers of open-source models, should release transparency reports.

#### Transparency reports must cover all three types of harms from AI-generated content

There are three main types of harms that may result from model outputs.[1](https://www.normaltech.ai/p/generative-ai-companies-must-publish#footnote-1-131196575)

First, generative AI tools could be used to harm others, such as by creating non-consensual deepfakes or child sexual exploitation materials. Developers do have policies that prohibit such uses. For example, [OpenAI's policies](https://openai.com/policies/usage-policies) prohibit a long list of uses, including the use of its models to generate unauthorized legal, financial, or medical advice for others. But these policies cannot have real-world impact if they are not enforced, and due to platforms' lack of transparency about enforcement, we have no idea if they are effective. Similar challenges in ensuring platform accountability have also plagued social media in the past; for instance, ProPublica reporters [repeatedly](https://www.propublica.org/article/facebook-advertising-discrimination-housing-race-sex-national-origin) [found](https://www.propublica.org/article/facebook-doj-advertising-discrimination-settlement) that Facebook failed to fully remove discriminatory ads from its platform despite claiming to have done so.

Sophisticated bad actors might use open-source tools to generate content that harms others, so enforcing use policies can never be a comprehensive solution. In a recent essay, we [argued](https://knightcolumbia.org/content/how-to-prepare-for-the-deluge-of-generative-ai-on-social-media) that disinformation is best addressed by focusing on its distribution (e.g., on social media) rather than its generation. Still, some actors will use tools hosted in the cloud either due to convenience or because the most capable models don’t tend to be open-source. For these reasons, transparency is important for cloud-based generative AI.

Second, users may over-rely on AI for factual information, such as legal, financial, or [medical advice](https://jamanetwork.com/journals/jama-health-forum/fullarticle/2805334). Sometimes they are simply unaware of the tendency of current chatbots to frequently generate incorrect information. For example, a user might ask "what are the divorce laws in my state?" and not know that the answer is unreliable. Alternatively, the user might be harmed because they weren’t careful enough to verify the generated information, despite knowing that it might be inaccurate. Research on [automation bias](https://journals.sagepub.com/doi/10.1177/0018720810376055) shows that people tend to over-rely on automated tools in many scenarios, sometimes making more errors than when not using the tool.

ChatGPT includes a [disclaimer](https://www.theverge.com/2023/5/30/23741996/openai-chatgpt-false-information-misinformation-responsibility) that it sometimes generates inaccurate information. But OpenAI has often touted its performance on medical and legal exams. And importantly, the tool is often genuinely useful at medical diagnosis or legal guidance. So, regardless of whether it’s a good idea to do so, people are in fact using it for these purposes. That makes harm reduction important, and transparency is an important first step.

Third, generated content could be intrinsically undesirable. Unlike the previous types, here the harms arise not because of users' malice, carelessness, or lack of awareness of limitations. Rather, intrinsically problematic content is generated even though it wasn’t requested. For example, Lensa's avatar creation app generated [sexualized images](https://www.technologyreview.com/2022/12/12/1064751/the-viral-ai-avatar-app-lensa-undressed-me-without-my-consent/) and nudes when women uploaded their selfies. [Defamation](https://news.bloomberglaw.com/ip-law/first-chatgpt-defamation-lawsuit-to-test-ais-legal-liability) is also intrinsically harmful rather than a matter of user responsibility. It is no comfort to the target of defamation to say that the problem would be solved if every user who might encounter a false claim about them were to exercise care to verify it.

#### Transparency reporting is technically feasible

It would be cost prohibitive for companies to analyze every user interaction to identify possible harms. But transparency reporting only requires computing statistics, that is, the frequency with which various kinds of harmful or potentially harmful interactions occur. This only requires analyzing a [small sample](https://transparency.fb.com/policies/improving/prevalence-metric/).

Furthermore, the process can be largely automated. Returning to the social media analogy, content moderation has been increasingly automated over the last 10-15 years. And generative AI itself represents a significant advance in automation capabilities: OpenAI offers a GPT-based [moderation API](https://openai.com/blog/new-and-improved-content-moderation-tooling) to detect violations of its policies. Of course, policy violations are only a small fraction of the universe of harmful interactions, but the types of judgments involved are similar, and the same kinds of classifiers can be used to detect them.

To be sure, harm detection can’t be completely automated. If it could, generative AI products could be configured to simply avoid the problems in question, and transparency reporting wouldn’t be needed.

Still, AI can greatly cut down the number of interactions that need to be examined. For example, it can identify which conversations involve protected groups, but a human would need to judge which of those conversations resulted in hate speech. AI can flag medical, financial, or legal topics, but an expert would have to determine whether the bot gave incorrect advice. AI can identify conversations involving living people, but a person would need to judge whether any contained derogatory false information about them.

For many categories of harm, companies already have the necessary human resources in place. [Moderators](https://futurism.com/the-byte/ai-content-moderators-unionized-africa) do the work of labeling the appropriateness of inputs and outputs so that companies can fine-tune their models to be more aligned with user expectations. They would repurpose that infrastructure for transparency reporting. Unfortunately, moderation is often traumatic work. Moderators are [underpaid and undervalued](https://time.com/6247678/openai-chatgpt-kenya-workers/) across the industry, and companies must do better.

No doubt companies will resist transparency reporting for many reasons. For some types of content, such as medical, legal, or financial, they will need to hire experts. Having good coverage of the world’s languages and cultures will also likely raise costs. But AI companies [externalize their costs](https://twitter.com/random_walker/status/1624065031062138884) in many ways, and we think that this expense is necessary and justified.

Another reason companies might resist transparency is the reputational and possibly legal risk of publicly revealing that they are doing a poor job of harm mitigation. Of course, the reason we are advocating for transparency is precisely to be able to assess how well they are doing. If the benefits of transparency are widely recognized, not being transparent will incur a reputational cost, and we hope that companies will decide that it is better to improve their products rather than fight transparency.

Companies might view interaction data as a competitive advantage and resist transparency for that reason. If data about what people use generative AI for is made public, perhaps it would make it easier to build competing apps. But as we’ve argued before, the generative AI market is [too concentrated](https://aisnakeoil.substack.com/p/licensing-is-neither-feasible-nor). So while individual companies might not benefit from increased transparency, consumers and the market as a whole would benefit.

Ultimately, if generative AI companies don’t open up on their own, policymakers must require them to. We note that the EU’s draft AI Act has about a [dozen transparency measures](https://crfm.stanford.edu/2023/06/15/eu-ai-act.html) for foundation models, but none of them pertain to usage transparency.

#### Closing thoughts

Generative AI companies have welcomed regulations such as pre-release auditing requirements. But AI harms have at least as much to do with how people are using them as they do with the model itself. Lab testing can’t tell us about real-world use, which is why transparency reports are important.

Knowing which types of harms most significantly affect real people will help researchers understand which harm-mitigation interventions are most in need of development. It will help educators better teach people how to use generative AI responsibly. And most importantly, it will help regulators and civil society hold companies accountable for enforcing their policies.

_Cross-posted on the[Knight First Amendment Institute](https://knightcolumbia.org/blog/generative-ai-companies-must-publish-transparency-reports) blog._

_**Acknowledgments**. We thank Solon Barocas, Rishi Bommasani, and Katy Glenn Bass for their insightful comments._

[1](https://www.normaltech.ai/p/generative-ai-companies-must-publish#footnote-anchor-1-131196575)

Here, we consider the harms stemming from model outputs. [Weidinger and others](https://dl.acm.org/doi/pdf/10.1145/3531146.3533088) have a broader taxonomy of the various harms of language models. 
