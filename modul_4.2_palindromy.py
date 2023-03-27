def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

palindromes = ("sos", "zakupy",
                "anna", "droga",
                "sedes", "samochód",
                "zaraz", "noc",
                "kajak", "dzień",
                "zakaz", "długo",
                "owocowo", "krótko",
                "potop", "radar")
for word in palindromes:
    if is_palindrome(word):
        print(word, "jest palindromem")
    else:
        print(word, "nie jest palindromem")  
   

