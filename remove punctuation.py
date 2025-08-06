import string
def remove_punctuation(input_str):
    return input_str.translate(str.maketrans('', '', string.punctuation))
s=input("Enter a string:")
r=remove_punctuation(s)
print(r)
