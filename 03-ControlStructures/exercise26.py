car_speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if speed_limit_min >= car_speed or car_speed >= speed_limit_max:
    print(f'Warning: invalid car speed!!')