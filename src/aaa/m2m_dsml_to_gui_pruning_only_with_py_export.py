"""
m2m_dsml_to_gui_pruning_only_with_py_export_fixed.py

DSML -> GUI (M2M) using a FULL baseline GUI model (canonical template),
applying DSML ONLY as PRUNING / RETARGETING (no augment),
binding DataSources to REAL Structural classes/properties (Property lookup inside Class.attributes),
and exporting ALWAYS to a VALID Python model file: generated_gui_model.py

Inputs (expected in same folder):
  - gui_community_platform.py
  - structural_community_platform.py
  - dsml_metamodel.ecore
  - test_custom.xmi

Run:
  python m2m_dsml_to_gui_pruning_only_with_py_export_fixed.py
"""

from __future__ import annotations

from typing import Optional, Dict, Set, Tuple, Any, List
import inspect
import importlib
import importlib.util
from pathlib import Path
import os

# Optional DSML XMI loader (pyecore)
try:
    from pyecore.resources import ResourceSet
except Exception:
    ResourceSet = None

# BESSER GUI metamodel
from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen, Button, InputField, DataList,
    DataSourceElement, ViewComponent,
    ButtonType, ButtonActionType, InputFieldType
)

# BESSER Structural metamodel types
# (We only need Property class for typing/identity; properties will be obtained from Class.attributes.)
from besser.BUML.metamodel.structural import Property as StructuralProperty


# ------------------------------------------------------------
# DSML loader
# ------------------------------------------------------------
def load_dsml_appconfig(xmi_path: str, ecore_path: str):
    if ResourceSet is None:
        raise RuntimeError("pyecore is required to load DSML XMI. Install pyecore.")
    rset = ResourceSet()
    ecore_resource = rset.get_resource(ecore_path)
    mm_root = ecore_resource.contents[0]
    rset.metamodel_registry[mm_root.nsURI] = mm_root
    xmi_res = rset.get_resource(xmi_path)
    return xmi_res.contents[0]


# ------------------------------------------------------------
# Baseline import
# ------------------------------------------------------------
def _import_baseline_gui_model(baseline_py_path: str) -> GUIModel:
    p = Path(baseline_py_path).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Baseline GUI file not found: {p}")

    spec = importlib.util.spec_from_file_location("baseline_gui_module", str(p))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load baseline module from: {p}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore

    if not hasattr(mod, "community_gui_model"):
        raise AttributeError("Baseline module must define `community_gui_model: GUIModel`.")
    return getattr(mod, "community_gui_model")


# ------------------------------------------------------------
# Version-tolerant constructors (important for BESSER variants)
# ------------------------------------------------------------
def _accepted_kwargs(cls, provided: dict) -> dict:
    sig = inspect.signature(cls.__init__)
    params = set(sig.parameters.keys())
    params.discard("self")
    return {k: v for k, v in provided.items() if k in params}


def mk_input(*, name: str, description: str, field_type=InputFieldType.Text, validation_rules: str = "") -> InputField:
    base = {"name": name, "description": description}
    p = inspect.signature(InputField.__init__).parameters

    # validation
    if "validationRules" in p:
        base["validationRules"] = validation_rules
    elif "validation" in p:
        base["validation"] = validation_rules
    elif "validation_rules" in p:
        base["validation_rules"] = validation_rules

    # field type key
    if "field_type" in p:
        base["field_type"] = field_type
    elif "type" in p:
        base["type"] = field_type
    elif "inputFieldType" in p:
        base["inputFieldType"] = field_type
    elif "fieldType" in p:
        base["fieldType"] = field_type

    return InputField(**_accepted_kwargs(InputField, base))


def mk_screen(*, name: str, description: str, is_main: bool = False) -> Screen:
    base = {
        "name": name,
        "description": description,
        "x_dpi": "x_dpi",
        "y_dpi": "y_dpi",
        "screen_size": "Medium",
        "view_elements": set(),
        "is_main_page": is_main,
    }
    return Screen(**_accepted_kwargs(Screen, base))


def mk_datasource(*, name: str, dataSourceClass, fields: Set) -> DataSourceElement:
    # In some BESSER variants, parameter name could differ; accepted_kwargs protects us.
    base = {"name": name, "dataSourceClass": dataSourceClass, "fields": set(fields)}
    return DataSourceElement(**_accepted_kwargs(DataSourceElement, base))


def mk_datalist(*, name: str, description: str, sources: Set[DataSourceElement]) -> DataList:
    p = inspect.signature(DataList.__init__).parameters
    base = {"name": name, "description": description}
    if "list_sources" in p:
        base["list_sources"] = set(sources)
    elif "listSources" in p:
        base["listSources"] = set(sources)
    elif "sources" in p:
        base["sources"] = set(sources)
    return DataList(**_accepted_kwargs(DataList, base))


def mk_button(*, name: str, description: str, label: str,
              button_type=ButtonType.TextButton,
              action_type=ButtonActionType.Navigate,
              target: Optional[Screen] = None) -> Button:
    """
    Some BESSER variants validate Navigate requires targetScreen at construction.
    We protect by using OpenForm during ctor if target is None.
    """
    p = inspect.signature(Button.__init__).parameters
    base = {"name": name, "description": description, "label": label}

    if "buttonType" in p:
        base["buttonType"] = button_type
    elif "button_type" in p:
        base["button_type"] = button_type

    ctor_action = action_type
    if action_type == ButtonActionType.Navigate and target is None:
        ctor_action = ButtonActionType.OpenForm

    if "actionType" in p:
        base["actionType"] = ctor_action
    elif "action_type" in p:
        base["action_type"] = ctor_action

    if target is not None and "targetScreen" in p:
        base["targetScreen"] = target

    b = Button(**_accepted_kwargs(Button, base))

    # best-effort assign final values
    if hasattr(b, "buttonType"):
        try: b.buttonType = button_type
        except Exception: pass
    if hasattr(b, "targetScreen"):
        try: b.targetScreen = target
        except Exception: pass
    if hasattr(b, "actionType"):
        try: b.actionType = action_type
        except Exception: pass

    return b


# ------------------------------------------------------------
# Deep clone baseline -> new GUIModel (keeping Screen objects consistent)
# ------------------------------------------------------------
def _clone_gui_model(template: GUIModel) -> Tuple[GUIModel, Dict[str, Screen], Dict[str, DataSourceElement]]:
    # Clone root
    cloned = GUIModel(**_accepted_kwargs(GUIModel, {
        "name": getattr(template, "name", "GeneratedApp"),
        "package": getattr(template, "package", "com.example.generated"),
        "versionCode": getattr(template, "versionCode", "1"),
        "versionName": getattr(template, "versionName", "1.0"),
        "description": getattr(template, "description", ""),
        "screenCompatibility": getattr(template, "screenCompatibility", True),
        "modules": set(),
    }))

    # ViewComponent
    vc_t = getattr(template, "viewComponent", None)
    if vc_t is not None:
        vc = ViewComponent(**_accepted_kwargs(ViewComponent, {
            "name": getattr(vc_t, "name", f"{cloned.name}ViewComponent"),
            "description": getattr(vc_t, "description", ""),
        }))
        cloned.viewComponent = vc

    # Clone DataSources
    datasources_by_name: Dict[str, DataSourceElement] = {}
    ds_set = getattr(template, "data_sources", None) or set()
    for d in ds_set:
        fields = getattr(d, "fields", set()) or set()
        if isinstance(fields, list):
            fields = set(fields)
        dd = mk_datasource(
            name=getattr(d, "name", "DataSource"),
            dataSourceClass=getattr(d, "dataSourceClass", None),
            fields=set(fields),
        )
        datasources_by_name[dd.name] = dd
    cloned.data_sources = set(datasources_by_name.values())

    # Collect screens across modules
    all_template_screens: Set[Screen] = set()
    for m in (getattr(template, "modules", None) or set()):
        all_template_screens |= set(getattr(m, "screens", None) or set())

    # Screen map
    screen_map: Dict[Screen, Screen] = {}
    screens_by_name: Dict[str, Screen] = {}
    for s in all_template_screens:
        sc = mk_screen(
            name=getattr(s, "name", "Screen"),
            description=getattr(s, "description", ""),
            is_main=bool(getattr(s, "is_main_page", False)),
        )
        for k in ["x_dpi", "y_dpi", "screen_size"]:
            if hasattr(sc, k) and hasattr(s, k):
                try: setattr(sc, k, getattr(s, k))
                except Exception: pass
        screen_map[s] = sc
        screens_by_name[sc.name] = sc

    # Clone elements, ensuring targetScreen points to CLONED screens
    elem_map: Dict[int, Any] = {}

    def clone_element(e: Any) -> Any:
        key = id(e)
        if key in elem_map:
            return elem_map[key]

        if isinstance(e, InputField):
            ftype = getattr(e, "field_type", None) or getattr(e, "type", None) or InputFieldType.Text
            ce = mk_input(
                name=getattr(e, "name", "InputField"),
                description=getattr(e, "description", ""),
                field_type=ftype,
                validation_rules=getattr(e, "validationRules", "") or getattr(e, "validation", "") or "",
            )

        elif isinstance(e, Button):
            tgt = getattr(e, "targetScreen", None)
            tgt_c = screen_map.get(tgt) if tgt is not None else None
            ce = mk_button(
                name=getattr(e, "name", "Button"),
                description=getattr(e, "description", ""),
                label=getattr(e, "label", getattr(e, "name", "Button")),
                button_type=getattr(e, "buttonType", ButtonType.TextButton),
                action_type=getattr(e, "actionType", ButtonActionType.Navigate),
                target=tgt_c,
            )

        elif isinstance(e, DataList):
            srcs = getattr(e, "list_sources", None) or getattr(e, "listSources", None) or getattr(e, "sources", None) or set()
            if isinstance(srcs, list):
                srcs = set(srcs)
            new_sources: Set[DataSourceElement] = set()
            for src in srcs:
                n = getattr(src, "name", None)
                if n and n in datasources_by_name:
                    new_sources.add(datasources_by_name[n])
                elif isinstance(src, DataSourceElement):
                    new_sources.add(src)
            ce = mk_datalist(
                name=getattr(e, "name", "DataList"),
                description=getattr(e, "description", ""),
                sources=new_sources,
            )

        else:
            ce = e

        elem_map[key] = ce
        return ce

    # Assign elements per cloned screen
    for s_t, s_c in screen_map.items():
        s_c.view_elements = set()
        for e in (getattr(s_t, "view_elements", None) or set()):
            s_c.view_elements.add(clone_element(e))

    # Clone modules with cloned screens
    for m in (getattr(template, "modules", None) or set()):
        cm = Module(**_accepted_kwargs(Module, {"name": getattr(m, "name", "Module"), "screens": set()}))
        for s in (getattr(m, "screens", None) or set()):
            cm.screens.add(screen_map[s])
        cloned.modules.add(cm)

    return cloned, screens_by_name, datasources_by_name


# ------------------------------------------------------------
# Pruning helpers
# ------------------------------------------------------------
def _remove_screen(gui: GUIModel, screen_name: str):
    for m in (getattr(gui, "modules", None) or set()):
        rm = [s for s in (getattr(m, "screens", None) or set()) if getattr(s, "name", "") == screen_name]
        for s in rm:
            m.screens.discard(s)


def _remove_element(screen: Optional[Screen], element_name: str):
    if screen is None:
        return
    rm = [e for e in (getattr(screen, "view_elements", None) or set()) if getattr(e, "name", "") == element_name]
    for e in rm:
        screen.view_elements.discard(e)


def _set_button_target(screen: Optional[Screen], button_name: str, action: ButtonActionType, target: Optional[Screen]):
    if screen is None:
        return
    for e in (getattr(screen, "view_elements", None) or set()):
        if isinstance(e, Button) and getattr(e, "name", "") == button_name:
            if hasattr(e, "targetScreen"):
                try: e.targetScreen = target
                except Exception: pass
            if hasattr(e, "actionType"):
                try: e.actionType = action
                except Exception: pass


def _prune_ds_field(ds: Optional[DataSourceElement], field_obj: Any):
    if ds is None or field_obj is None:
        return
    fields = getattr(ds, "fields", set()) or set()
    if isinstance(fields, list):
        fields = set(fields)
    ds.fields = set(fields) - {field_obj}


# ------------------------------------------------------------
# Structural binding (robust to your structural file layout)
# - Your structural module defines Class.attributes sets, not global Property variables. :contentReference[oaicite:5]{index=5}
# - Also your structural has Category but not Tag. :contentReference[oaicite:6]{index=6}
# ------------------------------------------------------------
def _get_structural_class(st_mod, name: str):
    if not hasattr(st_mod, name):
        raise RuntimeError(f"structural binding missing: {st_mod.__name__}.{name}")
    return getattr(st_mod, name)


def _get_attr_prop(cls_obj, prop_name: str) -> Optional[StructuralProperty]:
    attrs = getattr(cls_obj, "attributes", None) or set()
    if isinstance(attrs, list):
        attrs = set(attrs)
    for a in attrs:
        if isinstance(a, StructuralProperty) and getattr(a, "name", None) == prop_name:
            return a
    # some BESSER variants don't use StructuralProperty class identity; fallback by duck-typing
    for a in attrs:
        if getattr(a, "name", None) == prop_name:
            return a  # type: ignore
    return None


def _ensure_structural_binding(gui: GUIModel, datasources_by_name: Dict[str, DataSourceElement], structural_module: str):
    st = importlib.import_module(structural_module)

    # Required classes from your structural file :contentReference[oaicite:7]{index=7}
    Item = _get_structural_class(st, "Item")
    Community = _get_structural_class(st, "Community")
    Message = _get_structural_class(st, "Message")
    Conversation = _get_structural_class(st, "Conversation")

    # Optional classes
    Category = getattr(st, "Category", None)   # exists in your structural :contentReference[oaicite:8]{index=8}
    Rating = getattr(st, "Rating", None)       # exists in your structural :contentReference[oaicite:9]{index=9}
    Offer = getattr(st, "Offer", None)         # exists in your structural :contentReference[oaicite:10]{index=10}

    # Bind ItemsDataSource -> Item + properties by name (from Item.attributes)
    if "ItemsDataSource" in datasources_by_name:
        d = datasources_by_name["ItemsDataSource"]
        d.dataSourceClass = Item
        fields = set()

        # baseline GUI uses descriptions like: title, description, minExchangeValue.amount, state, createdAt :contentReference[oaicite:11]{index=11}
        # structural Item has: title, description, createdAt, state, ... and maybe not "price" directly :contentReference[oaicite:12]{index=12}
        for pn in ["title", "description", "createdAt", "state", "condition", "kind"]:
            p = _get_attr_prop(Item, pn)
            if p is not None:
                fields.add(p)

        # if you want "price", your structural uses Money association 'minExchangeValue', not an Item attribute. :contentReference[oaicite:13]{index=13}
        # keep GUI field as-is (description "minExchangeValue.amount") but datasource fields can stay minimal.
        d.fields = fields

    # Bind TagsDataSource -> Category (since Tag does not exist) :contentReference[oaicite:14]{index=14}
    if "TagsDataSource" in datasources_by_name:
        d = datasources_by_name["TagsDataSource"]
        if Category is not None:
            d.dataSourceClass = Category
            name_prop = _get_attr_prop(Category, "name")
            d.fields = {name_prop} if name_prop is not None else set()
        else:
            # remove datasource if neither Tag nor Category exists
            del datasources_by_name["TagsDataSource"]

    # Bind RatingsDataSource -> Rating
    if "RatingsDataSource" in datasources_by_name:
        d = datasources_by_name["RatingsDataSource"]
        if Rating is not None:
            d.dataSourceClass = Rating
            fields = set()
            for pn in ["stars", "comment", "createdAt"]:
                p = _get_attr_prop(Rating, pn)
                if p is not None:
                    fields.add(p)
            d.fields = fields
        else:
            del datasources_by_name["RatingsDataSource"]

    # Bind MessagesDataSource -> Message
    if "MessagesDataSource" in datasources_by_name:
        d = datasources_by_name["MessagesDataSource"]
        d.dataSourceClass = Message
        fields = set()
        for pn in ["content", "sentAt", "kind"]:
            p = _get_attr_prop(Message, pn)
            if p is not None:
                fields.add(p)
        d.fields = fields

    # Bind ConversationsDataSource -> Conversation (no fields)
    if "ConversationsDataSource" in datasources_by_name:
        d = datasources_by_name["ConversationsDataSource"]
        d.dataSourceClass = Conversation
        d.fields = set()

    # Bind CommunitiesDataSource -> Community
    if "CommunitiesDataSource" in datasources_by_name:
        d = datasources_by_name["CommunitiesDataSource"]
        d.dataSourceClass = Community
        name_prop = _get_attr_prop(Community, "name")
        d.fields = {name_prop} if name_prop is not None else set()

    # Bind OffersDataSource -> Offer (if exists)
    if "OffersDataSource" in datasources_by_name:
        if Offer is not None:
            d = datasources_by_name["OffersDataSource"]
            d.dataSourceClass = Offer
            d.fields = set()
        else:
            del datasources_by_name["OffersDataSource"]

    gui.data_sources = set(datasources_by_name.values())


# ------------------------------------------------------------
# Python exporter (exports a runnable generated_gui_model.py)
# - IMPORTANT: we do NOT import Property globals from structural module.
#   We reconstruct datasource fields by looking up properties in Class.attributes at runtime.
# ------------------------------------------------------------
def _safe_ident(s: str) -> str:
    if not s:
        return "Unnamed"
    out = []
    for ch in s:
        out.append(ch if (ch.isalnum() or ch == "_") else "_")
    t = "".join(out)
    if t[0].isdigit():
        t = "_" + t
    return t


def export_gui_model_to_python(gui: GUIModel, structural_module: str, output_py: str = "generated_gui_model.py"):
    p = Path(output_py).resolve()

    modules = getattr(gui, "modules", None) or set()
    screens: Set[Screen] = set()
    for m in modules:
        screens |= set(getattr(m, "screens", None) or set())
    data_sources = getattr(gui, "data_sources", None) or set()

    screens_sorted = sorted(list(screens), key=lambda s: getattr(s, "name", "") or "")
    ds_sorted = sorted(list(data_sources), key=lambda d: getattr(d, "name", "") or "")
    modules_sorted = sorted(list(modules), key=lambda m: getattr(m, "name", "") or "")

    gui_name = getattr(gui, "name", "GeneratedApp")
    gui_pkg  = getattr(gui, "package", "com.example.generated")
    vcode    = getattr(gui, "versionCode", "1")
    vname    = getattr(gui, "versionName", "1.0")
    gdesc    = getattr(gui, "description", "")
    compat   = bool(getattr(gui, "screenCompatibility", True))

    vc = getattr(gui, "viewComponent", None)
    vc_name = getattr(vc, "name", "ViewComponent") if vc else None
    vc_desc = getattr(vc, "description", "") if vc else None

    # Gather structural classes referenced by datasources
    needed_classes: Set[str] = set()
    for d in ds_sorted:
        cls = getattr(d, "dataSourceClass", None)
        if cls is not None and hasattr(cls, "name"):
            # class object likely imported as global in structural module; we will import by its global name
            # fallback: use cls.name as symbol, expecting same
            needed_classes.add(getattr(cls, "name"))

    L: List[str] = []
    L += ['"""', 'generated_gui_model.py', '', 'FULL generated GUI model (Python) from M2M (pruning-only).', '"""', ""]
    L += ["from __future__ import annotations", "import inspect", "from typing import Set, Optional", ""]
    L += ["from besser.BUML.metamodel.gui import (",
          "    GUIModel, Module, Screen, Button, InputField, DataList,",
          "    DataSourceElement, ViewComponent,",
          "    ButtonType, ButtonActionType, InputFieldType",
          ")", ""]
    L += [f"import {structural_module} as st", ""]
    L += [
        "def _accepted_kwargs(cls, provided: dict) -> dict:",
        "    sig = inspect.signature(cls.__init__)",
        "    params = set(sig.parameters.keys())",
        "    params.discard('self')",
        "    return {k: v for k, v in provided.items() if k in params}",
        "",
        "def _get_prop(cls_obj, prop_name: str):",
        "    attrs = getattr(cls_obj, 'attributes', None) or set()",
        "    if isinstance(attrs, list):",
        "        attrs = set(attrs)",
        "    for a in attrs:",
        "        if getattr(a, 'name', None) == prop_name:",
        "            return a",
        "    return None",
        "",
        "def mk_screen(*, name: str, description: str, is_main: bool = False) -> Screen:",
        "    base = {",
        "        'name': name, 'description': description,",
        "        'x_dpi': 'x_dpi', 'y_dpi': 'y_dpi',",
        "        'screen_size': 'Medium', 'view_elements': set(),",
        "        'is_main_page': is_main,",
        "    }",
        "    return Screen(**_accepted_kwargs(Screen, base))",
        "",
        "def mk_datasource(*, name: str, dataSourceClass, fields: Set) -> DataSourceElement:",
        "    base = {'name': name, 'dataSourceClass': dataSourceClass, 'fields': set(fields)}",
        "    return DataSourceElement(**_accepted_kwargs(DataSourceElement, base))",
        "",
        "def mk_input(*, name: str, description: str, field_type=InputFieldType.Text, validation_rules: str = '') -> InputField:",
        "    base = {'name': name, 'description': description}",
        "    p = inspect.signature(InputField.__init__).parameters",
        "    if 'validationRules' in p: base['validationRules'] = validation_rules",
        "    elif 'validation' in p: base['validation'] = validation_rules",
        "    elif 'validation_rules' in p: base['validation_rules'] = validation_rules",
        "    if 'field_type' in p: base['field_type'] = field_type",
        "    elif 'type' in p: base['type'] = field_type",
        "    elif 'inputFieldType' in p: base['inputFieldType'] = field_type",
        "    elif 'fieldType' in p: base['fieldType'] = field_type",
        "    return InputField(**_accepted_kwargs(InputField, base))",
        "",
        "def mk_button(*, name: str, description: str, label: str,",
        "              button_type=ButtonType.TextButton,",
        "              action_type=ButtonActionType.Navigate,",
        "              target: Optional[Screen] = None) -> Button:",
        "    p = inspect.signature(Button.__init__).parameters",
        "    base = {'name': name, 'description': description, 'label': label}",
        "    if 'buttonType' in p: base['buttonType'] = button_type",
        "    elif 'button_type' in p: base['button_type'] = button_type",
        "    ctor_action = action_type",
        "    if action_type == ButtonActionType.Navigate and target is None:",
        "        ctor_action = ButtonActionType.OpenForm",
        "    if 'actionType' in p: base['actionType'] = ctor_action",
        "    elif 'action_type' in p: base['action_type'] = ctor_action",
        "    if target is not None and 'targetScreen' in p: base['targetScreen'] = target",
        "    b = Button(**_accepted_kwargs(Button, base))",
        "    if hasattr(b, 'buttonType'):",
        "        try: b.buttonType = button_type",
        "        except Exception: pass",
        "    if hasattr(b, 'targetScreen'):",
        "        try: b.targetScreen = target",
        "        except Exception: pass",
        "    if hasattr(b, 'actionType'):",
        "        try: b.actionType = action_type",
        "        except Exception: pass",
        "    return b",
        "",
        "def mk_datalist(*, name: str, description: str, sources: Set[DataSourceElement]) -> DataList:",
        "    p = inspect.signature(DataList.__init__).parameters",
        "    base = {'name': name, 'description': description}",
        "    if 'list_sources' in p: base['list_sources'] = set(sources)",
        "    elif 'listSources' in p: base['listSources'] = set(sources)",
        "    elif 'sources' in p: base['sources'] = set(sources)",
        "    return DataList(**_accepted_kwargs(DataList, base))",
        "",
        "def mk_module(*, name: str, screens: Set[Screen]) -> Module:",
        "    base = {'name': name, 'screens': set(screens)}",
        "    return Module(**_accepted_kwargs(Module, base))",
        "",
        "def build_generated_gui_model() -> GUIModel:",
        f"    gui_name = {gui_name!r}",
        f"    gui_pkg  = {gui_pkg!r}",
        f"    vcode    = {vcode!r}",
        f"    vname    = {vname!r}",
        f"    gdesc    = {gdesc!r}",
        f"    compat   = {compat!r}",
        "",
        "    # Screens",
    ]

    # Screens
    for s in screens_sorted:
        sn = getattr(s, "name", "Screen")
        sv = _safe_ident(sn)
        sd = getattr(s, "description", "")
        sm = bool(getattr(s, "is_main_page", False))
        L += [f"    {sv} = mk_screen(name={sn!r}, description={sd!r}, is_main={sm!r})"]
    L += ["", "    # DataSources"]

    # DataSources (rebuild fields via _get_prop on class.attributes)
    ds_var: Dict[str, str] = {}
    for d in ds_sorted:
        dn = getattr(d, "name", "DataSource")
        dv = _safe_ident(dn)
        ds_var[dn] = dv

        cls = getattr(d, "dataSourceClass", None)
        cls_sym = getattr(cls, "name", None) if cls is not None else None
        cls_expr = f"getattr(st, {cls_sym!r})" if cls_sym else "None"

        fields = getattr(d, "fields", None) or set()
        if isinstance(fields, list):
            fields = set(fields)

        # we don't rely on global property names; we map back to property.name strings
        prop_names = sorted({getattr(f, "name", None) for f in fields if getattr(f, "name", None)})
        if prop_names and cls_sym:
            props_expr = "{ " + ", ".join([f"_get_prop(getattr(st, {cls_sym!r}), {pn!r})" for pn in prop_names]) + " }"
        else:
            props_expr = "set()"

        L += [f"    {dv} = mk_datasource(name={dn!r}, dataSourceClass={cls_expr}, fields={props_expr})"]

    L += ["", "    # View elements per screen"]

    # Elements per screen
    for s in screens_sorted:
        sn = getattr(s, "name", "Screen")
        sv = _safe_ident(sn)
        L += [f"    # Elements for {sn}"]
        created: List[str] = []

        elems = sorted(list(getattr(s, "view_elements", None) or set()), key=lambda e: getattr(e, "name", "") or "")
        for e in elems:
            en = getattr(e, "name", "Element")
            ev = _safe_ident(f"{sv}_{en}")

            if isinstance(e, InputField):
                ed = getattr(e, "description", "")
                ftype = getattr(e, "field_type", None) or getattr(e, "type", None) or InputFieldType.Text
                ftype_expr = f"InputFieldType.{getattr(ftype, 'name', 'Text')}"
                vr = getattr(e, "validationRules", "") or getattr(e, "validation", "") or ""
                L += [f"    {ev} = mk_input(name={en!r}, description={ed!r}, field_type={ftype_expr}, validation_rules={vr!r})"]
                created.append(ev)

            elif isinstance(e, DataList):
                ed = getattr(e, "description", "")
                srcs = getattr(e, "list_sources", None) or getattr(e, "listSources", None) or getattr(e, "sources", None) or set()
                if isinstance(srcs, list):
                    srcs = set(srcs)
                src_expr = []
                for src in sorted(list(srcs), key=lambda x: getattr(x, "name", "") or ""):
                    sdn = getattr(src, "name", None)
                    if sdn and sdn in ds_var:
                        src_expr.append(ds_var[sdn])
                sources_expr = "{ " + ", ".join(src_expr) + " }" if src_expr else "set()"
                L += [f"    {ev} = mk_datalist(name={en!r}, description={ed!r}, sources={sources_expr})"]
                created.append(ev)

            elif isinstance(e, Button):
                ed = getattr(e, "description", "")
                label = getattr(e, "label", en)
                bt = getattr(e, "buttonType", ButtonType.TextButton)
                at = getattr(e, "actionType", ButtonActionType.Navigate)
                bt_expr = f"ButtonType.{getattr(bt, 'name', 'TextButton')}"
                at_expr = f"ButtonActionType.{getattr(at, 'name', 'Navigate')}"
                tgt = getattr(e, "targetScreen", None)
                tgt_expr = _safe_ident(getattr(tgt, "name", "")) if tgt is not None else "None"
                L += [f"    {ev} = mk_button(name={en!r}, description={ed!r}, label={label!r}, button_type={bt_expr}, action_type={at_expr}, target={tgt_expr})"]
                created.append(ev)

            else:
                L += [f"    # skipped unknown element type: {e.__class__.__name__} name={en!r}"]

        if created:
            L += [f"    {sv}.view_elements.update({{{', '.join(created)}}})", ""]
        else:
            L += [f"    # no elements in {sn}", ""]

    # View component
    if vc_name is not None:
        L += [f"    vc = ViewComponent(name={vc_name!r}, description={vc_desc!r})"]
    else:
        L += ["    vc = None"]

    # Modules
    L += ["", "    modules = set()"]
    for m in modules_sorted:
        mn = getattr(m, "name", "Module")
        mv = _safe_ident(f"Module_{mn}")
        mscreens = sorted(list(getattr(m, "screens", None) or set()), key=lambda x: getattr(x, "name", "") or "")
        ms_expr = "{ " + ", ".join(_safe_ident(getattr(x, "name", "Screen")) for x in mscreens) + " }"
        L += [f"    {mv} = mk_module(name={mn!r}, screens={ms_expr})", f"    modules.add({mv})"]

    # GUIModel build
    L += [
        "",
        "    gui = GUIModel(**_accepted_kwargs(GUIModel, {",
        "        'name': gui_name,",
        "        'package': gui_pkg,",
        "        'versionCode': vcode,",
        "        'versionName': vname,",
        "        'description': gdesc,",
        "        'screenCompatibility': compat,",
        "        'modules': modules,",
        "    }))",
        "    if vc is not None: gui.viewComponent = vc",
        "    gui.data_sources = { " + ", ".join(ds_var.values()) + " }" if ds_var else "    gui.data_sources = set()",
        "    return gui",
        "",
        "community_gui_model = build_generated_gui_model()",
        "",
    ]

    p.write_text("\n".join(L), encoding="utf-8")


# ------------------------------------------------------------
# Main transformer (pruning only + export .py)
# ------------------------------------------------------------
def generate_gui_from_dsml_pruning_only_export_py(
    baseline_gui_py_path: str,
    dsml_xmi_path: str,
    dsml_ecore_path: str,
    structural_module: str,
    output_py_path: str = "generated_gui_model.py",
) -> GUIModel:
    dsml = load_dsml_appconfig(dsml_xmi_path, dsml_ecore_path)

    accounts = getattr(dsml, "accounts", None)
    listings = getattr(dsml, "listings", None)
    messaging = getattr(dsml, "messaging", None)
    ratings = getattr(dsml, "ratings", None)
    payments = getattr(dsml, "payments", None)
    subcommunities = getattr(dsml, "subcommunities", None)
    access_policies = getattr(dsml, "accessPolicies", None)

    price_mode = bool(listings and getattr(listings, "priceMode", False))
    chat_enabled = bool(messaging and getattr(messaging, "chat", False))
    ratings_enabled = bool(ratings and (getattr(ratings, "simple", False) or getattr(ratings, "bidirectional", False)))

    login_enabled = bool(accounts and (
        getattr(accounts, "localLogin", False) or
        getattr(accounts, "oauthLogin", False) or
        getattr(accounts, "phoneVerification", False)
    ))

    any_payment = bool(payments and (
        getattr(payments, "mbway", False) or
        getattr(payments, "multibanco", False) or
        getattr(payments, "paypal", False)
    ))

    sub_enabled = bool(subcommunities and getattr(subcommunities, "enabled", False))

    anonymous_browse = bool(access_policies and getattr(access_policies, "anonymousBrowse", False))

    # clone baseline
    baseline = _import_baseline_gui_model(baseline_gui_py_path)
    gui, screens, datasources = _clone_gui_model(baseline)

    # structural binding (robust)
    _ensure_structural_binding(gui, datasources, structural_module)

    # apply metadata
    gui.name = getattr(dsml, "appName", None) or gui.name
    short = getattr(dsml, "shortName", None)
    if short:
        gui.package = f"com.example.{short}"
    gui.description = f"GUI generated from baseline + DSML pruning for {gui.name}"

    # references to baseline screen names (these names exist in gui_community_platform.py) :contentReference[oaicite:15]{index=15}
    item_list = screens.get("ItemListScreen")
    item_details = screens.get("ItemDetailsScreen")
    chat_screen = screens.get("ChatScreen")
    payment_screen = screens.get("PaymentScreen")

    # --- PRUNING aligned with baseline element names :contentReference[oaicite:16]{index=16} ---

    # Price mode OFF -> remove ItemPrice field and Pay button + PaymentScreen
    if not price_mode:
        _remove_element(item_details, "ItemPrice")   # baseline uses ItemPrice
        _remove_element(item_details, "PayBtn")      # baseline uses PayBtn
        _remove_screen(gui, "PaymentScreen")

    # Payments OFF (or price off) -> remove Pay screen and payment buttons
    if (not any_payment) or (not price_mode):
        _remove_element(item_details, "PayBtn")
        _remove_screen(gui, "PaymentScreen")
    else:
        # prune specific payment methods
        if payment_screen is None:
            raise RuntimeError("Baseline FULL missing PaymentScreen.")
        if not getattr(payments, "mbway", False):
            _remove_element(payment_screen, "MBWayBtn")
        if not getattr(payments, "multibanco", False):
            _remove_element(payment_screen, "MultibancoBtn")
        if not getattr(payments, "paypal", False):
            _remove_element(payment_screen, "PayPalBtn")

        # ensure PayBtn navigates to PaymentScreen (baseline already does)
        _set_button_target(item_details, "PayBtn", ButtonActionType.Navigate, payment_screen)

    # Chat OFF -> remove Contact button and ChatScreen, plus datasources
    if not chat_enabled:
        _remove_element(item_details, "ContactBtn")
        _remove_screen(gui, "ChatScreen")
        if "MessagesDataSource" in datasources:
            del datasources["MessagesDataSource"]
        if "ConversationsDataSource" in datasources:
            del datasources["ConversationsDataSource"]
        gui.data_sources = set(datasources.values())
    else:
        if chat_screen is None:
            raise RuntimeError("Baseline FULL missing ChatScreen.")
        _set_button_target(item_details, "ContactBtn", ButtonActionType.Navigate, chat_screen)

    # Ratings OFF -> remove ItemRatingsList + RatingsListScreen + datasource
    if not ratings_enabled:
        _remove_element(item_details, "ItemRatingsList")
        _remove_screen(gui, "RatingsListScreen")
        if "RatingsDataSource" in datasources:
            del datasources["RatingsDataSource"]
            gui.data_sources = set(datasources.values())

    # Subcommunities OFF -> remove SubcommunitySelectorScreen + datasource
    if not sub_enabled:
        _remove_screen(gui, "SubcommunitySelectorScreen")
        if "CommunitiesDataSource" in datasources:
            del datasources["CommunitiesDataSource"]
            gui.data_sources = set(datasources.values())

    # Login OFF or anonymous browse -> remove LoginScreen
    if anonymous_browse or (not login_enabled):
        _remove_screen(gui, "LoginScreen")

    # Export ALWAYS as Python file
    export_gui_model_to_python(gui, structural_module=structural_module, output_py=output_py_path)
    return gui


# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------
if __name__ == "__main__":
    baseline_py = "gui_community_platform.py"
    dsml_ecore = "dsml_metamodel.ecore"
    dsml_xmi = "test_custom.xmi"
    structural_mod = "structural_community_platform"

    print("Baseline exists?", os.path.exists(baseline_py))
    print("Ecore exists?   ", os.path.exists(dsml_ecore))
    print("XMI exists?     ", os.path.exists(dsml_xmi))
    print("Structural mod? ", os.path.exists(structural_mod + ".py"))

    gui = generate_gui_from_dsml_pruning_only_export_py(
        baseline_gui_py_path=baseline_py,
        dsml_xmi_path=dsml_xmi,
        dsml_ecore_path=dsml_ecore,
        structural_module=structural_mod,
        output_py_path="generated_gui_model.py",
    )
    print("Generated GUIModel:", gui.name)
    print("Wrote:", Path("generated_gui_model.py").resolve())
