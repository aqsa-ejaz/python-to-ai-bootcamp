message = "hello im akif"

print(message[2])
print(message[-1])

print(message[0:5])

print(message)

# string_name[start : stop]

# methods
print(message.upper())
print(message.title())

st = "   a    "
print(st.strip())
print(st.lstrip())
print(st.rstrip())


# My practice: my own string
my_text = "  i am learning python  "

print(my_text.strip())
print(my_text.strip().title())
print(my_text.strip().upper())

clean = my_text.strip()
print(clean[0])
print(clean[-1])
print(clean[0:6])
print(clean[::-1])   # reversed text

print(clean.replace("python", "AI"))
print(clean.split(" "))
print(len(clean))
print(message.replace("hello", "Hey!"))

s = "a,b,c"
print(s.split(","))
