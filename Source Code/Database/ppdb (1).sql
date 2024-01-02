-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jan 02, 2024 at 11:07 AM
-- Server version: 11.3.0-MariaDB-log
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ppdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `hasil_kuis`
--

CREATE TABLE `hasil_kuis` (
  `id_peserta` int(12) NOT NULL,
  `id_Pendaftaran` int(12) NOT NULL,
  `skor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `hasil_kuis`
--

INSERT INTO `hasil_kuis` (`id_peserta`, `id_Pendaftaran`, `skor`) VALUES
(3, 1, 20),
(4, 4, 30);

--
-- Triggers `hasil_kuis`
--
DELIMITER $$
CREATE TRIGGER `tambah_status_kuis_finish` AFTER INSERT ON `hasil_kuis` FOR EACH ROW BEGIN
    INSERT INTO kuis_sudah_dilakukan (id_pendaftaran) VALUES (NEW.id_Pendaftaran);
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `hasil_puzzle`
--

CREATE TABLE `hasil_puzzle` (
  `id_hasil_puzzle` int(11) NOT NULL,
  `id_peserta` int(11) DEFAULT NULL,
  `skor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `hasil_puzzle`
--

INSERT INTO `hasil_puzzle` (`id_hasil_puzzle`, `id_peserta`, `skor`) VALUES
(1, 3, 732),
(2, 3, 585),
(3, 3, 299);

-- --------------------------------------------------------

--
-- Table structure for table `kuis_sudah_dilakukan`
--

CREATE TABLE `kuis_sudah_dilakukan` (
  `id_pendaftaran` int(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `kuis_sudah_dilakukan`
--

INSERT INTO `kuis_sudah_dilakukan` (`id_pendaftaran`) VALUES
(1),
(4);

-- --------------------------------------------------------

--
-- Table structure for table `pendaftaran`
--

CREATE TABLE `pendaftaran` (
  `id_pendaftaran` int(12) NOT NULL,
  `nama_siswa` varchar(255) NOT NULL,
  `usia` int(3) NOT NULL,
  `nama_ayah` varchar(255) NOT NULL,
  `nama_ibu` varchar(255) NOT NULL,
  `asal_sekolah` varchar(255) NOT NULL,
  `alamat_siswa` text DEFAULT NULL,
  `status_penerimaan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `pendaftaran`
--

INSERT INTO `pendaftaran` (`id_pendaftaran`, `nama_siswa`, `usia`, `nama_ayah`, `nama_ibu`, `asal_sekolah`, `alamat_siswa`, `status_penerimaan`) VALUES
(1, 'Willy Rahma Wijaya', 7, 'Wi', 'Ra', 'TK Dharma Wanita', 'Mojoroto', 'Diterima'),
(2, 'Allvin', 6, 'Al', 'Vin', 'TK Dharma Wanita', 'Tamanan', 'Tidak Diterima'),
(3, 'Apriyanto', 7, 'Ap', 'Ri', 'TK Dharma Wanita', 'Sukorame', 'Diterima'),
(4, 'Nanda', 7, 'Allvin', 'Nuni', 'TK Dharma Wanita', 'Tamanan', 'Diterima');

--
-- Triggers `pendaftaran`
--
DELIMITER $$
CREATE TRIGGER `tambah_status_kuis` AFTER UPDATE ON `pendaftaran` FOR EACH ROW BEGIN
    DECLARE is_exists INT;

    SELECT COUNT(*) INTO is_exists FROM status_kuis WHERE id_pendaftaran = NEW.id_pendaftaran;

    IF NEW.status_penerimaan = 'Diterima' AND is_exists = 0 THEN
        INSERT INTO status_kuis (id_pendaftaran, status_kuis) VALUES (NEW.id_pendaftaran, 'diterima');
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `pertanyaan`
--

CREATE TABLE `pertanyaan` (
  `id_pertanyaan` int(11) NOT NULL,
  `pertanyaan` text DEFAULT NULL,
  `pilihan_a` varchar(255) DEFAULT NULL,
  `pilihan_b` varchar(255) DEFAULT NULL,
  `pilihan_c` varchar(255) DEFAULT NULL,
  `poin` int(11) DEFAULT NULL,
  `jawaban` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `pertanyaan`
--

INSERT INTO `pertanyaan` (`id_pertanyaan`, `pertanyaan`, `pilihan_a`, `pilihan_b`, `pilihan_c`, `poin`, `jawaban`) VALUES
(3, 'Siapa Bapak Koperasi Indonesia?', 'Muhammad Hatta', 'Soekarno', 'Soedirman', 10, 'Muhammad Hatta'),
(4, '1 + 3 = ?', '3', '4', '1', 10, '4'),
(5, '5 + 5 = ?', '12', '10', '11', 10, '10');

-- --------------------------------------------------------

--
-- Table structure for table `status_kuis`
--

CREATE TABLE `status_kuis` (
  `id_status_kuis` int(12) NOT NULL,
  `id_pendaftaran` int(12) NOT NULL,
  `status_kuis` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `status_kuis`
--

INSERT INTO `status_kuis` (`id_status_kuis`, `id_pendaftaran`, `status_kuis`) VALUES
(9, 1, 'diterima'),
(10, 3, 'diterima'),
(11, 4, 'diterima');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hasil_kuis`
--
ALTER TABLE `hasil_kuis`
  ADD PRIMARY KEY (`id_peserta`),
  ADD KEY `id_Pendaftaran` (`id_Pendaftaran`);

--
-- Indexes for table `hasil_puzzle`
--
ALTER TABLE `hasil_puzzle`
  ADD PRIMARY KEY (`id_hasil_puzzle`),
  ADD KEY `id_peserta` (`id_peserta`);

--
-- Indexes for table `kuis_sudah_dilakukan`
--
ALTER TABLE `kuis_sudah_dilakukan`
  ADD KEY `id_pendaftaran` (`id_pendaftaran`);

--
-- Indexes for table `pendaftaran`
--
ALTER TABLE `pendaftaran`
  ADD PRIMARY KEY (`id_pendaftaran`);

--
-- Indexes for table `pertanyaan`
--
ALTER TABLE `pertanyaan`
  ADD PRIMARY KEY (`id_pertanyaan`);

--
-- Indexes for table `status_kuis`
--
ALTER TABLE `status_kuis`
  ADD PRIMARY KEY (`id_status_kuis`),
  ADD KEY `id_pendaftaran` (`id_pendaftaran`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hasil_kuis`
--
ALTER TABLE `hasil_kuis`
  MODIFY `id_peserta` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `hasil_puzzle`
--
ALTER TABLE `hasil_puzzle`
  MODIFY `id_hasil_puzzle` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `pertanyaan`
--
ALTER TABLE `pertanyaan`
  MODIFY `id_pertanyaan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `status_kuis`
--
ALTER TABLE `status_kuis`
  MODIFY `id_status_kuis` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hasil_kuis`
--
ALTER TABLE `hasil_kuis`
  ADD CONSTRAINT `hasil_kuis_ibfk_1` FOREIGN KEY (`id_Pendaftaran`) REFERENCES `pendaftaran` (`id_pendaftaran`);

--
-- Constraints for table `hasil_puzzle`
--
ALTER TABLE `hasil_puzzle`
  ADD CONSTRAINT `hasil_puzzle_ibfk_1` FOREIGN KEY (`id_peserta`) REFERENCES `pendaftaran` (`id_pendaftaran`);

--
-- Constraints for table `kuis_sudah_dilakukan`
--
ALTER TABLE `kuis_sudah_dilakukan`
  ADD CONSTRAINT `kuis_sudah_dilakukan_ibfk_1` FOREIGN KEY (`id_pendaftaran`) REFERENCES `pendaftaran` (`id_pendaftaran`);

--
-- Constraints for table `status_kuis`
--
ALTER TABLE `status_kuis`
  ADD CONSTRAINT `status_kuis_ibfk_1` FOREIGN KEY (`id_pendaftaran`) REFERENCES `pendaftaran` (`id_pendaftaran`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
