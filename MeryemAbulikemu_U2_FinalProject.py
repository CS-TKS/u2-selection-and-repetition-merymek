# initialize score
score = 0

# define a quiz function to make everything easy on the eyes

# create list for questions, choices, information, and answers
questions = ["When did practices involving vaccinating begin in human history?",
             "Who first brought the inoculation (immunization) of smallpox to Europe in 1721?",
             "Who invented the world's first successful vaccine?",
             "How many children in the world currently remain un-vaccinated?",
             "When was the first influenza vaccine used?"]

choices = [
    ["1) 1500 CE, 2) 100 CE, 3) 300 BCE, 4) 2020 CE"],
    ["1) Benjamin Jesty, 2) Mary Montagu, 3) Albert Einstein, 4) Marie Curie"],
    ["1) Thomas Edison, 2) Edward Jenner, 3) Christian Doppler, 4) Michael Faraday"],
    ["1) 1/2, 2) 2/6, 3) Everyone is vaccinated, 4) 1/5"],
    ["1) 1946, 2) 1937, 3) 1945, 4) 1831"]
]

more_info = ["Certainly! Although practices may have begun as early as 200 BCE, people have definitely started to "
             "attempt to prevent illness by exposing healthy individuals to smallpox in the 15th century.",
             "Affirmative! Lady Mary Wortley Montagu brought immunization to Europe, asking for the inoculation of "
             "her two daughters after observing the practice in Turkey.",
             "By all means! Dr. Edward Jenner expanded on previous efforts and discovered that those who had "
             "contracted cowpox were immune to smallpox, which then led him to using the first successful vaccine "
             "on"
             "8-year-old James Phipps, the first person to successfully receive a vaccine.",
             "Indeed, some people don’t have access to life-saving vaccinations, while other parents believe that "
             "it"
             "isn’t necessary to put extra vaccines in the bodies of their children to prevent ‘common’ diseases.",
             "After 20-50 million people worldwide were killed by the influenza vaccine, included 1 in 67 U.S. "
             "soldiers, creating a vaccine became a top priority of the U.S. military. The first influenza vaccines"
             "were approved for military use in 1945, then civilian use was permitted in 1946 after favourable "
             "results."]

answers = [1, 2, 2, 4, 3]

# create quiz
for i in range(len(questions)):
    print(f"Question {i + 1}: {questions[i]}")
    print(choices[i])
    user = int(input(f"Answer {i + 1} (Number only): "))
    if user == answers[i]:
        score = score + 1
        print(f"Congratulations! The answer is ({answers[i]})! Your score is now {score}.")
    else:
        info = input(f"Your answer was ({user}), which is incorrect. The answer is ({answers[i]}). "
                     "Would you like to learn more info about this question?: ").lower()
        if info == 'yes':
            print(more_info[i])
    print("")

# introduction
while True:
    print("-"*15)
    choice_to_play = input("Welcome to the amazing quiz of medical history! The history of vaccination began in the "
                       "late 18th century when scientist Edward Jenner discovered that cowpox could protect against"
                       "smallpox. This groundbreaking finding led to the development of vaccines that train the "
                       "immune system to fight diseases. Over time, vaccines have played a crucial role in "
                       "controlling and even eradicating deadly illnesses like smallpox and polio. Today, vaccination "
                       "remains one of the most effective public health tools for preventing disease and saving lives "
                       "worldwide. So, would yu like to play a quiz on medical history?").lower()
    if choice_to_play == 'yes':
        print("Great! Let's begin the amazing quiz on vaccination history!")
    else:
        print("Too bad; let's meet again next time!")
        break





