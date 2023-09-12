1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat sebuah proyek Django baru
    Pertama-tama saya membuat folder di direktori lokal bernama Tugas 2. Selanjutnya saya membuat repositori baru bernama inventori di github. Lalu saya menginisiasi git di dalam direktori lokal dan menghubungkan kedua direktori tersebut. Kemudian saya membuat virtual environment dengan menjalankan perintah "python -m venv env" dan mengaktifkannya dengan perintah "env\Scripts\activate.bat". Setelah aktif, saya membuat requirements.txt untuk menambahkan dependencies. Setelah itu saya memasangkannya melalui perintah "pip install -r requirements.txt" dengan kondisi environment aktif. Setelah di install, saya membuat proyek saya bernama inventori melalui perintah "django-admin startproject inventori .". Selanjutnya saya mengkonfigurasinya dengan memasukkan "\*" pada ALLOWED_HOSTS di settings.py dan menjalankannya untuk mengecek apakah berfungsi melalui perintah "python manage.py runserver". Setelah itu, saya mematikkan virtual environment dengan perintah "deactivate" untuk membuat folder .gitignore di dalam direktori lokal. Setelah itu, saya melakukan add, commit, dan push dari direktori repositori lokal.

    b. Membuat aplikasi dengan nama main pada proyek tersebut
    Saya membuat main dengan melakukan perintah "python manage.py startapp main" pada cmd dengan path direktori lokal. Hal ini membuat folder baru bernama main di direktori lokal. Selanjutnya saya mendaftarkan main ke dalam proyek dengan memasukkan "main" ke dalam settings.py pada variabel INSTALLED_APPS di direktori proyek. Sehingga aplikasi main sudah terbuat dan terdaftar di proyek inventori.

    c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
    Saya menambahkan fungsi "include" dari django.urls dan "path('', include('main.urls'))" ke dalam urls.py di dalam direktori proyek (inventori). Saya menghapus "main/" dan menggantinya dengan "" karena sebelumnya aplikasi main menunjukkan error. Pada dasarnya routing ini bertujuan untuk dapat mengakses aplikasi main oleh projek dan prambanan web

    d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib (name, amount, description)
    Saya menambahkan
    "
    from django.db import models

    class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    "
    pada models.py di direktori aplikasi main. Models ini berfungsi untuk mengatur dan mengelola data yang dapat kita buat, akses, perbarui, dan hapus serta biasanya berada di belakang tampilan. Models ini dapat berinteraksi langsung dengan database melalui perintah "python manage.py makemigrations" untuk membuat migrasi model dan "python manage.py migrate" untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data. Jika terdapat perubahan dalam model, kita selalu menggunakan kedua perintah tersebut untuk menyimpan perubahan ke dalam database

    e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
    Pertama saya mengisi views.py di direktori aplikasi main dengan
    "
    def show_main(request):
    context = {
    'nameApp': 'Inventori App',
    'name': 'Fauzan',
    'class': 'PBP E',
    }

        return render(request, "main.html", context)

    "
    dan membuat main.html di dalam folder templates pada direktori aplikasi main. main.html saya isi dengan kode
    "
    <h1>{{ nameApp }}</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    "
    Hubungan kedua file tersebut adalah views.py bertugas untuk mengatur http request dan mengembalikkan isi kontennya ke file yang dituju, yakni main.html untuk ditampilkan ke user. Ini diatur pada kode "return render(request, "main.html", context)"

    f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    Saya mengisi urls.py di dalam direktori main dengan
    "
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
    path('', show_main, name='show_main'),
    ]
    "
    Kode tersebut akan membuat URL pada aplikasi main yang menampilkan views.py menggunakan fungsi show_main.

    g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
    Deployment bertujuan untuk menunjukkan hasil kode yang kita buat supaya dapat diakses oleh orang lain. Dalam hal ini, saya menggunakan Adaptable yang mengharuskan untuk connect ke github untuk dapat melakukan deployment. Saya menggunakan Python App Template, database PostgreSQL, dan start command menggunakan "python manage.py migrate && gunicorn adventurers-inventory.wsgi"

2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Saat pengguna mengirimkan request HTTP melalui urls.py, urls.py mengirimkannya ke views.py. views.py akan meminta data ke models.py. Sementara itu, models.py akan mengambil data dari database dan dikirimkan ke views.py. Setelah mendapatkannya, views.py akan mengolahnya untuk ditampilkan ke pengguna. Setelah mengelolanya, data akan dikirim ke html sehingga pengguna dapat melihat requestnya

3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Kita perlu menggunakan virtual environment supaya package serta dependencies dari aplikasi kita dapat diisolasi sehingga tidak bertabrakan dan terpengaruh oleh versi lainnya. Hal ini meminimalisir adanya error yang tidak kita duga. Saya membuat virtual environment dengan perintah "python -m venv env" dan mengaktifkannya dengan perintah "env\Scripts\activate.bat". Sebenarnya, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini merupakan opsi yang harus dihinndari. Karena, tanpa virtual environment, package serta dependencies pada proyek kita dapat bertabrakan dan terpengaruh oleh python global.

4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
    MVC (Model, View, Controller) adalah konsep arsitektur yang digunakan dalam mengembangkan web untuk memisahkan bagian-bagian web menjadi beberapa komponen yang berbeda.
    Model = Komponen yang merepresentasikan pengelolaan sumber data. Tugasnya adalah menerima perintah dari Controller dan mengambil semua data (seusai kebutuhan) dari database atau remote API atau keduanya. Ia saling berinteraksi dengan Controller.
    View = Komponen yang merepresentasikan ui elements untuk menampilkan data yang telah di request oleh user yang diambil dari Model.
    Controller = Komponen yang mengatur interaksi pengguna dengan aplikasi atau web, seperti mouse yang di klik, dll dengan cara mengirimkan perintah ke model yang nanti akan diteruskan ke View.

    MVT (Model, View, Template) adalah konsep arsitektur yang digunakan dalam mengembangkan web dengan framework tertentu untuk memisahkan bagian-bagian aplikasi menjadi beberapa komponen yang berbeda.
    Model = Komponen yang mempresentasikan pengelolaan sumber data. Ia secara langsung berinteraksi dengan database. Selain itu, ia juga menerima perintah dari View berdasarkan request dari user. Jika sudah melakukan operasi pada database, ia akan meneruskannya ke View.
    View = Komponen yang mengatur interaksi pengguna dengan aplikasi atau web. Ia menerima request dari pengguna dan meneruskannya ke Model. Setelah mendapat sesuatu dari Model, ia meneruskannya ke template untuk ditampilkan ke pengguna.
    Template = Komponen yang merepresentasikan ui element dan menampilkan data sesuai perintah yang diteruskan oleh View ke pengguna.

    MVVM (Model, View, ViewModel) adalah konsep arsitektur yang biasanya digunakan dalam mengembangkan aplikasi mobile atau desktop untuk memisahkan bagian-bagian aplikasi menjadi beberapa komponen yang berbeda.
    Model = Komponen yang merepresentasikan pengelolaan sumber data. Tugasnya adalah melakukan operasi semua data (seusai kebutuhan) dari database atau remote API atau keduanya. Ia saling berinteraksi dengan ViewModel.
    View = Komponen yang merepresentasikan ui elements dan mendapatkan event dari ViewModel untuk ditampilkan ke pengguna.
    ViewModel = Komponen yang merepresentasikan business logic. Tugasnya adalah tidak hanya meneruskan data dari model, akan tetapi sebagai pengontrol tampilan bagaimana data tersebut akan ditampilkan ke pengguna. Ia saling berinteraksi dengan ViewModel dan View.

    Perbedaan antara ketiganya:
    MVC = Merupakan arsitektur yang terdiri dari Model, View, Controller. Ia merupakan asritekstur perancangan untuk pengaplikasian web tradisional
    MVT = Merupakan arsitektur yang terdiri dari Model, View, Template. Pada MVT, Template menggantikan View pada MVC. Hal ini dikarenakan MVT dirancang khusus untuk pengembangan web dengan framework tertentu, seperti python yang memungkinkan pemisahan yang lebih jelas antara tampilan dan pemrosesan HTTP
    MVVM = Merupakan arsitektur yang terdiri dari Model, View, ViewModel. Untuk menampilkan data ke user, ia sama seperti MVC menggunakan View, tetapi menggantikan Controller dengan ViewModel. Hal ini disebabkan MVVM dirancang untuk pengembangan aplikasi mobile atau desktop yang berbasis pengguna. Ini memungkinkan ViewModel dapat terus melakukan interaksi dengan Model dalam meneruskan data untuk ditamplikan ke pengguna.
