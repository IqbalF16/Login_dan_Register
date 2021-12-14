/*
SQLyog Enterprise - MySQL GUI v5.01
Host - 5.5.16 : Database - py_iqbal
*********************************************************************
Server version : 5.5.16
*/


create database if not exists `py_iqbal`;

USE `py_iqbal`;

/*Table structure for table `penjualan` */

DROP TABLE IF EXISTS `penjualan`;

CREATE TABLE `penjualan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `barang` varchar(200) DEFAULT NULL,
  `harga_jual` int(200) DEFAULT NULL,
  `stok` int(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `penjualan` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `username` varchar(200) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert into `user` values 
(1,'iqbal','iqbal','1'),
(2,'aguez','agus','12'),
(3,'reiner','re','123'),
(4,'awa','awa','awa');
