# 🛍️ eCommerce-QA-Tests

Repositorio creado como parte del desarrollo de mi perfil profesional como QA Tester.  
**Temporada 1** finalizada: enfocada en **Testing Manual estructurado y documentado**.

---

## 📁 Estructura del proyecto

- `Manual-Bug-Report/`: carpeta con reportes de bugs hallados manualmente.
- `TestCases_eCommerce.xlsx`: primeros casos de prueba manuales.
- `TestCases_eCommerce_v2.xlsx`: nueva versión organizada en múltiples hojas (Home, Login, Carrito), con resultados reales y estados.

---

## ✅ Objetivos alcanzados (Temporada 1)

- ✔️ Planificación y escritura de casos de prueba funcionales.
- ✔️ Documentación en Excel con estructura clara: pasos, datos, resultado esperado/real y estado.
- ✔️ Reportes de bugs documentados en formato manual.
- ✔️ Flujo completo de trabajo con Git Bash, Visual Studio Code y GitHub:
  - Clonado del repositorio.
  - Edición local de archivos.
  - Versionado de cambios con commits descriptivos.
  - Push al repositorio público.
  
---

## 🚀 Próximo objetivo: Automatización (Temporada 2)

En la siguiente etapa comenzaré a automatizar los test cases usando **Python + Selenium**, apuntando a dominar buenas prácticas en automatización, Page Object Model y reportes automáticos.

---

🔗 UPDATE

Este proyecto contiene pruebas de calidad (QA) para una aplicación eCommerce.  
Es parte de mi entrenamiento y evolución profesional como QA Tester Manual y Automatizado.

---

## 🧪 Temporada 1: Testing Manual

**Estado:** Finalizado  
**Tecnologías:**  
- Planilla de Excel (.xlsx) para Casos de Prueba
- Pruebas de Caja Negra (Black Box Testing)
- Estrategias de Testing Funcional
- Gestión de versiones con Git y GitHub

**Archivos:**  
📁 `test-cases/` → Casos de prueba en Excel.

---

## 🤖 Temporada 2: Testing Automatizado

**Estado:** En progreso 🚧  
**Tecnologías:**  
- Python 🐍  
- Selenium WebDriver  
- Automatización de Navegador (Chrome)  
- Estructuración de pruebas con `unittest`

**Tests actuales:**  
📁 `automation/`  
- `test_open_homepage.py`: Abre el navegador y carga una página base.  
- `test_google_search.py`: Simula una búsqueda automatizada en Google.

---

## 🚀 Roadmap Próximo

- 🔐 Simular un login en un sitio real
- ✅ Verificar contenido dinámico en una página
- 🔄 Añadir setup/teardown automáticos
- 📦 Aprender PyTest para estructurar mejor los tests
- ☁️ Explorar GitHub Actions para CI/CD básico

---

🔗 UPDATE

## 🧪 Temporada 2: Automatización con Python + Selenium (Finalizada)

Esta segunda etapa del proyecto representa mi evolución hacia la automatización de pruebas funcionales. Se trabajó con:

- **Selenium WebDriver**
- **Python (versión 3.13)**
- **ChromeDriver**
- **Estructuras con unittest**
- Exploración inicial de **pytest** y **conftest.py** (pospuesta para temporada 3)
- Navegación por proyectos reales
- Manejo del flujo Git/GitHub desde terminal

---

### ✔️ Tests implementados:
| Test                            | Tecnología     | Resultado |
|---------------------------------|----------------|-----------|
| Búsqueda en Google              | Selenium + Python + unittest | ✅ |
| Simulación de login             | Selenium + Python + unittest | ✅ |
| Verificación de contenido real  | Selenium + Python + unittest | ✅ |
| Refactorización con setup/teardown | unittest | ✅ |
| Test con POM (inicial)          | pytest + conftest.py (pendiente) | 🔄 |
| DuckDuckGo search (final test)  | unittest (refactorizado) | ✅ |

---

### 📂 Estructura del proyecto

eCommerce-QA-Tests/
- automation/
    - test_google_search.py
    - test_login_demo.py
    - test_verify_content.py
    - test_with_setup_teardown.py
    - test_duckduckgo_unittest.py ✅
    - chromedriver.exe
    - archive/   🗃️ Tests pausados o reemplazados
        - test_wikipedia_pom.py
        - test_wikipedia_unittest.py
        - conftest.py
        - wikipedia_homepage.py
 - Manual-Bug-Report/
 - TestCases_eCommerce.xlsx
 - TestCases_eCommerce_v2.xlsx
 - README.md

## ✍️ Autor

Luis Ortiz
QA Automation Engineer – Remote-ready 💻🌎
Este proyecto es parte de mi transición profesional hacia el mundo del QA Automatizado.  
Hecho con 💻, curiosidad y muchas ganas de aprender.

- GitHub: Lale11Ortiz
- LinkedIn: www.linkedin.com/in/luis-ortiz-qa