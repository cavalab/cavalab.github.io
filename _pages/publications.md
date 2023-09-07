---
title: Publications
permalink: /publications/
classes: wide
layout: archive
---

[Google Scholar](https://scholar.google.com/citations?user=iZB7inEAAAAJ&hl=en)
|
[Sort by topic](/publications-by-topic)

{% assign pubs = site.publications | reverse %}
{% for pub in pubs %}
  {% include pub-single.html %}
  <div class="back-to-top"></div>
{% endfor %}