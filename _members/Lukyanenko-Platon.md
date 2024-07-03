---
title: Platon Lukyanenko
header:
  teaser: "../assets/images/lukyanenko_profile.png"
author: platon
given_name: Platon
family_name:  Lukyanenko
author_profile: true
---


{{ site.data.authors[page.author].about }}

{% include pubs_by_author.html given=page.given_name family=page.family_name %}
{% unless pubs_by_author == empty %}
  <h2 class="archive__subtitle">Recent Papers </h2> 
  <div class="entries-list">
    {% for paper in pubs_by_author  limit: 2 %}
      {% include pub-single.html pubid=paper%}
    {% endfor %}
  </div>
{% endunless %}

{% assign posts = site.posts | where: "author", page.author %}
{% unless posts == empty %}
  <h2 class="archive__subtitle">Recent Posts</h2> 
  <div class="entries-list">
    {% for post in posts limit: 2 %}
      {% include archive-single.html type="list" %}
    {% endfor %}
  </div>
{% endunless %}
