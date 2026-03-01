import time
from datetime import datetime
now = datetime.now()
#Modules required, plus the datetime required.


print("NO ERRORS")
print("DEVELOPER ENTER 'DEV' AS NAME")
print(now.strftime("DATE: %y-%m-%d"))
#If users see this, program ran correctly


time.sleep(0.5); print("PROGRAM STARTING")
print("INITIALIZED\n")
#Let users know program is starting


print("DARKNET INDEX / GUIDE")
print("VERSION 6.23.13")
#Introduction


name = input("[NAME] ").upper()
#Allows name input


if name == "":
    print("WELCOME USER")
else:
    print("WELCOME, " + name)
#So users dont actually need a name


print("\n ALL OPTIONS: ZONES [Z], OPERATIONS [O], ARCHTYPES [A], SITES [S], VERSION [V], HISTORY [H], DOCUMENATION [D], RESOURCES [RS], DEVELOPER [DR], RECOMMENDATIONS [R], EXIT")
#This prints the options


while True:
    document = input("\n[Input] ").upper()
    if document == "EXIT":
        print("Program will end. You cannot revert the command")
        time.sleep(1); print("3 SECOND[S] LEFT")
        time.sleep(1); print("2 SECOND[S] LEFT")
        time.sleep(1); print("PROGRAM SHUTTING DOWN")
        break
#This allows the loop.
    elif document == "Z":
        print("\nWhite-Zone: legal | Borderline-Gray-Zone: Practices mixed with legality and with illegal. But even the illegal parts are truly legal, just extremely ambiguous | Gray-Zone: Where most practices lose the inhibition to care about the law, but still not diving into illegal things, just slowly diving into it | Borderline-Black-Zone: Where those who were in the gray zone stops caring fully. Diving deep into crime, often because of needs & wants | Black-Zone: Often called the 'Point of no Return' by those who are still in the White-Zone or Gray-Zone. Where everything has some illegality in it.")

    elif document == "O":
        print("\nSmall-Time Operations: Actors doing small acts of crime in small quantities. Usually harder to track, but does less harm than others | Middle-Time Operations: Actors doing big acts in small quantities. Hard to spot, does more harm | Big-Time Operation: Big acts in large quantities, usually things like a well-organised militia, cartel, etc.")

    elif document == "A":
        print("\nTourist: New or visiting | Resident: Knows things that an actor would without being one | Operator: an actor, doing acts of crime or activities | Enforcer: Law Enforcement | Predator: Actors marketing sexual products.")

    elif document == "S":
        print("\nDarknet Army Forum: Forum of [edgy] sellers, varying from different things | DigAI: An uncensored AI. Willing to help with any projects | WSS: A Darknet chatroom, full of a different types of people, and featured on videos from people like Tranium | Tor.Link: A site that is a hub for other sites | NEXTCCV.CC: A Darknet market ranging from pre-made scripts, to CCV | CRYPTBB: A forum and a market [FURTHER RESEARCH REQUIRED] | DEF-CON: A legal site that uses onion for protection, where those of Cybersecurity, government cyber jobs, and more come together | DIGITAL THRIFT SHOP (PL): A market selling cheap items on the Darknet ranging from fake IDs to stolen items of medium to high value | GERMANIA: A Germanic-based market selling items [FURTHER RESEARCH REQUIRED] | BLACKMARK: A market selling a high variety of items [FURTHER RESEARCH REQUIRED] | THE HIDDEN WIKI: Not a site on the Darknet but is a wiki-style hub to other sites that are Darknet| Onionindex: Not a site on the Darknet but is a site that leads to other sites that are Darknet [FURTHER RESEARCH REQUIRED] | BREAKING BAD FORUM: A forum and a market place selling items to make the illegal substance Breaking Bad revolves around, also selling recipes alike | Onionlinks: a Darknet hub that links to other Darknet sites | Onion Identity Services: A market that sells fake IDs, fake Passports, and more | Dread: An onion site themed like Reddit, the original went down and now only copy-cats are left | Excavator: A Darknet hub that leads to other sites, even those that should never be interacted with | Anubis Market: A new, small, little site of vendors/sellers [FURTHER RESEARCH REQUIRED] | Osiris Market: A small trading site [FURTHER RESEARCH REQUIRED].")

    elif document == "D":
        print("\nThe nature of this program is educational [for those who are not willing to get on the Darknet/Market] and a safety guide for those who are on the Darknet. The legality of this program is lawfully in a gray-zone. As it depends on the user's purpose of consuming this program.")

    elif document == "V":
        print("Version: Official Release")

    elif document == "H":
        print("Version 00.00.00: added the introduction | Version 00.01.00: added the core options | Version 00.01.01: fixed the options selection | 01.01.01: added the 'not in' function | 01.01.02: fixed some typos | 02.01.02: finishes the core options of the program. It is now ready to be released to the public. Updates of course will still take place | 02.02.01: changed program name from 'Dark Web & Market Index / Guide' to 'Darknet & Market Index / Guide' as it is better fitting | 02.03.02: Added a donation link, to further fund projects and machines I use to make the projects | 02.04.02: Added a 'developer' section | 02.05.02: Added an add-on for developers | 02.05.03: Added a clear input section, so users know what to do | 03.05.03: Added the loop mechanism | 03.06.03: Forgot to remove the placeholder for Version History, sorry | 03.06.03: I am never doing placeholders again | 3.06.04: Fixed some typos. Should be clean for now | 3.06.05: Changed a few security ratings based off research | 3.06.06: Fixed some issues I accidentally created | 3.07.06: Removed the redundant 'not in' statement | 3.07.07: Added version shorthand next to the version-numbers | 3.07.08: Fixed some typos | 4.07.08: Program officially launched. First number changed to align. Will be going by 'V-O<>, O for OFFICIAL | 4.08.08: Added a largest donation amount section and changes the bulletin list from '-' to '#' | 4.09.08: Added two more options, Recommendations and Developer Recommendations | 4.10.08: made input simple | 4.10.08: Made some changes in donator area and enter-name-area | 4.11.08: Changed 'Dark Net' to 'Darknet' to be linguistically accurate | 4.11.10: Changed Dark Net to Darknet inside the printed text itself | 4.12.10: Added a Resources [rs] page to the selection and fixed the versioning issue in the History [h] page | 4.13.10: Removed the Security page from the program for easier maintenance, quicker updating, and easier user-usage | 4.14.10: Changed things in thye Archetypes page | 4.15.10: Added a 'news' page | 4.16.10: Added a mechanic that allows multiple variants of 'DEV' name | 4.17.10: Reverted mechanic back to previous as it did not work | 4.18.10: Removed donations and news page | 5.18.10: Added a countdown for the exit command and adde the Y/M/D time | 5.19.10: Added a timer to the beginning of the program. Tweaked end-program timer | 5.20.10: Changed the countdown timer to be a second longer | 5.21.10: Changed option names | 5.21.11: Fixed an obvious typo that I missed | 5.21.12: Changed the invalid input print to also show what the input the user did | 5.22.12: Restructured DEVELOPER name system | 5.22.13: Changed text color and input printing | 5.23.12: Added two new sites to the list | 6.23.13: Made it more DOS-like. I am getting more interested in old tech.")

    elif document == "DR":
        print("\nWarning: If you are a developer, please use the term 'DEV' as your name | All work done by you will be credited to you on GitHub.")

    elif document == "R":
        print("\nThe Recommended equipment for accessing and safely using the Darknet is the official Tor Browser on Personal Comouters and Laptops and Onion Browser on Smart Phones. The recommended VPN is ProtonVPN which will allow up to 10 regions for free.")

    elif document == "DS":
        print("\nRecommended equipment for developers accessing and safely using the Darknet is Tor Browser on Personal Computers and Laptops and Onion Browser on Smart Devices. Mullvad VPN is the best privacy-first VPN. Although has no free options.")

    elif document == "RS":
        print("These are the resources from the Recommended page of the program, please refer to Recommended [r] and Documentation [d] before continuing on this | Tor Browser: https://www.torproject.org/download/ | ProtonVPN: https://protonvpn.com/pricing | MullvadVPN: https://mullvad.net/en/download/vpn/")

    else:
        print(document + " is an invalid selection, please select an option listed above.")
#These are the options.


#write words here to find it anywhere in the code:
