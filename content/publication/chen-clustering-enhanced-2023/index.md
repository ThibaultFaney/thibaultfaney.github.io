---
title: Clustering-Enhanced Deep Learning Method for Computation of Full Detailed Thermochemical
  States via Solver-Based Adaptive Sampling
authors:
- Xi Chen
- Cédric Mehl
- Thibault Faney
- Florent Di Meglio
date: '2023-09-01'
publishDate: '2025-04-20T06:43:49.105043Z'
publication_types:
- article-journal
publication: '*Energy & Fuels*'
doi: 10.1021/acs.energyfuels.3c01955
abstract: Detailed chemistry computations are indispensable in numerous complex simulation
  tasks, which focus on accurately capturing the ignition process or predicting pollutant
  levels. The machine learning method is a modern data-driven approach for predicting
  a full detailed thermochemical state-to-state behavior in reacting flow simulations.
  By combining unsupervised clustering algorithms to subdivide the composition space,
  the complexity of adaptive regression models for temporal dynamics can be significantly
  reduced. In this article, a more compact dataset is generated, which is essential
  for the clustering algorithm, by leveraging the adaptive CVODE solver time steps
  for data augmentation for stiff reactive states. A learning workflow that utilizes
  a deep residual network model (ResNet) in conjunction with an adaptive clustering
  algorithm is proposed. This approach aims to replace the stiff ordinary differential
  equation direct integration solver traditionally used for computing thermochemical
  species’ state-to-state temporal evolution for detailed chemistry simulations. The
  learning models are adaptively trained using the K-means clustering algorithm in
  the non-linear transformation space for different subspaces of dynamic systems.
  Three test cases, H2 (9 species), C2H4 (32 species), and CH4 (53 species), are investigated,
  each exhibiting varying complexities. The study demonstrates that the iterative
  predictions of thermochemical states align well with the results obtained from direct
  numerical integration. Additionally, employing multiple adaptive regression models
  in subdomains yields superior performance compared to a single regression model
  prediction case.
links:
- name: URL
  url: https://doi.org/10.1021/acs.energyfuels.3c01955
---
