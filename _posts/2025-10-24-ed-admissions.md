---
title: "What Drives Disparities in Emergency Admissions?"
date: 2025-10-24
layout: posts
author: helena
excerpt: Understanding unwarranted variations in emergency care
tags: 
    - Machine Learning
header:
    teaser: /assets/images/admission_plot.png
---


{% include pub-single.html pubid="cogganDecipheringInfluenceDemographic2025" %}
{:.notice}

## Background

When a patient arrives at the emergency department (ED), they are seen by a variety of health professionals before any decision is made to admit them to hospital or send them home. 
First, a triage nurse takes their demographics, chief complaint, and initial vitals (heart rate, respiratory rate, weight, temperature, oxygen saturation, blood pressure, etc.), and assigns them a ‘triage acuity’ score between 1 and 5 (the *Emergency Severity Index*, or ESI). 
In the ESI, a 1 indicates a very sick patient who must be seen immediately (because they’re in respiratory arrest, anaphylactic shock, etc), and 5 indicates a well patient who can be safely deprioritised. 
After being seen by the triage nurse, a patient is given an individual waiting room (‘boarded’) as soon as one is available, and is assessed by clinicians until an admission decision can be made. 
Various interventions—medications, laboratory tests, or radiological imaging—may be ordered for the patient during this time.

It is well-established in the US literature that Non-Hispanic Black (NHB) and Hispanic patients receive disparate treatment in the ED (compared to Non-Hispanic White (NHW) patients), even in the pediatric care setting. 
Previous studies, usually working from a single, weighted national database of ED visits across the US (the [National Hospital Ambulatory Medical Care Survey](https://www.cdc.gov/nchs/nhamcs/about/index.html) (NHAMCS)), have found that Black patients are assigned less urgent triage acuity scores, wait longer to be seen, and are less likely to receive opioids when the visit relates to pain. 
Other studies have found that female patients wait longer for care than male patients. 
A recent study by one of our collaborators (Aysola et. al. 2022[^aysola]) suggested that such disparities may at least partly be due to clinician bias, which they could observe in interpersonal interactions—they found that healthcare providers were more likely to interrupt patients or break eye contact when they didn’t share an ethnicity with those patients. 

There is an urgent need to reduce these disparities, to ensure that everyone has fair access to high-quality emergency care. 
To do this, we need to go further than merely quantifying unwarranted variations in admission decisions. 
We might observe that NHB patients are less likely to be admitted than NHW patients overall, but that doesn’t tell us much about why. 
Even if all the observed variation is due to subconscious bias (and thus could be addressed through clinician education), it is unlikely that these biases affect all patients equally. 
Subconscious biases may apply to specific subpopulations (i.e. patients with particular conditions, presentations or backgrounds). 
Decisions to admit patients are also not made in isolation; they also might be downstream of decisions to give particular medications, or order specific tests. 
Efforts to reduce admission disparities should first identify contributing disparities in these ‘upstream’ decisions.

In a recent paper[^coggan], we examined ~340k visits to a single pediatric ED from 2019-2025, measuring sex- and race-based disparities in admission decisions-- both overall and in specific subpopulations-- as well as disparities in ‘upstream’ decisions. 
As machine learning (ML) tools used to predict clinical decisions, trained on past visits, are becoming increasingly common in the ED setting, we also observed whether an ML tool trained to predict admission would reproduce these biases. 
These results will be presented at the [Pacific Symposium on Biocomputing](https://psb.stanford.edu/) this January. 

{% include figure 
image_path="/assets/images/admission_plot.png" 
caption="Adjusted odds ratios describing the likelihood that different demographic groups of patients will be admitted to hospital. Significance is indicated with asterisks, corrected for multiple hypothesis testing (*** =
p < 0.001, ** = p < 0.01, * = p < 0.05). NH=Non-Hispanic. N=number of visits (i.e. N visits from female patients are compared to N visits from male patients). ‘Partial’ adjustment accounts for all patient-specific factors; full adjustment incorporates visit-specific factors."
alt="Adjusted odds ratios describing the likelihood that different demographic groups of patients will be admitted to hospital. Significance is indicated with asterisks, corrected for multiple hypothesis testing (*** =
p < 0.001, ** = p < 0.01, * = p < 0.05). NH=Non-Hispanic. N=number of visits (i.e. N visits from female patients are compared to N visits from male patients). ‘Partial’ adjustment accounts for all patient-specific factors; full adjustment incorporates visit-specific factors."
%}

## Methods: Propensity Score Matching and Machine Learning
When measuring disparities, it is important to compare like with like. In an ‘ideal’ cohort (from a statistical perspective), for every visit from a NHB patient, we would be able to identify an identical visit from a NHW patient—the same age, comorbidity profile, complaint, vitals, and so on—match them up, and measure the differences in admission rates across all paired visits. This would ensure that any differences we observed were due only to race. In a real cohort, NHB visits will differ from NHW visits in a number of different ways, some of which could skew our results.

To address this, we match visits up based on their *propensity score*, which is a measure of how likely a patient is to be, for example, NHB based on their other characteristics. For example, if NHB patients are more likely to be female than NHW patients, then visits from female patients will then have a higher propensity score. When we match one-to-one on propensity score, we will ensure that the male/female distribution is roughly the same in the two cohorts and that NHW female patients are generally matched to NHB female patients. Propensity scores are calculated by fitting a multivariable logistic regression model to the cohort, with Lasso regression used for regularization. 

To measure the effect of disparities on an ML clinical decision support (CDS) tool, we trained an XGBoost model to predict admission. We used ‘snapshots’ from individual visits, taken every thirty minutes from arrival to departure, in order to allow the model to learn from information (tests orders and result, dispensing of medications, etc.) acquired over the course of the stay. We trained the model on visits from Jan 2019 to May 2023, and tested it on visits from May 2023 to May 2024. We then computed the ‘importance’ (SHAP value) of each feature to the model’s prediction, and examined how those importances were affected by demographics.

## Results

We measured differences in outcomes and adjusted for various factors, including age, complaint, vitals, past medical history, socioeconomic status, and how crowded the ED was when the visit began. We found:

1.	There were no overall sex disparities in admissions, but female patients tended have longer stays than male patients, both before admission and before discharge.
2.	NHB and Hispanic patients were significantly less likely to be admitted than NHW patients (see key figure). 
3.	NHB and Hispanic patients waited longer than NHW patients to be admitted, but were discharged more quickly.
4.	Female patients were assigned significantly less urgent triage acuity scores than male patients, and NHB/Hispanic patients were assessed as less urgent than NHW patients.
5.	NHB/Hispanic patients were less likely to be admitted than NHW patients even at the same triage acuity score.
6.	Female patients were more likely than male patients to have lab tests and intravenous [IV] medications ordered for them, but were less likely to be admitted after those interventions, suggesting possible overtreatment in the ED (or displacement of necessary care from inpatient to the ED).
7.	Hispanic patients are less likely to have radiological imaging ordered for them than NHW patients. NHB and Hispanic patients were less likely to receive IV medications. Amongst patients who had received lab tests or medications, NHB and Hispanic patients were less likely to be admitted.
8.	NHW patients using a Portuguese interpreter were less likely to be admitted than NHW English speakers. However, NHB patients were more likely to be admitted when using a Portuguese interpreter than when they spoke English, suggesting that the effects of language barriers are highly dependent on race and the language itself. (Roughly 2% of the arrivals to the ED speak Portuguese as their primary language, about 25 times higher than the national average.)
9.	Disparities were particularly acute in specific subpopulations, including patients with public insurance, abnormal weight, moderate (but not extreme) socio-economic deprivation, normal vitals, or a home address distant from the hospital. 
10. The ML model assigned different importances to certain features based on race. For example, it considered less-urgent triage score more important for NHB and Hispanic patients than for NHW patients.


## Discussion

Our findings suggest that race-based disparities exist in the pediatric emergency care setting, and are particularly acute where patients are less ill, are moderately socio-economically deprived, or have public insurance. 
These disparities may arise in part from ‘upstream’ disparities in the assessment of triage acuity, and the decision to order certain labs, tests and IV medications. 
ML tools developed for clinical decision support may learn and reproduce these biases. 
Efforts to address unwarranted variations in care should focus on the specific decisions and clinical populations which are most affected.

## References

[^aysola]: Aysola, J., Clapp, J. T., Sullivan, P., Brennan, P. J., Higginbotham, E. J., Kearney, M. D., Xu, C., Thomas, R., Griggs, S., Abdirisak, M., Hilton, A., Omole, T., Foster, S., & Mamtani, M. (2022). Understanding Contributors to Racial/Ethnic Disparities in Emergency Department Throughput Times: A Sequential Mixed Methods Analysis. Journal of General Internal Medicine, 37(2), 341–350. [doi](https://doi.org/10.1007/s11606-021-07028-5)

{% include citation.html pubid="cogganDecipheringInfluenceDemographic2025" prefix="[^coggan]:" %}


