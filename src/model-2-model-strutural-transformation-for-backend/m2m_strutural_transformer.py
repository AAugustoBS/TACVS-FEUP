import os
import io
from lxml import etree
from pyecore.resources import ResourceSet, URI
from buml.buml_model import domain_model
from besser.BUML.metamodel.structural import (
    DomainModel, Class, Property, BinaryAssociation, 
    Enumeration, EnumerationLiteral, Multiplicity
)

def run_m2m():
    print("[1/3] A carregar configurações...")
    try:
        rset = ResourceSet()
        def get_clean_bytes(path):
            parser = etree.XMLParser(remove_comments=True, recover=True)
            tree = etree.parse(path, parser)
            return etree.tostring(tree)

        ecore_res = rset.create_resource(URI('dsml_metamodel.ecore'))
        ecore_res.load(io.BytesIO(get_clean_bytes('dsml_metamodel.ecore')))
        mm_root = ecore_res.contents[0]
        rset.metamodel_registry[mm_root.nsURI] = mm_root
        
        xmi_res = rset.create_resource(URI('test_custom.xmi'))
        xmi_res.load(io.BytesIO(get_clean_bytes('test_custom.xmi')))
        dsml = xmi_res.contents[0]
    except Exception as e:
        print(f"ERRO: {e}")
        return

    print("[2/3] A filtrar e mapear tipos...")
    new_classes_data = []
    new_enums = []
    new_associations = []
    class_names_survived = set()

    for element in domain_model.types:
        if isinstance(element, Class):
            if element.name in ["Conversation", "Message"] and not dsml.messaging.chat: continue
            if element.name == "SubCommunity" and not dsml.subcommunities.enabled: continue
            
            class_names_survived.add(element.name)
            new_classes_data.append((element, list(element.attributes)))
        elif isinstance(element, Enumeration):
            new_enums.append(element)

    for assoc in domain_model.associations:
        ends = list(assoc.ends)
        if ends[0].type.name in class_names_survived and ends[1].type.name in class_names_survived:
            new_associations.append(assoc)

    print("[3/3] A gerar buml/custom_buml_model.py...")
    os.makedirs("buml", exist_ok=True)
    output_path = os.path.join("buml", "custom_buml_model.py")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("from besser.BUML.metamodel.structural import *\n\n")
        
        for enum in new_enums:
            literals = ", ".join([f'EnumerationLiteral("{l.name}")' for l in enum.literals])
            f.write(f"{enum.name} = Enumeration(name='{enum.name}', literals={{{literals}}})\n")
        
        f.write("\n# Classes\n")
        for cls_obj, _ in new_classes_data:
            f.write(f"{cls_obj.name} = Class(name='{cls_obj.name}')\n")
        
        f.write("\n# Attributes\n")
        for cls_obj, attrs in new_classes_data:
            attr_defs = []
            for attr in attrs:
                if cls_obj.name == "User" and attr.name == "isModerator" and not dsml.accounts.moderators: continue
                
                if isinstance(attr.type, (Class, Enumeration)):
                    t_name = attr.type.name
                else:
                    raw = str(attr.type).lower()
                    if 'string' in raw or 'str' in raw: t_name = "StringType"
                    elif 'int' in raw: t_name = "IntegerType"
                    elif 'bool' in raw: t_name = "BooleanType"
                    elif 'float' in raw or 'double' in raw: t_name = "FloatType"
                    elif 'datetime' in raw: t_name = "DateTimeType"
                    elif 'date' in raw: t_name = "DateType"
                    else: t_name = "StringType" # Fallback

                attr_defs.append(
                    f"Property(name='{attr.name}', type={t_name}, multiplicity=Multiplicity({attr.multiplicity.min}, {attr.multiplicity.max}))"
                )
            f.write(f"{cls_obj.name}.attributes = {{{', '.join(attr_defs)}}}\n")

        f.write("\n# Associations\n")
        for assoc in new_associations:
            e = list(assoc.ends)
            f.write(f"{assoc.name} = BinaryAssociation(name='{assoc.name}', ends={{\n")
            f.write(f"    Property(name='{e[0].name}', type={e[0].type.name}, multiplicity=Multiplicity({e[0].multiplicity.min}, {e[0].multiplicity.max}), is_navigable={e[0].is_navigable}),\n")
            f.write(f"    Property(name='{e[1].name}', type={e[1].type.name}, multiplicity=Multiplicity({e[1].multiplicity.min}, {e[1].multiplicity.max}), is_navigable={e[1].is_navigable})\n")
            f.write("})\n")

        all_types = ", ".join([c[0].name for c in new_classes_data] + [e.name for e in new_enums])
        all_assocs = ", ".join([a.name for a in new_associations])
        f.write(f"\ndomain_model = DomainModel(name='CustomModel', types={{{all_types}}}, associations={{{all_assocs}}})\n")

    print(f"✓ SUCESSO: {output_path} gerado corretamente.")

if __name__ == "__main__":
    run_m2m()