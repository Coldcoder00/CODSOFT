def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("What Next: ").lower()
        if 'hello' in user_input:
            print("Chatbot: Hi there!")
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a bunch of code, so I don't have feelings, but thanks for asking!")
        elif 'bye' in user_input:
            print("Chatbot: Goodbye!")
            break
        elif 'what is your name' in user_input:
            print("Chatbot: I'm a simple chatbot created by Dharmveer.")
        elif 'name the seven wonders of the world' in user_input:
            print("Chatbot:\n 1. Colossus of Rhodes\n 2. Great Pyramid of Giza\n 3. Hanging Garden of Babylon\n 4. Statue of Zeus at Olympia\n 5. The Great Wall of China\n 6. Machu Picchu\n 7. Taj Mahal")
        elif 'from which country does your developer belong' in user_input:
            print("Chatbot: My developer belongs from India.")
        elif 'in which language are you coded' in user_input:
            print("Chatbot: I'm mainly coded in the Python language.")
        elif 'name the seven days of the week' in user_input:
            print("Chatbot:\n 1. Sunday\n 2. Monday\n 3. Tuesday\n 4. Wednesday\n 5. Thursday\n 6. Friday\n 7. Saturday")
        elif 'the months in a year' in user_input:
            print("Chatbot: The months in a year are:\n 1. January\n 2. February\n 3. March\n 4. April\n 5. May\n 6. June\n 7. July\n 8. August\n 9. September\n 10. October\n 11. November\n 12. December.")
        elif 'name any 4 seasons' in user_input:
            print("Chatbot:\n 1. Summer\n 2. Winter\n 3. Spring\n 4. Rainy")
        elif 'in which year were you developed' in user_input:   
            print("Chatbot: I was developed in the year 2023.") 
        elif 'name the largest country in the world' in user_input:
            print("Chatbot: Russia is the largest country in the world.")                        
        else:
            print("Chatbot: Sorry, I don't understand that.")
        
simple_chatbot()