# M2T (Model-to-Text) Architecture

This generator follows the **template-based M2T transformation** approach, separating static and dynamic code.

## Architecture Overview

```
Model (GUIModel) → Template Engine (Jinja2) → Generated Code (HTML/CSS/JS)
     ↑                      ↑                         ↑
  Dynamic info         Meta-markers              Static structure
```

## Template Components

### 1. Static Parts (Blueprint/Skeleton)
Fixed text fragments shared by all generated artifacts:

**Example from `templates/index.html.j2`:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Static HTML structure -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <div id="app">
        <nav class="navbar">
            <div class="navbar-container">
                <div class="navbar-brand">
```

### 2. Dynamic Parts (Meta-markers)
Placeholders interpreted by the template engine that query the model:

**Example from `templates/index.html.j2`:**
```html
<!-- Dynamic: Application name from model -->
<span class="navbar-title">{{ gui.name }}</span>

<!-- Dynamic: Conditional feature toggle -->
{% if gui.features.show_logout %}
<button id="logout-btn" class="navbar-link">Logout</button>
{% endif %}
```

**Example from `templates/page.js.j2`:**
```javascript
// Static: Class structure
export class {{ screen.name | camel_case }}Page {
    constructor(params = {}) {
        this.params = params;
        // ...
    }
    
    async render() {
        return `
            <div class="page page-{{ screen.name | kebab_case }}">
                <div class="page-header">
                    <!-- Dynamic: Screen name -->
                    <h1 class="page-title">{{ screen.name }}</h1>
                </div>
                
                <div class="page-content">
                    <!-- Dynamic: Conditional payment options -->
                    {% if screen.name == 'PaymentScreen' %}
                    <div class="payment-options">
                        {% if gui.features.show_mbway %}
                        <button class="btn">Pay with MBWay</button>
                        {% endif %}
                        {% if gui.features.show_multibanco %}
                        <button class="btn">Pay with Multibanco</button>
                        {% endif %}
                    </div>
                    {% endif %}
                </div>
            </div>
        `;
    }
}
```

## Template Processing Flow

```
1. Input Model (your_model.py)
   ↓
   gui = GUIModel(
       name="CommunityPlatform",
       features={'show_mbway': True, 'show_multibanco': False}
   )

2. Template Engine (Jinja2)
   ↓
   template = env.get_template('index.html.j2')
   content = template.render(gui=gui)

3. Generated Output (index.html)
   ↓
   <span class="navbar-title">CommunityPlatform</span>
   <button class="btn">Pay with MBWay</button>
   <!-- NO Multibanco button because show_multibanco=False -->
```

## Meta-markers Reference

### Variable Substitution
- `{{ gui.name }}` → Application name
- `{{ screen.name }}` → Screen name
- `{{ gui.package }}` → Package identifier

### Control Structures
- `{% if condition %}...{% endif %}` → Conditional rendering
- `{% for item in collection %}...{% endfor %}` → Iteration
- `{% if gui.features.show_mbway %}` → Feature flags

### Filters (Transformations)
- `{{ screen.name | lower }}` → lowercase
- `{{ screen.name | camel_case }}` → camelCase
- `{{ screen.name | kebab_case }}` → kebab-case
- `{{ screen.name | snake_case }}` → snake_case

## Example: Complete M2T Flow

### Input Model (`generate_from_besser_gui.py`):
```python
gui = GUIModel(
    name="MyShop",
    features={
        'show_mbway': True,
        'show_multibanco': False,
        'show_logout': True
    }
)
module = Module(name="Main", screens=set())
module.screens.add(Screen(name="PaymentScreen"))
gui.modules.add(module)
```

### Template (`templates/page.js.j2`):
```javascript
// STATIC: Class structure
export class {{ screen.name | camel_case }}Page {
    async render() {
        return `
            <!-- STATIC: HTML structure -->
            <div class="page">
                <!-- DYNAMIC: Screen name -->
                <h1>{{ screen.name }}</h1>
                
                <!-- DYNAMIC: Conditional content based on model -->
                {% if screen.name == 'PaymentScreen' %}
                <div class="payment-options">
                    {% if gui.features.show_mbway %}
                    <button>Pay with MBWay</button>
                    {% endif %}
                    {% if gui.features.show_multibanco %}
                    <button>Pay with Multibanco</button>
                    {% endif %}
                </div>
                {% endif %}
            </div>
        `;
    }
}
```

### Generated Output (`paymentscreen.js`):
```javascript
// STATIC parts from template
export class paymentscreenPage {
    async render() {
        return `
            <div class="page">
                <!-- DYNAMIC parts filled from model -->
                <h1>PaymentScreen</h1>
                
                <div class="payment-options">
                    <button>Pay with MBWay</button>
                    <!-- NO Multibanco - show_multibanco was False -->
                </div>
            </div>
        `;
    }
}
```

## Benefits of This Approach

✅ **Separation of Concerns**: Static structure vs dynamic data  
✅ **Reusability**: Same template → many artifacts with different data  
✅ **Maintainability**: Change layout once in template, affects all outputs  
✅ **Flexibility**: Model controls what features appear without template changes  
✅ **Consistency**: All pages share same static structure automatically  

## File Organization

```
src/model-2-text/
├── templates/              # Templates (blueprints with meta-markers)
│   ├── index.html.j2      # Static HTML + {{ gui.* }} markers
│   ├── page.js.j2         # Static JS + {% if %} conditionals
│   ├── styles.css.j2      # Static CSS + theme markers
│   └── ...
├── gui_model.py           # Model definition (GUIModel, Screen, Module)
├── besser_web_ui_generator.py  # Template engine orchestrator
└── generate_app.py        # Entry point: Model → Engine → Output
```

## Adding New Dynamic Elements

To add a new dynamic feature:

1. **Model**: Add to `GUIModel.features`
   ```python
   gui.features['show_cart'] = True
   ```

2. **Template**: Add meta-marker
   ```html
   {% if gui.features.show_cart %}
   <button>Cart</button>
   {% endif %}
   ```

3. **Generate**: Run `python3 generate_app.py`
   - Static parts remain unchanged
   - Dynamic part appears/disappears based on model

No code regeneration needed for the template engine itself!

## Summary

This M2T generator:
- ✅ Uses **Jinja2** as template engine
- ✅ Separates **static** (HTML structure) and **dynamic** (model queries)
- ✅ Uses **meta-markers** (`{{ }}`, `{% %}`) as placeholders
- ✅ Processes templates to produce **case-specific artifacts**
- ✅ Follows the **blueprint pattern** for code generation
