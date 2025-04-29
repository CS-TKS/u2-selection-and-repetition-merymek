# initialize score
score = 0

# create list for questions, choices, information, and answers
questions = ["Why are vaccines important?",
             "When did practices involving vaccinating begin in human history?",
             "Who first brought the inoculation (immunization) of smallpox to Europe in 1721?",
             "Who invented the world's first successful vaccine?",
             "How many children in the world currently remain un-vaccinated?",
             "When was the first influenza vaccine used?",
             "What did Louis Pasteur do in 1885?",
             "What was the first country in history to eradicate polio?",
             "What causes malaria?",
             "How many diseases do vaccines protect against?"]

choices = [
    ["1) Teaches the body how to respond to diseases, 2) Destroys every disease in the world, 3) They're dangerous, "
     "4) They're important?"],
    ["1) 1500 CE, 2) 100 CE, 3) 300 BCE, 4) 2020 CE"],
    ["1) Benjamin Jesty, 2) Mary Montagu, 3) Albert Einstein, 4) Marie Curie"],
    ["1) Thomas Edison, 2) Edward Jenner, 3) Christian Doppler, 4) Michael Faraday"],
    ["1) 1/2, 2) 2/6, 3) Everyone is vaccinated, 4) 1/5"],
    ["1) 1946, 2) 1937, 3) 1945, 4) 1831"],
    ["1) Successfully prevented rabies, 2) Created the first laboratory produced vaccine, 3) Created pasteurization, "
     "4) Married Napoleon Bonaparte"],
    ["1) The United States of America, 2) Uganda, 3) Czechoslovakia, 4) Democratic Republic of Congo"],
    ["1) Mosquitoes, 2) vaccines, 3) parasites, 4) tropical climate"],
    ["1) 20+, 2) less than 20, 3) 100+, 4) only 10"]
]

more_info = ["- Vaccines teach your immune system how to create antibodies that protect you from diseases. It's much "
             "\nsafer for your immune system to learn this through vaccination than by catching the diseases and "
             "\ntreating them. Once your immune system knows how to fight a disease, it can often give you life long "
             "protection.",
             "- Certainly! Although practices may have begun as early as 200 BCE, people have definitely started to "
             "\nattempt to prevent illness by exposing healthy individuals to smallpox in the 15th century.",
             "- Affirmative! Lady Mary Wortley Montagu brought immunization to Europe, asking for the inoculation of "
             "\nher two daughters after observing the practice in Turkey.",
             "- By all means! Dr. Edward Jenner expanded on previous efforts and discovered that those who had "
             "\ncontracted cowpox were immune to smallpox, which then led him to using the first successful vaccine "
             "on"
             "\n8-year-old James Phipps, the first person to successfully receive a vaccine.",
             "- Indeed, some people don’t have access to life-saving vaccinations, while other parents believe that "
             "it"
             "\nisn’t necessary to put extra vaccines in the bodies of their children to prevent ‘common’ diseases.",
             "- After 20-50 million people worldwide were killed by the influenza vaccine, included 1 in 67 U.S. "
             "\nsoldiers, creating a vaccine became a top priority of the U.S. military. The first influenza vaccines"
             "\nwere approved for military use in 1945, then civilian use was permitted in 1946 after favourable "
             "results.",
             "- Louis Pasteur used this method, post-exposure, which is when a preventive medicine is used after "
             "\nexposure to an illness to prevent it from occurring. For example, Pasteur used the spinal cord fluid of"
             "\nrabid rabbits as a vaccine against rabies, injecting it into rabid dogs and noticing that they didn’t "
             "develop rabies.",
             "- Czechoslovakia started vaccinating in the early 1960s with the newly developed oral polio vaccines, "
             "\nand soon became the first country in the world to completely eradicate polio.",
             "- Malaria is actually caused by a parasite, which spreads to humans through infected mosquitoes. Malaria "
             "\nis completely preventable and treatable, yet most deaths occur in children aged under 5.",
             "- The WHO reports that there are roughly 31 vaccines available for the prevention or control of diseases."
             ]

answers = [1, 1, 2, 2, 4, 3, 1, 3, 3, 1]

# introduction
while True:
    print("-" * 15)
    choice_to_play = input("Welcome to the amazing quiz of medical history! The history of vaccination began in the "
                           "\nlate 18th century when scientist Edward Jenner discovered that cowpox could protect "
                           "against"
                           "\nsmallpox. This groundbreaking finding led to the development of vaccines that train the "
                           "\nimmune system to fight diseases. Over time, vaccines have played a crucial role in "
                           "\ncontrolling and even eradicating deadly illnesses like smallpox and polio. Today, "
                           "\nvaccination"
                           "remains one of the most effective public health tools for preventing disease and saving "
                           "lives "
                           "worldwide. "
                           "\n "
                           "\nSo, would you like to play a quiz on the history of vaccination?: ").lower()
    # quiz
    if choice_to_play == 'yes':
        print("Great! Let's begin the amazing quiz on vaccination history!")
        print("-" * 15)
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
            print("-" * 15)
        if score == len(questions):
            print("Congratulations, you mastered the history of vaccination!")
        elif score <= 2:
            print(f"Your score is {score}. You might want to try redoing the test.")
        else:
            print(f"Your score was {score}. Good job! Next time, try to master the quiz.")
        # end of quiz
        second_choice_playing = int(input("Would you like to play again? (1) Yes (0) No: "))
        if second_choice_playing == 0:
            print("See you next time!")
            break
    else:
        print("Too bad; let's meet again next time!")
        break
