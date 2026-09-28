# Quantitative Audit 01 — Earth Thermal Ledger and Deep-Slab Constraint

Status: initial quantitative framing. No chronology conclusion authorized.

## Research question

Does the observed terrestrial thermal state, including global surface heat loss and deep high-velocity slab structures, discriminate between conventional long-duration mantle evolution and a substantially compressed/catastrophic Earth-history model?

## Direct observations retained

### O1 — Global surface heat loss

Davies & Davies (2010) estimate Earth's present surface heat flux at **47 ± 2 TW** from 38,347 measurements with corrections/modeling for sparsely sampled regions and hydrothermal circulation.

This is a present-state boundary constraint, not a historical integral.

### O2 — Radiogenic power is independently constrained

Geoneutrino observations provide an independent empirical constraint on uranium/thorium radiogenic power and therefore on the radiogenic component of Earth's heat budget.

### O3 — Deep slab-like seismic structures

Hutko et al. (2006) report seismic evidence consistent with folded/subducted lithosphere in the D'' region near the core-mantle boundary and describe relatively cold slab material as a candidate explanation for high seismic velocities.

This is a seismic-state observation/inference. It is not by itself a clock.

## Governing energy balance

A minimally adequate whole-Earth thermal ledger has the form:

```text
C_eff(T,t) dT/dt = H_rad(t) + H_core(t) + H_other(t) - Q_surface(T,t)
```

with spatially resolved work requiring:

```text
rho c_p (dT/dt + v·grad T)
  = div(k grad T) + H + Phi
```

where the advection term is essential for moving cold lithosphere through the mantle.

Therefore:

```text
integral(H_rad dt) != retained internal thermal energy
```

unless heat loss, advection, phase effects, secular cooling, differentiation, and boundary fluxes are shown negligible. They are not negligible in standard thermal-history models.

## Disposition of source calculation

The source claims that integrating radiogenic decay over 4.55 Ga produces ~10^30–10^31 J and that this cumulative energy should have melted or homogenized Earth.

**Disposition: REJECT AS DEMONSTRATED.**

Reason: cumulative generated energy is not equivalent to simultaneously stored energy. Conventional thermal-evolution models explicitly couple time-varying radioactive production to convective/surface heat loss and secular cooling. A contradiction requires solving or bounding the complete energy/transport problem and demonstrating that no admissible parameter history satisfies present constraints.

This rejection does not establish that conventional thermal history is correct. It identifies the calculation required to test it.

## Deep-slab discriminator

The slab question remains potentially valuable.

Required comparison:

```text
Model C: long-duration plate/mantle evolution
Model K: compressed/catastrophic tectonic episode
                 |
                 v
forward thermo-mechanical evolution
                 |
                 v
predicted present:
  - slab depth
  - seismic velocity anomaly
  - thermal anomaly
  - morphology/folding
  - phase state
  - surrounding mantle response
                 |
                 v
compare with tomography/seismology
```

### Parameters requiring independent constraints

- slab initial temperature/thickness;
- descent velocity history;
- mantle thermal diffusivity/conductivity;
- temperature-dependent viscosity;
- phase transitions;
- slab-mantle mixing;
- adiabatic heating;
- geometry and folding;
- CMB boundary condition;
- mineral-physics mapping from temperature/composition to seismic velocity.

## Falsification burden

A compressed-history model gains evidential force only if it predicts observed deep-slab morphology/thermal contrast substantially better than conventional models using independently constrained parameters.

A conventional model is challenged only if physically admissible long-duration models cannot preserve the observed anomaly without parameter choices inconsistent with independent geophysical constraints.

## Corpus recommendation

- **Canonical candidate:** the complete-energy-ledger requirement and the distinction between cumulative generation and retained heat.
- **Earth History research:** forward-model deep slab thermal survival under competing histories.
- **DFM relevance:** present thermal/seismic state as a constraint on admissible initialization and history.
- **Rejected argument:** "integrated radiogenic energy alone melts Earth."
- **Research quarantine:** any numerical heat-multiplier claim until its isotope inventory, initial abundance, heat-loss model, and transport assumptions are reproducible.

## Primary/technical sources

- Davies, J.H. & Davies, D.R. (2010), *Earth's surface heat flux*, Solid Earth 1, 5–24. DOI 10.5194/se-1-5-2010.
- Dye, S.T. (2012), *Geoneutrinos and the radioactive power of the Earth*, Reviews of Geophysics 50. DOI 10.1029/2012RG000400.
- Hutko, A.R. et al. (2006), *Seismic detection of folded, subducted lithosphere at the core–mantle boundary*, Nature 441, 333–336.
- Cook, F.A. & Turcotte, D.L. (1981), *Parameterized convection and the thermal evolution of the earth*, Tectonophysics 75, 1–17.

Confidence: HIGH for the energy-ledger correction and existence of deep slab seismic observations. UNCERTAIN for chronology discrimination pending forward-model comparison.
