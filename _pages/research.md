---
layout: archive
collection: research
title: Research 
permalink: /research/
entries_layout: listpic
---

Our research focuses on developing machine learning methods and using them to explain the principles underlying complex, biomedical processes.
We use these methods to learn predictive models from electronic health records (EHRs) that are both <i>interpretable</i> to clinicians and <i>fair</i> to the population on which they are deployed. 
Our long-term goals are to positively impact human health by developing methods that are flexible enough to automate entire computational workflows underlying scientific discovery and medicine.

See our <a href="/publications">publications</a> and <a href="/posts">posts</a> about them.

<h2 class="archive__subtitle">Themes</h2>
<div class="entries-grid">
  {% for post in site.research %}
      {% include archive-single.html type="list" %}
  {% endfor %}
</div>
<div class="back-to-top"></div>

<h2 class="archive__subtitle">Projects</h2>

<div class="entries-grid">
  {% for post in site.projects %}
      {% include archive-single.html type=page.entries_layout %}
  {% endfor %}
</div>
<div class="back-to-top"></div>

