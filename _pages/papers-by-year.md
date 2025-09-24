---
title: Papers by Year
permalink: /papers-by-year/
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
        {% assign pass = false %}
        {% for author in pub.author %}
            {% if author.family contains "Cava" or author.literal contains "Cava" %}
                {% assign pass = true %}
                {% break %}
            {% endif %}
        {% endfor %}
        {% if pass %}
            {% include pub-single.html %}
        {% endif %}
      {% endif %}
    {% endfor %}
  </div>

{% endfor %}