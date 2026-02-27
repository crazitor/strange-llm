---
title: "The SSL Certificate of Damocles"
author: "Scott Aaronson"
date: "Wed, 15 May 2019"
source: "scottaaronson_blog"
url: "https://scottaaronson.blog/?p=4191"
---

Ever since I "upgraded" this website to use SSL, it's become completely inaccessible once every three months, because the SSL certificate expires. Several years in, I've been unable to find any way to prevent this from happening, and Bluehost technical support was unable to suggest any solution. The fundamental problem is that, as long as the site remains up, the Bluehost control panel tells me that there's nothing to do, since there _is_ a current certificate. Meanwhile, though, I start getting menacing emails saying that my SSL certificate is about to expire and "you must take action to secure the site"--_never_ , of course, specifying what action to take. The only thing to do seems to be to wait for the whole site to go down, then frantically take random certificate-related actions until somehow the site goes back up. Those actions vary each time and are not repeatable.

Does anyone know a simple solution to this ridiculous problem?

(The deeper problem, of course, is that a PhD in theoretical computer science left me utterly unqualified for the job of webmaster. And webmasters, as it turns out, need to do a lot just to prevent anything from changing. And since childhood, I’ve been accustomed to countless tasks that are trivial for most people being difficult for me—-if that ever stopped being the case, I’d no longer feel like myself.)
