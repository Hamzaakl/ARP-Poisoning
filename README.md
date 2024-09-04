
# ARP Spoofing Saldırısı Script'i

Scapy kütüphanesini kullanarak bir **ARP Spoofing** (ARP Poisoning) saldırısı gerçekleştirir. Script, hedef IP adresini yanıltarak, ağ trafiğini kendi cihazınız üzerinden geçirmeyi amaçlar.

## Gereksinimler

- Python 3.x
- Scapy (`pip install scapy`)
- Ağ arayüzünüzün `eth0` olarak ayarlanmış olması

## Nasıl Çalışır?

1. **MAC Adresinin Alınması**: Script, saldırıyı gerçekleştirecek cihazın MAC adresini `ifconfig` komutu ile alır.
 

2. **ARP Paketlerinin Oluşturulması**:
    - Hedef IP adresi (`targetIp`) ve ağ geçidi IP adresi (`gatewayIp`) belirlenir.
    - Saldırgan MAC adresi, sahte olarak bu IP adreslerine atanır.
    - ARP paketleri oluşturulur.
  

3. **Saldırının Başlatılması**:
    - ARP paketleri sürekli olarak hedef ve ağ geçidi arasında gönderilir, böylece hedef cihaz yanıltılır.
    - `Ctrl + C` ile saldırı durdurulabilir.
  

## Kullanım

```bash
sudo python3 ARP-Poisoning.py
```

**Uyarı:** Bu script, yalnızca eğitim ve güvenlik testi amacıyla kullanılmalıdır..
