---
title: Publications
permalink: /publications-by-topic/
layout: single
toc: true
toc_label: "Topics"
---

[By date](/publications)
|
By topic

{% assign tags = site.data.publications.references | map: 'tags' | uniq | sort %}
{% assign pubs = site.data.publications.references | reverse %}

{% for tag in tags %}
  <a href="#{{ tag | slugify }}"></a>
{% endfor %}

{% for tag in tags %}
  <h2 id="{{ tag | slugify }}" class="archive__subtitle">{{ tag }}</h2>

  <div class="entries-{{ entries_layout }}">
    {% for pub in pubs %}
      {% if pub.tags contains tag %}
            {% include pub-single.html %}
      {% endif %}
    {% endfor %}
  </div>

  <a href="#page-title" class="back-to-top">Back to Top &uarr;</a>
{% endfor %}