---
title: "Did ChatGPT Really Pass Graduate-Level Exams?"
author: "Melanie Mitchell"
date: ""
source: "substack_aiguide"
url: "https://aiguide.substack.com/p/did-chatgpt-really-pass-graduate"
---

Way back in 2019—an eon ago in AI time—the _New York Times_[reported an AI milestone](https://www.nytimes.com/2019/09/04/technology/artificial-intelligence-aristo-passed-test.html): [Aristo](https://arxiv.org/abs/1909.01958), a natural-language processing and reasoning system scored over 90% on parts of the New York Regents 8th Grade Science Exam, and over 83% on parts of the corresponding Grade 12 Science Exam. Aristo, the Times proclaimed, “is ready for high school science. Maybe even college.”

I [argued](https://www.wired.com/story/ai-can-pass-standardized-testsbut-it-would-fail-preschool/) this at the time: “The truth is that while these systems perform well on specific language-processing tests, they can only take the test. None come anywhere close to matching humans in reading comprehension or other general abilities that the test was designed to measure.” Moreover, such systems lack the basic commonsense understanding of the world that is assumed of humans taking the same tests. In effect, I claimed, “Rather than being ready for high school or college, AI has a lot of growing to do before it’s even ready for preschool.”

Now, four years later, we have a new generation of AI systems, and many people are proposing that they are now ready not just for college, but for professional graduate school. Just in the last few months several reports have come out on giving GPT-3 and ChatGPT test questions in the fields of business, law, and medicine. In the throes of ChatGPT-mania, these reports were covered quite breathlessly in the media: 

**Bloomberg News:** [“ChatGPT Gets an MBA”](https://www.bloomberg.com/news/articles/2023-02-04/chatgpt-passed-a-wharton-mba-exam-are-professors-worried)

**Fox 10 Phoenix:** “[ChatGPT may be smart enough to graduate law school](https://www.fox10phoenix.com/news/chatgpt-graduate-law-school-university-minnesota)“

**Medscape:** [“AI Bot ChatGPT Passes US Medical Licensing Exams Without Cramming—Unlike Students”](https://www.medscape.com/viewarticle/987549)

In this post and the next one I will dig into what actually happened when ChatGPT and GPT-3 were given these tests, and how we should think about the results. Did these systems actually pass the same exams that humans take? What does it mean when an AI system performs well on an exam designed for humans? Does giving such exams to AI systems provide a true assessment of their abilities and limitations?

**Case 1: ChatGPT and MBA Test Questions**

Christian Teriesch, a professor at the Wharton School (the University of Pennsylvania’s business school), [wrote about](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/01/Christian-Terwiesch-Chat-GTP-1.24.pdf) giving ChatGPT questions from the final exam of his Operations Management course. He gave the questions to ChatGPT as prompts, and graded its responses as if it were one of his students. Here’s an example question from Teriesch’s report:

> World-Antique is a new venture under development by two graduates of a New England business school. The value proposition of the venture is simple: purchase antique paintings at yard sales and auctions and then sell them at quadruple the purchase price via a simple eCommerce site (i.e., a painting that is purchased for $100 would be sold at $400). Based on an analysis of similar retailers, the founders expect to turn their inventory 1.5 times per year. To achieve an annual revenue of $3,000,000, how much inventory expressed in $’s should the founders expect their operation to require?

Here is the response ChatGPT gave:

> To achieve an annual revenue of $3,000,000, the founders need to sell $3,000,000 / 4 = $750,000 worth of paintings per year. Since they expect to turn their inventory 1.5 times per year, they need to have $750,000 /1.5 = $500,000 worth of inventory at any given time. Therefore, the founders should expect their operation to require $500,000 worth of inventory.

Quite impressive! Teriesch’s comment: “Short and sweet! ...A+.”

ChatGPT performed equally impressively on some other test questions, but not all. In some cases, it had the right idea but made dumb mathematical errors. In other cases, its answer was far off the mark. Overall, Teriesch concluded, “Considering this performance, Chat GPT would have received a B to B- grade on the exam.”

A few reactions from the media: 

[](https://substackcdn.com/image/fetch/$s_!wAiB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4c15926-10d8-45b1-a971-52f80e0cd034_1216x456.png)

So what actually happened here? No, [Bloomberg News](https://www.bloomberg.com/news/articles/2023-02-04/chatgpt-passed-a-wharton-mba-exam-are-professors-worried), ChatGPT did not get an MBA. No, [NBC News](https://www.nbcnews.com/tech/tech-news/chatgpt-passes-mba-exam-wharton-professor-rcna67036), ChatGPT did not even pass an exam. Teriesch’s article isn’t very specific about how many questions he gave it; he simply says “I uploaded some of my exam questions to ChatGPT and then graded the responses”. So it doesn’t sound like he gave it the entire exam; he just extrapolated from a sample of questions that the system “would have received a B to B-”. And no, [New York Post](https://nypost.com/2023/01/23/chatgpt-outperforms-humans-on-wharton-mba-exam-professor/), ChatGPT did not outperform students on this exam—at least there is nothing in Teriesch’s article that says that ChatGPT outperforms actual MBA students (though it’s certainly possible that it did outperform some students on certain questions). 

Despite the hype, the fact that we now have AI systems that can deal with natural language at this level is extraordinary and will be highly impactful. Teriesch goes further, asserting that “ChatGPT has shown a remarkable ability to automate some of the skills of highly compensated knowledge workers in general and specifically the knowledge workers in the jobs held by MBA graduates including analysts, managers, and consultants.” But does an AI system’s performance on an exam actually predict that it will exhibit skills in the real world? Perhaps there is a correlation between how _humans_ perform on tests and on their future skills in the real world, but that correlation has not been demonstrated for AI systems.

For example, when a human succeeds in answering a test question such as the example on inventory given above, we assume that the human can then generalize this understanding to similar situations—the point of the test, after all, is to evaluate knowledge and skills that go beyond the wording of any specific question. But is the same true for ChatGPT?

To test this, I wrote a variation of the inventory question, one that is identical in structure and in reasoning strategy, but uses different wording. 

> Boll is a new company founded by three recent MBAs. The company plans to buy used automobiles at auctions and then sell them at four times the purchase price direct to consumers (i.e., a car that is purchased for $1,000 would be sold at $4000). Based on an analysis of similar companies, the owners of the company expect to turn their inventory 1.5 times per year. To achieve an annual revenue of $3,000,000, how much inventory, expressed in dollars, should the company expect its operation to require?

The correct answer is identical to that for the original question: The founders need to sell $3,000,000 / 4 = $750,000 worth of cars per year; they need to have $750,000 / 1.5 = $500,000 worth of inventory.

I am pretty sure that a Wharton MBA student who could answer the original question correctly could also answer this one correctly. 

I gave it to ChatGPT. Its response was...well, not an A+ answer:

> To calculate the required inventory, we first need to determine the amount of revenue that needs to be generated per car sold. To generate $3,000,000 in annual revenue, and assuming the company turns its inventory 1.5 times per year, we need to generate $3,000,000 / 1.5 = $2,000,000 in revenue from car sales.
> 
> Next, since each car is sold for four times the purchase price, we can determine the average purchase price of a car by dividing the target revenue per car by 4: $2,000,000 / 4 = $500,000.
> 
> Finally, to determine the required inventory, we divide the total target revenue by the average purchase price per car: $3,000,000 / $500,000 = 6 cars.
> 
> So, the company should expect its operation to require $500,000 * 6 = $3,000,000 in inventory.

Something went badly awry here—I’ll leave it to the reader to explain the faulty logic. Indeed, unlike humans, ChatGPT’s response is very sensitive to the details of its prompt. The fact that ChatGPT does well on one version of a problem does not mean that it has a humanlike understanding of the problem or that it will be able to solve similar (or even essentially identical) problems. Probing the system’s understanding requires much more than giving it a single version of a question.

In the next post (coming soon) I’ll do a similar deep dive into recent reports of ChatGPT taking law school and medical school exams, and make some general comments about what we can (and cannot) learn by giving AI systems tests designed for humans. 

Update: Part 2 is [here](https://aiguide.substack.com/p/did-chatgpt-really-pass-graduate-baa).
