# BESSER Web UI Generator

Template-Based Model-to-Text Generator using **BESSER Framework + Jinja2** for transforming DSML GUI models into web applications (HTML+CSS+Vanilla JavaScript).

## Architecture

### BESSER Integration

This generator extends BESSER's `CodeGenerator` class to leverage the framework's infrastructure:

1. **XML to B-UML Converter** (`xml_to_buml.py`)
   - Parses XML/XMI GUI models
   - Converts to BESSER's B-UML structural metamodel
   - Extracts GUI-specific data

2. **GUI Metamodel** (`gui_metamodel.py`)
   - Extends BESSER structural metamodel
   - Defines GUI-specific classes: `GUIApplication`, `GUIScreen`, `GUIComponent`
   - Component types: `ListView`, `DetailView`, `ActionButton`, `ChatComponent`

3. **Web UI Generator** (`web_ui_generator.py`)
   - Extends `besser.generators.CodeGenerator`
   - Uses Jinja2 for template rendering
   - Generates complete web application structure

### Template Structure

```
templates/
├── index.html.j2          # Main HTML template
├── styles.css.j2          # Global styles with theme variables
├── components.css.j2      # Component-specific styles
├── app.js.j2             # Application entry point
├── router.js.j2          # SPA router
├── components.js.j2      # Component renderers
├── api.js.j2             # API service layer
├── page.js.j2            # Page template (one per screen)
└── README.md.j2          # Generated app documentation
```

## Installation

### Prerequisites

```bash
pip install besser-framework jinja2
```

### Project Structure

```
model-2-text/
├── generate.py              # Main generator script
├── web_ui_generator.py      # BESSER CodeGenerator extension
├── xml_to_buml.py          # XML to B-UML converter
├── gui_metamodel.py        # GUI metamodel classes
├── templates/              # Jinja2 templates
└── README.md               # This file
```

## Usage

### Basic Usage

```bash
python generate.py <path_to_xml_model> [output_directory]
```

### Examples

```bash
# Generate from example.gui.xmi to default output directory
python generate.py example.gui.xmi

# Generate to specific output directory
python generate.py example.gui.xmi ./output/ballet-swap

# Use absolute paths
python generate.py C:/models/app.xmi C:/output/webapp
```

### Running the Generated Application

```bash
cd output
python -m http.server 8000
# Open http://localhost:8000
```

## GUI Model Format

The generator accepts XML/XMI files following the GUI metamodel:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<gui:AppGUI appName="My App">
  
  <!-- Theme -->
  <theme
    primaryColor="#F06292"
    secondaryColor="#4A148C"
    logoUrl="https://example.com/logo.png"/>

  <!-- Screens -->
  <screens name="Home" path="/" type="HOME" title="Home">
    <components xmi:type="gui:ListView"
      id="item-list"
      entity="Item"
      showImage="true"
      showPrice="true"/>
    
    <components xmi:type="gui:ActionButton"
      id="new-item"
      label="New Item"
      icon="plus"
      actionType="NAVIGATE"
      targetPath="/items/new"/>
  </screens>
  
  <screens name="Detail" path="/items/:id" type="DETAIL" title="Item">
    <components xmi:type="gui:DetailView"
      id="item-detail"
      entity="Item"/>
  </screens>

</gui:AppGUI>
```

## Component Types

### ListView
Displays collection of items with configurable fields.

**Attributes:**
- `entity`: Entity type (e.g., "Item")
- `showImage`: Display images (true/false)
- `showPrice`: Display prices (true/false)
- `showLocation`: Display locations (true/false)
- `showRating`: Display ratings (true/false)

### DetailView
Shows detailed information about a single entity.

**Attributes:**
- `entity`: Entity type

### ActionButton
Interactive button for navigation or actions.

**Attributes:**
- `label`: Button text
- `icon`: Icon name (plus, chat, edit, etc.)
- `actionType`: NAVIGATE, SUBMIT, etc.
- `targetPath`: Navigation target

### ChatComponent
Real-time messaging interface.

**Attributes:**
- Configured via screen parameters

## Generated Output

### File Structure

```
output/
├── index.html              # Single-page application shell
├── css/
│   ├── styles.css         # Global styles + theme
│   └── components.css     # Component styles
├── js/
│   ├── app.js            # App initialization
│   ├── router.js         # Client-side routing
│   ├── components.js     # Component registry
│   ├── api.js            # API service (with mocks)
│   └── pages/
│       ├── home.js
│       ├── detail.js
│       └── chat.js
└── README.md             # App documentation
```

### Features

- ✅ **BESSER Framework Integration**: Extends `CodeGenerator`
- ✅ **B-UML Metamodel**: Converts XML to BESSER's structural metamodel
- ✅ **Jinja2 Templates**: Template-based code generation
- ✅ **Component-Based**: Reusable UI components
- ✅ **SPA Router**: Hash-based client-side routing
- ✅ **Responsive Design**: Mobile-friendly CSS
- ✅ **Theme Support**: CSS custom properties
- ✅ **Mock API**: Ready for backend integration

## Customization

### Jinja2 Filters

Available in templates:

- `snake_case`: Convert to snake_case
- `kebab_case`: Convert to kebab-case
- `camel_case`: Convert to camelCase
- `pascal_case`: Convert to PascalCase

Example:
```jinja2
{{ screen.name | snake_case }}  {# home_screen #}
{{ screen.name | kebab_case }}  {# home-screen #}
```

### Extending Templates

1. Add new template to `templates/`
2. Update `WebUIGenerator._generate_*()` methods
3. Regenerate application

### Adding Components

1. Define in `gui_metamodel.py`:
```python
@dataclass
class MyComponent(GUIComponent):
    custom_attr: str = ""
```

2. Add to `component_factory()` in `gui_metamodel.py`

3. Create renderer in `templates/components.js.j2`:
```javascript
class MyComponentRenderer extends Component {
    render() {
        return `<div class="my-component">...</div>`;
    }
}
```

4. Add styles to `templates/components.css.j2`

## API Integration

Generated code includes mock API. To connect real backend:

1. Update `API_BASE_URL` in generated `js/api.js`
2. Uncomment real API calls
3. Remove mock implementations

## Testing

To test the generator with the example:

```bash
# From model-2-text directory
python generate.py ../example.gui.xmi ./test-output

# Run the app
cd test-output
python -m http.server 8000
```

## Advantages of BESSER Approach

1. **Framework Integration**: Leverages BESSER's infrastructure
2. **B-UML Metamodel**: Standard structural metamodel
3. **Extensibility**: Easy to extend with new component types
4. **Separation of Concerns**: Clear separation between model, metamodel, and templates
5. **Template Reusability**: Jinja2 templates can be reused across projects
6. **Type Safety**: Python dataclasses provide structure validation

## Comparison with JSON DSML

| Aspect | BESSER Approach | JSON DSML |
|--------|-----------------|-----------|
| Framework | BESSER + Jinja2 | Custom |
| Metamodel | B-UML extension | Custom JSON schema |
| Validation | BESSER + Python types | Custom validators |
| Templates | Jinja2 standard | Custom or Jinja2 |
| Extensibility | Framework support | Manual |

## Troubleshooting

### Import Errors

Ensure BESSER is installed:
```bash
pip install besser-framework
```

### Template Not Found

Check that `templates/` directory is in same location as `web_ui_generator.py`.

### XML Parsing Errors

Validate XML structure matches GUI metamodel schema.

## Future Enhancements

- [ ] Form components (input, select, checkbox)
- [ ] Grid/Table components
- [ ] Image upload components
- [ ] Navigation drawer/sidebar
- [ ] Tab navigation
- [ ] Backend generator (Django/Flask/FastAPI)
- [ ] Database model generator
- [ ] API endpoint generator
- [ ] Test generation
- [ ] Deployment scripts

## License

Generated code is provided as-is for modification and use.

## References

- **BESSER Framework**: https://github.com/BESSER-PEARL/BESSER
- **Jinja2 Documentation**: https://jinja.palletsprojects.com/
- **Model-Driven Engineering**: https://en.wikipedia.org/wiki/Model-driven_engineering

---

**Generated by BESSER Framework - Low-Code Model-Driven Development**
