---
title: "SWE-Bench Pro is even worse"
author: "Jonathan Gabor"
date: "2026-02-24"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/nAMhbz5sfpcynjPP5/swe-bench-pro-is-even-worse"
score: 22
votes: 10
---

Yesterday, OpenAI [announced](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/) that they would be no longer using [SWE-Bench Verified](https://openai.com/index/introducing-swe-bench-verified/), instead recommending [SWE-Bench Pro](https://scale.com/leaderboard/swe_bench_pro_public).

One of their justifications was: many tasks from SWE-Bench Verified are broken. A correct solution might not be accepted. They are correct about this. These issues have been [documented](https://fulcrumresearch.ai/2025/12/15/lunette.html) [by others](https://arxiv.org/abs/2410.06992).

However, as bad as SWE-Bench Verified is, SWE-Bench Pro is much, much worse.

* * *

I audited 100 random Swe-Bench pro problems[^vquxu6zo3i]. The full audit results are [here](https://github.com/JonathanGabor/swe-bench-pro-audit/blob/main/audit_results/20260127_171004/audit.txt).

![](https://substackcdn.com/image/fetch/$s_!e8lF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbeff28fd-39ec-4015-9c9e-42ec6c61d5a7_754x204.png)

The most common issue was test leniency. In many cases, the tests ***barely checked the required functionality at all***.

For example, here’s Claude on NodeBB-a91721:

> **Core Issue Not Tested**: The original problem states users should be able to register “using only a valid invitation token, without requiring an email.” Neither test verifies registration without an email - both tests still provide an email during registration.

How did this happen? My guess is: SWE-Bench Pro simply scraped any GitHub commit that modified test cases, regardless of whether those modifications were substantive. In this instance, existing test cases were modified to match the new type signature, but no new test cases were added.

* * *

In another instance, the test cases ***require the agent’s solution to be incorrect***.

In [flipt](https://github.com/flipt-io/flipt), the IsNotOneOf operator was incorrectly implemented to be identical to the IsOneOf operator. This was [later fixed](https://github.com/flipt-io/flipt/pull/2912).

![](https://substackcdn.com/image/fetch/$s_!9wJU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7460486-170b-495d-9721-ccd51aff1d72_936x592.png)

But SWE-Bench Pro (flipt-cd2f3b0) simply ***scraped the original, incorrect, test cases***.

> There’s a critical bug here. Looking at the tests:
> 
> \- “is not one of”: value “3” is NOT in `\[5, 3.14159, 4\]`, so \`isnotoneof\` should return \*\*TRUE\*\*, but test expects \`false\`
> 
> …
> 
> An agent correctly implementing the requirements would \*\*FAIL\*\* these tests.

—Claude

* * *

The most common issue was “requirements inflation”.

Real world test cases scraped by SWE-Bench Pro will assume implementation details not mentioned in the corresponding issue description. Such tests would be unfair to an agent that produced a correct but alternative implementation.

SWE-Bench Pro addresses this issue by adding a “requirements” section, that includes information about the gold patch’s implementation.

However, these requirements sections frequently go far beyond the details necessary to pass the tests, including implementation details that are not tested at all.

For example, here’s claude’s analysis of tutanota-09c277. While the core functionality is tested, extra implantation details specified in the requirements are not:

![](https://substackcdn.com/image/fetch/$s_!FD-O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F745b81d9-b99a-45ad-980b-afccf457b41f_1360x624.png)

* * *

So if the time has come to retire SWE-Bench verified, then the time has come. But please, please, do not switch to SWE-Bench Pro.

[^vquxu6zo3i]: Using a similar methodology to my Terminal-Bench 2 audit. This time, I also searched for cases where the tests were too strict.