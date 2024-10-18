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
-- Table structure for table `packages`
--

DROP TABLE IF EXISTS `packages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `packages` (
  `pid` mediumint(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  `price` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `packages`
--

LOCK TABLES `packages` WRITE;
/*!40000 ALTER TABLE `packages` DISABLE KEYS */;
INSERT INTO `packages` VALUES (1,'PARIS Tour','A 5 day 4 night trip in which you can immerse yourself in the beauty of Paris and is attractions you can see spectacluar views of the paris skyline from The Eiffel Tower, look at archetectual marvel of The Arc de Thrombe and visit the world renowned Musse du Louvre showcasing the Mona Lisa by Leonardo da Vinci, Relive your childhood by visiting the Diseneyland.All accomodation,travel and meals are inclusive','5 days','2,50,000 Rs'),(2,'Andaman and Nicobar Tour','A 3 day 2 nights trip that will let you experience the serene beaches of bay of Bengal and let you have an umforgetable experience of scuba diving relaxing in the finest of resorts it has to offer, boating to a uninhabited islands and paragliding. All accomodation,travel and meals are inclusive','3 days and 2 nights','1,20,000 Rs'),(3,'Golden Triangle Tour','Embark on a classic Indian adventure with the Golden Triangle Tour, covering Delhi, Agra, and Jaipur. Explore Delhi’s bustling streets and historical monuments, witness the majestic Taj Mahal in Agra, and marvel at the royal palaces and forts of Jaipur. This tour offers a captivating glimpse into India\'s rich history, culture, and architecture.','5 days 4 nights','3,00,000 Rs'),(4,'French Riviera Tour','Bask in the glamour and beauty of the French Riviera with this stunning coastal tour. Explore glamorous cities like Nice, Cannes, and Monaco, enjoy the azure waters of the Mediterranean, and stroll along luxurious promenades. This tour offers a blend of sophistication, relaxation, and breathtaking sea views.','4 days and 3 nights','6,00,000 Rs'),(5,'Kerala Backwaters Serenity','Experience the tranquil beauty of Kerala with this 5-day tour that highlights the state\'s enchanting landscapes. Start in Kochi, exploring its historic Fort Kochi area and the lively spice markets. Head to Munnar, where lush tea plantations and misty hills offer a serene escape. Finally, unwind with a houseboat cruise through the serene backwaters of Alleppey, gliding past traditional Kerala villages and verdant landscapes. This tour is perfect for those seeking relaxation amidst nature\'s splendor.',' 5 Days','2,00,000 Rs'),(6,'Rajasthan Royalty Journey','Dive into the regal heritage of Rajasthan with this 10-day journey through its royal cities. Begin in Udaipur, known as the City of Lakes, and explore the stunning Lake Palace and City Palace. Continue to Jaisalmer, the Golden City, with its intricate sandstone architecture and the grand Jaisalmer Fort. In Jodhpur, visit the imposing Mehrangarh Fort and the bustling Sardar Market. Finally, enjoy the vibrant charm of Jaipur with its majestic palaces and forts. This tour is a majestic celebration of Rajasthan\'s opulent past and colorful present.','10 Days','3,00,000 Rs'),(7,'Himalayan Adventure Expedition','Embark on an exhilarating journey through the Himalayan region with this 8-day adventure tour. Begin in Shimla, the charming colonial hill station with its scenic vistas and historic landmarks. Move on to Manali, where you can explore the Solang Valley and Rohtang Pass for stunning views and thrilling activities. Conclude your trip in Dharamshala, home to the Dalai Lama and surrounded by serene landscapes and Tibetan culture. This tour is perfect for adventure seekers and nature enthusiasts looking to experience the majestic Himalayas.','8 Days','3,00,000 Rs'),(8,'South India Cultural Odyssey','Delve into the rich cultural tapestry of South India with this comprehensive 8-day tour. Begin in Chennai, where you\'ll explore the historic Fort St. George and the beautiful Marina Beach. Travel to Mahabalipuram to admire the ancient rock-cut temples and sculptures. In Pondicherry, experience the charming French colonial architecture and vibrant café culture. Visit Madurai to marvel at the grand Meenakshi Temple, and conclude your journey in Coimbatore, known for its textile industry and serene surroundings. This tour offers a deep dive into the region’s historical and cultural highlights.','8 Days','2,00,000 Rs'),(9,' Classic Safari Adventure in Kenya ','Embark on a classic African safari with this 12-day adventure through Kenya. Start in Nairobi with a visit to the Giraffe Centre and the David Sheldrick Wildlife Trust. Journey into the Maasai Mara for thrilling game drives in search of the Big Five and witness the Great Migration (seasonal). Cross into Tanzania to explore the vast Serengeti plains and the stunning Ngorongoro Crater, home to incredible wildlife and breathtaking landscapes. Conclude your journey with relaxation on the idyllic beaches of Zanzibar, where you can unwind and soak up the sun. This tour is perfect for wildlife enthusiasts and those seeking a quintessential safari experience.','12 Days','6,00,000 Rs'),(10,'South Africa Highlights and Cape Winelands','Discover the diverse wonders of South Africa with this 10-day tour. Start in Cape Town, exploring the iconic Table Mountain, the vibrant V&A Waterfront, and the scenic Cape Peninsula. Enjoy a day of wine tasting and gourmet dining in Stellenbosch, renowned for its world-class vineyards. Experience thrilling safaris in Kruger National Park, where you’ll have the chance to spot a variety of wildlife including the Big Five. Conclude your journey in Johannesburg, with visits to Soweto and the Apartheid Museum, offering insights into South Africa\'s rich history and culture.','10 Days','5,00,000 Rs'),(11,'Egyptian Wonders and Nile Cruise','Uncover the ancient mysteries of Egypt with this 8-day tour. Begin in Cairo, where you\'ll marvel at the Great Pyramids of Giza, the Sphinx, and the Egyptian Museum. Embark on a luxurious Nile River cruise from Luxor to Aswan, exploring remarkable sites such as the Valley of the Kings, Karnak Temple, and the stunning temples of Abu Simbel. Enjoy onboard amenities and guided excursions as you sail along one of the world\'s most famous rivers. This tour offers a captivating blend of historical exploration and relaxing river cruising.','8 Days','4,00,000 Rs');
/*!40000 ALTER TABLE `packages` ENABLE KEYS */;
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
