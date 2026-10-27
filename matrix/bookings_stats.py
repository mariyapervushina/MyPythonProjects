bookings = [['Дата', 'Квартира', 'Ночей'],
            ['01.11', 'Мармарис-1', 3],
            ['05.11', 'Мармарис-2', 5],
            ['12.11', 'Мармарис-1', 2]]
total_nights = 0
for row in bookings[1:]:
    total_nights += row[2]
marmaris_1_nights = 0
for row in bookings[1:]:
     if row[1] == 'Мармарис-1':
         marmaris_1_nights += row[2]
print(marmaris_1_nights)
print(total_nights)
