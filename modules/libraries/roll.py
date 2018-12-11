from random import randint
import re

def roll_dice(argument):
    """Rolls dice based on a {x}d{y}+{z} pattern where the only necessary argument is at the very least a d{y}.
    This will return a message that can be sent.
    """
    message = ""
    detailed = "detailed" in argument
    firstcheck = re.search(r'[0-9]+d[0-9]+[+][0-9]+', argument)
    if firstcheck: 
        outcomeList = "{"
        matchString = str(firstcheck.group())
        argsList = matchString.split('d')
        splitArg = argsList[1].split('+')
        diceAmount = int(argsList[0])
        diceEyes = int(splitArg[0])
        bonus = int(splitArg[1])
        outcome = 0
        for _ in range(1, diceAmount + 1):
            randomNumber = randint(1, diceEyes)
            if detailed:
                outcomeList += str(randomNumber) + " , "
            outcome += randomNumber

        outcome += bonus

        # message = "Rolled " + str(diceAmount) + " d" + str(diceEyes) + " with a bonus of " + str(bonus) + " for a total count of: " + str(outcome)
        message = str(outcome)

        if detailed: 
            message += " | Details on the rolls: " + outcomeList + " }"
    
    else:
        secondCheck = re.search(r'[0-9]+d[0-9]+', argument)
        if secondCheck:
            outcomeList = "{ "
            matchedString = str(secondCheck.group())
            argsList = matchedString.split('d')
            diceAmount = int(argsList[0])
            diceEyes = int(argsList[1])
            outcome = 0
            for _ in range(1, diceAmount + 1):
                randomNumber = randint(1, diceEyes)
                if detailed:
                    outcomeList += str(randomNumber) + " , "
                outcome += randomNumber

            # message = "Rolled " + str(diceAmount) + " d" + str(diceEyes) + " for a total count of: " + str(outcome)
            message = str(outcome)

            if detailed: 
                message += " | Details on the rolls: " + outcomeList + " }"
        else:
            tertiaryCheck = re.search(r'd[0-9]+', argument)
            if tertiaryCheck:
                matchedString = str(tertiaryCheck.group())
                argsList = matchedString.split('d')
                diceEyes = int(argsList[1])
                outcome = randint(1, diceEyes)
                # message = "Rolled a d" + str(diceEyes) + " for: " + str(outcome)
                message = str(outcome)
            
            else:
                message = "That is not a valid die. Proper formatting is `>roll {x]d{y}+{z}`, `>roll {x]d{y}` or `>roll d{x}`"
    
    return message

            