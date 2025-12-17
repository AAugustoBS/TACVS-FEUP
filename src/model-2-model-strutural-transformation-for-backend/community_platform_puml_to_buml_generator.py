import os
import sys
import platform
import subprocess

if platform.system() == "Windows":
    user_scripts = os.path.join(os.environ['APPDATA'], 'Python', 'Python312', 'Scripts')
    if user_scripts not in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + user_scripts

from besser.BUML.notations.structuralPlantUML import plantuml_to_buml
from besser.BUML.metamodel.structural import DomainModel
from besser.generators.django import DjangoGenerator

def check_tools():
    """Verifica se as dependências de formatação exigidas pelo BESSER estão presentes."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "black", "isort"], 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Aviso: Não foi possível validar formatadores: {e}")

def main():
    check_tools()
    
    puml_path = 'community_platform_strutural_with_enums.plantuml'
    buml_path = 'buml/buml_model.py'
    output_dir = 'django_backend'

    os.makedirs('buml', exist_ok=True)

    try:
        print(f"1. Transformando Metamodelo ({puml_path})...")
        structural_buml: DomainModel = plantuml_to_buml(
            plantUML_model_path=puml_path, 
            buml_file_path=buml_path
        )

        print(f"2. Gerando Backend Django em '{output_dir}'...")
        
        django_app = DjangoGenerator(
            model=structural_buml, 
            project_name="CommunityBackend", 
            app_name="CoreAPI", 
            output_dir=output_dir
        )
        django_app.generate()

        print("\nBackend Django gerado com sucesso!")
        print(f"Próximos passos:\n  cd {output_dir}\n  python manage.py makemigrations\n  python manage.py migrate")

    except Exception as e:
        print(f"\nErro crítico: {e}")
        if "WinError 2" in str(e):
            print("\nERRO DE SISTEMA: O BESSER não encontrou o formatador 'black'.")
            print("Tente rodar: pip install black")

if __name__ == "__main__":
    main()