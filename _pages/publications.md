---
title: Publications
permalink: /publications/
classes: wide
layout: archive
---

{% include pubs_by_date.html %}
{% for pubs in pubs_by_date %}
  {% for pub in pubs.items %}
    {% include pub-single.html %}
  {% endfor %}
{% endfor %}