---
title: Fair Machine Learning for Health Care
permalink: /fairness/
header:
    teaser: /assets/images/pareto_adult.png
tags: Fairness
layout: overview
references:
    - note: inter
      pubid: lettTranslatingIntersectionalityFair2023
    - note: fomo
      pubid: lacavaOptimizingFairnessTradeoffs2023
    - note: pmc
      pubid: lacavaFairAdmissionRisk2023
    - note: kleinberg
      text: "Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent Trade-Offs in the Fair Determination of Risk Scores [Innovations in Theoretical Computer Science (ITCS)](https://doi.org/10.48550/arXiv.1609.05807)"
    - note: gerryfair
      text: "Kearns, M., Neel, S., Roth, A., & Wu, Z. S. (2018). Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness. Proceedings of the 35th International Conference on Machine Learning, 2564–2572. [PMLR](https://proceedings.mlr.press/v80/kearns18a.html)"
---

When deployed in healthcare settings, it's important that models are _fair_ - i.e., that they do not cause harm or unjustly benefit specific subgroups of a population. 
Improving the fairness of computational models is a complex and nuanced challenge that requires decision makers to carefully reason about multiple, sometimes conflicting criteria. 
Specific definitions of fairness can vary considerably (e.g. prioritizing equivalent error rates across patient groups vs. similar treatment of similar individuals) and must be contextually appropriate to each application. 
Inherent conflicts may arise when striving to maximize multiple types of fairness simultaneously (e.g. calibration by group vs. equalized odds[^kleinberg]). 
There are often fundamental trade-offs between the overall error rate of a model and its fairness, and it is important to clearly and intuitively characterize and present these trade-offs to stakeholders in the health system. 
For example, one might care more about fairly prioritizing patients in patient triage settings[^pmc] but care more about error rates in predicting individual treatment plans and outcomes. 
Furthermore, it is computationally challenging to audit and improve model fairness when considering a large set of intersecting patient attributes including gender, race, ethnicity, age, socioeconomic status, among others[^gerryfair]; yet, preventing worst-case performance for minoritized groups is often a central ethical prerogative. 
Thus, it is critical for investigators to consider not only fairness by *what measure*, but also fairness *for whom*, and *with what tradeoffs* to other measures of model performance and fairness. 

Providing a *set* of models[^fomo] by jointly optimizing for fairness and accuracy is one way to aid a decision maker in understanding how an algorithm will affect the people it interacts with when it is deployed. 
As we describe in a perspective on intersectionality in machine learning[^inter], achieving fairness also requires an broader ethical analysis to extend beyond the model development process (data collection, preprocessing, training, deployment) to the wider context of an algorithm’s use as a socio-technical artifact, for example by eliciting community participation in defining project goals and establishing criteria for monitoring downstream outcomes of the model’s use throughout its complete lifecycle. 

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
