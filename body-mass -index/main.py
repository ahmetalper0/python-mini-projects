weight = int(input('\nKilonuzu kilogram (kg) şeklinde giriniz : '))
height = int(input('\nBoyunuzu santimetre (cm) şeklinde giriniz : '))

BMI = weight / ( ( height / 100 ) ** 2 )

print(f'\nVücut kitle indeksiniz : {BMI}')

if BMI>0:

    if BMI <= 16:

        print('\nÇok zayıfsınız\n')

    elif BMI <= 18.5:

        print('\nZayıfsınız\n')

    elif BMI <= 25:

        print('\nSağlıklısının\n')

    elif BMI <= 30:

        print('\nKilolusunuz\n')
    
    elif BMI <= 35:
        
        print('\nAşırı kilolusunuz\n')
    
else:

    print('\nHatalı değerler girdiniz !\n')
