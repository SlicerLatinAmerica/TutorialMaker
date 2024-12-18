---
layout: default
title: 3D Slicer for Latin America
---
<style>
  .rectangular-button {
    background-color: #4CAF50; /* Verde */
    color: white; /* Texto en blanco */
    border: none; /* Sin borde */
    padding: 12px 24px; /* Espaciado interno (alto y ancho) */
    font-size: 16px; /* Tamaño de texto */
    text-transform: uppercase; /* Texto en mayúsculas */
    cursor: pointer; /* Cursor en forma de mano */
    text-align: center; /* Centra el texto */
    margin: 10px auto; /* Centrado con margen */
    display: inline-block; /* Permite el centrado */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Sombra */
    transition: all 0.3s ease; /* Transición suave */
  }

  /* Efecto hover (al pasar el ratón) */
  .rectangular-button:hover {
    background-color: #45a049; /* Verde más oscuro */
    transform: scale(1.05); /* Pequeña ampliación */
  }

  .button-description {
    font-size: 14px;
    color: #666;
    margin-top: 10px;
    text-align: center;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
  }
    .button-container {
    display: inline-block;
    text-align: center;
    margin: 10px;
  }

  .button-description {
    margin-top: 10px;
    font-size: 14px;
    color: #555;
  }
   .blue-box {
    border: 2px solid #007BFF; /* Borde azul */
    padding: 15px; /* Espaciado interno */
    border-radius: 5px; /* Esquinas ligeramente redondeadas */
    background-color: #f8f9fa; /* Fondo claro */
    color: #333; /* Color del texto */
    font-size: 16px; /* Tamaño de la fuente */
    max-width: 400px; /* Ancho máximo del cuadro */
    margin: 20px auto; /* Centrar el cuadro */
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra sutil */
  }
</style>


<div style="display: flex; justify-content: center; gap: 10px; padding:15px; ">
  <a href="Index" style="margin-right: 10px; text-decoration:none;">
    <button style="padding:10px 20px; color:#28a745; border:2px solid #28a745; border-radius:5px; background:none; cursor:pointer;">
      Introduction
    </button>
  </a>
  <a href="TutorialMakerTool" style="margin-right: 10px; text-decoration:none;">
    <button style="padding:10px 20px; color:#ffc107; border:2px solid #ffc107; border-radius:5px; background:none; cursor:pointer;">
      Tutorial Maker tool
    </button>
  </a>
  <a href="ProfessionalEvents" style="text-decoration:none;">
    <button style="padding:10px 20px; color:#007BFF; border:2px solid #007BFF; border-radius:5px; background:none; cursor:pointer;">
      Event participations
    </button>
  </a>
    <a href="EducationalMaterials" style="text-decoration:none;">
    <button style="padding:10px 20px; color:#6A0DAD; border:2px solid #6A0DAD; border-radius:5px; background:none; cursor:pointer;">
      Internationalization
    </button>
  </a>
</div>

<div style="background-color:#e9ecef; padding:20px; margin-top:20px; text-align:center; font-size:24px; font-weight:bold;">
  Tutorial Maker Tool
</div>

## **Tutorial Maker Tool**

**Description**

The Tutotial Maker is a tool to automate the creation of tutorials within the 3D Slicer environment. To achieve this goal, a project management methodology has been implemented, combining weekly virtual meetings and using the GitHub platform as a code development and collaboration system version control.


This tool was developed by **The 3D Slicer Latin America team**, whose members have made significant progress in developing the Tutorial Maker Module, focusing on improving its functionality, usability, and accessibility.

<div style="text-align:center; margin-top:40px;">
  <video width="640" height="360" controls>
    <source src="https://drive.google.com/uc?export=download&id=16IayI-S9uughLSn8hDL57y23291Wfw7w" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  <div class="button-description">Demo of the Tutorial Maker.</div>
</div>


Among the features of the tutorial maker tool are the following.    

<ul>
  <li>Internazionalization: The strings of the module's user interface were marked, enabling easy translation into multiple languages. The module's installation steps in Spanish [55], Portuguese [53] and English [54] are documented.
</li>
  <li>Accesibility: A simplified installation and use of the module allows a broader range of users to benefit from the tool.
</li>
  <li>Flexibility in Content Creation: 	The possibility to generate tutorials in multiple formats broadens the possibilities for distributing and utilizing the created content.
</li>
<li>Improved user experience: Interface optimizations and new features make the process of creating tutorials more intuitive and efficient. </li>
<li> Project sustainability: Process automation and improved project management ensure the module's continuous development and long-term maintenance.
 </li>
</ul>


**Repository**

<a href="https://github.com/SlicerLatinAmerica/SlicerTutorialMaker" target="_blank">
    The Tutorial Maker tool repository
  </a>
  contains a step-by-step installation process, and is constantly updated according to the improvements introduced by the team.
  


**First evaluations**

 6 Zoom meetings have been held with collaborators of the 3D Slicer In My Language project (EOSS cycle 4) to evaluate the Tutorial Maker tool. During the meeting, team members from Senegal reported on the tests they conducted using the Tutorial Maker tool to create a French version of the Slicer4Minute tutorial using the latest version of 3D Slicer (3D Slicer 5.7 Preview Release). The first test was carried out on September and consist on recreate the "FourMinTutorial"

