import vk


APP_ID = 5647961


def get_user_login():
    return input('Enter login: ')


def get_user_password():
    return input('Enter password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    friends_id_online = api.friends.online()
    for friend in friends_id_online:
        print(api.users.get(friend))

def output_friends_to_console(friends_online):
    pass


if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)

