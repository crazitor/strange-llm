---
title: "The machine that makes the thing is more valuable than the thing"
author: "François Chollet"
date: ""
source: "substack_fchollet"
url: "https://fchollet.substack.com/p/the-machine-that-makes-the-thing"
---

_Sparks in the Wind_ is now structured into two parts: a quick list of updates about what’s going on in my corner of the world, and a “weekly idea” — a short article about something for you to think about.

## News round-up for November 20, 2022

  * The Keras **FeatureSpace** utility for easy tabular data preprocessing is now available in tf-nightly. [See it in action in this tutorial](https://keras.io/examples/structured_data/structured_data_classification_with_feature_space/).

  * Join the StableDiffusion + Keras workshop at the **Women in ML Symposium 2022** online on Dec 7th. Everyone is welcome. [Register here](https://eventsonair.withgoogle.com/events/women-in-machine-learning-2022).

  * We’re in the process of crowdsourcing task candidates for **ARC 2** , a new benchmark for AI reasoning abilities. We’re giving out $100 weekly to top contributors. [Get started here](https://arc-editor.lab42.global/).

  * The **Keras code examples** page is now reorganized by category and subcategory. [Browse through our 167 tutorials](https://keras.io/examples/).




## Weekly idea: The machine that makes the thing is more valuable than the thing

Software companies aren't made of code, much like bakeries aren't made of bread. Software companies are made of _processes that produce and maintain code_. Software is a by-product of these processes. It's not even the _final_ product — it's a means to an end. The final product is a solution to a business problem.

#### Your company’s real hierarchy: from people to culture to processes

The foremost component of these processes are people. Software companies run on people, not servers. Your people are what make your company what it is.

The second most important component is culture. Your mission. Your values. The image that your team members have of themselves. And culture is shaped by your people. By leaders, most of all. And especially by founders. You can’t astroturf culture — culture is a reflection of who you are.

Then you have the organizational macrostructure — or architecture. The breakdown of your company into different units, with different scopes, coordinating in a certain way. Who works with who. Towards what. Why.

[](https://substackcdn.com/image/fetch/$s_!P4gP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fd31caf00-e073-40a9-9631-8cca88fec7a6_920x744.png)

Then you have the organizational specifics — the tooling and communication structure within each group. Does your team use Jira? GitHub issues? Do you do daily stand-ups or weekly email snippets? None of that?

Finally, you have the output of the machine — the code. The servers. Transient, sometimes expendable. Usually expensive to keep around. More of a liability than an asset.

Each of these layers influences every other layer. But each layer is _fundamentally_ _shaped_ by the layer above it.__ And it all starts with your people.

#### Company maturation as decantation

In a startup, the lower layers are entirely expendable, and will often get thrown away and rebuilt multiple times. But as a company matures, value starts decanting through the pile of layers. The lower layers become more sophisticated, and thus less expandable, more stable — they crystallize. They accrue in value and importance.

Look at that bottom layer. Your codebase gets bigger, more complex, increasingly harder to recreate from scratch. At some point, you might even mistake that pile of code for the center of gravity of your company. After all, it’s this code that’s generating the revenue, right? The team is just there to maintain it.

That would be a mistake. This decantation process slows down the flow of determinism, but does not reverse it. The codebase will always be downstream of the processes that produce it, no matter how complex and valuable it gets.

#### The key difference between the thing and the thing-making machine: adaptability

Here’s why: a codebase on its own is static. It lacks the ability to adapt, much less pivot. It solves a specific problem, in a specific context. But tomorrow something new will come up. A new technology. A new business model. New regulations. A new competitor. And you will have to adapt or die. Only a reliable process can save you. Your codebase, left on its own, won’t stay valuable for very long. The 2005 Google codebase would be largely worthless today. It is Google’s staff and Google’s engineering culture that have made it a trillion-plus dollar company today. And it is them that will keep steering the ship over the coming years.

It’s not just about maintenance. It’s about the ability to evolve. And, when push comes to shove, the ability to move on to something new entirely and give up the old thing.

#### Lessons

If you want to drive change, invest your efforts in each layer of the stack proportionally to its importance. People first. Then culture. Then organizational architecture. Code is downstream of processes, which are downstream of culture, which is downstream of people.

People are not replaceable cogs in service of a codebase. They’re the only real vector of success you have. Certainly, like in the ship of Theseus, you can replace one person or ten without meaningfully damaging the machine. But take away too many, and the stack falls down. All you will be left with is a static codebase built for a world that will soon no longer exist.
