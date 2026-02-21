# 🧪 QA Suite — Saucedemo E2E Testing

Suite completa de tests automatizados E2E para [Saucedemo](https://www.saucedemo.com), simulando un entorno de QA real con cobertura de flujos críticos, regresión y casos negativos.

---

## 🎯 ¿Por qué este proyecto?

La mayoría de proyectos de QA en portafolios testean solo el camino feliz. Este proyecto cubre la suite completa como se haría en una empresa real: smoke tests, regresión, flujos negativos y CI/CD integrado.

---

## 🧩 Cobertura de tests

| Módulo | Smoke | Regression | Negative | Total |
|--------|-------|------------|----------|-------|
| Login / Logout | ✅ | ✅ | ✅ | 5 |
| Carrito | ✅ | ✅ | ✅ | 5 |
| Inventario / Filtros | ✅ | ✅ | — | 5 |
| Checkout | ✅ | ✅ | ✅ | 5 |
| **Total** | **4** | **10** | **6** | **20** |

---

## 🏗️ Estructura del proyecto
```
qa-suite-saucedemo/
│
├── .github/
│   └── workflows/
│       └── tests.yml          # CI/CD con GitHub Actions
│
├── pages/                     # Page Object Model
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/                     # Casos de prueba
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_inventory.py
│
├── data/
│   └── users.py               # Datos de prueba centralizados
│
├── conftest.py                # Fixtures reutilizables
├── pytest.ini                 # Configuración y markers
└── requirements.txt
```

---

## ⚙️ Tecnologías

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Playwright](https://img.shields.io/badge/Playwright-latest-green)
![pytest](https://img.shields.io/badge/pytest-latest-orange)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-black)

---

## 🚀 Cómo ejecutar los tests

### 1. Clonar el repositorio
```bash
git clone https://github.com/ivonny88/qa-suite-saucedemo.git
cd qa-suite-saucedemo
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
playwright install chromium
```

### 3. Ejecutar los tests

**Todos los tests:**
```bash
pytest --headed
```

**Solo smoke tests:**
```bash
pytest -m smoke --headed
```

**Solo regression:**
```bash
pytest -m regression --headed
```

**Solo negativos:**
```bash
pytest -m negative --headed
```

**Con reporte HTML:**
```bash
pytest --html=report.html --self-contained-html
```

---

## 🔄 CI/CD

Los tests se ejecutan automáticamente en cada push a `main` mediante **GitHub Actions**, separados por tipo: smoke, regression y negative. Los reportes HTML se guardan como artefactos descargables.

---

## 🧠 Decisiones técnicas

**Page Object Model (POM)** — cada página tiene su propia clase, separando la lógica de interacción de los tests. Si cambia un selector, se modifica en un solo lugar.

**Fixtures en conftest.py** — `logged_in_page` hace el login automáticamente para los tests que lo necesitan, evitando repetición de código y haciendo los tests más rápidos.

**Datos centralizados** — todos los usuarios de prueba están en `data/users.py`. Si cambia una credencial, se actualiza en un solo fichero.

**Markers** — smoke, regression y negative permiten ejecutar subconjuntos de tests según la necesidad, como se hace en pipelines reales de CI/CD.

---

## 👩‍💻 Autora

**Fátima Ocaña** — QA Engineer | Manual & Automation Testing  
[LinkedIn](https://www.linkedin.com/in/f%C3%A1tima-oca%C3%B1a-caba%C3%B1as-1141005b/) · [GitHub](https://github.com/ivonny88)