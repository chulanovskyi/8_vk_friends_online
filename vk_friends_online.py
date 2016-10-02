import vk
import getpass


APP_ID = 5647961


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return getpass.getpass('Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope = 'friends',
    )
    api = vk.API(session)
    friends_id_online = api.friends.getOnline()
    friends_online = api.users.get(user_ids=friends_id_online)
    return friends_online


def output_friends_to_console(friends_online):
    print('Friends are currently online:')
    for friend in friends_online:
        print(friend['last_name'], friend['first_name'])


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
