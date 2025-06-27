#1
user_email = input("Please enter your email address: ")
if '@' in user_email:
    username, domain = user_email.split('@')
    print(f"\nUsername: {username}")
    print(f"Domain: {domain}")
    
    if 'gmail' in domain.lower():
        print("Status: Gmail user detected")
    else:
        print("Status: Other domain")
else:
   print("Invalid email address format. Please include '@' in your email.")

#2
user_password=input("Enter your password: ")
if  len(user_password)<8:
    print("Password is weak")
else:
    print("Password is Strong")


#3
user_fullname=input("Enter your full name: ")
print(user_fullname.upper())
print(user_fullname.lower())
name_count= len(user_fullname)
print(name_count)

#4
example="Samuel is a brilliant student." 
name_input=input("Enter your name: ") 
quality_input=input("Enter your quality")
new_sentence=example.replace("Samuel", name_input).replace("brilliant", quality_input) 
print(new_sentence)


#5
user_sentenceloop=input("Enter a sentence: ")
for letter in user_sentenceloop:
    print(letter + "**")


#6
story_name=input("Enter your name: ")
story_place=input("Enter your dream country: ")
story=("Once upon a time,",{story_name}, "went to", {story_place}, "to eat.")
print(story)

#7
user_sentence=input("Enter your sentence: ")
split_words=user_sentence.split()
sentence_count=len(user_sentence)
for word in user_sentence:
    print(word)

#8
user_message=input("Enter your message: ")
short_message=user_message.replace(" ")
print(short_message)

#10
user_profile=input("Enter your name: ")
user_age=input("Enter your age: ")
user_school=("Enter the school you attend: ")
profile=("Hello, my name is"+ user_profile+ "I am"+ user_age+ "I attend"+ user_school)
print(profile)
