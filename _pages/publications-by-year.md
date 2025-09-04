---
title: Papers
permalink: /papers/
redirect_from:
    - /publications/
classes: wide
layout: archive
---

{% include pubs_by_date.html %}

{% for year in years %}
  <a href="#{{ year }}"></a>
{% endfor %}

{% for year in years %}
  <h2 id="{{ year }}" class="archive__subtitle">{{ year }}</h2>

  <div class="entries-{{ entries_layout }}">
    {% for pub in pubs_by_date %}
      {% if pub.issued.first.year == year %}
            {% include pub-single.html %}
      {% endif %}
    {% endfor %}
  </div>

{% endfor %}