-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: dream_holidays
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `countries` (
  `con_id` int(11) NOT NULL AUTO_INCREMENT,
  `country_name` varchar(50) DEFAULT NULL,
  `cid` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`con_id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'France','5'),(2,'India','3'),(3,'Uganda','1'),(4,'Kazakhstan','3'),(5,'China','3'),(6,'Japan','3'),(7,'Republic of Korea ','3'),(8,'Bhutan ','3'),(9,'Sri Lanka','3'),(10,'Indonesia','3'),(11,'Thailand','3'),(12,'Vietnam','3'),(13,'Bahrain','3'),(14,'Jordan','3'),(15,'United Arab Emirates','3'),(16,'Saudi Arabia','3'),(17,'Qatar','3'),(18,'Oman','3'),(19,'Germany','5'),(20,'Portugal','5'),(21,'Spain','5'),(22,'Belgium','5'),(23,'Finland','5'),(24,'Italy','5'),(25,'Netherlands','5'),(26,'United Kingdom','5'),(27,'Nigeria','1'),(28,'Egypt','1'),(29,'South Africa','1'),(30,'Kenya','1'),(31,'Morocco','1'),(32,'Mozambique','1'),(33,'Madagascar','1'),(34,'Zambia','1'),(35,'Rwanda','1'),(36,'Botswana','1'),(37,'Seychelles','1'),(38,'Australia','4'),(39,'Antartica','2'),(40,'New Zealand','4'),(41,'Fiji','4'),(42,'United States of America','6'),(43,'Canada','6'),(44,'Puerto Rico','6'),(45,'Mexico','6'),(46,'Dominican Republic','6'),(47,'Cuba','6'),(48,'Costa Rica','6'),(49,'Trinidad and Tobago','6'),(50,'Brazil','7'),(51,'Colombia','7'),(52,'Argentina','7'),(53,'Peru','7'),(54,'Venezuela','7'),(55,'Chile','7'),(56,'Ecuador','7'),(57,'Uruguay','7');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-09 12:14:45
