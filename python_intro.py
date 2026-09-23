from PIL import Image, ImageFilter
import os
import pyttsx3 
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
    

def main():
    # say_hello()
    # blur_image()
    # say_hello_to()
    # play_with_int()
    # test_range()
    # test_list()
    # test_tuple()
    # test_dict()
    # get_int()
    #math_operation()
    talk_to_gemini()
    
 
def talk_to_gemini():
    _ = load_dotenv(find_dotenv())
    gemini_api_key = os.environ["GEMINI_API_KEY"]
    genai.configure(api_key = gemini_api_key)
    system_prompt = "You are a friendly and supportive lecturer in Dundalk Institute of Technology."
    user_prompt = input("What do you want to know? ")
    llm_model = "gemini-2.5-flash"
    model = genai.GenerativeModel(llm_model)
    prompt = [
        {"role" : "user", "parts" : [system_prompt, user_prompt]}
    ]
    response = model.generate_content(prompt)
    print(response.text.strip())
    
def math_operation():
    a = 7
    b = 3
    print(f"{a/b:.50f}")
 
 
def test_range():
    for i in range(10):
        print(i)
        
# Lists are mutable(I can add to them without creating a new piece of memory) and ordered(I can access then [0], [1]....)   
def test_list():
    names = ["Aleksy", "Aloka", "Adhira", "Matthew", "Jack", "Bernard", "Martyna", "Hanna", "Michal"]
    names.append("Nikita")
    print(names)
    
# Tuples are immutable and ordered  
def test_tuple():
    aleksy = ("Black hair", "Blue eyes", "Glasses")
    print(aleksy[0])
    
    
def get_int():
    while(True):
        try:
            value = int(input("Please enter an integer: "))
            return value
        except ValueError:
            print("Not an integer")
    print(value)
    
    
    
# Dict are mutable and unordered
def test_dict():
    sd3a = {"Aleksy":60, "Aloka":75, "Matthew":100}
    sd3a["Jack"] = 80
    for student in sd3a.keys():
        print(f"{student} : {sd3a[student]}")
    
def play_with_int():
    big_number = 5000000000000000000
    print(type(big_number))
    print(big_number)
    
    
def say_hello_to():
    name = input("Please enter your name: ")
    thing_to_say = "Hello, " + name
    print(f"The computer will say {thing_to_say}")
    really_say_hello(thing_to_say)
    
 
def really_say_hello(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
 
    
def blur_image():
    before = Image.open("test_image.png")
    after = before.filter(ImageFilter.BoxBlur(3))
    after.save("out.png")


def say_hello():
    print("Hello, world")
    
    
if __name__ == "__main__":
    main()
    
    