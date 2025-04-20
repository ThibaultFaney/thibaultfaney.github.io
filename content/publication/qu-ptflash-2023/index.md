---
title: 'PTFlash : A vectorized and parallel deep learning framework for two-phase
  flash calculation'
authors:
- Jingang Qu
- Thibault Faney
- Jean-Charles de Hemptinne
- Soleiman Yousef
- Patrick Gallinari
date: '2023-01-01'
publishDate: '2025-04-20T06:43:49.051746Z'
publication_types:
- article-journal
publication: '*Fuel*'
doi: 10.1016/j.fuel.2022.125603
abstract: Phase equilibrium calculations are an essential part of numerical simulations
  of multi-component multi-phase flow in porous media, accounting for the largest
  share of the computational time. In this work, we introduce a fast and parallel
  framework, PTFlash, that vectorizes algorithms required for two-phase flash calculation
  using PyTorch, and can facilitate a wide range of downstream applications. Vectorization
  promotes parallelism and consequently leads to attractive hardware-agnostic acceleration.
  In addition, to further accelerate PTFlash, we design two task-specific neural networks,
  one for predicting the stability of given mixtures and the other for providing estimates
  of the distribution coefficients, which are trained offline and help shorten computation
  time by sidestepping stability analysis and reducing the number of iterations to
  reach convergence. The evaluation of PTFlash was conducted on three case studies
  involving hydrocarbons, CO2 and N2, for which the phase equilibrium was tested over
  a large range of temperature, pressure and composition conditions, using the Soave–Redlich–Kwong
  (SRK) equation of state. We compare PTFlash with an in-house thermodynamic library,
  Carnot, written in C++ and performing flash calculations one by one on CPU. Results
  show speed-ups of up to two order of magnitude on large scale calculations, while
  maintaining perfect precision with the reference solution provided by Carnot.
tags:
- Deep learning
- Flash calculation
- Two-phase equilibrium
- Vectorization
links:
- name: URL
  url: https://www.sciencedirect.com/science/article/pii/S0016236122024334
---
