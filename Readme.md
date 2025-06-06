📚 Biblioteca Virtual Django
Benvinguts al projecte Biblioteca Virtual, una aplicació web desenvolupada amb Django que permet gestionar llibres, autors i etiquetes (tags). Aquesta aplicació està pensada per oferir una experiència senzilla i intuïtiva per als usuaris interessats en consultar, afegir i gestionar continguts literaris.

🌟 Característiques Principals
Gestió de Publicacions (Posts): Crear, editar i eliminar llibres o articles amb informació detallada.

Gestió d'Autors: Registre d'autors amb informació com nom, biografia i altres dades rellevants.

Sistema de Tags: Assignació d'etiquetes als llibres/artícles per facilitar la cerca i la classificació temàtica.

Interfície Administrativa: Panell d’administració potent basat en Django Admin.

Interfície pública: Llista i detall de llibres/entrades publicades, filtrades per autor i/o etiquetes.

Buscador: Cerca ràpida per títol o contingut.

Responsiu: Adaptació als dispositius mòbils i tauletes.

⚙️ Instal·lació Ràpida
Segueix aquests passos per instal·lar i posar en marxa el projecte localment:

1. Clonar el repositori
bash
Copiar
Editar
git clone https://github.com/EL_TEU_USUARI/BibliotecaVirtual.git
cd BibliotecaVirtual
2. Crear i activar un entorn virtual
bash
Copiar
Editar
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
3. Instal·lar les dependències
bash
Copiar
Editar
pip install -r requirements.txt
4. Configurar la base de dades i aplicar migracions
bash
Copiar
Editar
python manage.py makemigrations
python manage.py migrate
5. Crear un superusuari per accedir al panell d'administració
bash
Copiar
Editar
python manage.py createsuperuser
6. Executar el servidor de desenvolupament
bash
Copiar
Editar
python manage.py runserver
7. Accedir a l'aplicació
Web pública: http://127.0.0.1:8000/

Panell d’administració: http://127.0.0.1:8000/admin/

🗂️ Estructura del Projecte
php
Copiar
Editar
BibliotecaVirtual/
│
├── manage.py
├── requirements.txt
├── biblioteca/        # Aplicació principal
│   ├── models.py       # Models: Post, Autor, Tag
│   ├── views.py        # Vistes per mostrar llibres, autors, tags
│   ├── urls.py         # Rutes URL de l'app
│   ├── templates/      # Plantilles HTML
│   ├── static/         # Fitxers CSS, JS, imatges
│   └── admin.py        # Configuració del panell d'administració
│
├── BibliotecaVirtual/  # Configuració general de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md
📖 Models Principals
Post
Representa cada llibre o article disponible a la biblioteca.

Títol

Descripció

Data de publicació

Autor (ForeignKey)

Etiquetes (ManyToMany)

Autor
Informació de cada autor:

Nom

Biografia

Data de naixement (opcional)

Tag
Sistema d’etiquetatge per categoritzar posts:

Nom de l'etiqueta

🛡️ Requisits
Python 3.8+

Django 4.x

Entorn virtual (recomanat)

