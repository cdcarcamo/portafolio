# portafolio

# Cárcamo Systems — Portafolio Profesional

Portafolio personal enfocado en desarrollo backend, APIs y sistemas,
construido con FastAPI y Jinja2.

El objetivo de este proyecto es presentar de forma clara mi perfil
técnico, experiencia y proyectos relacionados con automatización,
procesamiento de datos y arquitectura backend.

---

# Tecnologías utilizadas

- Python
- FastAPI
- Jinja2
- HTML5 / CSS3
- Git & GitHub

---

# Ejecución local

1. Clona el repositorio:

git clone https://github.com/cdcarcamo/portfolio.git
cd carcamo-systems-portfolio

2. Crear entorno virtual

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. instala dependencias

pip install -r requirements.txt

4. Ejecuta el servidor
   
uvicorn app.main:app --reload

5. abre en el navegador

http://127.0.0.1:8000
