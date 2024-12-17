#madlib story:
#Yesterday was a (adjective) day. I started the day by eating (breakfast food) but it tasted weird and
#smelled like (a type of fish). After that, I went to the (place) to ease my mind, but then a (adjective) man with a 
#(object) came in and started (verb that ends in -ing). I started to get bored so I decided to go to the (place) to 
#(verb). However, I got interrupted by a (animal) that started to (verb). It was a very (adjective) animal but I just
# wasn't in the mood. By then, I was feeling so (adjective) that I decided I should go to my room at home and take a nap.
# I was so (adjective) and ready to rest, after my long (adjective) day. 

def get_user_input(prompt):
    user_input = input(prompt)
    if not user_input:
        print("Try actually entering something")
        return get_user_input(prompt)
    elif user_input == " ":
            print("That's not gunna cut it")
    return user_input

def madlib_blanks_to_user_input(): 
    blanks = {}
    prompts = [
        ("adjective1", "enter an adjective: "),
        ("adjective2", "enter an adjective: "),
        ("adjective3", "enter an adjective: "),
        ("adjective4", "enter an adjective: "),
        ("adjective5", "enter an adjective: "),
        ("breakfast food", "enter a breakfast food: "),
        ("a type of fish", "enter a type of fish: "),
        ("place1", "enter a place: "),
        ("place2", "enter a place: "),
        ("object", "enter an object: "),
        ("verb (-ing)", "enter a verb ending in -ing: "),
        ("verb1", "enter a verb: "),
        ("verb2", "enter a verb: "),
        ("animal", "enter an animal: "),]

    for key, prompt in prompts:
        blanks[key] = get_user_input(prompt)
    
    print(f"""Yesterday was a {blanks["adjective1"]} day. I started the day by eating {blanks["breakfast food"]}, 
but it tasted weird and smelled like {blanks["a type of fish"]}. After that, I went to the 
{blanks["place1"]} to ease my mind, but then a {blanks["adjective2"]} man with a {blanks["object"]} 
came in and started {blanks["verb (-ing)"]}. I started to get bored, so I decided to go to the 
{blanks["place2"]} to {blanks["verb1"]}. However, I got interrupted by a {blanks["animal"]} 
that started to {blanks["verb2"]}. It was a very {blanks["adjective3"]} animal, but I just wasn't in the mood. 
By then, I was feeling so {blanks["adjective4"]} that I decided I should go to my room at home and take a nap. 
I was so {blanks["adjective5"]} and ready to rest, after my long {blanks["adjective1"]} day.""")

madlib_blanks_to_user_input()