from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categoria'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text)

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    colegio = db.Column(db.Integer)
    sede = db.Column(db.Integer)
    modalidad = db.Column(db.Integer)
    curso = db.Column(db.String(4))
    nombre = db.Column(db.String(12))
    jornada = db.Column(db.String(15))
    denominacion = db.Column(db.String(1))
    durahora = db.Column(db.Integer)
    horasemana = db.Column(db.Integer)

class OCCB_CCI_Fras(db.Model):
    __tablename__ = 'occb_CCI_fras'
    id = db.Column(db.Integer, primary_key=True)
    inst = db.Column(db.Integer)
    CODIGO = db.Column(db.Integer)
    SIGLA = db.Column(db.Integer)
    FRASE = db.Column(db.Text)
    item = db.Column(db.String(16))
    evidencias = db.Column(db.String(256))
    responsable = db.Column(db.String(256))

class User(db.Model):
    __tablename__ = 'occb_user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_group_id = db.Column(db.Integer)
    username = db.Column(db.String(20))
    password = db.Column(db.String(40))
    salt = db.Column(db.String(16))
    firstname = db.Column(db.String(32))
    lastname = db.Column(db.String(32))
    email = db.Column(db.String(96))
    image = db.Column(db.String(255))
    code = db.Column(db.String(40))
    ip = db.Column(db.String(40))
    status = db.Column(db.Boolean)
    date_added = db.Column(db.DateTime)
    saldo = db.Column(db.Text)
    template = db.Column(db.Integer)
    celular = db.Column(db.String(16))
    celular2 = db.Column(db.String(16))
    cedula = db.Column(db.Integer)
    banco = db.Column(db.String(64))

class UserGroup(db.Model):
    __tablename__ = 'occb_user_group'
    user_group_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    permission = db.Column(db.Text)
    proyecto = db.Column(db.Text)
    usado = db.Column(db.Integer)

class Noticias(db.Model):
    __tablename__ = 'occb_noticias'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    noticia = db.Column(db.Text)
    fecha = db.Column(db.Date)
    foto = db.Column(db.String(255))
    id_autor = db.Column(db.Integer)

class Profesor(db.Model):
    __tablename__ = 'occb_profesor'
    CC_NUMERO = db.Column(db.Integer, primary_key=True)
    NOMBRES = db.Column(db.Text)
    APELLIDOS = db.Column(db.Text)
    FECHA_NAC = db.Column(db.Text)
    CARGO = db.Column(db.Text)
    LUG_EXP = db.Column(db.Text)
    EST_CIVIL = db.Column(db.Text)
    CC_LUGAR = db.Column(db.Text)
    LIB_MILIT = db.Column(db.Text)
    GENERO = db.Column(db.Text)
    DIRECCION = db.Column(db.Text)
    TELEFONO = db.Column(db.Text)
    FEC_VINCUL = db.Column(db.Text)
    DECRETO = db.Column(db.Text)
    UNIVERS = db.Column(db.Text)
    CURSILLOS = db.Column(db.Text)
    NOM_GRADO1 = db.Column(db.Text)
    REG_GRADO1 = db.Column(db.Text)
    ESCAL_SE = db.Column(db.Text)
    email = db.Column(db.String(255))

class Socioeconomico(db.Model):
    __tablename__ = 'occb_socioeconomicos'
    codigo = db.Column(db.Integer, primary_key=True)
    codigo_estudiante = db.Column(db.Integer)
    direccion = db.Column(db.String(128))
    ciudad = db.Column(db.String(32))
    telefono = db.Column(db.String(16))
    departamento = db.Column(db.String(32))
    religion = db.Column(db.String(32))
    sisben = db.Column(db.String(1))
    seguridad_social = db.Column(db.String(32))
    eps = db.Column(db.String(32))
    estrato = db.Column(db.String(1))
    tipo_sangre = db.Column(db.String(4))

class Decreto(db.Model):
    __tablename__ = 'occb_decretos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    colegio = db.Column(db.Integer)
    titulo = db.Column(db.String(64))
    resumen = db.Column(db.Text)

class Empresa(db.Model):
    __tablename__ = 'occb_empresa'
    client_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(124))
    email = db.Column(db.String(124))
    phone = db.Column(db.String(124))
    servicio = db.Column(db.Integer)
    images = db.Column(db.String(32))
    compartir = db.Column(db.Integer)

# Continúa con los modelos restantes siguiendo el mismo patrón...
