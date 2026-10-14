from archivos_capy.presentacion import cargar_menu
from archivos_capy.datos.repositorios.repo_curso import listado_cursos

cargar_menu()
for curso in listado_cursos():
    print(curso.id_cursos, curso.titulo_curso)