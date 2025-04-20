---
title: Hybrid Newton method for the acceleration of well event handling in the simulation
  of CO2 storage using supervised learning
authors:
- Antoine Lechevallier
- Sylvain Desroziers
- Thibault Faney
- Eric Flauraud
- Frédéric Nataf
date: '2025-03-01'
publishDate: '2025-04-20T06:43:49.077656Z'
publication_types:
- article-journal
publication: '*Computers & Geosciences*'
doi: 10.1016/j.cageo.2025.105872
abstract: 'Geological storage of CO2 is an essential instrument for efficient Carbon
  Capture and Storage policies. Numerical simulations provide the solution to the
  multi-phase flow equations that model the behavior of the CO2 injection site. However,
  numerical simulations of fluid flow in porous media are computationally demanding:
  it can take up to several hours on a HPC cluster in order to simulate one injection
  scenario for a large CO2 reservoir if we want to accurately model the complex physical
  processes involved. This becomes a limiting issue when performing a large number
  of simulations, e.g. in the process of ‘history matching’. Well events, such as
  opening and closure, cause important numerical difficulties due to their instant
  impact on the pressure and saturation unknowns. This often forces a drastic reduction
  of the time step size to be able to solve the non-linear system of equations resulting
  from the discretization of the continuous mathematical model. However, these specific
  well events in a simulation have a relatively similar impact across space and time.
  We propose a proof of concept methodology to alleviate the impact of well events
  during the numerical simulation of CO2 storage in the underground by using a machine-learning
  based non-linear preconditioning. We complement the standard fully implicit solver
  by predicting an initialization of Newton’s method directly in the domain of quadratic
  convergence using supervised learning. More specifically, we replace the initialization
  in pressure by a linear approximation obtained through an implicit solver and we
  use a Fourier Neural Operator (FNO) to predict the saturation initialization. Furthermore,
  we present an open-source Python framework for conducting reservoir simulations
  and integrating machine-learning models. We apply our methodology to two test cases
  derived from a realistic CO2 storage in saline aquifer benchmark. We reduce the
  required number of Newton iterations to handle a well opening by 53% for the first
  test case, i.e required number of linear system to solve and by 38% for the second
  test case.'
tags:
- CO storage
- Fourier Neural Operator
- Machine learning
- Newton method
- Non-linear preconditioning
- Reservoir simulation
links:
- name: URL
  url: https://www.sciencedirect.com/science/article/pii/S0098300425000226
---
