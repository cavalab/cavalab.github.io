---
title: Members
layout: archive
permalink: /members/
collection: members
entries_layout: grid
---

{% assign entries_layout = page.entries_layout | default: 'list' %}
<div class="entries-{{ entries_layout }}">
  {% include members-collection.html 
    collection=page.collection 
    sort_by=page.sort_by 
    sort_order=page.sort_order 
    type=entries_layout 
  %}
</div>

<div class="back-to-top"></div>

## Prior Members and Trainees

- [Guangya Wan](https://datascience.virginia.edu/people/guangya-wan), MS HSPH &#8594; UVA Data Science PhD program
- Zongjun Liu, MS HSPH &#8594; Kaiser Permanente
- Sid Barthulwar, BS candidate, Harvard University 
- Tilak Raj Singh, M.S. SEAS, UPenn &#8594; Microsoft
- James Taggart, B.S. CIS, UPenn &#8594; Google
- Srinivas Suri, M.S. SEAS, UPenn &#8594; Microsoft
- Max Roling, B.S. Wharton, UPenn &#8594; Morgan Stanley
- Saurav Bose, M.S. SEAS, UPenn &#8594; Foursquare 
- Nupur Baghel, M.S. SEAS, UPenn &#8594; Meta
- Rishabh Gupta, M.S. EMBS, UPenn &#8594; Meta