

-- -----------------------------------------------------------
-- 1) Crear base de datos y configuración general
-- -----------------------------------------------------------
DROP DATABASE IF EXISTS universidad;
CREATE DATABASE universidad
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
USE universidad;

-- -----------------------------------------------------------
-- 2) Tablas principales
-- -----------------------------------------------------------

-- Departamento
CREATE TABLE Departamento (
  id_departamento INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL UNIQUE,
  descripcion TEXT,
  creado_en DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Profesor
CREATE TABLE Profesor (
  id_profesor INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  email VARCHAR(150) UNIQUE,
  id_departamento INT NOT NULL,
  contratado_en DATE,
  activo TINYINT(1) DEFAULT 1,
  CONSTRAINT fk_prof_depto FOREIGN KEY (id_departamento)
    REFERENCES Departamento(id_departamento)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Estudiante
CREATE TABLE Estudiante (
  id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  correo VARCHAR(150) UNIQUE,
  fecha_nacimiento DATE,
  fecha_ingreso DATE DEFAULT CURRENT_DATE,
  estado VARCHAR(20) DEFAULT 'activo',
  creado_en DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Curso
CREATE TABLE Curso (
  id_curso INT AUTO_INCREMENT PRIMARY KEY,
  codigo VARCHAR(20) NOT NULL UNIQUE,
  nombre VARCHAR(150) NOT NULL,
  descripcion TEXT,
  creditos TINYINT UNSIGNED NOT NULL DEFAULT 3,
  id_departamento INT NOT NULL,
  CONSTRAINT fk_curso_depto FOREIGN KEY (id_departamento)
    REFERENCES Departamento(id_departamento)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Clase (instancia de curso: semestre, profesor, cupos)
CREATE TABLE Clase (
  id_clase INT AUTO_INCREMENT PRIMARY KEY,
  id_curso INT NOT NULL,
  id_profesor INT NOT NULL,
  semestre VARCHAR(20) NOT NULL, -- ej. '2025-01' o '2025-02'
  horario VARCHAR(100),
  cupos INT UNSIGNED DEFAULT 30,
  activa TINYINT(1) DEFAULT 1,
  CONSTRAINT fk_clase_curso FOREIGN KEY (id_curso)
    REFERENCES Curso(id_curso)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  CONSTRAINT fk_clase_prof FOREIGN KEY (id_profesor)
    REFERENCES Profesor(id_profesor)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Inscripcion (tabla puente: M:M Estudiante <-> Clase)
CREATE TABLE Inscripcion (
  id_estudiante INT NOT NULL,
  id_clase INT NOT NULL,
  fecha_inscripcion DATETIME DEFAULT CURRENT_TIMESTAMP,
  estado_inscripcion VARCHAR(20) DEFAULT 'matriculado', -- 'matriculado','retirado'
  PRIMARY KEY (id_estudiante, id_clase),
  CONSTRAINT fk_insc_est FOREIGN KEY (id_estudiante)
    REFERENCES Estudiante(id_estudiante)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_insc_clase FOREIGN KEY (id_clase)
    REFERENCES Clase(id_clase)
    ON UPDATE CASCADE
    ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Calificacion
CREATE TABLE Calificacion (
  id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
  id_estudiante INT NOT NULL,
  id_clase INT NOT NULL,
  nota DECIMAL(5,2) NOT NULL,
  fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
  tipo VARCHAR(50) DEFAULT 'parcial', -- parcial, final, proyecto, etc.
  CONSTRAINT fk_calif_est FOREIGN KEY (id_estudiante)
    REFERENCES Estudiante(id_estudiante)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT fk_calif_clase FOREIGN KEY (id_clase)
    REFERENCES Clase(id_clase)
    ON UPDATE CASCADE
    ON DELETE CASCADE,
  CONSTRAINT chk_nota_range CHECK (nota >= 0 AND nota <= 100)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Índices para performance en joins/consultas
CREATE INDEX idx_clase_curso ON Clase (id_curso);
CREATE INDEX idx_clase_profesor ON Clase (id_profesor);
CREATE INDEX idx_calif_estudiante ON Calificacion (id_estudiante);
CREATE INDEX idx_calif_clase ON Calificacion (id_clase);
CREATE INDEX idx_estudiante_correo ON Estudiante (correo);
CREATE INDEX idx_profesor_departamento ON Profesor (id_departamento);

-- -----------------------------------------------------------
-- 3) Datos de ejemplo (inserts masivos pequeños)
-- -----------------------------------------------------------

-- Departamentos
INSERT INTO Departamento (nombre, descripcion) VALUES
('Ciencias de la Computación', 'Departamento de CS'),
('Matemáticas', 'Departamento de Matemáticas'),
('Humanidades', 'Lengua y Estudios Sociales');

-- Profesores
INSERT INTO Profesor (nombre, apellido, email, id_departamento, contratado_en) VALUES
('María', 'Gomez', 'maria.gomez@uni.edu', 1, '2018-09-01'),
('Carlos', 'Perez', 'carlos.perez@uni.edu', 1, '2020-02-15'),
('Ana', 'Rodriguez', 'ana.rodriguez@uni.edu', 2, '2015-01-10'),
('Luis', 'Martinez', 'luis.martinez@uni.edu', 3, '2019-08-20');

-- Estudiantes
INSERT INTO Estudiante (nombre, apellido, correo, fecha_nacimiento, fecha_ingreso) VALUES
('Juan', 'Lopez', 'juan.lopez@mail.com', '2001-05-20', '2021-08-15'),
('Carla', 'Diaz', 'carla.diaz@mail.com', '2000-11-02', '2020-08-15'),
('Pedro', 'Sanchez', 'pedro.sanchez@mail.com', '1999-03-12', '2019-08-15'),
('Luis', 'Fernandez', 'luis.fernandez@mail.com', '2002-07-01', '2022-01-10');

-- Cursos
INSERT INTO Curso (codigo, nombre, descripcion, creditos, id_departamento) VALUES
('CS101', 'Introducción a la Programación', 'Fundamentos de programación', 4, 1),
('CS201', 'Estructuras de Datos', 'Listas, árboles, grafos', 4, 1),
('MAT101', 'Cálculo I', 'Derivadas e integrales', 4, 2),
('HUM101', 'Historia Universal', 'Repaso de la historia', 3, 3);

-- Clases (instancias del curso por semestre)
INSERT INTO Clase (id_curso, id_profesor, semestre, horario, cupos) VALUES
(1, 1, '2025-01', 'Lun 08:00-10:00', 30),
(2, 2, '2025-01', 'Mar 10:00-12:00', 25),
(3, 3, '2025-01', 'Mie 09:00-11:00', 40),
(4, 4, '2025-01', 'Jue 14:00-16:00', 20),
(1, 2, '2025-02', 'Lun 10:00-12:00', 30); -- otra sección

-- Inscripciones
INSERT INTO Inscripcion (id_estudiante, id_clase) VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 3),
(3, 3),
(4, 4);

-- Calificaciones (ejemplo)
INSERT INTO Calificacion (id_estudiante, id_clase, nota, tipo) VALUES
(1,1,85.50,'parcial'),
(1,1,90.00,'final'),
(1,2,70.00,'final'),
(2,1,60.00,'final'),
(2,3,88.00,'final'),
(3,3,40.00,'final'),
(4,4,95.00,'final');

-- -----------------------------------------------------------
-- 4) Vistas y consultas predefinidas
-- -----------------------------------------------------------

-- Vista: transcripción / promedio por estudiante por curso
CREATE VIEW vw_transcripcion_estudiante AS
SELECT
  e.id_estudiante,
  CONCAT(e.nombre, ' ', e.apellido) AS estudiante,
  c.id_curso,
  c.codigo AS codigo_curso,
  c.nombre AS nombre_curso,
  cl.id_clase,
  cl.semestre,
  AVG(cal.nota) AS promedio_clase,
  COUNT(cal.id_calificacion) AS cantidad_notas
FROM Estudiante e
JOIN Inscripcion i ON e.id_estudiante = i.id_estudiante
JOIN Clase cl ON i.id_clase = cl.id_clase
JOIN Curso c ON cl.id_curso = c.id_curso
LEFT JOIN Calificacion cal ON cal.id_estudiante = e.id_estudiante AND cal.id_clase = cl.id_clase
GROUP BY e.id_estudiante, c.id_curso, cl.id_clase, cl.semestre;

-- Vista: promedio general por estudiante (across clases)
CREATE VIEW vw_promedio_general_estudiante AS
SELECT e.id_estudiante, CONCAT(e.nombre,' ',e.apellido) AS estudiante,
       AVG(cal.nota) AS promedio_general, COUNT(cal.id_calificacion) AS total_notas
FROM Estudiante e
LEFT JOIN Calificacion cal ON cal.id_estudiante = e.id_estudiante
GROUP BY e.id_estudiante;

-- -----------------------------------------------------------
-- 5) Stored Procedures / Transacciones: inscripción con control de cupos
-- -----------------------------------------------------------
DELIMITER $$
CREATE PROCEDURE sp_inscribir(IN p_est INT, IN p_clase INT)
BEGIN
  DECLARE v_cupos INT DEFAULT 0;
  DECLARE v_total INT DEFAULT 0;
  DECLARE v_activa TINYINT(1) DEFAULT 0;

  -- Empezar transacción
  START TRANSACTION;

    -- Bloquear la fila de clase para evitar race conditions
    SELECT cupos, activa INTO v_cupos, v_activa FROM Clase WHERE id_clase = p_clase FOR UPDATE;

    IF v_activa = 0 THEN
      ROLLBACK;
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La clase no está activa';
    ELSE
      SELECT COUNT(*) INTO v_total FROM Inscripcion WHERE id_clase = p_clase;
      IF v_total < v_cupos THEN
        -- Insertar si no existe (PK compuesta evitará duplicados)
        INSERT IGNORE INTO Inscripcion (id_estudiante, id_clase) VALUES (p_est, p_clase);
        COMMIT;
      ELSE
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No hay cupos disponibles';
      END IF;
    END IF;

END$$
DELIMITER ;

-- -----------------------------------------------------------
-- 6) Trigger de ejemplo: registrar auditoría simple al insertar calificación
-- -----------------------------------------------------------
-- Nota: para auditoría real preferir una tabla separada. Aquí se crea una tabla
--       simple y un trigger que la alimenta al insertar calificaciones.

CREATE TABLE AuditoriaCalificaciones (
  id_audit INT AUTO_INCREMENT PRIMARY KEY,
  id_calificacion INT,
  id_estudiante INT,
  id_clase INT,
  nota_old DECIMAL(5,2),
  nota_new DECIMAL(5,2),
  operacion VARCHAR(10), -- INSERT/UPDATE/DELETE
  operado_en DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DELIMITER $$
CREATE TRIGGER trg_calificacion_insert AFTER INSERT ON Calificacion
FOR EACH ROW
BEGIN
  INSERT INTO AuditoriaCalificaciones (id_calificacion, id_estudiante, id_clase, nota_old, nota_new, operacion)
  VALUES (NEW.id_calificacion, NEW.id_estudiante, NEW.id_clase, NULL, NEW.nota, 'INSERT');
END$$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER trg_calificacion_update AFTER UPDATE ON Calificacion
FOR EACH ROW
BEGIN
  INSERT INTO AuditoriaCalificaciones (id_calificacion, id_estudiante, id_clase, nota_old, nota_new, operacion)
  VALUES (NEW.id_calificacion, NEW.id_estudiante, NEW.id_clase, OLD.nota, NEW.nota, 'UPDATE');
END$$
DELIMITER ;

-- -----------------------------------------------------------
-- 7) Consultas avanzadas (bloque listo para ejecutar / adaptar)
-- -----------------------------------------------------------

-- 7.1 Ranking de estudiantes por promedio general (desc)
-- SELECT * FROM vw_promedio_general_estudiante ORDER BY promedio_general DESC;

-- 7.2 Cursos con mayor tasa de desaprobación (nota < 60)
-- SELECT
--   c.id_curso, c.codigo, c.nombre,
--   SUM(CASE WHEN cal.nota < 60 THEN 1 ELSE 0 END) AS reprobados,
--   COUNT(cal.id_calificacion) AS total_calificaciones,
--   ROUND(100 * SUM(CASE WHEN cal.nota < 60 THEN 1 ELSE 0 END) / NULLIF(COUNT(cal.id_calificacion),0),2) AS pct_reprobacion
-- FROM Curso c
-- JOIN Clase cl ON cl.id_curso = c.id_curso
-- LEFT JOIN Calificacion cal ON cal.id_clase = cl.id_clase
-- GROUP BY c.id_curso
-- ORDER BY pct_reprobacion DESC;

-- 7.3 Profesores con más clases activas y su promedio por clase
-- SELECT p.id_profesor, CONCAT(p.nombre,' ',p.apellido) AS profesor, COUNT(cl.id_clase) AS clases_activas,
--        AVG(sub.promedio_clase) AS promedio_por_clase
-- FROM Profesor p
-- JOIN Clase cl ON cl.id_profesor = p.id_profesor AND cl.activa = 1
-- LEFT JOIN (
--   SELECT id_clase, AVG(nota) AS promedio_clase FROM Calificacion GROUP BY id_clase
-- ) AS sub ON sub.id_clase = cl.id_clase
-- GROUP BY p.id_profesor
-- ORDER BY clases_activas DESC;

-- 7.4 Historial de un estudiante: inscripciones, notas y estado (ejemplo para id_estudiante = 1)
-- SELECT * FROM vw_transcripcion_estudiante WHERE id_estudiante = 1;

-- 7.5 Estadísticas por departamento: # cursos, # estudiantes inscritos (en sus cursos), promedio general
-- SELECT d.id_departamento, d.nombre AS departamento,
--        COUNT(DISTINCT c.id_curso) AS total_cursos,
--        COUNT(DISTINCT i.id_estudiante) AS estudiantes_inscritos,
--        ROUND(AVG(cal2.promedio_clase),2) AS promedio_departamento
-- FROM Departamento d
-- LEFT JOIN Curso c ON c.id_departamento = d.id_departamento
-- LEFT JOIN Clase cl ON cl.id_curso = c.id_curso
-- LEFT JOIN Inscripcion i ON i.id_clase = cl.id_clase
-- LEFT JOIN (
--   SELECT id_clase, AVG(nota) AS promedio_clase FROM Calificacion GROUP BY id_clase
-- ) cal2 ON cal2.id_clase = cl.id_clase
-- GROUP BY d.id_departamento;

-- -----------------------------------------------------------
-- 8) Consultas útiles de verificación (ejecutar para probar la BD)
-- -----------------------------------------------------------

-- Ver todos los departamentos
-- SELECT * FROM Departamento;

-- Ver profesores
-- SELECT * FROM Profesor;

-- Ver estudiantes
-- SELECT * FROM Estudiante;

-- Ver clases con cupos y conteo de inscritos
-- SELECT cl.id_clase, c.codigo, c.nombre AS curso, CONCAT(p.nombre,' ',p.apellido) AS profesor,
--        cl.semestre, cl.cupos, COUNT(i.id_estudiante) AS inscritos
-- FROM Clase cl
-- JOIN Curso c ON c.id_curso = cl.id_curso
-- JOIN Profesor p ON p.id_profesor = cl.id_profesor
-- LEFT JOIN Inscripcion i ON i.id_clase = cl.id_clase
-- GROUP BY cl.id_clase;

-- Calificaciones por estudiante
-- SELECT e.id_estudiante, CONCAT(e.nombre,' ',e.apellido) AS estudiante, cal.id_clase, cal.nota, cal.tipo
-- FROM Calificacion cal
-- JOIN Estudiante e ON e.id_estudiante = cal.id_estudiante
-- ORDER BY e.id_estudiante;

-- -----------------------------------------------------------
-- 9) Ejemplos de uso del procedimiento sp_inscribir
--    -- Ejecutar para inscribir (maneja control de cupos y transacción)
-- CALL sp_inscribir(3, 1); -- intenta inscribir al estudiante 3 en la clase 1
-- -----------------------------------------------------------

-- -----------------------------------------------------------
-- 10) Limpieza de ejemplo (comandos útiles si quieres resetear datos de prueba)
-- -----------------------------------------------------------
-- TRUNCATE TABLE Calificacion;
-- TRUNCATE TABLE Inscripcion;
-- TRUNCATE TABLE Clase;
-- TRUNCATE TABLE Curso;
-- TRUNCATE TABLE Estudiante;
-- TRUNCATE TABLE Profesor;
-- TRUNCATE TABLE Departamento;

-- -----------------------------------------------------------
-- 11) Mensajes finales / comprobación rápida
-- -----------------------------------------------------------
SELECT 'Script ejecutado correctamente. Revise las vistas: vw_transcripcion_estudiante, vw_promedio_general_estudiante' AS mensaje;