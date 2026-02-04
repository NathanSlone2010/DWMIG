print("Darknet & Market Index / Guide, Experimental")
#Introduction

name = input("\n Enter username / name: ")
#This is to allow actual name input

answer = input("Do you want to proceed? y / n: ")


while True:
    if answer == "y":
        print("\n All options: zones [z], operations [o], archetypes [a], sites [s], version [v], history [h], documentation [d], Resources [rs], donations [do], developer [de], developer recommendations [dr], exit")
        print("Experimental Version option: Break Counter [bc]")
    if answer == "n":
        break
    document = input("\n Selection: ")
    if document == "exit":
        break
    #The above allows a loop
    if document == "w":
        print("WARNING: THIS PROGRAM IS EXPERIMENTAL VERSION OF THE DARKNET & MARKET INDEX / GUIDE. VOID STUDIOS DOES NOT RECOMMEND USAGE OF THIS PROGRAM UNLESS A DEVELOPER OR HAVE BASIC PROGRAMMING KNOWLEDGE OF PYTHON CODING LANGUAGE.")

    elif document == "z":
        print("\n White-Zone: legal | Borderline-Gray-Zone: Practices mixed with legality and with illegal. But even the illegal parts are truly legal, just extremely ambiguous | Gray-Zone: Where most practices lose the inhibition to care about the law, but still not diving into illegal things, just slowly diving into it | Borderline-Black-Zone: Where those who were in the gray zone stops caring fully. Diving deep into crime, often because of needs & wants | Black-Zone: Often called the 'Point of no Return' by those who are still in the White-Zone or Gray-Zone. Where everything has some illegality in it.")

    elif document == "o":
        print("\n Small-Time Operations: Actors doing small acts of crime in small quantities. Usually harder to track, but does less harm than others | Middle-Time Operations: Actors doing big acts in small quantities. Hard to spot, does more harm | Big-Time Operation: Big acts in large quantities, usually things like a well-organised militia, cartel, etc.")

    elif document == "a":
        print("\n Tourist: New or visiting | Resident: Knows things that an actor would without being one | Operator: an actor, doing acts of crime or activities | Enforcers: Law Enforcement | Predator: Actors marketing sexual products.")

    elif document == "s":
        print("\n Darknet Army Forum: Forum of [edgy] sellers, varying from different things | DigAI: An uncensored AI. Willing to help with any projects | WSS: A Darknet chatroom, full of a different types of people, and featured on videos from people like Tranium | Tor.Link: A site that is a hub for other sites | NEXTCCV.CC: A Darknet market ranging from pre-made scripts, to CCV | CRYPTBB: A forum and a market [FURTHER RESEARCH REQUIRED] | DEF-CON: A legal site that uses onion for protection, where those of Cybersecurity, government cyber jobs, and more come together | DIGITAL THRIFT SHOP (PL): A market selling cheap items on the Darknet ranging from fake IDs to stolen items of medium to high value | GERMANIA: A Germanic-based market selling items [FURTHER RESEARCH REQUIRED] | BLACKMARK: A market selling a high variety of items [FURTHER RESEARCH REQUIRED] | THE HIDDEN WIKI: Not a site on the Darknet but is a wiki-style hub to other sites that are Darknet| Onionindex: Not a site on the Darknet but is a site that leads to other sites that are Darknet [FURTHER RESEARCH REQUIRED] | BREAKING BAD FORUM: A forum and a market place selling items to make the illegal substance Breaking Bad revolves around, also selling recipes alike | Onionlinks: a Darknet hub that links to other Darknet sites | Onion Identity Services: A market that sells fake IDs, fake Passports, and more | Dread: An onion site themed like Reddit, the original went down and now only copy-cats are left | Excavator: A Darknet hub that leads to other sites, even those that should never be interacted with.")

    elif document == "d":
        print("\n The nature of this program is educational [for those who are not willing to get on the Darknet/Market] and a safety guide for those who are on the Darknet. The legality of this program is lawfully in a gray-zone. As it depends on the user's purpose of consuming this program.")

    elif document == "v":
        print("Version: Experimental Version")

    elif document == "sv":
        print("This program is the Experimental Version of the project Darknet & Market Index / Guide by Nathan T. Slone. The following link leads to the Official Version, the recommended version of the program. | https://github.com/NathanSlone2010/DWMIG/tree/main/CORE")

    elif document == "de":
        print("\n Warning: If you are a developer, please use the term 'DEV' as your name | All work done by you will be credited to you on GitHub.")

    elif document == "do":
        print("Donation Links: https://cash.app/$onixiti")

    elif document == "r":
        print("\n The Recommended equipment for accessing and safely using the Darknet is the official Tor Browser on Personal Comouters and Laptops and Onion Browser on Smart Phones. The recommended VPN is ProtonVPN which will allow up to 10 regions for free.")

    elif document == "dr":
        print("\n Recommended equipment for developers accessing and safely using the Darknet is Tor Browser on Personal Computers and Laptops and Onion Browser on Smart Devices. Mullvad VPN is the best privacy-first VPN. Although has no free options.")

    elif document == "rs":
        print("These are the resources from the Recommended page of the program, please refer to Recommended [r] and Documentation [d] before continue on this | Tor Browser: https://www.torproject.org/download/ | ProtonVPN: https://protonvpn.com/pricing | MullvadVPN: https://mullvad.net/en/download/vpn/")

    elif document == "bc":
        print("Break Counter: 1 | DEVs, please update this whenever the code breaks.")

    else:
        print("Invalid selection, please select an option listed above, " + name + ".")
#These are the options.


supporters = ["tempuser1", "tempuser2"]
print("\n Thank you to all who donated. The following names are those who have donated (handtyped):")
for user in supporters:
    print("~$ " + user)
print("Largest donation amount: $0")
print("\n The support from you all is what keeps the project alive! I thank you endlessly!")
#This is so we can thank those who are generous as we do not deserve their kindness.

#write words here to find it anywhere in the code:
