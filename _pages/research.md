---
collection: research
title: Research 
permalink: /research/
entries_layout: listpic
---

Our research focuses on developing machine learning methods and using them to explain the principles underlying complex, biomedical processes.
We use these methods to learn predictive models from electronic health records (EHRs) that are both <i>interpretable</i> to clinicians and <i>fair</i> to the population on which they are deployed. 
Our long-term goals are to positively impact human health by developing methods that are flexible enough to automate entire computational workflows underlying scientific discovery and medicine.

See our <a href="/publications">publications</a> and <a href="/posts">posts</a> about them.

## Projects

### Fair Machine Learning for Health

<div class="entries-grid">
  {% assign posts = site.projects | where:"tag","fairness" %}
  {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
  {% endfor %}
</div>
<div class="back-to-top"></div>

### Interpretable Machine Learning for Health

<div class="entries-grid">
  {% assign posts = site.projects | where:"tag","interpretability" %}
  {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
  {% endfor %}
</div>
<div class="back-to-top"></div>

### Automating Digital Health

<div class="entries-grid">
  {% assign posts = site.projects | where:"tag","ai" %}
  {% for post in posts %}
      {% include archive-single.html type=page.entries_layout %}
  {% endfor %}
</div>
<div class="back-to-top"></div>