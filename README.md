# Big Data Ağ Programlama

  Bu proje, Django ile hazırlanmış bir web uygulamasıdır. Uygulama, bir Excel dosyası kullanarak veri tabanı yönetimini sağlar ve vis.js kullanarak veri görselleştirmesi yapar. Proje HTML, CSS, JavaScript, Ajax ve Python ile geliştirilmiştir. Ayrıca, Pandas ve Regex kütüphanelerini de kullanmaktadır.


## Gereksinimler

- asgiref==3.8.1
- Django==5.0.6
- django-extensions==3.2.3
- et-xmlfile==1.1.0
- numpy==1.26.4
- openpyxl==3.1.4
- pandas==2.2.2
- python-dateutil==2.9.0.post0
- pytz==2024.1
- six==1.16.0
- sqlparse==0.5.0
- tzdata==2024.1


## Kurulum Talimatları

Bu projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### Adım 1: Depoyu Klonlayın

*Öncelikle, GitHub reposunu yerel makinenize klonlayın:*

Yerelde oluşturduğunuz bir dosyayı git bash ile açarak

```git clone https://github.com/hypynnax/Ag-Programlama-Big-Data.git```

komutu ile repoyu kendi localinize çekin.


### Adım 2: Gerekli Kütüphaneleri İndirin

```
pip install django
pip install pandas
pip install openpyxl
pip install django-extensions
```


### Adım 3: Projeyi Çalıştırın

Yeni bir terminal açın ve 

```py manage.py runserver```

komudunu yazın bu sayede proje başlatılabilir.

Şöyle bir çıktı alacaksınız;

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
June 13, 2024 - 13:16:46
Django version 5.0.6, using settings 'BigDataProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

bundan sonra [http://127.0.0.1:8000/bigData/generatedData/](http://127.0.0.1:8000/bigData/generatedData/) adresini ziyaret ederek projeyi görebilirsiniz.


