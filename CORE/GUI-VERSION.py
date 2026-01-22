import tkinter as tk
from tkinter import scrolledtext

# Core data
supporters = ["tempuser1", "tempuser2"]

options_user = ["zones", "operations", "archetypes", "sites", "security", "version", "history", "documentation", "donations", "exit"]
options_dev = options_user + ["developer"]

# Functions
def process_input():
    document = user_input.get()
    output_text.config(state='normal')
    output_text.insert(tk.END, f"\nInput: {document}\n")
    user_input.delete(0, tk.END)

    if document == "exit":
        output_text.insert(tk.END, "Program ending...\n")
        root.after(1000, root.destroy)

    elif document == "zones":
        output_text.insert(tk.END, "\n White-Zone: legal | Borderline-Gray-Zone: Practices mixed with legality and with illegal. But even the illegal parts are truly legal, just extremely ambiguous | Gray-Zone: Where most practices lose the inhibition to care about the law, but still not diving into illegal things, just slowly diving into it | Borderline-Black-Zone: Where those who were in the gray zone stops caring fully. Diving deep into crime, often because of needs & wants | Black-Zone: Often called the 'Point of no Return' by those who are still in the White-Zone or Gray-Zone. Where everything has some illegality in it.\n")

    elif document == "operations":
        output_text.insert(tk.END, "\n Small-Time Operations: Actors doing small acts of crime in small quantities. Usually harder to track, but does less harm than others | Middle-Time Operations: Actors doing big acts in small quantities. Hard to spot, does more harm | Big-Time Operation: Big acts in large quantities, usually things like a well-organised militia, cartel, etc.\n")

    elif document == "archetypes":
        output_text.insert(tk.END, "\n Tourist: New or visiting | Resident: Knows things that an actor would without being one | Operator: an actor, doing acts of crime or activities | Blue: Law Enforcement | Dog: Actors marketing sexual products | White Hat: Those not part of the law, doing vigilante behaviour.\n")

    elif document == "sites":
        output_text.insert(tk.END, "\n Darknet Army Forum: Forum of [edgy] sellers, varying from different things | DigAI: An uncensored AI. Willing to help with any projects | WSS: A Darknet chatroom, full of a different types of people, and featured on videos from people like Tranium | Tor.Link: A site that is a hub for other sites | NEXTCCV.CC: A Dark Net market ranging from pre-made scripts, to CCV | CRYPTBB: A forum and a market [FURTHER RESEARCH REQUIRED] | DEF-CON: A legal site that uses onion for protection, where those of Cybersecurity, government cyber jobs, and more come together | DIGITAL THRIFT SHOP (PL): A market selling cheap items on the Dark Net ranging from fake IDs to stolen items of medium to high value | GERMANIA: A Germanic-based market selling items [FURTHER RESEARCH REQUIRED] | BLACKMARK: A market selling a high variety of items [FURTHER RESEARCH REQUIRED] | THE HIDDEN WIKI: Not a site on the Dark Net but is a wiki-style hub to other sites that are Dark Net| Onionindex: Not a site on the Dark Net but is a site that leads to other sites that are Dark Net [FURTHER RESEARCH REQUIRED] | BREAKING BAD FORUM: A forum and a market place selling items to make the illegal substance Breaking Bad revolves around, also selling recipes alike | Onionlinks: a Dark Net hub that links to other Dark Net sites | Onion Identity Services: A market that sells fake IDs, fake Passports, and more | Dread: An onion site themed like Reddit, the original went down and now only copy-cats are left | Excavator: A Dark Net hub that leads to other sites, even those that should never be interacted with.\n")

    elif document == "security":
        output_text.insert(tk.END, "\n Dark Net Army Forum: 6/10; Standard Dark Net security issues, although, there is a few issues with possible federal agents/police overwatch | DigAI: 8/10; Possible privacy issues due to it originating from corporate hands, although it has been changed to be less corporate | WSS: 7.6/10; Besides standard security issues in Dark Net sites, although there has been some overtly obvious sting operations regarding CSAM content | Tor.Link: 9.5/10; It being legal prevents government from looking at it's users most of the time[!!], although it can lead to unsafe sites | NEXTCCV.CC: 4/10; Likely scammers, honey-pots, and federal agents lurking | CRYPTBB: ?/10 | DEF-CON: 5/10; Depends on who you are. Due to it normally having federal agents, it might not be safe for certain types of people | DIGITAL THRIFT SHOP (PL): 4/10; Most likely is scammers, honey-pots, with federal agents lurking due to low prices of normally-high-priced items | GERMANIA: ?/10 | BLACKMARK: ?/10 | THE HIDDEN WIKI: 9/10; Standard web safety issues | Onionindex: 8.6/10; Some sites can/are unsafe and honey-pots. Plus security on the site itself seems lack-luster | BREAKING BAD FORUM: 7/10; Seems like average security, almost constant moderator activity | Onionlinks: 5/10; Normal security problems | Dread: 3/10; Mostly because only fakes who go by the same name exist, original site was took down | Excavator: 4/10; Leads to honey-pot sites, mostly foreign sites [foreign to Americans]\n")

    elif document == "documentation":
        output_text.insert(tk.END, "\n The nature of this program is educational [for those who are not willing to get on the Dark Net/Market] and a safety guide for those who are on the Dark Net. The legality of this program is lawfully in a gray-zone. As it depends on the user's purpose of consuming this program.\n")

    elif document == "version":
        output_text.insert(tk.END, "Version: Official Release\n")

    elif document == "history":
        output_text.insert(tk.END, "Version 00.00.00: added the introduction | Version 00.01.00: added the core options | Version 00.01.01: fixed the options selection | 01.01.01: added the 'not in' function | 01.01.02: fixed some typos | 02.01.02: finishes the core options of the program. It is now ready to be released to the public. Updates of course will still take place | 02.02.01: changed program name from 'Dark Web & Market Index / Guide' to 'Dark Net & Market Index / Guide' as it is better fitting | 02.03.02: Added a donation link, to further fund projects and machines I use to make the projects | 02.04.02: Added a 'developer' section | 02.05.02: Added an add-on for developers | 02.05.03: Added a clear input section, so users know what to do | 03.05.03: Added the loop mechanism | 03.06.03: Forgot to remove the placeholder for Version History, sorry | 03.06.03: I am never doing placeholders again | 3.06.04: Fixed some typos. Should be clean for now | 3.06.05: Changed a few security ratings based off research | 3.06.06: Fixed some issues I accidentally created | 3.07.06: Removed the redundant 'not in' statement | 3.07.07: Added version shorthand next to the version-numbers | 3.07.08: Fixed some typos | 4.07.08: Program officially launched. First number changed to align. Will be going by 'V-O<>, O for OFFICIAL\n")

    elif document == "developer":
        output_text.insert(tk.END, "\n Warning: If you are a developer, please use the term 'DEV' as your name | All work done by you will be credited to you on GitHub.\n")

    elif document == "donations":
        output_text.insert(tk.END, "Donation Links: https://cash.app/$onixiti\n")

    else:
        output_text.insert(tk.END, f"Invalid selection, please select an option listed above, {name}.\n")

    output_text.see(tk.END)
    output_text.config(state='disabled')

# GUI Setup
root = tk.Tk()
root.title("Dark Net & Market Index / Guide")

# Intro
intro_label = tk.Label(root, text="Dark Net & Market Index / Guide\nVersion O-04.07.08")
intro_label.pack()

# Name input
def submit_name():
    global name
    name = name_input.get()
    name_frame.destroy()
    output_text.config(state='normal')
    if name == "DEV":
        output_text.insert(tk.END, "\n Welcome back, DEVELOPER.\n")
        output_text.insert(tk.END, "\n All options: " + ", ".join(options_dev) + "\n")
    else:
        output_text.insert(tk.END, f"Welcome, {name}\n")
        output_text.insert(tk.END, "\n All options: " + ", ".join(options_user) + "\n")
    output_text.config(state='disabled')

name_frame = tk.Frame(root)
name_input = tk.Entry(name_frame)
name_input.pack(side=tk.LEFT)
name_submit = tk.Button(name_frame, text="Submit", command=submit_name)
name_submit.pack(side=tk.LEFT)
name_frame.pack()

# Output box
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=120, height=30, state='disabled')
output_text.pack()

# Input field
user_input = tk.Entry(root, width=100)
user_input.pack(side=tk.LEFT, padx=(10,0))
submit_button = tk.Button(root, text="Enter", command=process_input)
submit_button.pack(side=tk.LEFT)

# Display supporters
output_text.config(state='normal')
output_text.insert(tk.END, "\n Thank you to all who donated. The following names are those who have donated (handtyped):\n")
for user in supporters:
    output_text.insert(tk.END, f"- {user}\n")
output_text.insert(tk.END, "\n The support from you all is what keeps the project alive! I thank you endlessly!\n")
output_text.config(state='disabled')

root.mainloop()
