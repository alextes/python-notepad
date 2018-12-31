def help_message():
    print("""
        help        see this menu, obviously
        say         say some text placed in a ascii banner
        poem        say a little poem for your muse
        exit        say bye!
        """)


def banner_say(message):
    print("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    %s
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """ % message)


def say_poem_for(muse):
    print("""
        Dear %s,

        Roses are not blue
        Violets are not red
        Whatever you do
        It trumps being dead
        """ % muse)


def error(incorrect_input):
    print("""
    '%s' was an example of an incorrect command
    """ % incorrect_input)
    help_message()


def read_cmd(user_input):
    inputs = user_input.split()
    cmd = inputs[0]
    args = inputs[1:]

    commands = {
        "help": help_message,
        "poem": lambda muse: say_poem_for(muse[0]),
        "say": lambda words: " ".join(words),
        "exit": lambda _: banner_say("Bye cruel world!"),
    }
    command = commands.get(cmd, lambda _: error(user_input))
    command(args)


# Fabricate some fake user inputs for testing
TEST_INPUTS = ["Incorrect command",
               "say Welcome to the mean poem machine", "poem reader", "exit"]

for test_input in TEST_INPUTS:
    read_cmd(test_input)
