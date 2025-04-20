---
title: 'NNEoS : Neural network-based thermodynamically consistent equation of state
  for fast and accurate flash calculations'
authors:
- Jingang Qu
- Soleiman Yousef
- Thibault Faney
- Jean-Charles de Hemptinne
- Patrick Gallinari
date: '2024-11-01'
publishDate: '2025-04-20T06:43:49.116819Z'
publication_types:
- article-journal
publication: '*Applied Energy*'
doi: 10.1016/j.apenergy.2024.124025
abstract: Equations of state (EOS) correlate thermodynamic properties and are essential
  for flash calculations. However, solving for an EOS can be time-consuming, and EOS
  do not precisely represent physical reality, causing the deviation of flash results
  from phase equilibrium data. In this work, we propose a neural network-based EOS
  (NNEoS) inherently satisfying thermodynamic consistency. NNEoS first predicts the
  residual Gibbs energy and then derives other thermodynamic properties through differentiation.
  NNEoS can be trained using an analytical EOS and then serve as a reliable, computationally
  efficient substitute. NNEoS can also be fine-tuned with experimental data to better
  match flash results to experimental data. We evaluate the performance of NNEoS against
  analytical EOS on three case studies, including binary and multicomponent mixtures
  with and without cross-association. The results show that NNEoS achieves significantly
  faster flash calculations via GPU-based parallel computing and offers superior predictive
  accuracy after fine-tuning compared to analytical EOS.
tags:
- Deep learning
- Equation of states
- Flash calculations
- Neural networks
- Parallel computing
- Two-phase equilibrium
links:
- name: URL
  url: https://www.sciencedirect.com/science/article/pii/S0306261924014089
---
