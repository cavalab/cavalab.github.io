---
title: Papers
permalink: /papers/
redirect_from:
    - /publications/
classes: wide
layout: archive
---

---

{% include pubs_by_date.html %}
{% for pub in pubs_by_date %}
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
{% endfor %}
