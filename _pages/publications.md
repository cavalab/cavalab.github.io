---
title: Publications
permalink: /publications/
classes: wide
layout: archive
---

{% assign pubs = site.publications | reverse %}
{% for pub in pubs %}
  {% include pub-single.html %}
  <div class="back-to-top"></div>
{% endfor %}