from oldboy.day5.User import  User

def main():
    user = User("admin","admin")
    print(user.checkValidate())
    print(user.selectAll())

if __name__ == '__main__':
    main()