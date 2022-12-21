#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open('../Mail Merge Project Start/Input/Letters/starting_letter.txt') as letter:
    invitation = letter.read()
with open('../Mail Merge Project Start/Input/Names/invited_names.txt') as names:
    name_list = names.read()
    name_list = name_list.strip()
for name in name_list.split():

    new_invitation = invitation.replace('[name]', name)
    with open(f'../Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt', 'w') as f:
        f.write(new_invitation)


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp