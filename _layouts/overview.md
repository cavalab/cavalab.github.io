---
layout: single
---
{{ content }}

{% if page.references %}
## References
{% for ref in page.references %}
    {% assign pref = '[^' | append: ref.note | append: ']: ' %}
    {% if ref.pubid %}
        {% include citation.html pubid=ref.pubid prefix = pref %}
    {% else if ref.text %}
{{ pref }} {{ ref.text }}
    {% endif %}
{% endfor %}
{% endif %}
