---
title: "Open sourcing a browser extension that shows when people are wrong on the internet"
author: "lc"
date: "2026-02-24"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/iMw7qhtZGNFxMRD4H/open-sourcing-a-browser-extension-that-shows-when-people-are"
score: 143
votes: 83
---

![Screenshot From 2026-02-22 14-58-40 bordered-shadow.png](https://res.cloudinary.com/lesswrong-2-0/image/upload/v1771801565/lexical_client_uploads/gqxuyfkozrs4psnuiv01.png)

*Example of OpenErrata nitting the Sequences*

I just published [OpenErrata](https://github.com/ZeroPathAI/OpenErrata), a browser extension that investigates the posts you read using your OpenAI API key, and underlines any factual claims that are sourceably incorrect. It then saves the results of the investigation so that whenever anybody else using the extension visits the post (with or without an API key), they get the corrections on their first visit.

I've noticed that while people can theoretically paste everything they're reading into ChatGPT for verification:

*   No one has the time to do that
*   It duplicates work between readers
*   It takes around 5 minutes to get a really good sourced response for most mid-length posts. 

I figure most of LessWrong is reading the same stuff, and that if a good portion of the community begins using this or something like it, we can avoid these problems.

Here is OpenErrata at work on some LessWrong & Substack articles that were published within the last week. I was a little surprised at what a high percentage of the articles I read seem to have at least one or two errors, even with how conservative [my prompt](https://github.com/ZeroPathAI/OpenErrata/blob/main/src/typescript/api/src/lib/investigators/prompt.ts) is. When I delete rows from the database and rerun, often it finds different (and valid) ones it didn't find the first time:

![OpenErrata highlighting an incorrect claim on Astral Codex Ten with a hover tooltip showing the correction and source](https://github.com/ZeroPathAI/OpenErrata/raw/main/assets/demo-hover.jpg)

["Record Low Crime Rates Are Real, Not Just Reporting Bias Or Improved Medical Care" ](https://www.astralcodexten.com/p/record-low-crime-rates-are-real-not)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/9eaa73dc8fbbe3d0deccc2182c7da30c44ffd739b03686da.png)

[Life at the Frontlines of Demographic Collapse](https://www.lesswrong.com/posts/FreZTE9Bc7reNnap7/life-at-the-frontlines-of-demographic-collapse)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/23c7e7d630e3492c8bc36ba32146668c05708219da0c93d4.png)

[Be skeptical of milestone announcements by young AI startups](https://www.lesswrong.com/posts/qefrWyeiMvWEFRitN/be-skeptical-of-milestone-announcements-by-young-ai-startups)

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/e334375067cd054a05d43e17b5d5dd0f3a8f8d68550290d5.png)

[Did Claude 3 Opus align itself via gradient hacking?](https://www.lesswrong.com/posts/ioZxrP7BhS5ArK59w/did-claude-3-opus-align-itself-via-gradient-hacking) (Note: as pointed out by commenters, [this correction is incorrect](https://www.lesswrong.com/posts/iMw7qhtZGNFxMRD4H/open-sourcing-a-browser-extension-that-shows-when-people-are?commentId=eYTiut5uHnztxLFP6). Leaving it up as it still seems interesting as a statement about the models.)

The project is published under my company, but the entire thing is self-hostable and AGPLv3 licensed. I also made an API available so that providers can use the results for articles independently and do statistics on them/embed them. Some future additions I & others could work on:

*   A website for 'leaderboards'/'loserboards', viewing in progress investigations, helpful-to-the-reader reputation mechanics, etc.
*   Reasoning for no-nit results.
*   An appeal process that is completely AI driven, so that you can talk to the AI to point out either additional ways articles are wrong, or reasons previous nits are incorrect, which are reflected in the results. I think it should be possible to figure out how to make that adversarially robust as the tool gets better.
*   Support for other sites (NYT, Wikipedia, Reddit, Nitter, etc.) Right now it only works on LessWrong/Substack and X (sort of).
    *   Better support for X/Twitter; I've got some ideas for ways the investigator could actually access related tweets and sources, for example.
*   Support for comments.

I really enjoyed working on & using this and want to keep doing so, so let me know if you like it/find it useful!