---
title: Automating Digital Health
header:
    teaser: "/assets/images/pennai_overview_r2.png"
tags: 
    - Machine Learning for Health
---

While artificial intelligence (AI) has become widespread, many commercial AI systems are not yet accessible to individual researchers nor the general public due to the deep knowledge of the systems required to use them. 
We believe that AI has matured to the point where it should be an [accessible technology for everyone](#2017OlsonSystemAccessible)[^1]. 
The ultimate goal of this research area is to develop AI systems that [automate the entire computational workflows](#2020LaCavaEvaluatingrecommendersystems) of today's data scientists. 
Doing will accelerate the analysis of complex data in the biomedical and health care domains. 

{% include figure 
image_path="/assets/images/pennai_overview_r2.png" alt="Overview of the PennAI GUI" 
caption="*Accessible, Automatic Data Science*: [github.com/EpistasisLab/Aliro](https://github.com/EpistasisLab/Aliro/)" 
%}


See my [post](http://williamlacava.com/research/pennai-paper) talking about our Bioinformatics paper[^3]. 


<h3 class="archive__subtitle">Related Publications</h3>

<div class="entries-{{ entries_layout }}">
{% assign pubs = site.publications | reverse %}
{% for pub in pubs %}
    {% if pub.tags contains "autoML" %}
        {% include pub-single.html %}
    {% endif %}
{% endfor %}
</div>

<h3 class="archive__subtitle">Footnotes</h3>


[^1]: Pearson, J. (2017). These Researchers Want the People to Seize the Means of AI Production.  Motherboard.  [link](https://motherboard.vice.com/en_us/article/z4jb9j/researchers-want-people-to-seize-the-means-of-ai-production-penn-ai)