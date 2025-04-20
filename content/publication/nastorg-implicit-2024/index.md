---
title: An implicit GNN solver for Poisson-like problems
authors:
- Matthieu Nastorg
- Michele-Alessandro Bucci
- Thibault Faney
- Jean-Marc Gratien
- Guillaume Charpiat
- Marc Schoenauer
date: '2024-12-01'
publishDate: '2025-04-20T06:43:49.070246Z'
publication_types:
- article-journal
publication: '*Computers & Mathematics with Applications*'
doi: 10.1016/j.camwa.2024.10.036
abstract: 'This paper presents Ψ-GNN, a novel Graph Neural Network (GNN) approach
  for solving the ubiquitous Poisson PDE problems on general unstructured meshes with
  mixed boundary conditions. By leveraging the Implicit Layer Theory, Ψ-GNN models
  an “infinitely” deep network, thus avoiding the empirical tuning of the number of
  required Message Passing layers to attain the solution. Its original architecture
  explicitly takes into account the boundary conditions, a critical pre-requisite
  for physical applications, and is able to adapt to any initially provided solution.
  Ψ-GNN is trained using a physics-informed loss, and the training process is stable
  by design. Furthermore, the consistency of the approach is theoretically proven,
  and its flexibility and generalization efficiency are experimentally demonstrated:
  the same learned model can accurately handle unstructured meshes of various sizes,
  as well as different boundary conditions. To the best of our knowledge, Ψ-GNN is
  the first physics-informed GNN-based method that can handle various unstructured
  domains, boundary conditions and initial solutions while also providing convergence
  guarantees.'
links:
- name: URL
  url: https://www.sciencedirect.com/science/article/pii/S0898122124004851
---
