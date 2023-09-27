Nama = Mohammad Fauzan Aditya NPM = 2206827831 Kelas = PBP E

PERTANYAAN TUGAS 4

1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
   Django UserCreationForm merupakan struktur formulir yang disediakan oleh django melalui `django.contrib.auth.forms`. Form ini berfungsi untuk user register di web django yang mengandung field username, 2 password, dan satu email.
   Kelebihan:

   - Mudah digunakan = django sudah membantu developer untuk dapat memastikan bahwa inputan user valid atau tidak
   - Terintegrasi dengan django authentication = Data pengguna dapat secara otomatis diproses dan disimpan ke dalam database

   Kekurangan:

   - Tampilan kaku = Untuk membuat tampilan web yang lebih cakep, user memodifikasinya sendiri dan django hanya menyediakan tampilan yang sederhana
   - Kustomisasi terbatas = UserCreationForm hanya memiliki 4 fields dan terbatas

2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
   Autentikasi berfungsi untuk mengecek/memvalidasi apakah user yang akan login merupakan user yang tepat berdasarkan username dan passwordnya. Sementara itu, otorisasi berfungsi untuk mengatur/memberikan hak-hak pengguna setelah melalui tahap autentikasi berdasarkan rolenya untuk dapat melakukan sesuatu pada sebuah web. Keduanya berbeda, tetapi sangat penting bagi sebuah web karena dapat melindungi user dari kejahatan pencurian data, masalah privasi data, dan pembatasan kewenangan user supaya tidak dapat melangkah lebih jauh yang nantinya dapat merusak web itu sendiri maupun tindakan-tindakan yang beresiko.

3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
   Cookies adalah bagian terkecil dari suatu informasi yang dikirim oleh server ke browser dan dikirim dari browser ke server pada permintaan halaman berikutnya. Cookies berfungsi untuk authentication, user tracking, maintaining user preferences. Dalam mengelola cookies ini, django memiliki kode yang khusus untuk membuat cookies dan menambahkannya ke dalam response, yaitu `response.set_cookie('last_login', str(datetime.datetime.now()))`. Selain itu, untuk dapat menampilkan ke halaman web yang menginformasikan siapa yang sedang login, django memberikan alternative, seperti perintah `'last_login': request.COOKIES['last_login'],` yang nantinya dikirim ke tampilan html. Kemudian, ketika user mengakhiri sesinya di web, django memnggunakan perintah `response.delete_cookie('last_login')` yang berfungsi untuk menghapus cookie dari web browser.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
   Cookies secara default adalah aman. Hal ini karena cookies pada dasarnya adalah data yang berbentuk dictionary bukan program data, tidak mengandung informasi personal, dan tidak dapat menghapus atau membaca informasi dari komputer user. Namun, cookies juga dapat berpotensi untuk digunakan sebagai "vektor" dalam melakukan tindak berbahaya, seperti menyisipkan kode berbahaya ke dalam web yang dimana cookies menyimpan data sesi pengguna. Hal ini akan menimbulkan penyerangan cookies sehingga sesi pengguna dapat diakses oleh orang yang menyisipkan kode

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   a. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
   a.1. Fungsi Registrasi.
   Pertama-tama saya mengimpor redirect, UserCreationForm, dan messages, dengan memasukkan kode `from django.shortcuts import redirect`, `from django.contrib.auth.forms import UserCreationForm`, dan `from django.contrib import messages` pada bagian paling atas di views.py. Kemudian, saya membuat fungsi baru di views.py bernama register untuk memungkinkan user dapat membuat akun barunya. Berikut fungsi registernya,

   ```
   def register(request):
       form = UserCreationForm()

       if request.method == "POST":
           form = UserCreationForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, 'Your account has been successfully created!')
               return redirect('main:login')
       context = {'form':form}
       return render(request, 'register.html', context)
   ```

   Kemudian saya membuat berkas register.html di folder main/templates sebagai tampilan web ketika user ingin membuat akun. Berikut kodenya,

   ```
   {% extends 'base.html' %}

   {% block meta %}
       <title>Register</title>
   {% endblock meta %}

   {% block content %}

   <div class = "login">

       <h1>Register</h1>

           <form method="POST" >
               {% csrf_token %}
               <table>
                   {{ form.as_table }}
                   <tr>
                       <td></td>
                       <td><input type="submit" name="submit" value="Daftar"/></td>
                   </tr>
               </table>
           </form>

       {% if messages %}
           <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
                   {% endfor %}
           </ul>
       {% endif %}

   </div>

   {% endblock content %}
   ```

   Selanjutnya saya menambahkan url fungsi register, `path('register/', register, name='register')`, yang telah dibuat ke dalam urlpatterns pada urls.py yang ada di folder main. Hal ini berfungsi untuk mengenali fungsi register kepada perintah user. Tetapi sebelumnya saya mengimport fungsi registernya terlebih dahulu dari main.views.

   a.2. Fungsi Login.
   Pertama-tama saya mengimpor authenticate dan login dengan memasukkan kode `from django.contrib.auth import authenticate, login` pada bagian paling atas di views.py. Kemudian, saya membuat fungsi baru di views.py bernama login_user untuk memungkinkan user dapat masuk melalui akun yang telah dipunya. Berikut fungsi login_user,

   ```
   def login_user(request):
       if request.method == 'POST':
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('main:show_main')
           else:
               messages.info(request, 'Sorry, incorrect username or password. Please try again.')
       context = {}
       return render(request, 'login.html', context)
   ```

   Kemudian saya membuat berkas login.html di folder main/templates sebagai tampilan web ketika user ingin masuk melalui akun yang telah dipunya. Berikut kodenya,

   ```
   {% extends 'base.html' %}

   {% block meta %}
       <title>Login</title>
   {% endblock meta %}

   {% block content %}

   <div class = "login">

       <h1>Login</h1>

       <form method="POST" action="">
           {% csrf_token %}
           <table>
               <tr>
                   <td>Username: </td>
                   <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
               </tr>

               <tr>
                   <td>Password: </td>
                   <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
               </tr>

               <tr>
                   <td></td>
                   <td><input class="btn login_btn" type="submit" value="Login"></td>
               </tr>
           </table>
       </form>

       {% if messages %}
           <ul>
               {% for message in messages %}
                   <li>{{ message }}</li>
               {% endfor %}
           </ul>
       {% endif %}

       Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

   </div>

   {% endblock content %}
   ```

   Selanjutnya saya menambahkan url fungsi login_user, `path('login/', login_user, name='login')`, yang telah dibuat ke dalam urlpatterns pada urls.py yang ada di folder main. Hal ini berfungsi untuk mengenali fungsi login_user kepada perintah user. Tetapi sebelumnya saya mengimport fungsi login_usernya terlebih dahulu dari main.views.

   a.3 Fungsi Logout.
   Pertama-tama saya mengimpor logout dengan memasukkan kode `from django.contrib.auth import logout` pada bagian paling atas di views.py. Kemudian, saya membuat fungsi baru di views.py bernama logout_user untuk memungkinkan user dapat keluar dari akun webnya. Berikut fungsi logout_user,

   ```
   def logout_user(request):
       logout(request)
       return redirect('main:login')
   ```

   Kemudian saya menambahkan sedikit tombol logout pada berkas main.html melalui kode berikut,

   ```
   <a href="{% url 'main:logout' %}">
       <button>
           Logout
       </button>
   </a>
   ```

   Kode tersebut mengarahkan perintah user, setelah user menekan tombol logout, ke fungsi logout_user yang telah dibuat sebelumnya melalui perantara url yang akan kita buat setelah ini. Kita membuat urlnya dengan menambahkan url fungsi logout_user, `path('logout/', logout_user, name='logout'),`, yang telah dibuat ke dalam urlpatterns pada urls.py yang ada di folder main. Tetapi sebelumnya saya mengimport fungsi logout_usernya terlebih dahulu dari main.views.

   b. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
   Akun 1
   Nama = meimei
   password = temennyamail
   ![Screenshot (1190)](https://github.com/mohammadfauzan21/inventori/assets/110477943/e2705c91-5a14-42b6-9151-ff3420f92325)

   Akun 2
   Nama = mail
   password = temennyameimei
   ![Screenshot (1189)](https://github.com/mohammadfauzan21/inventori/assets/110477943/c5a33686-81b2-42b6-8737-18121b760aa3)

   c. Menghubungkan model Item dengan User.
   Pertama-tama saya akan menambahkan suatu kode untuk membuat sebuah relationship antara satu produk dengan satu user dengan memasukkan kode berikut ke model Product yang telah dibuat sebelumnya,

   ```
   class Product(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE)
       ...
   ```

   Akan tetapi, sebelum menambahkannya, saya telah mengimport user dari django.contrib.auth.models. Kemudian saya mengubah kode pada fungsi create_product supaya django tidak menyimpan secara otomatis hasil dari inputan user. Berikut kodenya,

   ```
   def create_product(request):
       form = ProductForm(request.POST or None)

       if form.is_valid() and request.method == "POST":
           product = form.save(commit=False)
           product.user = request.user
           product.save()
           return HttpResponseRedirect(reverse('main:show_main'))
       ...
   ```

   Hal tersebut berguna untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Karena kita telah merubah model product kita, maka kita harus untuk melakukan migrate supaya model databasenya sesuai dengan yang terkini dengan melakukan perintah `python manage.py makemigrations` dan memasukkan 1 dua kali secara bertahap setelah itu dan dilanjutkan `python manage.py migrate` pada terminal yang sudah diaktifkan envnya.

   d. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
   Untuk dapat menampilkan username pengguna yang sedang logged in pada halaman main, kita harus mengubah fungsi show_main pada views.py. Berikut kodenya,

   ```
   def show_main(request):
       products = Product.objects.filter(user=request.user)

       context = {
           'name': request.user.username,
       ...
       }
   ...
   ```

   Kemudian, sebelum kita menerapkan cookies seperti last login pada halaman utama aplikasi kita harus membuat cookiesnya terlebih dahulu dengan mengubah fungsi login_user di views.py pada blok ifnya menjadi seperti berikut,

   ```
   ...
   if user is not None:
       login(request, user)
       response = HttpResponseRedirect(reverse("main:show_main"))
       response.set_cookie('last_login', str(datetime.datetime.now()))
       return response
   ...
   ```

   `response.set_cookie('last_login', str(datetime.datetime.now()))` akan membuat cookies last login dan menambahkannya ke dalam response. Untuk dapat menampilkannya ke main.html, kita harus menambahkan `'last_login': request.COOKIES['last_login']` dibagian context pada show_main. Tidak hanya itu, kita juga perlu untuk menambahkan `<h5>Sesi terakhir login: {{ last_login }}</h5>` supaya halaman mainnya benar benar dapat menampilkan waktu last loginnya.
   Untuk memastikan cookies tersebut dihapus dengan benar, kita bisa mengubah fungsi logout_user menjadi seperti berikut,

   ```
   def logout_user(request):
       logout(request)
       response = HttpResponseRedirect(reverse('main:login'))
       response.delete_cookie('last_login')
       return response
   ```

   `response.delete_cookie('last_login')` akan menghapus cookie last_login saat pengguna melakukan logout.

   e. Melakukan add-commit-push ke GitHub.
   Saya memasukkan perintah git add . pada cmd path folder tugas saya. Kemudian saya melihat status dengan perintah git status. Selanjutnya saya membuat commit dengan perintah git commit -m "Menyelesaikan tugas 4" dan mempushnya dengan branch yang berbeda dan me-mergenya ke branch main.

===========================================================================================================================

PERTANYAAN TUGAS 3

1. Apa perbedaan antara form POST dan form GET dalam Django?
   Form POST 1. Pengambilan variablenya dari request.POST 2. Di script htmlnya ada method = POST root elementnya 3. Sebagian besar digunakan untuk input data melalui form 4. Bertujuan untuk mengirimkan data yang penting 5. Tidak dibatasi panjang string 6. Nilai variable tidak ditampilkan di urlnya sehingga langsung disimpan ke action

   Form GET 1. Pengambilan variablenya dari request.GET 2. Di script htmlnya ada method = GET pada bagian root elementnya 3. Sebagian besar digunakan untuk input data melalui link 4. Bertujuan untuk mengirimkan data yang tidak penting 5. Panjang string hanya sampai 2047 karakter 6. Nilai variable ditampilkan di urlnya yang kemudian disimpan oleh action

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data adalah XML menggunakan konsep struktur pohon untuk menyimpan data dan menyajikan informasinya. Sementara itu, JSON menggunakan konsep pasangan key-value untuk membuat struktur seperti peta. Dimana setiap value memiliki key tersendiri sehingga untuk melihat value tertentu, kita dapat memanggil keynya saja. Lain halnya dengan HTML. HTML tidak dirancang khusus untuk pengiriman data. HTML biasanya digunakan sebagai kerangka/pondasi dalam membangun sebuah web. HTML memiliki konsep yang sama dengan XML, yakni konsep struktur pohon. Namun, apabila HTML digunakan dalam konteks pengiriman data, HTML bisa digunakan untuk web scraping untuk mengekstrak data dari halaman web yang ada.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   Karena JSON sangat mudah dibaca dan dipahami. Dengan adanya konsep pasangan key-value, membuat JSON menjadi sangat sederhana. Hal ini juga membuat pertukaran data yang terjadi menjadi lebih cepat, efisien, dan dapat di generate langsung oleh computer

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
   a. Membuat input form untuk menambahkan objek model pada app sebelumnya.
   Input form berfungsi untuk menerima input data produk baru melalui struktur form yang telah dibuat melalui forms.py. Pertama-tama saya membuat berkas forms.py pada direktori main. Kemudian saya mengisi berkas tersebut dengan kode berikut,

   ```
   from django.forms import ModelForm
   from main.models import Product

   class ProductForm(ModelForm):
       class Meta:
       model = Product
       fields = ["name", "amount", "description", "price"]
   ```

   class tersebut berfungsi untuk menunjukkan model yang digunakan untuk form yang dimana ketika user menekan tombol untuk menyimpan, maka data yang dikirimkan akan disimpan menjadi sebuah object product. Selain itu, class itu juga menunjukkan field dari mode product yang digunakan untuk form yang sesuai dengan yang ada di models.py. Kemudian saya menambahkan `from django.http import HttpResponseRedirect` , `from main.forms import ProductForm` , `from django.urls import reverse` pada berkas views.py yang ada di direktori main. Di views.py juga, saya membuat sebuah fungsi baru create_product yang menerima parameter request. Berikut kodenya,

   ```
   def create_product(request):
       form = ProductForm(request.POST or None)
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
       context = {'form': form}
       return render(request, "create_product.html", context)
   ```

   Intinya, fungsi tersebut berfungsi untuk memvalidasi input user menggunakan fungsi ProductForm yang telah dibuat dan untuk menyimpan data tersebut. Selain itu, create_product merender isi object 'form' ke create_product.html. Tidak hanya itu, saya mengubah fungsi show_main pada berkas yang sama, yakni views.py supaya dapat mengambil seluruh object Product yang tersimpan pada database dan memasukkannya ke dalam dict context dengan key products supaya dapat di render ke main.html. Supaya dapat mengakses fungsi-fungsi tersebut, saya melakukan import fungsi tersebut pada urls.py di folder main dan menambahkan `path url path('create-product', create_product, name='create_product'),` untuk fungsi create_product. Kemudian, saya membuat berkas create_product.html pada direktori main/templates yang intinya menampilkan fields form yang sudah dibuat pada forms.py sebagai table dan membuat tombol submit untuk mengirimkan request ke view create_product(request). Berikut kode yang saya tambahkan pada berkas tersebut,

   ```
   {% extends 'base.html' %}

   {% block content %}
   <h1>Add New Product</h1>

   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>

   {% endblock %}
   ```

   b. Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
   b.1. Format HTML Saya membuat fungsi baru pada views.py di folder main bernama create_product yang menerima parameter request. Fungsi tersebut berfungsi untuk memvalidasi input user menggunakan fungsi ProductForm yang telah dibuat dan untuk menyimpan data tersebut. Selain itu, create_product merender isi object 'form' pada create_product.html yang nantinya akan menampilkan fields form yang sudah dibuat pada forms.py sebagai table dan membuat tombol submit untuk mengirimkan request ke view create_product(request). Berikut kodenya,

   ```
   def create_product(request):
       form = ProductForm(request.POST or None)
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))

       context = {'form': form}
       return render(request, "create_product.html", context)
   ```

   b.2. Format XML Pertama-tama saya menambahkan from django.http import HttpResponse dan from django.core import serializers pada views.py pada folder main di paling atas. Kemudian. saya menambahkan kode berikut,

   ```
   def show_xml(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

   Fungsi tersebut berfungsi untuk menerima parameter request, menyimpan hasil query dari seluruh data yang ada pada Product di variable data, dan mengembalikkan HttpResponse yang berisi data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".

   b.3. Format JSON saat `from django.http import HttpResponse` dan `from django.core import serializers` pada views.py di folder main sudah berada paling atas, saya menambahkan kode berikut,

   ```
   def show_json(request):
       data = Product.objects.all()
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

   Fungsi tersebut berfungsi untuk menerima parameter request, menyimpan hasil query dari seluruh data yang ada pada Product di variable data, dan mengembalikkan HttpResponse yang berisi data hasil query yang sudah diserialisasi menjadi json dan parameter content_type="application/json".

   b.4. Format XML by ID Pada bagian ini, saya menambahkan kode berikut,

   ```
   def show_xml_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
   ```

   Fungsi tersebut berfungsi untuk menerima parameter request dan id, menyimpan hasil query dari sebagian data yang ada berdasarkan pknya pada Product di variable data, dan mengembalikkan HttpResponse yang berisi data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml".

   b.5. Format JSON by ID Pada bagian ini, saya menambahkan kode berikut,

   ```
   def show_json_by_id(request, id):
       data = Product.objects.filter(pk=id)
       return HttpResponse(serializers.serialize("json", data), content_type="application/json")
   ```

   Fungsi tersebut berfungsi untuk menerima parameter request dan id, menyimpan hasil query dari sebagian data yang ada berdasarkan pknya pada Product di variable data, dan mengembalikkan HttpResponse yang berisi data hasil query yang sudah diserialisasi menjadi json dan parameter content_type="application/json".

   c. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. Saya menambahkan/menganti import yang berada paling atas di urls.py pada folder main menjadi `from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id`. Kemudian, saya menambahkan `path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'), path('json/<int:id>/', show_json_by_id, name='show_json_by_id')`, pada urlpatterns di berkas yang sama supaya fungsi yang sudah diimpor tadi bisa diakses.

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
   Pertama-tama saya membuka postman. Kemudian, saya mengaktifkan env pada cmd path folder tugasnya dengan env\Scripts\activate.bat dan menjalankannya dengan python manage.py runserver. Selanjutnya, saya meng-copy url lokal host saya dan memasukannya ke postman di bagian GET. Untuk mengakses create-product, saya menambahkan create-product pada akhir urlnya. Untuk mengakses xml, saya menambahkan xml pada akhir urlnya. Begitu juga dengan json. Tidak hanya itu, jika saya ingin mengakses data xml yang saya inginkan, saya menambahkan xml/1 pada url tersebut. Begitu juga dengan json.

  ![Screenshot (1154)](https://github.com/mohammadfauzan21/inventori/assets/110477943/143efa51-fb9b-4ca8-9985-563548138a04)
  ![Screenshot (1155)](https://github.com/mohammadfauzan21/inventori/assets/110477943/1f32d771-d634-41db-b89e-5e40b1194627)
  ![Screenshot (1156)](https://github.com/mohammadfauzan21/inventori/assets/110477943/7fa356e5-1e53-48a3-acdf-40c8226fbec5)
  ![Screenshot (1157)](https://github.com/mohammadfauzan21/inventori/assets/110477943/5f5197f8-801d-4279-bb4a-7d30fe9bb24d)
  ![Screenshot (1158)](https://github.com/mohammadfauzan21/inventori/assets/110477943/068a3907-b996-4aa1-91b3-2557930367e2)

7. Melakukan add-commit-push ke GitHub.
   Saya memasukkan perintah git add . pada cmd path folder tugas saya. Kemudian saya melihat status dengan perintah git status. Selanjutnya saya membuat commit dengan perintah git commit -m "Menyelesaikan tugas 3" dan mempushnya dengan git push -f origin main

===========================================================================================================================

PERTANYAAN TUGAS 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   a. Membuat sebuah proyek Django baru
   Pertama-tama saya membuat folder di direktori lokal bernama Tugas 2. Selanjutnya saya membuat repositori baru bernama inventori di github. Lalu saya menginisiasi git di dalam direktori lokal dan menghubungkan kedua direktori tersebut. Kemudian saya membuat virtual environment dengan menjalankan perintah `python -m venv env` dan mengaktifkannya dengan perintah `env\Scripts\activate.bat`. Setelah aktif, saya membuat requirements.txt untuk menambahkan dependencies. Setelah itu saya memasangkannya melalui perintah `pip install -r requirements.txt` dengan kondisi environment aktif. Setelah di install, saya membuat proyek saya bernama inventori melalui perintah `django-admin startproject inventori .`. Selanjutnya saya mengkonfigurasinya dengan memasukkan "\*" pada ALLOWED_HOSTS di settings.py dan menjalankannya untuk mengecek apakah berfungsi melalui perintah `python manage.py runserver`. Setelah itu, saya mematikkan virtual environment dengan perintah "deactivate" untuk membuat folder .gitignore di dalam direktori lokal. Setelah itu, saya melakukan add, commit, dan push dari direktori repositori lokal.

   b. Membuat aplikasi dengan nama main pada proyek tersebut
   Saya membuat main dengan melakukan perintah `python manage.py startapp main` pada cmd dengan path direktori lokal. Hal ini membuat folder baru bernama main di direktori lokal. Selanjutnya saya mendaftarkan main ke dalam proyek dengan memasukkan "main" ke dalam settings.py pada variabel INSTALLED_APPS di direktori proyek. Sehingga aplikasi main sudah terbuat dan terdaftar di proyek inventori.

   c. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
   Saya menambahkan fungsi "include" dari django.urls dan `path('', include('main.urls'))` ke dalam urls.py di dalam direktori proyek (inventori). Saya menghapus "main/" dan menggantinya dengan "" karena sebelumnya aplikasi main menunjukkan error. Pada dasarnya routing ini bertujuan untuk dapat mengakses aplikasi main oleh projek dan prambanan web

   d. Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib (name, amount, description)
   Saya menambahkan,

   ```
   from django.db import models

   class Product(models.Model):
       name = models.CharField(max_length=255)
       amount = models.IntegerField()
       description = models.TextField()
       price = models.IntegerField()
   ```

   pada models.py di direktori aplikasi main. Models ini berfungsi untuk mengatur dan mengelola data yang dapat kita buat, akses, perbarui, dan hapus serta biasanya berada di belakang tampilan. Models ini dapat berinteraksi langsung dengan database melalui perintah `python manage.py makemigrations` untuk membuat migrasi model dan `python manage.py migrate` untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data. Jika terdapat perubahan dalam model, kita selalu menggunakan kedua perintah tersebut untuk menyimpan perubahan ke dalam database

   e. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. Pertama saya mengisi views.py di direktori aplikasi main dengan

   ```
   def show_main(request):
       context = {
       'nameApp': 'Inventori App',
       'name': 'Fauzan',
       'class': 'PBP E',
       }

       return render(request, "main.html", context)
   ```

   dan membuat main.html di dalam folder templates pada direktori aplikasi main. main.html saya isi dengan kode,

   ```
   <h1>{{ nameApp }}</h1>

   <h5>Name: </h5>
   <p>{{ name }}<p>
   <h5>Class: </h5>
   <p>{{ class }}<p>
   ```

   Hubungan kedua file tersebut adalah views.py bertugas untuk mengatur http request dan mengembalikkan isi kontennya ke file yang dituju, yakni main.html untuk ditampilkan ke user. Ini diatur pada kode `return render(request, "main.html", context)`

   f. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
   Saya mengisi urls.py di dalam direktori main dengan,

   ```
   from django.urls import path
   from main.views import show_main

   app_name = 'main'

   urlpatterns = [
   path('', show_main, name='show_main'),
   ]
   ```

   Kode tersebut akan membuat URL pada aplikasi main yang menampilkan views.py menggunakan fungsi show_main.

   g. Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
   Deployment bertujuan untuk menunjukkan hasil kode yang kita buat supaya dapat diakses oleh orang lain. Dalam hal ini, saya menggunakan Adaptable yang mengharuskan untuk connect ke github untuk dapat melakukan deployment. Saya menggunakan Python App Template, database PostgreSQL, dan start command menggunakan "python manage.py migrate && gunicorn inventori.wsgi"

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

   ![MVT](https://github.com/mohammadfauzan21/inventori/assets/110477943/b722ea54-f7b4-42e6-94d7-1cc2fa27908b)

    Saat pengguna mengirimkan request HTTP melalui urls.py, urls.py mengirimkannya ke views.py. views.py akan meminta data ke models.py. Sementara itu, models.py akan mengambil data dari database dan dikirimkan ke views.py. Setelah mendapatkannya, views.py akan mengolahnya untuk ditampilkan ke pengguna. Setelah mengelolanya, data akan dikirim ke html sehingga pengguna dapat melihat requestnya

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
   Kita perlu menggunakan virtual environment supaya package serta dependencies dari aplikasi kita dapat diisolasi sehingga tidak bertabrakan dan terpengaruh oleh versi lainnya. Hal ini meminimalisir adanya error yang tidak kita duga. Saya membuat virtual environment dengan perintah `python -m venv env` dan mengaktifkannya dengan perintah `env\Scripts\activate.bat`. Sebenarnya, kita dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Namun, hal ini merupakan opsi yang harus dihinndari. Karena, tanpa virtual environment, package serta dependencies pada proyek kita dapat bertabrakan dan terpengaruh oleh python global.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   MVC (Model, View, Controller) adalah konsep arsitektur yang digunakan dalam mengembangkan web untuk memisahkan bagian-bagian web menjadi beberapa komponen yang berbeda. Model = Komponen yang merepresentasikan pengelolaan sumber data. Tugasnya adalah menerima perintah dari Controller dan mengambil semua data (seusai kebutuhan) dari database atau remote API atau keduanya. Ia saling berinteraksi dengan Controller. View = Komponen yang merepresentasikan ui elements untuk menampilkan data yang telah di request oleh user yang diambil dari Model. Controller = Komponen yang mengatur interaksi pengguna dengan aplikasi atau web, seperti mouse yang di klik, dll dengan cara mengirimkan perintah ke model yang nanti akan diteruskan ke View.

MVT (Model, View, Template) adalah konsep arsitektur yang digunakan dalam mengembangkan web dengan framework tertentu untuk memisahkan bagian-bagian aplikasi menjadi beberapa komponen yang berbeda. Model = Komponen yang mempresentasikan pengelolaan sumber data. Ia secara langsung berinteraksi dengan database. Selain itu, ia juga menerima perintah dari View berdasarkan request dari user. Jika sudah melakukan operasi pada database, ia akan meneruskannya ke View. View = Komponen yang mengatur interaksi pengguna dengan aplikasi atau web. Ia menerima request dari pengguna dan meneruskannya ke Model. Setelah mendapat sesuatu dari Model, ia meneruskannya ke template untuk ditampilkan ke pengguna. Template = Komponen yang merepresentasikan ui element dan menampilkan data sesuai perintah yang diteruskan oleh View ke pengguna.

MVVM (Model, View, ViewModel) adalah konsep arsitektur yang biasanya digunakan dalam mengembangkan aplikasi mobile atau desktop untuk memisahkan bagian-bagian aplikasi menjadi beberapa komponen yang berbeda. Model = Komponen yang merepresentasikan pengelolaan sumber data. Tugasnya adalah melakukan operasi semua data (seusai kebutuhan) dari database atau remote API atau keduanya. Ia saling berinteraksi dengan ViewModel. View = Komponen yang merepresentasikan ui elements dan mendapatkan event dari ViewModel untuk ditampilkan ke pengguna. ViewModel = Komponen yang merepresentasikan business logic. Tugasnya adalah tidak hanya meneruskan data dari model, akan tetapi sebagai pengontrol tampilan bagaimana data tersebut akan ditampilkan ke pengguna. Ia saling berinteraksi dengan ViewModel dan View.

Perbedaan antara ketiganya: MVC = Merupakan arsitektur yang terdiri dari Model, View, Controller. Ia merupakan asritekstur perancangan untuk pengaplikasian web tradisional MVT = Merupakan arsitektur yang terdiri dari Model, View, Template. Pada MVT, Template menggantikan View pada MVC. Hal ini dikarenakan MVT dirancang khusus untuk pengembangan web dengan framework tertentu, seperti python yang memungkinkan pemisahan yang lebih jelas antara tampilan dan pemrosesan HTTP MVVM = Merupakan arsitektur yang terdiri dari Model, View, ViewModel. Untuk menampilkan data ke user, ia sama seperti MVC menggunakan View, tetapi menggantikan Controller dengan ViewModel. Hal ini disebabkan MVVM dirancang untuk pengembangan aplikasi mobile atau desktop yang berbasis pengguna. Ini memungkinkan ViewModel dapat terus melakukan interaksi dengan Model dalam meneruskan data untuk ditamplikan ke pengguna.
