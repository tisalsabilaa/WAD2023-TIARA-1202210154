<?php 

// (1) Hapus cookie dengan key id 
setcookie("id", '', time() - 3600, "/JURNAL%20MODUL%204/views");
// 

// (2) Mulai session
session_start();
//

// (3) Hapus semua session yang berlangsung
session_destroy();
//

// (4) Lakukan redirect ke halaman login awal
header ('Location : ../views/login.php');
//

exit;

?>