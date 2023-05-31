# Hunty

### Objetivo

Desarrollar un sistema de recomendación de empleos basado en la similitud entre las características de las vacantes y los perfiles de los usuarios.

### Estructura

```

├── api
│   ├── Dockerfile
│   ├── app.py
│   ├── middleware.py
│   ├── templates
│   │   └── index.html
│   └── tests
│       └── test_api.py
├── model
│   ├── Dockerfile
│   ├── ml_service.py
│   ├── settings.py
│   └── tests
│       └── test_model.py
├── datasets
├── docker-compose.yml
└── README.md

```

### Arquitectura del proyecto

Los microservicios son un enfoque arquitectónico utilizado para desarrollar aplicaciones como un conjunto de servicios pequeños e independientes que se comunican entre sí a través de APIs.Cada servicio se centra en una única funcionalidad y se puede desarrollar, implementar y escalar de manera independiente.

![Texto alternativo](Arquitectura.jpeg)


### Sistema de recomendacion

Referecias

"Annoy" es una biblioteca de código abierto que permite realizar búsquedas aproximadas y eficientes en espacios vectoriales de alta dimensionalidad. Es útil para construir índices de búsqueda y recuperar vectores similares en función de su similitud coseno. En el contexto de un sistema de recomendación, Annoy puede utilizarse para buscar elementos similares basados en sus representaciones vectoriales.

Por otro lado, "Sentence Transformers" es una biblioteca que permite generar representaciones vectoriales de alta calidad para oraciones y textos. Utiliza modelos de lenguaje previamente entrenados para codificar oraciones en vectores numéricos de alta dimensión. Estos vectores capturan el significado semántico de las oraciones y pueden utilizarse para medir la similitud entre ellas.

Al combinar Annoy y Sentence Transformers, puedes construir un sistema de recomendación de la siguiente manera:

Preprocesamiento de los datos: Primero, debes preparar tus datos, que pueden consistir en una colección de elementos que deseas recomendar. Esto puede ser texto, imágenes o cualquier otra forma de datos que se pueda representar como vectores.

Extracción de características: Utiliza Sentence Transformers para generar representaciones vectoriales de alta calidad para cada elemento en tu conjunto de datos. Estos vectores representarán las características semánticas de cada elemento.

Construcción del índice de búsqueda: Utiliza Annoy para construir un índice que permita realizar búsquedas rápidas y eficientes en los vectores generados. Esto implica insertar cada vector en el índice y configurar los parámetros adecuados para el espacio vectorial y el nivel de precisión deseado.

Recomendación de elementos similares: Cuando un usuario solicita una recomendación, puedes utilizar Annoy para buscar los elementos más similares en función de la similitud coseno de sus vectores. El sistema puede devolver los elementos más cercanos al vector de consulta como recomendaciones.

En resumen, al utilizar Annoy y Sentence Transformers, puedes construir un sistema de recomendación eficiente que aproveche las capacidades de búsqueda aproximada de Annoy y las representaciones vectoriales de alta calidad generadas por Sentence Transformers. Esto permite ofrecer recomendaciones basadas en la similitud semántica entre los elementos.

https://huggingface.co/sentence-transformers/all-mpnet-base-v2 
https://github.com/spotify/annoy


### API

Documentacion

http://0.0.0.0:8000/docs


### DOCKER

Para leventar los contenedores utilizar el comando : docker-compose up --build

### Oportunidad de mejoras

- Generacion de TEST
- Guardar resultados en bases de datos
- Mostras las vacantes directamente 
