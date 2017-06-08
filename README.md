# Son Depremler
Python 3 ile Son Depremleri görüntüleyebilirsiniz.

### Kurulum için gerekenler:

 * python3
 * urllib
 * BeautifulSoup

 **Python 3** kurulu değilse:

***macOs için kurulum***

```
brew install python3
```

***linux için kurulum***
```
apt-get install python3
```

**pip** ile gerekli paketleri kuralım:
 ```
pip3 install -r requirements.txt
```

### Demonun çalıştırılması için

Terminal üzerinden aşağıdaki komut ile çalıştırabilirsiniz.

 ```
python3 example.py
```


#### Limit
example.py > work() methodu üzerinden 3 parametre ile istenilen aralık alınabilir.
Varsayılan değer boş olduğu için tüm veriler listelenecektir.
Limit için parametreler
--ilk
--son
--adım (aralık belirtilmek istenilirse)

