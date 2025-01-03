
# **Aplicación de Preguntas y Respuestas con Modelos LLM**  

En este repositorio he trabajado en varios proyectos diseñados para aprovechar el potencial de los modelos de lenguaje de última generación (LLM) utilizando la API de Hugging Face. A continuación, te presento los detalles de cada uno de los proyectos que he desarrollado:  

---

## **Proyecto 1: Aplicación de Preguntas y Respuestas**  

Se me pidió desarrollar una aplicación interactiva donde los usuarios pudieran realizar preguntas y recibir respuestas generadas por un modelo de lenguaje. La aplicación incluye una interfaz tipo chat que facilita la experiencia del usuario y está construida con Python y Flask.  

### **Características principales:**  
- Una interfaz intuitiva en formato de chat para interactuar con el modelo.  
- Respuestas generadas por un modelo preentrenado de Hugging Face, que aprovecha la tecnología más avanzada en procesamiento del lenguaje natural.  

### **Requisitos:**  
Para ejecutar este proyecto, asegúrate de tener instalado:  
- Python 3.7 o superior.  
- Las bibliotecas especificadas en el archivo `requirements.txt`:  
  - `transformers`  
  - `torch`  
  - `flask`  

### **Instalación:**  

1. Clona este repositorio en tu máquina local:  
   ```bash
   git clone https://github.com/OugMontiel/ChatBot-IA.git
   ```  

2. Instala las dependencias necesarias ejecutando:  
   ```bash
   pip install -r requirements.txt
   ```  

### **Uso:**  

1. Inicia la aplicación ejecutando:  
   ```bash
   python main.py
   ```  

2. Abre tu navegador y accede a:  
   ```
   http://127.0.0.1:5000
   ```  

3. Ingresa una pregunta en el campo de texto (puedes incluir un contexto opcional) y presiona "Enviar" para recibir la respuesta.  

### **Estructura del proyecto:**  

```
ChatBot-IA/
├── main.py            # Archivo principal para ejecutar la aplicación.
├── config.py          # Configuración y constantes del proyecto.
├── model.py           # Gestión del modelo de lenguaje.
├── app.py             # Lógica principal de la aplicación.
├── utils.py           # Archivo de utilidades
├── templates/
│   └── index.html     # Interfaz HTML de la aplicación.
└── requirements.txt   # Lista de dependencias necesarias.
```  

### **Capturas de pantalla:**  

#### Página principal:  
![Página Principal](Capturas/P2%20Sin%20Contenido.png)  

#### Ejemplo de interacción:  
Modelo 1 
![Pregunta](Capturas/P2%20con%20Contenido.png)  
![Respuesta](Capturas/P2%20Respuesta.png)  

Modelo 2
![Pregunta](Capturas/P2%20con%20Contenido%202%20Modelo.png)  
![Respuesta](Capturas/P2%20Respuesta%202%20modelo.png)  

----

## **Proyecto 2: Implementación de Múltiples Modelos con Iteración**

Este proyecto amplía la funcionalidad del primero al introducir la capacidad de utilizar múltiples modelos LLM mediante la API de Hugging Face. Se ha creado una clase gestionadora que permite cambiar fácilmente entre diferentes modelos, ofreciendo flexibilidad para comparar respuestas y seleccionar el modelo más adecuado para cada situación.

### **Características principales:**
- **Gestión de Múltiples Modelos:** Permite cargar y alternar entre varios modelos de lenguaje.
- **Comparación de Respuestas:** Facilita la evaluación de respuestas generadas por diferentes modelos para determinar cuál es más apropiado en diversos contextos.
- **Interfaz Intuitiva:** La interfaz tipo chat se ha mantenido, con la adición de un selector para elegir el modelo a utilizar.

### **Requisitos:**
Para ejecutar este proyecto, asegúrate de tener instalado:
- Python 3.7 o superior.
- Las bibliotecas especificadas en el archivo `requirements.txt`:  
  - `transformers`
  - `torch`
  - `flask`

### **Instalación:**

Sigue el mismo proceso de instalación que el Proyecto 1. Clona este repositorio y asegúrate de haber instalado todas las dependencias indicadas.

### **Uso:**

1. Inicia la aplicación ejecutando:
   ```bash
   python main.py
   ```

2. Abre tu navegador y accede a:
   ```
   http://127.0.0.1:5000
   ```

3. Escribe una pregunta en el campo de texto, selecciona el modelo deseado del menú desplegable, y presiona "Enviar" para obtener la respuesta.

### **Estructura del proyecto:**

```
ChatBot-IA/
├── main.py            # Archivo principal para ejecutar la aplicación.
├── config.py          # Configuración y constantes del proyecto.
├── model.py           # Gestión individual de modelos.
├── model_manager.py   # Clase para gestionar múltiples modelos.
├── app.py             # Lógica principal de la aplicación.
├── templates/
│   ├── index.html     # Interfaz HTML de la aplicación.
│   └── styles.css     # Estilos CSS para la interfaz.
└── requirements.txt   # Lista de dependencias necesarias.
```

### **Capturas de pantalla:**

#### Selector de modelos:
![Selector de Modelos](Capturas/P2%20Selector%20Modelos.png)

#### Ejemplo de interacción con diferentes modelos:
![Interacción Múltiples Modelos](Capturas/P2%20Interaccion%20Modelos.png)


----

# Proyecto 3: **Ejecución Local de Modelos**
Implementa un modelo que pueda ejecutarse localmente, sin necesidad de depender de servicios en la nube. Este proyecto puede abordar tareas como:
- **Análisis de sentimientos**: Aplicar técnicas de procesamiento del lenguaje natural (NLP) para determinar el tono de un texto.
- **Identificación de objetos en imágenes**: Usar visión por computadora para detectar y clasificar elementos en una imagen.  
Elige un modelo adecuado y demuestra su funcionalidad en un proyecto práctico.