---
title: "My RSS Reader is Done"
author: "Brendan Long"
date: "2026-02-22"
source: "lesswrong"
url: "https://www.lesswrong.com/posts/Ci8Zkf3bEHeRKBJAP/my-rss-reader-is-done"
score: 34
votes: 15
---

I [posted a few months ago about vibe-coding an RSS reader](https://www.lesswrong.com/posts/vzaZwZgifypbnSiuf/claude-wrote-me-a-400-commit-rss-reader-app). The mood on the internet seems to be that these apps are buggy and never get finished, so I figured it was worth posting an update. Another [thousand commits](https://github.com/brendanlong/lion-reader/graphs/commit-activity) later, [Lion Reader](https://lionreader.com/demo/all?entry=welcome) supports every feature I care about, works reliably, has very good performance, and is [open for public signups](https://lionreader.com/register)[^0zt1hlucizjc].

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/39742e6d38f1e70e46f4b5b6198ca1381ecd3a3484ebb3e3.png)

I've actually been using it for a while, and mostly kept signups closed because of some expensive features like AI summaries (now handled by making users provide their own API keys).

The features are entirely designed around what me and a friend find useful, but I think I have decent taste so consider Lion Reader if they're useful to you as well:

*   [Subscribe to RSS/ATOM/JSON/email newsletter feeds](https://lionreader.com/demo/subscription/feed-types)
*   [Save articles for later](https://lionreader.com/demo/all?entry=save-for-later), including [special logic for Google Docs, LessWrong, and ArXiv](https://lionreader.com/demo/all?entry=plugins)
*   On-demand [AI summaries](https://lionreader.com/demo/all?entry=ai-summaries) (requires an Anthropic API key)
*   An [MCP server](https://lionreader.com/demo/all?entry=mcp-server)
    *   Read feeds, i.e. "Summarize my most recently 10 articles in tag X"
    *   Upload reports as saved articles[^wrly2692x8p]
*   [Google Reader / Fresh RSS API](https://lionreader.com/demo/all?entry=google-reader-api) for native clients (doesn't support summaries)
*   [Narration](https://lionreader.com/demo/all?entry=text-to-speech)[^i4wws9tf1gj] with highlighting, similar to how Kindle narration works
*   [Algorithmic feed](https://lionreader.com/demo/all?entry=scoring) based on your votes (can be disabled)
*   [Firefox](https://addons.mozilla.org/en-CA/firefox/addon/lion-reader/) and Chrome[^koyq2wjk67] [browser extensions](https://lionreader.com/demo/all?entry=browser-extension) for saving articles
*   All of the things you'd expect like [dark/light themes](https://lionreader.com/demo/all?entry=appearance), [tags](https://lionreader.com/demo/all?entry=tags), etc.
*   It's [open source](https://github.com/brendanlong/lion-reader) of course, and free[^9846h6krc4g]

I thought it would be funny to use a demo of the app to describe the features, so if you're curious, [all of the features are listed in "articles" here](https://lionreader.com/demo/all?entry=welcome).

I think at this point, every feature I care about is implemented on the web app, although [I want to improve how the local caching works and incidentally add offline mode based on that](https://github.com/brendanlong/lion-reader/issues/411). At some point I might make a native app for Android again, but I don't really have time to validate one.

I'm open to [feature requests](https://github.com/brendanlong/lion-reader/issues) and pull requests (as long as they include screenshots to demonstrate that the feature works).

![](https://39669.cdn.cke-cs.com/rQvD3VnunXZu34m86e5f/images/983fb8079167eedbed5e9510fad7872039c4b67f22d0fe59.png)

[^0zt1hlucizjc]: Signups require a Google or Apple account as a minimal anti-bot measure. 

[^wrly2692x8p]: For example, you can tell Claude Code to run an ML experiment and upload a report to Lion Reader when it's done. 

[^i4wws9tf1gj]: Unfortunately, narration only works in the foreground because we're not a native app. I have ideas for supporting background play but it's very complicated so I haven't got around to it. 

[^koyq2wjk67]: The Chrome extension is still in review. 

[^9846h6krc4g]: Some features require paid API keys for other services, but they're all optional.