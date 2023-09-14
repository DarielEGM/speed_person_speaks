#We ask the user for a phrase
phrase = input("Tell me a sentence to calculate how long it takes you to say it: ")

#We create a space-separated list of the words in the phrase and then count them.
number_of_words = len(phrase.split(" "))

#If it's more than 120 words, we tell him to stop
if(number_of_words > 120):
    print("That's enough, I didn't ask you for a testament.")
    
#We calculate how long it takes in seconds for a person to say the phrase compared to Dalto
print(f"You said {number_of_words} words, and it would take {number_of_words/2} seconds to say the phrase")
print(f"Dalto would say it in {number_of_words/2*0.7} seconds")