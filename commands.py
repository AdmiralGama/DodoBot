import random

def command_parser(command, args):
    response = 'test'

    random.seed()
    
    if command == 'help':
        return help_parser(args)
    elif command == 'try':
        return try_processor(args)
    elif command == 'resources':
        with open ('resources.txt', 'r') as resources_file:
            return resources_file.read()
    elif command == 'pout':
        return 'https://images-ext-1.discordapp.net/external/towu7V9I3WgEfhQ_QNrKi9zTFZN6bPxujyc3knpCLts/https/cdn.weeb.sh/images/BJOqlyKP-.gif'
    elif command == 'rng':
        if args[0] == 'coin':
            if random.getrandbits(1) == 1: 
                response = 'Heads!'
            else:
                response = 'Tails!'
        elif args[0] == 'wep':
            response = rand_wep()
        elif args[0][0] == 'd':
            response = random.randint(1, int(args[0][1:]))

    return response

def help_parser(args):
    response = '(+ next to command means more info available with help [command])\n__**Commands:**__\n+Try: Tries pronouns and name\nResources: Gets a list of LGBTQ resources\nStats: Gets bot stats\n\n__**Administration:**__\nPrefix: Changes bot prefix\nUpdate: Hot reloads the bot'
    
    if len(args) != 0:
        if args[0] == 'try':
            response = 'Lets you try pronouns and names\nSyntax: try [subjective] [name]\n  or try [subjective] [objective] [possesive] [reflexive] [name]\n\noptional end argument "special"\n(used if personal pronoun is they or others with similar format)\n\nExamples: try he bob\n  or try they bob special\n  or try they her his themself bob special'

    return response

def try_processor(args):
    result = 'something went wrong\n'
    lastrandom = -1
    
    if len(args) == 3:
        if args[2] == 'special':
            file = 'phrasesthey.txt'
    elif len(args) == 6:
        if args[5] == 'special':
            file = 'phrasesthey.txt'
    else:
        file = 'phrases.txt'

    with open(file, 'r') as phrases:
        lines = phrases.readlines()

        if len(args) == 2 or len(args) == 3:
            name = args[1]

            if args[0] == 'he':
                args = ['he', 'him', 'his', 'himself', name]
            elif args[0] == 'she':
                args = ['she', 'her', 'her', 'herself', name]
            elif args[0] == 'they':
                args = ['they', 'them', 'their', 'themself', name]
    
        if file == 'phrasesthey.txt':
            args[0] = args[0].capitalize()
        args[4] = args[4].capitalize()

        result = ''

        for i in range(3):
            val = random.randrange(len(lines))
            while val == lastrandom:
                val = random.randrange(len(lines))
            
            lastrandom = val

            phrase = str(lines[val])
            
            for i in range(len(args)):
                phrase = phrase.replace(str(i), args[i])
            
            result += '-' + phrase

    return result

def rand_wep():
    weapons = ["CB", "DB", "GS", "SWAX", "HBG", "LBG", "Bow", "IG", "Lance", "GL", "HH", "Hammer", "LS", "SnS"]
    return weapons[random.randint(0, 13)]