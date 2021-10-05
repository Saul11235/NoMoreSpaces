# NoMoreSpaces

A simple script for rename folders and files and remove the spaces of them from the terminal
un script simple para quitar los espacios de archivos y carpetas desde la terminal

# setup - instalación

add the script to your bashrc or Microsoft.PowerShell_profile.ps1, 
añade el script a tu archivo bashr o Microsoft.PowerShell_profile.ps1

- **bash**
  
  ```
  function NoMoreSpaces() {
      # add the full path
      python "NoMoreSpaces.py"
  }
  ```

- **powershell**
  
  ```
  function NoMoreSpaces {
      # add the full path 
        python "NoMoreSpaces.py"
  }
  ```

# How to use - Cómo usar

go to your working directory and execute  <code>NoMoreSpaces</code>, if you want to continue put the random key for rename **ALL FILES AND DIRECTORIES** in your current working directory, (subdirs are included).

Ve a tu directorio de trabajo y ejecuta `NoMoreSpaces`, para continuar ingresa la llave aleatoria, para renombrar **TODOS LOS ARCHIVOS Y CARPETAS** en tu directorio de trabajo, (incluidas las subcarpetas).

![Alt Text](https://media3.giphy.com/media/PjgwfaQV5OrFSD8md9/giphy.gif)

# Final notes

- This script is designed if you have many files with spaces and you manage them from the terminal.
- Avoid using it in directories that contain executables
- Replace the spaces <code> </code> with underscores <code> _ </code> and the number sign <code>#</code> with <code>N</code>   

# Notas finales

- Este script está pensado si tienes muchos archivos con espacios y los manejas desde la terminal.
- Evita usarlo en directorios que contengan ejecutables
- Reemplaza los espacios <code> </code> por guiones bajos <code> _ </code> y las almoadillas <code>#</code> por <code>N</code> 
