---
title: "Simplifying symbolic regression models without simplification rules"
date: 2024-04-14
layout: posts
author: galdeia
excerpt: Relaxing the definition of equivalent mathematical expressions to get more simpler and interpretable models
tags: 
    - Symbolic Regression
    - Simplification
    - Interpretability
header:
    teaser: /assets/images/inexact-simplification-equivalent-models.svg
toc: true
---

Hello world!

{% assign pub = site.publications 
    | where_exp:"pub", "pub.title == 'Inexact Simplification of Symbolic Regression Expressions with Locality-sensitive Hashing'" 
    | first %}
{% include pub-single.html %}
{:.notice}