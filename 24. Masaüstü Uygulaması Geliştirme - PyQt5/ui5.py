# Designer.exe ile UI oluşturma.

"""
Dialog Penceresi => Bu pencerelerde işlem yapmadan diğer pencerelere geçiş yapılamaz.

.ui dosyasından(Designer'dan oluşturulan) .py dosyasını oluşturma => pyuic5 donusturelecek_ui_dosya.ui -o olusturulacak_yeni_dosyanin_ismi.py  => Terminal'e yaz.
==> Örn: pyuic5 ui6.ui -o ui6.py <==

--- Layouts ---
Horizontal Layouts  => Nesneleri yatayda ard arda sıralamaya yarar.
Vertical Layouts    => Nesneleri dikeyde ard arda sıralamaya yarar.
Grid Layouts    => İstenilen konumda nesneleri konumlandırılabilir.

Designer Üzerinde Eleman Özellikleri:
    layoutSpacing   => Her kenardan belirtilen oranda uzaklaşır.
    layoutStretch   => Layout üzerindeki elemanların sırasıyla boyutlarında oynama yapar.

    Vertical Policy => Elemanların boyutlarının olduğu kutuyu kapsayacak mı onu belirler. fixed mı, expended mı olacak vs.
    
"""