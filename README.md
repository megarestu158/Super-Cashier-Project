# *Super-Cashier-Project*

## *Backround Project*</br>
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan ekspansi bisnis, yaitu: Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukan item yang dibeli, jumlah yang dibeli dan fitur lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut.</br>

## *Tools*
### Bahasa Pemrograman:</br>
*   Python

### *Library*

*   Pandas
*   Numpy
*   Tabulate

## Requirements / Objectives
### Tujuan Program:
* Membuat objek dari class `Transaction()`
* Menambahkan method `add_item()` yang berisi parameter item_name, item_quantity, dan item_price ke dalam Super Cashier
* Menambahkan method `update_item_name()`, `update_item_quantity()`, dan `update_item_price()`. Mengubah berdasarkan parameter nama_item untuk mengubah nilai tiap-tiap item, jumlah, dan harga ke dalam Super Cashier.
* Menambahkan method `delete_item()` ke dalam Super Cashier untuk menghapus satu item berdasarkan parameter item_name
* Menambahkan method `reset_transaction()` ke dalam Super Cashier untuk menghapus semua transaksi
* Menambahkan method `check_order()` ke dalam Super Cashier untuk melihat seluruh detail transaksi
* Menambahkan method `total_price()` ke dalam Super Cashier untuk mengetahui total pembayaran, dengan beberapa ketentuan:
  * Jika total belanja di atas Rp.200.000 maka akan mendapatkan diskon 5%
  * Jika total belanja di atas Rp.300.000 maka akan mendapatkan diskon 8%
  * Jika total belanja di atas Rp.500.000 maka akan mendapatkan diskon 10%.

## *Flowchart*
![image](https://user-images.githubusercontent.com/54011659/218351463-29881488-8c5f-4335-b467-9d74e19ef92d.png)

Secara singkat proses seorang customer dalam melakukan pembelanjaan pertama kali adalah dengan menginputkan item apa saja yang ingin dibeli dengan menggunakan method `add_item` dengan input parameter item_name, item_quantity dan item_price. Selanjutnya untuk mengecek apakah pesanannya sudah sesuai customer dapat melihat seluruh daftar belanja dengan menggunakan method `check_orders`. Jika customer salah memasukan salah satu dari parameter tersebut maka customer dapat merubah nilainya dengan menggunakan method `update` dengan input parameter item_name dan parameter apa yang ingin dirubah. Apabila customer ingin membatalkan salah satu transaksi maka dapat menggunakan method `delete_item`. Jika customer ingin mereset list order atau ingin mengulang input list belanjaanya maka customer dapat menggunakan method `reset_transaction`. Setelah customer selesai menginput ulang dan dirasa yakin dengan list ordernya maka customer dapat mengetahui total belanja menggunakan method `total_price`. 
