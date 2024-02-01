art = '''

▒█▀▀█ █▀▀ █▀▀█ █▀▀ █▀▀ █▀▀█ 　 ▒█▀▀█ ░▀░ █▀▀█ █░░█ █▀▀ █▀▀█ 
▒█░░░ █▀▀ █▄▄█ ▀▀█ █▀▀ █▄▄▀ 　 ▒█░░░ ▀█▀ █░░█ █▀▀█ █▀▀ █▄▄▀ 
▒█▄▄█ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀ ▀░▀▀ 　 ▒█▄▄█ ▀▀▀ █▀▀▀ ▀░░▀ ▀▀▀ ▀░▀▀'''

dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art)

def encryptor(prompt, shiftnum, encordec):
    resmessage = ""
    if encordec == "d":
        shiftnum *= -1
    for letter in prompt:

        if letter in dict:
            order = dict.index(letter)
            neworder = order + shiftnum
            resmessage += dict[neworder]
        else:
            resmessage += letter
    import clipboard
    clipboard.copy(resmessage)
    if encordec == "d":
        print(f"The decrypted message: '{resmessage}' was copied to the clipboard.")
    else:
        print(f"The encrypted message: '{resmessage}' with shift number '{shiftnum}' was copied to the clipboard.")


exitnow = False
while not exitnow:

    encordecinput = input("Encrypt or decrypt? e/d \n")
    messinput = input("Type your message:\n").lower()
    shiftprompt = int(input("Type the shift number:\n"))
    shiftprompt = shiftprompt % 26

    encryptor(prompt=messinput, shiftnum=shiftprompt, encordec=encordecinput)

    postprompt = input("Do you need another query? y/n \n").lower()
    if postprompt == "n":
        exitnow = True
        print("App Closed")