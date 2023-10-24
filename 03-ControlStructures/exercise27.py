facebook = False
twitter = False
instagram = True
count = 0
print(f'Facebook: {facebook}')
print(f'Twitter: {twitter}')
print(f'Instagram: {instagram}')
if facebook:
    count += 1
if twitter:
    count += 1
if instagram:
    count += 1
if count >= 2:
    print('A person can be a good influencer!')
