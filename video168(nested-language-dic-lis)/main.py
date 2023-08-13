programming_language = [
    {"username": "Elshad", "favorites_languages": [
        "python", "java", "c++"], "experiance": 10
     },
    {
        "username": "Renad", "favorites_languages": [
            "python", "c#"], "experiance": 2
    }
]


def add_list_nested(my_list):

    new_user = {}
    new_user["username"] = input("Enter user name? ")
    new_user["experiance"] = int(input("Enter experiance? "))

    my_list.append(new_user)
    return my_list


print(add_list_nested(programming_language))
