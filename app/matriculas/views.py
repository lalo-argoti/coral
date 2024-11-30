from app.core.Mirlt import DB  # Importa la clase DB

def portal():
 return ""

# views.py
def process_student_data(student_data):
    #{'nombres': 'we', 'apellidos': 'we', 'identidad': 'we', 'fecha_nacimiento': '2099-12-12'}
    DB("""CREATE TABLE `informacion_sujeto` (
    `CODIGO` INT(11) NOT NULL,
    `NOM_ALUM` TEXT NOT NULL,
    `APEL_ALUM` TEXT NOT NULL,
    `TDOC` TEXT NOT NULL,
    `DOC_IDENT` TEXT NOT NULL,
    `GENERO` TEXT NOT NULL,
    `FECHA_NAC` DATE NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;""").run_query()

    return ""

