# 📚 Biblioteca Virtual Django

Benvingut al projecte **Biblioteca Virtual**, una aplicació web desenvolupada amb **Django** que permet gestionar llibres, autors i etiquetes (*tags*). Aquesta aplicació està pensada per oferir una experiència senzilla i intuïtiva a usuaris interessats en consultar, afegir i gestionar continguts literaris.

---

## 🌟 Característiques Principals

- **Gestió de Publicacions (Posts):** Crear, editar i eliminar llibres o articles amb informació detallada.
- **Gestió d'Autors:** Registre d'autors amb informació com nom, biografia i altres dades rellevants.
- **Sistema de Tags:** Assignació d'etiquetes als llibres/articles per facilitar la cerca i classificació temàtica.
- **Interfície Administrativa:** Panell d’administració potent basat en Django Admin.
- **Interfície Pública:** Llistat i detall de llibres/entrades publicades, filtrables per autor i/o etiqueta.
- **Buscador:** Cerca ràpida per títol o contingut.
- **Disseny Responsiu:** Adaptació a dispositius mòbils i tauletes.

---

## ⚙️ Instal·lació Ràpida

Segueix aquests passos per instal·lar i posar en marxa el projecte localment:

### 1. Clonar el repositori

```bash
git clone https://github.com/EL_TEU_USUARI/BibliotecaVirtual.git
cd BibliotecaVirtual
```

### 2. Crear i activar un entorn virtual

```bash
# Linux/Mac
python -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate
```

### 3. Instal·lar les dependències

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de dades i aplicar migracions

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear un superusuari per accedir al panell d'administració

```bash
python manage.py createsuperuser
```

### 6. Executar el servidor de desenvolupament

```bash
python manage.py runserver
```

### 7. Accedir a l'aplicació

- **Web pública:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Panell d’administració:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🗂️ Estructura del Projecte

```
BibliotecaVirtual/
├── manage.py
├── requirements.txt
├── biblioteca/          # Aplicació principal
│   ├── models.py         # Models: Post, Autor, Tag
│   ├── views.py          # Vistes: mostrar llibres, autors, tags
│   ├── urls.py           # Rutes URL de l'app
│   ├── templates/        # Plantilles HTML
│   ├── static/           # Fitxers CSS, JS, imatges
│   ├── admin.py          # Configuració del panell d'administració
└── BibliotecaVirtual/    # Configuració general de Django
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## 📖 Models Principals

### `Post`
Representa cada llibre o article disponible a la biblioteca.

**Atributs:**
- `titol` (CharField): Títol del llibre o article.
- `descripcio` (TextField): Resum o contingut.
- `data_publicacio` (DateField): Data de publicació.
- `autor` (ForeignKey): Autor del llibre.
- `etiquetes` (ManyToManyField): Tags associats.

### `Autor`
Informació de cada autor registrat.

**Atributs:**
- `nom` (CharField): Nom complet.
- `biografia` (TextField): Breu biografia.
- `data_naixement` (DateField, opcional): Data de naixement.

### `Tag`
Sistema d'etiquetatge per categoritzar llibres i articles.

**Atributs:**
- `nom` (CharField): Nom de l'etiqueta.

---

## 🛡️ Requisits

- Python 3.8 o superior
- Django 4.x
- Entorn virtual (opcional però recomanat)

---

## 📝 Documentació Automàtica (Pydoc)

El projecte està configurat amb **GitHub Actions** per generar automàticament la documentació HTML dels fitxers `.py` amb **Pydoc**.

🔗 **Accés a la documentació:** [Veure la documentació aquí](https://EL_TEU_USUARI.github.io/BibliotecaVirtual/)

---

## 🚀 Desplegament

Aquest projecte pot ser desplegat fàcilment en plataformes com:

- **Heroku**
- **Railway**
- **Render**

Per desplegar, recorda configurar:
- Variables d'entorn (`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`)
- Procfile (per a Heroku):

```bash
web: gunicorn BibliotecaVirtual.wsgi
```

---

## 🤝 Contribucions

Les contribucions són benvingudes! Procediment per contribuir:

1. Fes un fork del repositori.
2. Crea una branca (`git checkout -b feature/NovaFuncionalitat`).
3. Fes commits (`git commit -m 'Afegeix nova funcionalitat'`).
4. Puja la branca (`git push origin feature/NovaFuncionalitat`).
5. Obre una *Pull Request*.

## ✉️ Contacte

- **Nom:** Roger
- **Email:** roger.pont.2173@lacetania.com
- **GitHub:** [RogerPont](https://github.com/EL_TEU_USUARI)

---

## 🔗 Enllaços Ràpids

- [Documentació Django](https://docs.djangoproject.com/en/4.2/)
- [GitHub Pages](https://pages.github.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
