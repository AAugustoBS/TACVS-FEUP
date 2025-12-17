import os
import sys
import platform
import subprocess

if platform.system() == "Windows":
    user_scripts = os.path.join(os.environ['APPDATA'], 'Python', 'Python312', 'Scripts')
    if user_scripts not in os.environ['PATH']:
        os.environ['PATH'] += os.pathsep + user_scripts

sys.path.append(os.path.abspath('buml'))
try:
    from custom_buml_model import domain_model as structural_buml
except ImportError:
    print("Erro: Não foi possível encontrar 'buml/custom_buml_model.py' ou o objeto 'domain_model'.")
    sys.exit(1)

from besser.generators.django import DjangoGenerator

def check_tools():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "black", "isort"], 
                              stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Aviso: Não foi possível validar formatadores: {e}")

def main():
    check_tools()
    
    output_dir = 'custom_django_backend'

    try:
        print(f"1. A usar Modelo BUML Customizado já disponível...")
        
        print(f"2. Gerando Backend Django em '{output_dir}'...")
        
        django_app = DjangoGenerator(
            model=structural_buml, 
            project_name="CustomCommunityBackend", 
            app_name="CustomCoreAPI", 
            output_dir=output_dir
        )
        django_app.generate()

        print("\nBackend Django gerado com sucesso a partir do modelo customizado!")
        print(f"Próximos passos:\n  cd {output_dir}\n  python manage.py makemigrations\n  python manage.py migrate")

    except Exception as e:
        print(f"\nErro crítico: {e}")

if __name__ == "__main__":
    main()