#madlib story:
#Yesterday was a (adjective) day. I started the day by eating (breakfast food) but it tasted weird and
#smelled like (a type of fish). After that, I went to the (place) to ease my mind, but then a (adjective) man with a 
#(object) came in and started (verb that ends in -ing). I started to get bored so I decided to go to the (place) to 
#(verb). However, I got interrupted by a (animal) that started to (verb). It was a very (adjective) animal but I just
# wasn't in the mood. By then, I was feeling so (adjective) that I decided I should go to my room at home and take a nap.
# I was so (adjective) and ready to rest, after my long (adjective) day. 

def get_user_input(prompt):
    return input(f"enter a {prompt}: ")

def madlib_blanks(): 
    blanks = {
        "adjective1": get_user_input("adjective"),
        "adjective2": get_user_input("adjective"),
        "adjective3": get_user_input("adjective"),
        "adjective4": get_user_input("adjective"),
        "adjective5": get_user_input("adjective"),
        "breakfast food": get_user_input("breakfast food"),
        "a type of fish": get_user_input("a type of fish"),
        "place1": get_user_input("place"),
        "place2": get_user_input("place"),
        "object": get_user_input("object"),
        "verb (-ing)": get_user_input("verb ending in -ing"),
        "verb1": get_user_input("verb"),
        "verb2": get_user_input("verb"),
        "animal": get_user_input("animal")
    }
    print(f"""
    Yesterday was a {blanks["adjective1"]} day. I started the day by eating {blanks["breakfast food"]}, 
    but it tasted weird and smelled like {blanks["a type of fish"]}. After that, I went to the 
    {blanks["place1"]} to ease my mind, but then a {blanks["adjective2"]} man with a {blanks["object"]} 
    came in and started {blanks["verb (-ing)"]}. I started to get bored, so I decided to go to the 
    {blanks["place2"]} to {blanks["verb1"]}. However, I got interrupted by a {blanks["animal"]} 
    that started to {blanks["verb2"]}. It was a very {blanks["adjective3"]} animal, but I just wasn't in the mood. 
    By then, I was feeling so {blanks["adjective4"]} that I decided I should go to my room at home and take a nap. 
    I was so {blanks["adjective5"]} and ready to rest, after my long {blanks["adjective1"]} day.
    """)


madlib_blanks()
