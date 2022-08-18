---
title: Intelligible Predictive Health Models
permalink: /research/interpretable-ml/
---

We study both black-box and glass-box ML methods to improve the intelligibility and/or explainability of models that are trained for clinical prediction tasks using electronic health record (EHR) data.
EHR data offer a promising opportunity for advancing the understanding of how clinical decisions and patient conditions interact over time to influence patient health. 
However, EHR data are difficult to use for predictive modeling due to the various data types they contain (continuous, categorical, text, etc.), their longitudinal nature, the high amount of non-random missingness for certain measurements, and other concerns. 
Furthermore, patient outcomes often have heterogeneous causes and require information to be synthesized from several clinical lab measures and patient visits. 
Researchers often resort to using complex, black-box predictive models to overcome these challenges, thereby introducing additional concerns of accountability, transparency and intelligibility.

### Can't we just explain black-box models?

Although black-box models are typically accurate, they are often bad at explaining _how_ they arrive at those predictions, and may also disagree with very similar models about which factors are driving their predictive ability [1].

![EHR](../assets/RF_feature_permutation_clustermap_cutoff_1.jpg){: .center-image}

*Feature importance bi-clustering across diseases and predictors [3].* 

### Symbolic Regression for Interpretable Machine Learning 

An alternative, and promising approach, is to use glass-box ML methods such as _symbolic regression_ that can capture complex relationships in data and yet produce and intelligible final model. 
Symbolic regression methods jointly optimize structure of a model, as well as its parameters, usually with the goal of finding a simple and accurate symbolic model.

However, intelligibility is complicated to define, and is both context- and user-dependent.
In general, the intelligibility of a model depends heavily on its *representation*, i.e, how it defines its feature space.

![Rep learning](../assets/rep_learning_demo_2d.svg){: .center-image}

*An example representation from the [Feat docs.](https://lacava.github.io/feat/guide/overview/)*

What makes a representation good? 
At the minimum, a good representation produces a model with better generalization than a model trained only on the raw data attributes. 
In addition, a good representation teases apart the factors of variation in the data into independent components. 
Finally, an ideal representation is succinct so as to promote intelligibility. 
This means a representation should only have as many features as there are independent factors in the process, and each of those features should be digestible by the user. 
Many of our research projects center around these three motivations when designing novel algorithms for interpretable machine learning.

### Can a simple symbolic model be accurate?

Researchers often see the _complexity_ of a model as a trade-off with its _error_: more complex models should give better predictions than simple ones. 
However, very rarely is the nature of the trade-off actually characterized in a robust way. 

In fact, [what we have found](https://arxiv.org/abs/2107.14351) is that for many tasks, symbolic regression approaches can perform as well as or better than state-of-the-art black-box approaches - and still produce simpler expressions. 

![SRBench result](../assets/pairgrid-pointplot_r2_test_model_size_training-time-s.png){: .center-image}

*Symbolic regression algorithms (marked with asterisk) benchmarked against black-box ML on hundreds of regression problems. See more at <https://github.com/EpistasisLab/srbench>.*

### Do they work in clinical care? 

Our preliminary work on symbolic regression approaches to patient phenotyping have shown success in producing accurate and interpretable models of [treatment resistant hypertension](https://www.medrxiv.org/content/10.1101/2020.12.12.20248005v2). 
More work is needed to scale and study these algorithms in routine clinical care. 

![A simple model of treatment resistant hypertension](/assets/aTRH_model.svg){: .center-image}

*A symbolic regression model of treatment resistant hypertension [2].*
{: .center}

Relevant work: 

1. La Cava, W., Bauer, C. R., Moore, J. H., & Pendergrass, S. A. (2019). 
   Interpretation of machine learning predictions for patient outcomes in electronic health records. 
   AMIA 2019 Annual Symposium. 
   [arXiv](https://arxiv.org/abs/1903.12074)

2.  La Cava, W., Lee, P.C., Ajmal, I., Ding, X., Cohen, J.B., Solanki, P., Moore, J.H., and Herman, D.S (2021). 
    Application of concise machine learning to construct accurate and interpretable EHR computable phenotypes.
    [medRxiv](https://www.medrxiv.org/content/10.1101/2020.12.12.20248005v2),

3.  La Cava, W. & Moore, J.H. (2020). 
    Learning feature spaces for regression with genetic programming.
    *Genetic Programming and Evolvable Machines (GPEM)*. 
    [link](https://link.springer.com/article/10.1007/s10710-020-09383-4),
    [pdf](../pubs/feat_gpem.pdf)

4.  La Cava, W., & Moore, J. H. (2019). 
    Semantic variation operators for multidimensional genetic programming. 
    GECCO 2019. 
    https://doi.org/10.1145/3321707.3321776.
    [arXiv](http://arxiv.org/abs/1904.08577)

5.  La Cava, W., & Moore, J. H. (2019). 
    Learning concise representations for regression by evolving networks of trees. 
    ICLR 2019. 
    [arXiv](https://arxiv.org/abs/1807.00981)

6.  La Cava, W., & Moore, J. (2017). 
    A General Feature Engineering Wrapper for Machine Learning Using epsilon-Lexicase Survival. 
    European Conference on Genetic Programming.  
    [link](https://doi.org/10.1007/978-3-319-55696-3_6), [preprint](../../pubs/evostar_few_lacava.pdf)

 
7.  La Cava, W., & Moore, J. H. (2017). Ensemble representation learning: an analysis of fitness and
    survival for wrapper-based genetic programming methods. GECCO ’17 (pp. 961–968). Berlin, Germany: ACM.
    [link](https://doi.org/10.1145/3071178.3071215), [arXiv](https://arxiv.org/abs/1703.06934)


8.  La Cava, W., Silva, S., Vanneschi, L., Spector, L., & Moore, J. (2017). Genetic Programming 
    Representations for Multi-dimensional Feature Learning in Biomedical Classification. 
    Applications of Evolutionary Computation (pp. 158–173). Springer, Cham. 
    [link](https://doi.org/10.1007/978-3-319-55849-3_11 ), [preprint](../../pubs/evobio_m4gp_lacava.pdf)

9.  La Cava, W., Silva, S., Danai, K., Spector, L., Vanneschi, L., & Moore, J. H. (2018). 
    Multidimensional genetic programming for multiclass classification. 
    *Swarm and Evolutionary Computation*. 
    [link](https://doi.org/10.1016/j.swevo.2018.03.015),
    [preprint](../pubs/Multiclass_GP_journal_preprint.pdf)

10.  La Cava, W., Orzechowski, P., Burlacu, B., França, F. O. de, Virgolin, M., Jin, Y., Kommenda, M., & Moore, J. H. (2021). 
    Contemporary Symbolic Regression Methods and their Relative Performance. 
    *Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks* (Accepted).
    [arXiv](https://arxiv.org/abs/2107.14351),
    [repo](https://github.com/EpistasisLab/srbench)


