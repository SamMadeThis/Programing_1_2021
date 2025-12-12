import sys
import random

def main_page():

# start of the story........

    story_introduction = ["Once a upon a time, a long time ago in a far away land, lived a ",
                          "Last week, at School during recess, I met ",
                          "Last summer, at Band camp, I bumped into a "]
    
    color = ["black", "pink", "red"]
# I met a .....

    who = [ "a Cowboy", "an Astronaut", "a Queen", "a King", "a Superhero", "a Baby genius", "a Pirate", "a Scientist","a Fairy", "an Alien", "a Wizard", "a Witch", "a Monster", "my PE Teacher", "your Grandpa" 
,"a Hippo", "a Cat", "a Ladybug",  "a Shark", "a Dolphin", "a Dog" 
, "a Marshmallow", "a Blob of goo", "a Box of crayons", "a Meatball", "a Sunflower", "a Bubble", "a Meat-eating plant", "a Cowboy", "Astronaut", "Queen", "King", "Superhero",
                     "a Baby genius", "a Pirate", "a Scientist" ]
    
    who_fictional = [ "Fairy", "Alien", "Wizard"]
    
    who_evil = [ "Witch", "Monster" ]

    who_my_person = [ "PE Teacher", "Grandpa" ]

    who_animal = ["Hippo", "Cat", "Ladybug",  "Shark", "Dolphin", "Dog" ]

    who_thing = [ "Marshmallow", "Blob of goo", "Box of crayons", "Meatball", "Sunflower", "Bubble", "Meat-eating plant" ]

# who told me 
    
    what = ["to ride a roller coaster",
            "to be a ballerina",
            "to buy a home",
            "to escape from a dragon's belly",
            "to become a dancer",
            "to win a race",
            "to be the first from his planet to travel to Earth",
            "to make disco clothes fashionable",
            "to relax in a backpack",
            "to be big or smaller",
            "to ride a camel",\
            "to build a catapult",
            "to rule the world",
            "to overcome a fear of something",
            "to become a voice impersonator",
            "to enjoy a very lazy day",
            "to change from a bad guy to a good guy",
            "to bake a cake", "to save the world",
            "to bend air or water", "to rescue a stranded puppy",
            "to become a master chef",
            "to tame a Tazmanian Devil",
            "to get the one thing he always wanted",
            "to win a watermelond see spitting contest",
            "to make a friends"]

# will have a quest after the problem but it must be Y/N answers

    quests_what_he_problem = [ "that he wanted to ride a roller coaster, but a giant pool of slime is in the way.\
                                Can you help?",
                               "he really wants to buy a home, but the problem is a giant Ladybug appears blocking his path, and won't let him past. Could you help?",
                              "that she wanted to ride a roller coaster, but a giant pool of slime is in the way.\
                            Could you help?", "that she wanted to be a ballerina, the problem was, she doesn't know how to dance!\
                 Will you give her a dance lesson?",]

    
    problem = ["she doesn't know how to dance",
               "a pool of slime is in the way",
               "his minions sabotage his onboad navigation",\
               "a puppy won't leave it alone", "has an attack of the hiccups",
               "car/boat/spaceship is broken",\
               "magic wand/spell is broken", "is very clumsy",
               "gets trapped in a tower", "she doesn't know how",
               "is allergic to fun", "overcome by sleepiness",
               "gets distracted by a dance party",
               "evil nemesis has other plans",
               "forrest comes to life",
               "epic water gun battle starts",
               "doesn't have the right clothes or gear",
               "grumpy alligator",
               "minions quit",
               "gravity just became super strong",
               "they can't get any respect",
               "gets sucked into a magical vortex", 
               "plans never work out right", "is scared",
               "the internet is unavailable", "giant ladybug appears",
               "they are allergic to fun",  ]
    action_resolution = []


# ASCII Art
# ASCII Text gen http://www.network-science.de/ascii/

    sys.stdout. write (

    """
******************************* MAIN MENU **************************************



                     _   _      _ _       
                    | | | |    | | |      
                    | |_| | ___| | | ___  
                    |  _  |/ _ \ | |/ _ \ 
                    | | | |  __/ | | (_) |
                    \_| |_/\___|_|_|\___/


This will generate a story somehow, please answer the questions below!

********************************************************************************
    """)
    sys.stdout.write("\nWhat is your name: ")
    name_answer = str(sys.stdin.readline())
    
    who_answer = (random.choice(who))
    what_answer = (random.choice(what))
    problem_answer = (random.choice(problem))

    

    

    

    sys.stdout.write(str("\n**************************************"\
                                 + "******************************************\n\n"))
    sys.stdout.write("""

           .__..__ .  ..___.  ..___..  ..__ .___  .___.._..  ..___ | 
           [__]|  \\  /[__ |\ |  |  |  |[__)[__     |   | |\/|[__  | 
           |  ||__/ \/ [___| \|  |  |__||  \[___    |  _|_|  |[___ *     

""")



    sys.stdout.write("\n\n" + (name_answer) + " is a " + (who_answer) + " who wants to " + 
                       (what_answer) + "\n but for some reason \n" + (problem_answer) + "." )

    sys.stdout.write(str("\n**************************************"\
                                 + "******************************************\n\n"))


main_page()

## words taken from this link: # https://supereasystorytelling.com/printables/story-idea-generator.pdf
