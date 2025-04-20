---
title: Machine Learning Model for Gas–Liquid Interface Reconstruction in CFD Numerical
  Simulations
authors:
- Tamon Nakano
- Michele Alessandro Bucci
- Jean-Marc Gratien
- Thibault Faney
date: '2025-01-01'
publishDate: '2025-04-20T06:43:49.124522Z'
publication_types:
- article-journal
publication: '*Fluids*'
doi: 10.3390/fluids10010020
abstract: The volume of fluid (VoF) method is widely used in multiphase flow simulations
  to track and locate the interface between two immiscible fluids. The relative volume
  fraction in each cell is used to recover the interface properties (i.e., normal,
  location, and curvature). Accurate computation of the local interface curvature
  is essential for evaluation of the surface tension force at the interface. However,
  this interface reconstruction step is a major bottleneck of the VoF method due to
  its high computational cost and low accuracy on unstructured grids. Recent attempts
  to apply data-driven approaches to this problem have outperformed conventional methods
  in many test cases. However, these machine learning-based methods are restricted
  to computations on structured grids. In this work, we propose a machine learning-enhanced
  VoF method based on graph neural networks (GNNs) to accelerate interface reconstruction
  on general unstructured meshes. We first develop a methodology for generating a
  synthetic dataset based on paraboloid surfaces discretized on unstructured meshes
  to obtain a dataset akin to the configurations encountered in industrial settings.
  We then train an optimized GNN architecture on this dataset. Our approach is validated
  using analytical solutions and comparisons with conventional methods in the OpenFOAM
  framework on a canonical test. We present promising results for the efficiency of
  GNN-based approaches for interface reconstruction in multiphase flow simulations
  in the industrial context.
tags:
- graph neural network
- interface reconstruction
- unstructured mesh
- VoF method
links:
- name: URL
  url: https://www.mdpi.com/2311-5521/10/1/20
---
