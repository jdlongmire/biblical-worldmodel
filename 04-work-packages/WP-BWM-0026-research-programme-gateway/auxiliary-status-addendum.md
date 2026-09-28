# Gateway Addendum — Auxiliary Hypothesis Status Preservation

**Status:** approved integration-control candidate, 2026-09-28  
**Parent:** WP-BWM-0026 Research Programme Gateway Contract  
**Method authority:** WP-BWM-0009 Auxiliary Hypothesis Non-Credit Principle

## Rule

BWM shall not strengthen an imported programme's proposed mechanism merely because the mechanism is documented, modeled, simulated, or cited in a technical literature.

In addition to the gateway contract's existing claim-strength rule, imported mechanism claims shall preserve:

- hierarchy level, especially L2 auxiliary status;
- evidential state E0-E4 where assessed;
- fitted versus independently constrained parameters;
- unresolved historical-instantiation burden;
- tests/discriminators;
- failure conditions;
- Lakatosian status A-P/A-N/A-D where assessed.

## Interface extension

Where an export materially depends on an auxiliary hypothesis, include:

```yaml
auxiliary:
  id:
  hierarchy_level: L2
  evidential_state:
  parameters:
    independently_constrained: []
    fitted_or_assumed: []
  historical_trace:
  discriminators: []
  lakatos_status:
  explanatory_debt: []
```

Absence of these fields does not authorize BWM to infer that the auxiliary is established.

## Integration prohibition

BWM public or canonical synthesis shall not transform:

```text
candidate mechanism -> explanation
simulation fit -> historical occurrence
physical possibility -> historical sufficiency
literature response -> resolved anomaly
```

without source warrant and the evidential progression required by WP-BWM-0009.
