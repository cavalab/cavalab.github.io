---
title: Fair Machine Learning for Health Care
permalink: /fairness/
header:
    teaser: /assets/images/pareto_adult.png
tags: Fairness
---


{: .notice--info}
🎉 La Cava and Lett's fair ML tool, [Interfair](https://cavalab.org/interfair/), won first place ($250K) in the 2023 NIH Challenge, "[Bias Detection Tools for Clinical Decision Making](https://ncats.nih.gov/funding/challenges/winners/bias-detection)".  

When deployed in healthcare settings, it's important that models are _fair_ - i.e., that they do not cause harm or unjustly benefit specific subgroups of a population. 
Improving the fairness of computational models is a complex and nuanced challenge that requires decision makers to carefully reason about multiple, sometimes conflicting criteria. 
Specific definitions of fairness can vary considerably (e.g. prioritizing equivalent error rates across patient groups vs. similar treatment of similar individuals) and must be contextually appropriate to each application. 
Inherent conflicts may arise when striving to maximize multiple types of fairness simultaneously (e.g. calibration by group vs. equalized odds[^kleinberg]). 
There are often fundamental trade-offs between the overall error rate of a model and its fairness, and it is important to clearly and intuitively characterize and present these trade-offs to stakeholders in the health system. 
For example, one might care more about [fairly prioritizing patients in patient triage settings](#lacavaFairAdmissionRisk2023), but care more about error rates in predicting individual treatment plans and outcomes. 
Furthermore, it is computationally challenging to audit and improve model fairness when considering a large set of intersecting patient attributes including gender, race, ethnicity, age, socioeconomic status, among others[^gerryfair]; yet, preventing worst-case performance for minoritized groups is often a central ethical prerogative. 
Thus, it is critical for investigators to consider not only fairness by *what measure*, but also fairness *for whom*, and *with what tradeoffs* to other measures of model performance and fairness. 

[Providing a *set* of models](/publications/#lacavaOptimizingFairnessTradeoffs2023) by jointly optimizing for fairness and accuracy is one way to aid a decision maker in understanding how an algorithm will affect the people it interacts with when it is deployed. 
As we describe in a [perspective on intersectionality in machine learning](/publications/#lettTranslatingIntersectionalityFair2023), achieving fairness also requires an broader ethical analysis to extend beyond the model development process (data collection, preprocessing, training, deployment) to the wider context of an algorithm’s use as a socio-technical artifact, for example by eliciting community participation in defining project goals and establishing criteria for monitoring downstream outcomes of the model’s use throughout its complete lifecycle. 

<!-- {% include figure 
image_path="../assets/images/pareto_adult.png" 
alt="A Pareto front of different models and their trade-off between error and fairness on the adult dataset."
caption="An example of different models and their trade-off between error and fairness on the adult dataset."
%} -->



<h3 class="archive__subtitle">Related Publications</h3>

<div class="entries-{{ entries_layout }}">
{% assign pubs = site.data.publications.references | reverse %}
{% for pub in pubs.items %}
    {% if pub.tags contains "fairness" %}
        {% include pub-single.html %}
    {% endif %}
{% endfor %}
</div>


<h3 class="archive__subtitle">Footnotes</h3>

[^kleinberg]: Kleinberg, J., Mullainathan, S., & Raghavan, M. (2016). Inherent Trade-Offs in the Fair Determination of Risk Scores [arXiv:1609.05807](https://doi.org/10.48550/arXiv.1609.05807)

[^gerryfair]: Kearns, M., Neel, S., Roth, A., & Wu, Z. S. (2018). Preventing Fairness Gerrymandering: Auditing and Learning for Subgroup Fairness. Proceedings of the 35th International Conference on Machine Learning, 2564–2572. [PMLR](https://proceedings.mlr.press/v80/kearns18a.html)