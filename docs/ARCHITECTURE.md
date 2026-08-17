# Architecture

## Dependency Graph

```
constants / bodies
        |
        v
   source current J  (phenomenological)
        |
        v
   mutual matrix W_ij  (reduced geometric kernel)
        |
        v
   global amplitude A  (calibrated to one target)
        |
        v
   predicted torques  (out-of-sample for all other bodies)
```

Parallel field layer:

```
Lagrangian  ->  Euler-Lagrange  ->  dispersion relation
                |
                v
         stress-energy exchange logic (structured)
```

## Design Rules

1. One free amplitude only.
2. Calibration body is never counted as an independent validation.
3. Conservation statements are explicit and testable at the algebraic level.
4. Phenomenological inputs are labeled; they are not silently promoted.
5. The reduced geometric kernel is an approximation, not the final Green-function law.

## Intended Next Theoretical Layers

- Derive the source functional J from an explicit matter-field interaction.
- Replace the geometric kernel with the retarded Green function of the field operator.
- Close energy and angular-momentum exchange with the wake medium from the stress-energy tensor.
- Promote the static snapshot to a time-dependent integrator.
