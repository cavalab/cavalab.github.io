---
title: Automating Digital Health
header:
    teaser: "/assets/images/pennai_overview_r2.png"
tags: 
    - Machine Learning for Health
references:
    - note: olson
      pubid: olsonSystemAccessibleArtificial2017
    - note: pennai
      pubid: lacavaEvaluatingRecommenderSystems2020
    - note: vice
      text: "Pearson, J. (2017). These Researchers Want the People to Seize the Means of AI Production.  Motherboard.  [link](https://motherboard.vice.com/en_us/article/z4jb9j/researchers-want-people-to-seize-the-means-of-ai-production-penn-ai)"
    - note: blogpost
      text: "See my [post](http://williamlacava.com/research/pennai-paper) talking about our [Bioinformatics paper](/papers/#lacavaEvaluatingRecommenderSystems2020)."
---

While artificial intelligence (AI) has become widespread, many commercial AI systems are not yet accessible to individual researchers nor the general public due to the deep knowledge of the systems required to use them. 
We believe that AI has matured to the point where it should be an accessible technology for everyone[^olson][^vice]. 
The ultimate goal of this research area is to develop AI systems that automate the entire computational workflows of today's data scientists[^pennai]. 
Doing will accelerate the analysis of complex data in the biomedical and health care domains[^blogpost]. 

{% include figure 
image_path="/assets/images/pennai_overview_r2.png" alt="Overview of the PennAI GUI" 
caption="*Accessible, Automatic Data Science*: [github.com/EpistasisLab/Aliro](https://github.com/EpistasisLab/Aliro/)" 
%}


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
