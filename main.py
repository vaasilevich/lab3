print ('Введите РОСТ (м):')
#height = float (input())
height = 150
print ('Введите ВЕС (кг):')
#weight = int (input())
weight = 50
print ('Введите КОЛИЧЕСТВО ШАГОВ:')
#steps = int (input())
steps = 1000
print ('Введите ВРЕМЯ АКТИВНОСТИ (мин):')
#time = int (input())
time = 15

lenght = height/4 + 0.37  #Длина шага
print(lenght)

distance = lenght*steps/100  #Дистанция в метрах
print(distance)
V = distance / (time * 60)  #Скорость ходьбы шагов в минуту
print(V)

K = 0.035*weight + (V**2/height*0.029*weight)  #Количество сожжённых калорий

print(distance, round(K, 2))

distance = distance/1000

if distance < 2:
    print('В следующий раз постарайся пройти больше!')
elif (distance>2) and (distance<4):
    print('Неплохо, но можно и лучше!')
else:
    print('Ты умничка!')