---
title: Fair Machine Learning for Health Care
permalink: /research/fair-ml/
---


When deployed in healthcare settings, it's important that models are _fair_ - i.e., that they do not cause harm or unjustly benefit specific subgroups of a population. 
Otherwise, models deployed to assist in patient triage, for example, could exacerbate existing unfairness in the health system. 
There are [many ways](https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2697394?casa_token=Abys4wXOuMUAAAAA:B76kklZfzpEiEsA6pexAQjTPqoMrz9ASTMgSfkT95_CsyzPSvBRso_SqXQu1WBsmj-RDEdrXyg0) in which predictive health models can recapitulate and/or exacerbate systemic biases in treatment and outcomes.
The field of [fair ML](https://arxiv.org/abs/1810.08810) provides a framework for requiring a notion of fairness to be maintained in models generated from data containing protected attributes (e.g. race and sex). 
What fairness _means_ -- perhaps equivalent error rates across groups, or similar treatment of similar individuals -- varies considerably by application, and [inherent conflicts](https://arxiv.org/abs/1609.05807) can arise when asking for multiple types of fairness. 
Furthermore, there is a fundamental trade-off between the overall error rate of a model and its fairness (c.f. Fig. 1B [here](http://proceedings.mlr.press/v80/kearns18a.html)), and it is an open question how to best characterize and present these trade-offs to stakeholders in the health system.
For example, we might want to prioritize fairness heavily in an algorithm used in patient triage, but weigh error rates more when predicting individual treatment plans and outcomes. 
Due to combinatorial challenges, [fair models are hard to learn and audit](http://proceedings.mlr.press/v80/kearns18a.html) when considering intersections of protected attributes (e.g. black males over 65).
Thus, two open questions are how to best define the metrics for assessing [intersectional definitions of fairness](https://arxiv.org/abs/1807.08362), and [how to approximately satisfy them](https://arxiv.org/abs/2004.13282).

This research project focuses on addressing these challenges by developing flexible search methods that can explicitly optimize multiple criteria - in this case, between model accuracy and fairness. 
We are interested in understanding the intricacies of downstream impacts on healthcare that will arise as more and more models are deployed in the health system.
Providing a *set* of models (e.g. above) varying in fairness and accuracy is one way to aid a decision maker in understanding how an algorithm will affect the people it interacts with when it is deployed. 

[![pareto_front](../assets/pareto_adult.png)](https://arxiv.org/abs/2004.13282)

*An example from [1] of different models and their trade-off between error and fairness on the adult dataset.* 


1.  La Cava, W. & Moore, Jason H. (2020).
Genetic programming approaches to learning fair classifiers.
GECCO 2020. 
**Best Paper Award**.
[ACM](https://dl.acm.org/doi/abs/10.1145/3377930.3390157).
[arXiv](https://arxiv.org/abs/2004.13282)


