---
title: "Simplifying symbolic regression models without simplification rules"
date: 2024-04-14
layout: posts
author: guilherme
excerpt: Relaxing the definition of equivalent mathematical expressions to get more simpler and interpretable models
tags: 
    - Symbolic Regression
    - Simplification
    - Interpretability
header:
    teaser: /assets/images/inexact-simplification-equivalent-models.svg
toc: true
---

{% assign pub = site.publications 
    | where_exp:"pub", "pub.title == 'Inexact Simplification of Symbolic Regression Expressions with Locality-sensitive Hashing'" 
    | first %}
{% include pub-single.html %}
{:.notice}

Symbolic regression (SR) is a non-parametric technique for finding models that present a good balance between predictive power and model simplicity, and it is usually done with evolutionary algorithms[^srbench].
Symbolic regression creates models by using trees to compose a mathematical expression, like so:

{% include figure 
image_path="/assets/images/inexact-simplification-sr-model.svg" 
caption="A symbolic expression tree. The equivalent mathematical expression is shown besides each node. From bottom-up, we can see how an expression is created using this representation." 
alt="A symbolic regression model"
%}

SR is suitable when the user wants the final model to be interpretable, but these models don't always come in their simplest form; there are problems such as overparameterization of models[^overparameterization], introns (non-coding parts)[^introns], and semantic redundancies[^bloat] in the model. Although it is simple for humans to catch many simple cases of these problems at a glance, it is challenging for the computer to simplify these models automatically.

{% include figure 
image_path="/assets/images/inexact-simplification-isomorphic.svg" 
caption="Despite being very different in depth or number of nodes, all of these models evaluate to the same (or almost the same) prediction vector. Our inexact simplification method learned all these equivalences during the execution of the algorithm, and without being explicitly programmed to catch any specific simplification pattern." 
alt="Several models that have the same behavior on training data, but very different trees."
%}

Our recent work[^inexactsimp] explores a simplification approach based on memoization. 
By mapping similar expressions to the same hash, we create a table that stores similar expressions in increasing order of size, allowing us to quickly identify simpler and approximately equivalent substitute symbols.

In this post, I will discuss the main idea and then analyze its effects in a case study, focusing on the benefits of memorization as a strategy to learn to simplify.

# Background 

Many SR algorithms have a simplification step, but a non-linear problem has infinite solutions, and simplifying these models is difficult. Simplifying a model can be as complicated as finding it in the first instance.

Some previous works have formalized different strategies to simplify models. Still, these strategies are not perfect, either because they are simple enough to run fast or because they are so complex that they increase the algorithm's execution time (or they are so complicated that it is better not to implement them!).

# Approach

Instead of defining simplification rules, we can learn them during the algorithm's execution. This is done by iterating over parts of the models and learning which ones are similar enough to be considered equivalent during runtime.

If we create a map associating these model parts with different keys, we can map similar parts to the same key. If each key saves an ordered list of similar expressions, we can always replace the occurrence of any part with the smallest of the same key. This is where the idea of using LSH comes in, an approximate way of mapping similar objects to the same key.

Note that this depends on having good diversity in the first generations and that the number of individuals and generations is large enough to populate the table with the occurrences. It's the price you pay for not implementing a single rule!

## Locality-Sensitive Hashing (LSH)

Locality-sensitive hashing (LSH) techniques were first introduced by Gionis et al.[^lsh], and aim to map similar structures to the same hash without worrying too much about the accuracy of the similarity calculation: it is a trade-off between having a faster execution by relaxing the definition of equality of two large structures. This is particularly interesting when we want to work with a very large amount of data, such as when saving several parts of mathematical expressions.

{% include figure 
image_path="/assets/images/inexact-simplification-lsh.svg" 
caption="Given a set of vectors (such as the prediction vector), similar structures are mapped to the same hash. The two highlighted vectors present close values in this example and are mapped into the same hash." 
alt="Locality sensitive hashing maps similar structures to the same hash key"
%}

## Inexact simplification

Simply put, the inexact simplification algorithm works by mapping similar expressions to the same hash, and retrieving the simplest one when doing the simplification of an expression[^inexactsimp]. 

The structure being mapped in our case is the prediction vector of a sub-tree. As we traverse the expression, we calculate its prediction vector for each sub-tree and use it in LSH to obtain a hash. The obtained hash is used in a key-value dictionary, where the value is a list ordered by size --- so that there is at least one equivalent expression for each key added to it. When the list is not empty, the first element is used to replace the originating tree. If the list is empty, the tree is inserted as the simplest for that specific hash.

{% include figure 
image_path="/assets/images/inexact-simplification-lsh-simplification.svg" 
caption="In the first stage (1), we have a simplification table with only the problem variables plus the constant. Every node is seen as the root of a subtree and can generate a prediction vector. The second stage (2) uses the predictions to get hash values for each node, updating the simplification table. Finally, we get the simplified tree (3) by replacing the nodes with the smallest subtree of the same hash in the simplification table." 
alt="Step-by-step description of our proposed approach to inexact simplification"
%}

Although it is not necessary to store all occurrences of the same hash in a list, this brings some benefits, such as the possibility of identifying isomorphic trees that were created during execution, doing an analysis of the diversity and redundancy that exists in the data, find insights into data-based simplifications (e.g., a simplification that only makes sense when evaluating the data).

The inexact part comes from the fact that LSH has an stochastic way of mapping similar inputs to the same key, and we also tried to force some collisions (every near-constant prediction vector is mapped to the same hash by multiplying all values by zero if the variance of predictions is smaller than a very low value).

We allow the LSH to store an expression in the hashmap if the difference between the vectors is less than 0.01 (this is what we call tolerance threshold, and it was intended to give the models a small tolerance to numeric rounding, truncating, and calculation differences).

## Another example

As a proof of concept, we ran the algorithm for a database with and without simplification and observed the following results.

{% include figure 
image_path="/assets/images/inexact-simplification-simp-nosimp.svg" 
caption="Smallest expression found by our bottom-up inexact simplification (left) and without simplification (right) for the Yacht dataset. The MSE for each expression was 1.98 using the simplification and 2.08 without simplification." 
alt="Comparison of the final model found with and without our simplification method"
%}

The simplification led the SR algorithm to find a smaller expression with a better goodness-of-fit on the test data than without simplifying. With only 9 nodes, the simplified tree does not contain any redundancy (such as taking the square root of the square, as the other tree does). It also has one less parameter to adjust, and both models share the same features, which means they rely on the same information to make predictions. Cool!

# Takeaways

It is possible to eliminate the task of defining ways to simplify expressions at the cost of relaxing a little on how rigorous we are when making simplifications. This technique is easy to implement and can be pretty convenient for implementations where _i)_ defining simplifications is a tedious and laborious task or _ii)_ it is not known for sure what possible simplifications we can make.

# References

{% include citation.html pubid="2024AldeiaInexactSimplification" prefix = "[^inexactsimp]:" %}


[^srbench]: William La Cava, Patryk Orzechowski, Bogdan Burlacu, Fabricio de França, Marco Virgolin, Ying Jin, Michael Kommenda, and Jason Moore. 2021. Contemporary Symbolic Regression Methods and their Relative Performance. In Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks, J. Vanschoren and S. Yeung (Eds.), Vol. 1. Curran.

[^lsh]:  Aristides Gionis, Piotr Indyk, and Rajeev Motwani. [n. d.]. Similarity Search in High Dimensions via Hashing. ([n. d.]).

[^introns]: Michael Affenzeller, Stephan M Winkler, Gabriel Kronberger, Michael Kommenda, Bogdan Burlacu, and Stefan Wagner. 2014. Gaining deeper insights in symbolic regression. Genetic Programming Theory and Practice XI (2014), 175–190.

[^overparameterization]: Fabricio Olivetti de Franca and Gabriel Kronberger. 2023. Reducing Overparameterization of Symbolic Regression Models with Equality Saturation. In Proceedings of the Genetic and Evolutionary Computation Conference (Lisbon, Portugal) (GECCO ’23). Association for Computing Machinery, New York, NY, USA, 1064–1072. https://doi.org/10.1145/3583131.3590346

[^bloat]: Sean Luke and Liviu Panait. 2006. A Comparison of Bloat Control Methods for Genetic Programming. Evolutionary Computation 14, 3 (Sept. 2006), 309–344. https://doi.org/10.1162/evco.2006.14.3.309
