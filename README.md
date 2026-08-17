# SOVEREIGN Wake Coupling Research v3.0

**First-principles field-theoretic N-body wake interaction framework**

This package implements a clean research architecture for mutual wake coupling among Solar-System bodies. It separates:

- **Derived structure** (Lagrangian, field equation, conservation logic)
- **Phenomenological inputs** (source functional form, composition factors)
- **Calibration** (single global amplitude locked to one target)
- **Out-of-sample prediction** (all other bodies)

It does **not** claim physical validation. Numerical execution demonstrates internal consistency and the calibration/prediction protocol only.

---

## Quick Start

```bash
# From the package root
python -m src.demo_run
```

Or:

```bash
python scripts/run_demo.py
```

Optional tests:

```bash
python -m pytest tests/ -q
```

---

## Package Layout

```
sovereign_wake_coupling_v3/
├── README.md
├── LICENSE
├── requirements.txt
├── pyproject.toml
├── FREEZE_RECORD.json
├── manifest.sha256
├── src/
│   ├── __init__.py
│   ├── constants.py
│   ├── bodies.py
│   ├── field.py
│   ├── coupling.py
│   ├── conservation.py
│   ├── calibration.py
│   └── demo_run.py
├── scripts/
│   └── run_demo.py
├── tests/
│   └── test_structural.py
└── docs/
    ├── ARCHITECTURE.md
    └── EPISTEMIC_STATUS.md
```

---

## Scientific Status (Summary)

| Component                        | Status                |
|----------------------------------|-----------------------|
| Field Lagrangian + EL equation   | Derived               |
| Dispersion relation              | Derived               |
| Stress-energy exchange logic     | Structured            |
| Angular-momentum bookkeeping     | Structured            |
| Source functional $J$            | Phenomenological      |
| Exact Green-function $W_{ij}$    | Formal skeleton       |
| Global amplitude $A$             | Calibrated (Uranus)   |
| Other-body torques               | Out-of-sample predictions |
| Physical validation              | Not claimed           |

See `docs/EPISTEMIC_STATUS.md` for the full ledger.

---

## Design Principles

1. **No silent promotion of calibration into validation.**
2. **Conservation statements are explicit and testable.**
3. **Phenomenological pieces are labeled as such.**
4. **One global amplitude; everything else is prediction.**
5. **Reproducibility via freeze record and hashes.**

---

## Citation / Provenance

This package is a research artifact. It is intended for internal examination, extension, and refutation. It is not a finished physical theory.
