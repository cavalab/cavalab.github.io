---
title: Posts
permalink: /posts/
layout: archive
---

<div class="entries-{{ entries_layout }}">
  {% for post in site.posts %}
    {% include archive-single.html type='grid' %}
  {% endfor %}
</div>