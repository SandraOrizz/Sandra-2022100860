CREATE DATABASE curso_python;

USE curso_python;

CREATE TABLE registro (
    id INT AUTO_INCREMENT PRIMARY KEY,           
    matricula VARCHAR(100) NOT NULL,             
    direccion_url TEXT NOT NULL,                    
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
