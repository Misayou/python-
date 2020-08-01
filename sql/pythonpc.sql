/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50718
Source Host           : localhost:3306
Source Database       : pythonpc

Target Server Type    : MYSQL
Target Server Version : 50718
File Encoding         : 65001

Date: 2020-08-01 00:20:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `position`
-- ----------------------------
DROP TABLE IF EXISTS `position`;
CREATE TABLE `position` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `positionName` varchar(255) NOT NULL,
  PRIMARY KEY (`id`,`positionName`),
  UNIQUE KEY `pN` (`positionName`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of position
-- ----------------------------

-- ----------------------------
-- Table structure for `positionitem`
-- ----------------------------
DROP TABLE IF EXISTS `positionitem`;
CREATE TABLE `positionitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `positionid` int(11) NOT NULL,
  `positionName` varchar(255) DEFAULT NULL,
  `companySize` varchar(255) DEFAULT NULL,
  `financeStage` varchar(255) DEFAULT NULL,
  `companyLabelList` varchar(255) DEFAULT NULL,
  `firstType` varchar(255) DEFAULT NULL,
  `companyPosition` varchar(255) DEFAULT NULL,
  `salary` varchar(255) DEFAULT NULL,
  `workYear` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `district` varchar(255) DEFAULT NULL,
  `education` varchar(255) DEFAULT NULL,
  `companyFullName` varchar(255) DEFAULT NULL,
  `jobNature` varchar(255) DEFAULT NULL,
  `createTime` varchar(255) DEFAULT NULL,
  `secondType` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `positionid` (`positionid`),
  CONSTRAINT `positionitem_ibfk_1` FOREIGN KEY (`positionid`) REFERENCES `position` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2026 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of positionitem
-- ----------------------------
