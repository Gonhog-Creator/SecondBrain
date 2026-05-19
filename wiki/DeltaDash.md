# DeltaDash

Ballistic analytics and prediction platform for DeltaV. Stores historical vest test data and estimates trauma/BFD for untested material compositions.

## Stack
- **Frontend**: React + TypeScript + Vite + Tailwind + shadcn/ui + Recharts
- **Backend**: Python + FastAPI + SQLAlchemy 2.x + Alembic + Pandas + Statsmodels + scikit-learn
- **Database**: PostgreSQL (prod), SQLite (dev)
- **Deploy**: Railway + Docker

## Data model
- 12 shots per vest (6/side), per-shot: caliber, velocity (m/s), BFD/trauma (mm), angle, side, vest number
- Derived per shot: KE = ½mv² (in Joules), momentum p = mv
- Vest = multiple ArmorPanels, each panel = ordered VestLayers (material + thickness)
- Material library: areal density (g/cm²), thickness (mm), manufacturer, spec sheet

## Current backend structure
```
backend/app/
  api/v1/       — REST endpoints (analytics, materials, vests, shots, test_sessions, panels, ammunition...)
  utils/
    equations.py — KE, momentum, unit conversions (grains↔kg, fps↔m/s) — single source of truth
  services/
    excel_parser.py    — parses uploaded test spreadsheets
    test_session_service.py
  db/models/    — ORM: ShotData, TestSession, ArmorPanel, VestLayer, Material, Ammunition, ModelRun...
  schemas/      — Pydantic: prediction.py, analytics.py, shot_data.py, vest_layer.py, armor_panel_layer.py...
```

## Analytics endpoint (implemented)
`GET /analytics/velocity-vs-bfd` — returns all shots with velocity, BFD, bullet_energy (KE), caliber, protection_level, vest/side/shot metadata

## Prediction system (to build)
**Goal**: given a theoretical armor layup (list of materials + thicknesses), predict BFD ± uncertainty

**Approach: ANOVA-style regression**
- Response variable: BFD (mm)
- Predictors:
  - Bullet KE (J) — primary driver
  - Total areal density of layup (g/cm²) — proxy for protection mass
  - Material composition factors (categorical: material type per layer, or continuous: areal density per layer)
  - Possibly: caliber, angle, vest side
- Method: OLS regression or mixed-effects (session as random effect) using `statsmodels`
- One-way ANOVA first to test whether material type significantly affects BFD at fixed KE
- Then multiple regression: BFD ~ KE + areal_density + material_category + interaction terms
- Test: F-test, R², residual plots, prediction interval for new layup

**Dataset**: ~100 test sessions × 12 shots = ~1,200 shot records, dozens of material types — sufficient for ANOVA and multiple regression to be statistically meaningful. Prediction intervals will be reasonably tight for material types with many sessions; wider for underrepresented ones.

## Physics already implemented
- `grains_to_kg`, `grams_to_kg`, `fps_to_m_s`, `m_s_to_fps`
- `calculate_kinetic_energy(mass_kg, v_m_s)` → KE in Joules
- `calculate_momentum(mass_kg, v_m_s)` → p in kg·m/s

## Related
- [[ballistics-armor]]
- [[work-deltav]]
- [[business-deltav]]
- [[Doble-W-Servicios]]
