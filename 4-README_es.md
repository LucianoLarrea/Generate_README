# Generador de README de Proyecto

## Descripción

El **Generador de README de Proyecto** es una herramienta diseñada para automatizar la exploración, análisis y documentación de proyectos de software generando archivos README automáticamente. Este proyecto aprovecha una serie de agentes inteligentes para llevar a cabo tareas específicas, incluida la exploración de la estructura del directorio, el análisis de su contenido, la redacción del archivo README, e incluso su traducción a diferentes idiomas si es necesario.

## Propósito

El principal propósito de este proyecto es mejorar la eficiencia y precisión de la documentación de software. Al automatizar el proceso de generación de README, los desarrolladores pueden ahorrar tiempo y garantizar que su documentación sea completa y esté actualizada. Este proyecto es particularmente útil para bases de código grandes donde la documentación manual puede ser engorrosa y propensa a errores.

## Lógica de Ejecución

La ejecución del Generador de README de Proyecto comienza con el script `main.py`, que inicializa una instancia de la clase `ReadmeCrew` que se encuentra en `crew.py`. Esta instancia orquesta un equipo de agentes que trabajan juntos para llevar a cabo las tareas de generación de README. Las funcionalidades principales incluyen:

1. **Exploración:** El `explorer_agent` investiga el directorio del proyecto, enumerando sistemáticamente todos los archivos y la información relevante.
2. **Análisis:** El `analyzer_agent` procesa los datos recopilados en la fase de exploración para generar un resumen completo de la estructura del proyecto y sus componentes.
3. **Documentación:** El `writer_agent` compila el análisis en un archivo README estructurado.
4. **Traducción (opcional):** El `translator_agent` puede proporcionar una traducción del README al español, facilitando una mayor accesibilidad y uso.

La ejecución se orquesta a través del método `kickoff` de `ReadmeCrew`, que acepta una ruta de directorio como entrada y coordina las tareas definidas dentro del equipo.

## Archivos y Componentes Clave

- **`crew.py`:** Contiene la implementación de la clase `ReadmeCrew`, que integra múltiples agentes responsables de explorar, analizar, escribir y traducir.

- **`main.py`:** El punto de entrada principal que inicializa el proyecto y activa la ejecución de los agentes a través del método `kickoff`.

- **`__init__.py`:** Designa el directorio como un paquete, permitiendo que Python lo reconozca como tal.

- **`config/agents.yaml`:** Archivo de configuración que describe los roles y objetivos específicos de los diversos agentes desplegados dentro del proyecto.

- **`config/tasks.yaml`:** Define las tareas que deben ser ejecutadas por los agentes junto con sus resultados esperados, asegurando claridad en el flujo de trabajo.

- **`tools/custom_tool.py`:** Implementa funcionalidades adicionales que ayudan a los agentes en sus roles al proporcionar capacidades para leer archivos o directorios.

- **`tools/__init__.py`:** Marca el directorio de herramientas como un paquete, permitiendo importaciones estructuradas y el uso de las herramientas.

## Instalación y Configuración

Para configurar el Generador de README de Proyecto, puedes usar **Poetry** para la gestión de dependencias. Aquí se explica cómo instalar y configurar el proyecto:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/yourusername/project-readme-generator.git
   cd project-readme-generator
   ```

2. **Instala Poetry (si aún no está instalado):**
   Sigue las instrucciones de la [documentación oficial de Poetry](https://python-poetry.org/docs/#installation).

3. **Instala las dependencias:**
   ```bash
   poetry install
   ```

4. **Configuración:**
   - Modifica los archivos de configuración ubicados en el directorio `config` (`agents.yaml` y `tasks.yaml`) según sea necesario para adaptar el proyecto a tus requisitos específicos.

## Uso

Para ejecutar el Generador de README de Proyecto, utiliza el siguiente comando:

```bash
poetry run python main.py /ruta/a/tu/proyecto
```

Reemplaza `/ruta/a/tu/proyecto` con la ruta real al proyecto que deseas analizar y para el cual quieres generar la documentación.

Con esta configuración, puedes generar de manera eficiente un archivo README que no solo describa el propósito y la estructura de tu proyecto, sino que también se adapte rápidamente a tus necesidades de documentación. ¡Gracias por explorar el Generador de README de Proyecto!