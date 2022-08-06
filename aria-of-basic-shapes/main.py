print('''
1- Üçgen
2- Kare
3- Dikdörtgen
4- Çember
''')

choice = int(input('Hangisinin alanını hesaplamak istiyorsunuz : '))

if choice == 1:

    a = int(input('\nÜçgenin taban uzunluğunu giriniz : '))
    h = int(input('\nÜçgenin yüksekliğini giriniz : '))

    print(f'\nÜçgenin Alanı : { (a * h) / 2 }\n')

elif choice == 2:
    
    n = int(input('\nKarenin kenar uzunluğunu giriniz : '))

    print(f'\nKarenin Alanı : { n * n }\n')

elif choice == 3:
    
    k = int(input('\nDikdörtgenin uzun kenar uzunluğunu giriniz : '))
    u = int(input('\nDikdörtgenin kısa kenar uzunluğunu giriniz : '))

    print(f'\nDikdörtgenin Alanı : { k * u }\n')

elif choice == 4:
    
    PI = 3

    r = int(input('\nÇemberin yarıçap uzunluğunu giriniz : '))

    print(f'\nÇemberin Alanı : { PI * r * r }\n')

else:

    print('\nYanlış seçim yaptınız\n')

print('''
1- Üçgen
2- Kare
3- Dikdörtgen
4- Çember
''')

choice = int(input('Hangisinin alanını hesaplamak istiyorsunuz : '))

if choice == 1:

    a = int(input('\nÜçgenin taban uzunluğunu giriniz : '))
    h = int(input('\nÜçgenin yüksekliğini giriniz : '))

    print(f'\nÜçgenin Alanı : { (a * h) / 2 }\n')

elif choice == 2:
    
    n = int(input('\nKarenin kenar uzunluğunu giriniz : '))

    print(f'\nKarenin Alanı : { n * n }\n')

elif choice == 3:
    
    k = int(input('\nDikdörtgenin uzun kenar uzunluğunu giriniz : '))
    u = int(input('\nDikdörtgenin kısa kenar uzunluğunu giriniz : '))

    print(f'\nDikdörtgenin Alanı : { k * u }\n')

elif choice == 4:
    
    PI = 3

    r = int(input('\nÇemberin yarıçap uzunluğunu giriniz : '))

    print(f'\nÇemberin Alanı : { PI * r * r }\n')

else:

    print('\nYanlış seçim yaptınız\n')
