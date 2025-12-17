# Community Exchange Platform — Model-Driven Engineering (MDE) Pipeline

This repository contains a **complete Model-Driven Engineering (MDE) pipeline**.
It enables a **community exchange platform** to be visually designed, configured through business rules, and **automatically generated as a robust Django backend**.

The goal of this project is to demonstrate how high-level models can serve as the **single source of truth**, from design to executable software.

---

## System Requirements

To execute the full pipeline and run the generated backend, the following dependencies are required.

### 1. Modeling and Code Generation Tools (Pipeline)

```bash
pip install besser pyecore lxml
```

These tools are used to:
- Parse PlantUML models
- Manipulate BUML/Ecore-based metamodels
- Apply Model-to-Model (M2M) transformations

---

### 2. Django Backend Infrastructure (Runtime)

```bash
pip install django django-jazzmin black isort
```

These dependencies are required to run the generated backend application.

---

## Execution Flow

The pipeline is organized into **four logical stages**, ensuring that the final code precisely matches the specified models and configurations.

---

### Step 1: Universal Model Definition (PlantUML)

The file:

```
community_platform_strutural_with_enums.plantuml
```

defines **all domain classes and enumerations**, such as:
- `User`
- `Item`
- `Transaction`
- `Rating`
- `Money`
- Domain-specific enums

This model represents the **complete system**, without any customization or pruning.

**Command:**
```bash
python community_platform_puml_to_buml_generator.py
```

**Output:**
```
buml/buml_model.py
```

This file acts as the **“Super Model”**, from which all customized variants are derived.

---

### Step 2: Customization via DSML (XMI)

Customization is performed through a **Domain-Specific Modeling Language (DSML)** instance:

```
test_custom.xmi
```

This file specifies which features are enabled or disabled, for example:
- `chat="false"`
- `payments="true"`
- `ratings="true"`
- `subcommunities="false"`

**Command:**
```bash
python m2m_strutural_transformer.py
```

**Output:**
```
buml/custom_buml_model.py
```

This step performs a **pruning-only transformation**, producing a **filtered domain model** that reflects the selected business rules.

---

### Step 3: Backend Code Generation

The customized BUML model is then transformed into a **fully functional Django backend**.

**Command:**
```bash
python custom_community_platform_puml_to_buml_generator.py
```

**Output:**
```
CustomCommunityBackend/
```

This directory contains:
- Django models
- Admin configuration
- Project structure
- Ready-to-run backend code

---

## Backend Operation Guide

After the backend code is generated, follow the steps below to run the application.

```bash
# 1. Navigate to the generated project directory
cd CustomCommunityBackend

# 2. Create database migrations
python manage.py makemigrations
python manage.py migrate

# 3. Create an administrator user
python manage.py createsuperuser

# 4. Start the development server
python manage.py runserver
```

Access the administration panel at:

```
http://127.0.0.1:8000/admin/
```

---

## Technologies Used

- **BESSER Framework**  
  BUML modeling engine and model-based code generators.

- **Django 6.0**  
  Web framework used for the generated backend.

- **PyEcore**  
  Manipulation of EMF/Ecore-based metamodels and XMI instances.

- **Jazzmin**  
  Modern AdminLTE-based UI for the Django administration panel.

- **Black & isort**  
  Automatic code formatting and import organization.

---

## Technical Validation

To validate that the pipeline correctly **removed or preserved domain classes** according to the DSML configuration, use the Django shell:

```bash
python manage.py shell -c "from django.apps import apps; [print(m.__name__) for m in apps.get_models()]"
```

### Validation Result

In the latest successful test, this command listed **24 domain models**, including:
- `Rating`
- `Item`
- `Transaction`
- `Money`

This confirms **structural consistency** between:
- The visual domain model
- The customized BUML model
- The actual database schema

---

## Project Purpose

This project was developed as a **proof of concept for Model-Driven Engineering**, demonstrating how:

- High-level visual models
- Domain-specific configurations
- Automated transformations

can be combined to generate **correct-by-construction backend systems**.

