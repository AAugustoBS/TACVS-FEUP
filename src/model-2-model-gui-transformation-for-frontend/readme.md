# Frontend Modeling Flow — From Baseline GUI + DSML to `generated_gui_model.py`

This document describes the **step-by-step frontend pipeline** that produces the final **customized GUI model** (`generated_gui_model.py`) from the canonical templates and DSML configuration.

The output (`generated_gui_model.py`) is intended to be a **deterministic, pruned GUI specification** that reflects the enabled features in the DSML (e.g., payments on/off, chat on/off) while remaining consistent with the structural domain model.

---

## Inputs (What You Need)

Place the following files in the same folder (or update paths accordingly):

- `gui_community_platform.py` — **FULL baseline GUI model** (canonical template)
- `structural_community_platform.py` — **Structural domain model** (classes, attributes, associations)
- `dsml_metamodel.ecore` — DSML metamodel (Ecore)
- `test_custom.xmi` — DSML instance (feature selection) generated via dsml customization (blockly)
- `m2m_dsml_to_gui_pruning_only_with_py_export.py` — M2M transformer + Python exporter

---

## Goal of the Pipeline

The pipeline produces:

- `generated_gui_model.py`

This file contains a **runnable Python GUIModel** that:

1. **Starts from the baseline GUI template** (screens, UI elements, datasources).
2. **Applies DSML pruning-only rules** (removes disabled screens/elements).
3. **Binds datasources to real structural classes and properties** (using `Class.attributes`).
4. **Exports the final GUIModel to Python** so it can be consumed by your downstream generator.

---

## Step 1 — Maintain a Canonical Baseline GUI Template

The baseline GUI model (`gui_community_platform.py`) represents the **maximum-capability frontend** (all screens and features), for example:

- Screens: `ItemListScreen`, `ItemDetailsScreen`, `LoginScreen`, `ChatScreen`, `PaymentScreen`, etc.
- DataSources: `ItemsDataSource`, `RatingsDataSource`, `MessagesDataSource`, `OffersDataSource`, etc.
- Elements: buttons, inputs, lists, and navigation targets.

This baseline is the stable template that guarantees **consistency and completeness** before feature pruning.

---

## Step 2 — Define Feature Selection with DSML (XMI)

Your DSML instance (`test_custom.xmi`) is the feature-selection layer.

Typical examples:

- `messaging.chat = false` → remove Chat screen and Contact button
- `listings.priceMode = false` → remove price fields and payment flow
- `payments.mbway/multibanco/paypal = true/false` → keep only selected payment methods
- `subcommunities.enabled = false` → remove subcommunity selector

The DSML is treated as a **pure configuration source** (no UI augmentation), used only to decide what stays and what is removed.

---

## Step 3 — Run the M2M Transformer (Pruning-Only)

Execute the transformer script:

```bash
python m2m_dsml_to_gui_pruning_only_with_py_export.py
```

What happens internally:

### 3.1 Load DSML
- Loads `dsml_metamodel.ecore` and `test_custom.xmi` (via PyEcore).
- Extracts feature flags (accounts, listings, messaging, payments, ratings, subcommunities, access policies).

### 3.2 Import and Clone the Baseline GUI
- Imports `community_gui_model` from `gui_community_platform.py`.
- Deep clones screens and view elements to create an independent working copy.

### 3.3 Bind GUI DataSources to Structural Model
- Imports `structural_community_platform.py`.
- Ensures each GUI DataSource references a **real structural class** (e.g., `Item`, `Community`, `Rating`, `Offer`).
- Populates DataSource fields by looking up properties inside `Class.attributes`.

This step is the structural integrity layer: it prevents GUI artifacts from referencing classes that do not exist.

### 3.4 Apply DSML Pruning Rules
Typical pruning actions include:

- Remove `ChatScreen` and `ContactBtn` when chat is disabled.
- Remove `PaymentScreen` and `PayBtn` when price/payment is disabled.
- Remove individual payment method buttons if only some methods are enabled.
- Remove `LoginScreen` when login is not required.

The transformer must **only prune and retarget**, keeping the baseline’s structure whenever features remain enabled.

---

## Step 4 — Export the Final GUI as Python (`generated_gui_model.py`)

After pruning + binding, the script exports a fully runnable Python module:

- Defines all required screens
- Defines datasources with correct structural class references
- Defines all screen elements (inputs, datalists, buttons)
- Reconnects navigation targets
- Builds the final `community_gui_model` object

This is the file your custom frontend generator should consume.

---

## Output

After running the transformer, you should obtain:

- `generated_gui_model.py`

A typical verification is to import it in Python:

```bash
python -c "import generated_gui_model; print(type(generated_gui_model.community_gui_model))"
```

---

## Practical Validation Checklist

Before feeding the model into your own generator, validate:

1. **The expected screens exist** (and disabled ones are removed).
2. **Navigation targets are correct** (e.g., Details → Payment only if payment enabled).
3. **DataSources point to real structural classes** (no missing bindings).
4. **DataSource fields correspond to existing structural attributes**.

---

## Notes for Custom Generators

If you are not using BESSER for code generation and instead building your own generator, treat `generated_gui_model.py` as a structured specification:

- Use `Screen.view_elements` to render the layout.
- Use `Button.actionType` + `targetScreen` to build navigation.
- Use `DataList` sources and `InputField.description` as your binding keys.

The model is intentionally version-tolerant and exportable, so your generator can remain stable while you evolve DSML feature logic.

