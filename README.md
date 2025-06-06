
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
git clone https://github.com/RogerPont/Projecte_Django.git
cd Projecte_Django
```

### 2. Crear i activar un entorn virtual

```bash
# Linux/Mac
python3 -m venv env
source env/bin/activate

# Windows
python -m venv env
env\Scripts\activate
```

### 3. Instal·lar les dependències

```bash
pip install -r requirements.txt
```

### 4. Aplicar migracions

```bash
python manage.py migrate
```

### 5. Crear un superusuari per al panell d'administració

```bash
python manage.py createsuperuser
```

### 6. Executar el servidor de desenvolupament

```bash
python manage.py runserver
```

### 7. Accedir a l'aplicació

- Web pública: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Panell d’administració: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Estructura del Projecte

```
Projecte_Django/
├── manage.py
├── requirements.txt
├── blog/
│   ├── migrations/
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── my_site/
│   ├── settings.py
│   └── ...
├── models.html
├── views.html
├── urls.html
├── README.md
└── ...
```

---

## 📄 Documentació Generada Automàticament

A continuació tens els enllaços a la documentació HTML generada amb Pydoc per als fitxers principals del projecte:

- [Documentació models.py](https://htmlpreview.github.io/?https://github.com/RogerPont/Projecte_Django/blob/main/models.html)
- [Documentació views.py](https://htmlpreview.github.io/?https://github.com/RogerPont/Projecte_Django/blob/main/views.html)
- [Documentació urls.py](https://htmlpreview.github.io/?https://github.com/RogerPont/Projecte_Django/blob/main/urls.html)

---

## 🚀 Desplegament

Aquest projecte es pot desplegar en serveis com:

- Heroku
- Railway
- Render

Recorda configurar les variables d'entorn (ex. `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`) i afegir un `Procfile` si cal.

---

## 🤝 Contribucions

Les contribucions són benvingudes! Per contribuir:

1. Fes un fork del repositori.
2. Crea una branca per la teva funcionalitat: `git checkout -b feature/nova-funcionalitat`.
3. Fes commits amb missatges clars.
4. Puja la branca: `git push origin feature/nova-funcionalitat`.
5. Obre una Pull Request.

---

## 📜 Llicència

Aquest projecte està sota la llicència MIT.

---

## ✉️ Contacte

- Nom: Roger Pont
- GitHub: [RogerPont](https://github.com/RogerPont)

---

## Enllaços Útils

- [Documentació Django](https://docs.djangoproject.com/en/4.2/)
- [GitHub Pages](https://pages.github.com/)
- [htmlpreview.github.io](https://htmlpreview.github.io/)

