import time

print("\n Darknet & Market Index / Guide, Modulate")
print("Version MV-1.0.1")
#Introduction


time.sleep(0.5); print("\n All options: zones [z], operations [o], archetypes [a], sites [s], version [v], history [h], documentation [d], resources [rs], recommendations [r], developer [de], exit")
#This is to allow dev-specific things, user-input of name, and list all options.


while True:
    document = input("\n Input: ")
    if document == "exit":
        print("Program will end. You cannot revert the command.")
        time.sleep(0.5); break
#This allows the loop.
    elif document == "z":
        print("\n White-Zone: legal | Borderline-Gray-Zone: Practices mixed with legality and with illegal. But even the illegal parts are truly legal, just extremely ambiguous | Gray-Zone: Where most practices lose the inhibition to care about the law, but still not diving into illegal things, just slowly diving into it | Borderline-Black-Zone: Where those who were in the gray zone stops caring fully. Diving deep into crime, often because of needs & wants | Black-Zone: Often called the 'Point of no Return' by those who are still in the White-Zone or Gray-Zone. Where everything has some illegality in it.")

    elif document == "o":
        print("\n Small-Time Operations: Actors doing small acts of crime in small quantities. Usually harder to track, but does less harm than others | Middle-Time Operations: Actors doing big acts in small quantities. Hard to spot, does more harm | Big-Time Operation: Big acts in large quantities, usually things like a well-organised militia, cartel, etc.")
    
    elif document == "a":
        print("\n Tourist: New or visiting | Resident: Knows things that an actor would without being one | Operator: an actor, doing acts of crime or activities | Enforcer: Law Enforcement | Predator: Actors marketing sexual products.")

    elif document == "s":
        print("\n Darknet Army Forum: Forum of [edgy] sellers, varying from different things | DigAI: An uncensored AI. Willing to help with any projects | WSS: A Darknet chatroom, full of a different types of people, and featured on videos from people like Tranium | Tor.Link: A site that is a hub for other sites | NEXTCCV.CC: A Darknet market ranging from pre-made scripts, to CCV | CRYPTBB: A forum and a market [FURTHER RESEARCH REQUIRED] | DEF-CON: A legal site that uses onion for protection, where those of Cybersecurity, government cyber jobs, and more come together | DIGITAL THRIFT SHOP (PL): A market selling cheap items on the Darknet ranging from fake IDs to stolen items of medium to high value | GERMANIA: A Germanic-based market selling items [FURTHER RESEARCH REQUIRED] | BLACKMARK: A market selling a high variety of items [FURTHER RESEARCH REQUIRED] | THE HIDDEN WIKI: Not a site on the Darknet but is a wiki-style hub to other sites that are Darknet| Onionindex: Not a site on the Darknet but is a site that leads to other sites that are Darknet [FURTHER RESEARCH REQUIRED] | BREAKING BAD FORUM: A forum and a market place selling items to make the illegal substance Breaking Bad revolves around, also selling recipes alike | Onionlinks: a Darknet hub that links to other Darknet sites | Onion Identity Services: A market that sells fake IDs, fake Passports, and more | Dread: An onion site themed like Reddit, the original went down and now only copy-cats are left | Excavator: A Darknet hub that leads to other sites, even those that should never be interacted with.")

    elif document == "d":
        print("\n The nature of this program is educational [for those who are not willing to get on the Darknet/Market] and a safety guide for those who are on the Darknet. The legality of this program is lawfully in a gray-zone. As it depends on the user's purpose of consuming this program.")

    elif document == "v":
        print("Version: Modulated Version [MV]")

    elif document == "h":
        print("Version 01.00.00: Created Modulated Version | 1.0.1: Fixed some typos and versioning error.")

    elif document == "rs":
        print("Please refer to Documentation [d] before continuing on this | Tor Browser: https://www.torproject.org/download/ | ProtonVPN: https://protonvpn.com/pricing | MullvadVPN: https://mullvad.net/en/download/vpn/")

    else:
        print("Invalid.")
#These are the options.


#write words here to find it anywhere in the code:
