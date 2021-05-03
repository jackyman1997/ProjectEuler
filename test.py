# asdfuhasdkjfhfasd
import os
import pathlib
# %%
[item if os.path.isfile(item) else os.listdir(item) for item in os.listdir()]
# %%
words = ['apple', 'banana', 'orange']

words_to_len = {word if word != 'apple' else 'not apple': len(word) if word != 'apple' else 'not apple'  for word in words}
print(words_to_len)
# %%
import my_tools.maths

my_tools.maths.factorials.factorial(10)
# %%
