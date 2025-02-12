-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.30 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.1.0.6537
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para avm_web
CREATE DATABASE IF NOT EXISTS `avm_web` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `avm_web`;

-- Volcando estructura para tabla avm_web.prov
CREATE TABLE IF NOT EXISTS `prov` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) DEFAULT NULL,
  `contacto` varchar(200) DEFAULT NULL,
  `telefono` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.prov: ~2 rows (aproximadamente)
DELETE FROM `prov`;
INSERT INTO `prov` (`id`, `nombre`, `contacto`, `telefono`, `email`) VALUES
	(3, 'JC Solutions', 'Johan', '63407668', 'jcamachoc13@gmail.com'),
	(8, 'Ucentral y Asociados', 'Mauricio', '83407676', 'ucentral@ucentral.com');

-- Volcando estructura para tabla avm_web.tbbitacoraproceso
CREATE TABLE IF NOT EXISTS `tbbitacoraproceso` (
  `IDBitacoraCliente` int NOT NULL,
  `TablaProceso` int DEFAULT NULL,
  `FecProceso` datetime DEFAULT NULL,
  `TipProceso` varchar(15) DEFAULT NULL,
  `IdUsuario` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbbitacoraproceso: ~0 rows (aproximadamente)
DELETE FROM `tbbitacoraproceso`;

-- Volcando estructura para tabla avm_web.tbcliente
CREATE TABLE IF NOT EXISTS `tbcliente` (
  `IdCliente` int DEFAULT NULL,
  `NomCliente` varchar(250) DEFAULT NULL,
  `EmailCliente` varchar(250) DEFAULT NULL,
  `TelCliente` varchar(250) DEFAULT NULL,
  `PreferenciasCliente` varchar(1000) DEFAULT NULL,
  `EstCliente` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbcliente: ~0 rows (aproximadamente)
DELETE FROM `tbcliente`;
INSERT INTO `tbcliente` (`IdCliente`, `NomCliente`, `EmailCliente`, `TelCliente`, `PreferenciasCliente`, `EstCliente`) VALUES
	(1, 'Mauricio Rivera Villalobos', 'mrivera@edu.uc.ac.cr', '8899 4044', 'TIBAS', b'1');

-- Volcando estructura para tabla avm_web.tbdetallepaquete
CREATE TABLE IF NOT EXISTS `tbdetallepaquete` (
  `IdDetalle` int NOT NULL,
  `IdPaquete` int DEFAULT NULL,
  `IdServicio` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbdetallepaquete: ~4 rows (aproximadamente)
DELETE FROM `tbdetallepaquete`;
INSERT INTO `tbdetallepaquete` (`IdDetalle`, `IdPaquete`, `IdServicio`) VALUES
	(1, 1, 1),
	(2, 1, 2),
	(3, 1, 3),
	(4, 1, 4);

-- Volcando estructura para tabla avm_web.tbdetallereserva
CREATE TABLE IF NOT EXISTS `tbdetallereserva` (
  `IdDetReserva` int DEFAULT NULL,
  `IdReserva` int DEFAULT NULL,
  `IdPaquete` int DEFAULT NULL,
  `CantDetReserva` int DEFAULT NULL,
  `PrecDetReserva` decimal(18,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbdetallereserva: ~12 rows (aproximadamente)
DELETE FROM `tbdetallereserva`;
INSERT INTO `tbdetallereserva` (`IdDetReserva`, `IdReserva`, `IdPaquete`, `CantDetReserva`, `PrecDetReserva`) VALUES
	(1, 1, 1, 1, 1500.00),
	(2, 1, 5, 1, 2500.00),
	(3, 2, 6, 1, 2500.00),
	(4, 3, 4, 1, 3500.00),
	(5, 4, 1, 1, 1500.00),
	(6, 4, 2, 1, 1500.00),
	(7, 4, 3, 1, 1500.00),
	(8, 4, 4, 1, 1500.00),
	(9, 4, 5, 1, 1500.00),
	(10, 4, 6, 1, 1500.00);

-- Volcando estructura para tabla avm_web.tbexperienciacliente
CREATE TABLE IF NOT EXISTS `tbexperienciacliente` (
  `IdExperiencia` int NOT NULL,
  `IdCliente` int DEFAULT NULL,
  `FecExperiencia` datetime DEFAULT NULL,
  `DscExperiencia` varchar(2500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbexperienciacliente: ~0 rows (aproximadamente)
DELETE FROM `tbexperienciacliente`;

-- Volcando estructura para tabla avm_web.tbfactura
CREATE TABLE IF NOT EXISTS `tbfactura` (
  `IdFactura` int DEFAULT NULL,
  `IdReserva` int DEFAULT NULL,
  `FecFactura` datetime DEFAULT NULL,
  `TotFactura` decimal(18,2) DEFAULT NULL,
  `IdCliente` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbfactura: ~0 rows (aproximadamente)
DELETE FROM `tbfactura`;

-- Volcando estructura para tabla avm_web.tbpaqueteturistico
CREATE TABLE IF NOT EXISTS `tbpaqueteturistico` (
  `IdPaquete` int DEFAULT NULL,
  `NomPaquete` varchar(250) DEFAULT NULL,
  `FecCreacion` datetime DEFAULT NULL,
  `MontPaquete` decimal(18,2) DEFAULT NULL,
  `EstPaquete` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbpaqueteturistico: ~7 rows (aproximadamente)
DELETE FROM `tbpaqueteturistico`;
INSERT INTO `tbpaqueteturistico` (`IdPaquete`, `NomPaquete`, `FecCreacion`, `MontPaquete`, `EstPaquete`) VALUES
	(1, 'Playa Santa Teresa Paraiso del Surf', '2023-05-26 00:00:00', 1500.00, b'1'),
	(3, 'Parque Nacional Manuel Antonio el más Visitado del País', '2024-05-26 00:00:00', 2500.00, b'1'),
	(4, 'Miami de Compras', '2024-05-26 00:00:00', 4500.00, b'1'),
	(5, 'Explora el Salar de Uyuni el desierto salado más grande del mundo', '2024-05-26 00:00:00', 2500.00, b'1'),
	(6, 'Santorini Grecia: la joya del mar Egeo', '2024-05-26 00:00:00', 2500.00, b'1'),
	(12, 'Viaje por Mar egeo y turquia', '2024-08-23 00:00:00', 8888.00, b'1'),
	(2, 'Playa Quesera y Tour de Bioluminicencia', '2024-05-26 00:00:00', 4500.00, b'1');

-- Volcando estructura para tabla avm_web.tbpermisosistema
CREATE TABLE IF NOT EXISTS `tbpermisosistema` (
  `IdRolSistema` int NOT NULL,
  `DscPermisos` varchar(250) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbpermisosistema: ~0 rows (aproximadamente)
DELETE FROM `tbpermisosistema`;

-- Volcando estructura para tabla avm_web.tbproveedor
CREATE TABLE IF NOT EXISTS `tbproveedor` (
  `IdProveedor` int DEFAULT NULL,
  `NomProveedor` varchar(250) DEFAULT NULL,
  `ConProveedor` varchar(250) DEFAULT NULL,
  `TelProveedor` varchar(250) DEFAULT NULL,
  `EmailProveedor` varchar(250) DEFAULT NULL,
  `EstProveedor` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbproveedor: ~0 rows (aproximadamente)
DELETE FROM `tbproveedor`;

-- Volcando estructura para tabla avm_web.tbreserva
CREATE TABLE IF NOT EXISTS `tbreserva` (
  `IdReserva` int DEFAULT NULL,
  `FecReserva` datetime DEFAULT NULL,
  `IdCliente` int DEFAULT NULL,
  `TotReserva` decimal(18,2) DEFAULT NULL,
  `EstReserva` bit(1) DEFAULT NULL,
  `IdUsuario` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbreserva: ~9 rows (aproximadamente)
DELETE FROM `tbreserva`;
INSERT INTO `tbreserva` (`IdReserva`, `FecReserva`, `IdCliente`, `TotReserva`, `EstReserva`, `IdUsuario`) VALUES
	(1, '2024-06-04 00:00:00', 1, 1500.00, b'1', 13),
	(2, '2024-07-04 00:00:00', 1, 2500.00, b'1', 13),
	(3, '2024-08-04 00:00:00', 1, 3500.00, b'1', 13),
	(4, '2024-08-11 00:00:00', 1, 0.00, b'1', 13);

-- Volcando estructura para tabla avm_web.tbrestriccionespaq
CREATE TABLE IF NOT EXISTS `tbrestriccionespaq` (
  `IDRestriccion` int DEFAULT NULL,
  `IDPaquete` int DEFAULT NULL,
  `DscRestriccion` varchar(250) DEFAULT NULL,
  `EstRestriccion` tinyint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbrestriccionespaq: ~7 rows (aproximadamente)
DELETE FROM `tbrestriccionespaq`;
INSERT INTO `tbrestriccionespaq` (`IDRestriccion`, `IDPaquete`, `DscRestriccion`, `EstRestriccion`) VALUES
	(1, 1, 'Válido para redimir del 16/08/24 al 15/11/24. ', 1),
	(2, 1, 'Se puede redimir en días normales. Para los días festivos o feriados sería aplicando el cupón de fin de semana.', 1),
	(3, 1, 'Para ésta oferta se debe adquirir mínimo 2 noches y requiere reservación sujeta a disponibilidad al correo: info@condovac.com . ', 1),
	(4, 1, 'Teléfonos: 4001-1182 / 4001-1116 / 4001-1118 / 4001-1100. ', 1),
	(5, 1, 'Se permiten mascotas bajo reserva (con mínimo 3 días de anticipación) y con un costo adicional de $21 por noche.', 1),
	(6, 1, 'Cancelaciones o cambios sobre la reservación se debe realizar con 8 días de anterioridad o se pierde el derecho de utilizarlo. ', 1),
	(8, 1, 'No se aceptan mascotas', 1);

-- Volcando estructura para tabla avm_web.tbservicio
CREATE TABLE IF NOT EXISTS `tbservicio` (
  `IdServicio` int DEFAULT NULL,
  `IdTipoServicio` int DEFAULT NULL,
  `DesServicio` varchar(250) DEFAULT NULL,
  `PrecioServicio` decimal(18,2) DEFAULT NULL,
  `IDProveedor` int DEFAULT NULL,
  `EstServicio` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbservicio: ~4 rows (aproximadamente)
DELETE FROM `tbservicio`;
INSERT INTO `tbservicio` (`IdServicio`, `IdTipoServicio`, `DesServicio`, `PrecioServicio`, `IDProveedor`, `EstServicio`) VALUES
	(1, 1, 'Hospedaje Cardinal Hotel & Villas', 100.00, 1, b'1'),
	(2, 2, 'Desayuno Incluido', 1000.00, 1, b'1'),
	(3, 3, 'Cena Incluida', 1000.00, 1, b'1'),
	(4, 4, 'Clase de Surf con instructores certificados de la zona', 111.00, 1, b'1');

-- Volcando estructura para tabla avm_web.tbtiposervicio
CREATE TABLE IF NOT EXISTS `tbtiposervicio` (
  `IdTipoServicio` int DEFAULT NULL,
  `DscTipoServicio` varchar(250) DEFAULT NULL,
  `EstTipoServicio` bit(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbtiposervicio: ~0 rows (aproximadamente)
DELETE FROM `tbtiposervicio`;

-- Volcando estructura para tabla avm_web.tbusuario
CREATE TABLE IF NOT EXISTS `tbusuario` (
  `IdUsuario` int DEFAULT NULL,
  `NomUsuario` varchar(250) DEFAULT NULL,
  `FecIngUsuario` datetime DEFAULT NULL,
  `IdRolUsuario` int DEFAULT NULL,
  `EsVendedor` tinyint DEFAULT NULL,
  `EstUsuario` tinyint DEFAULT NULL,
  `DscPassword` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Volcando datos para la tabla avm_web.tbusuario: ~1 rows (aproximadamente)
DELETE FROM `tbusuario`;
INSERT INTO `tbusuario` (`IdUsuario`, `NomUsuario`, `FecIngUsuario`, `IdRolUsuario`, `EsVendedor`, `EstUsuario`, `DscPassword`) VALUES
	(13, 'jcamachoc13', '2024-08-04 21:23:38', 1, 1, 1, '123456');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
