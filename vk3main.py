from lab3id import IdFromUsername
from lab3frnds import Friends

uClient = IdFromUsername('borzovand')
uid = uClient.execute()
print(uid)

friends_client = Friends(uid)
friends = friends_client.execute()

for (age, count) in friends:
    print('{} {}'.format(int(age), '#' * count))