---
title: Posts
permalink: /posts/
layout: archive
entries_layout: listpic
---

<div class="entries-{{ page.entries_layout }}">
  {% for post in site.posts %}
    {% include archive-single.html type=page.entries_layout %}
  {% endfor %}
</div>