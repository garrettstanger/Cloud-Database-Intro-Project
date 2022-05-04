from abc import update_abstractmethods
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Using a service account with path to JSON file
cred = credentials.Certificate('cloud-database-intro-project-27c80c0f9082.json')
firebase_admin.initialize_app(cred)
# Create the database
db = firestore.client()
## The Classes collection will probably remain static.
## I can query the specializtions for a class.
doc_ref = db.collection(u'classes').document(u'Warrior')
doc_ref.set({
    u'specializations': [u'Protection', u'Fury', u'Arms' ]
})
doc_ref = db.collection(u'classes').document(u'Demon Hunter')
doc_ref.set({
    u'specializations': [u'Havoc', u'Vengeance']
})
doc_ref = db.collection(u'classes').document(u'Paladin')
doc_ref.set({
    u'specializations': [u'Holy', u'Retribution', u'Protection']
})
doc_ref = db.collection(u'classes').document(u'Death Knight')
doc_ref.set({
    u'specializations': [u'Blood', u'Unholy', u'Frost']
})
doc_ref = db.collection(u'classes').document(u'Mage')
doc_ref.set({
    u'specializations': [u'Frost', u'Arcane', u'Fire']
})
doc_ref = db.collection(u'classes').document(u'Warlock')
doc_ref.set({
    u'specializations': [u'Destruction', u'Demonology', u'Affliction']
})
doc_ref = db.collection(u'classes').document(u'Priest')
doc_ref.set({
    u'specializations': [u'Holy', u'Shadow', u'Discipline']
})
doc_ref = db.collection(u'classes').document(u'Shaman')
doc_ref.set({
    u'specializations': [u'Elemental', u'Enhancement', u'Restoration']
})
doc_ref = db.collection(u'classes').document(u'Rogue')
doc_ref.set({
    u'specializations': [u'Assassination', u'Outlaw', u'Subtlety']
})
doc_ref = db.collection(u'classes').document(u'Monk')
doc_ref.set({
    u'specializations': [u'Windwalker', u'Mistweaver', u'Brewmaster']
})
doc_ref = db.collection(u'classes').document(u'Hunter')
doc_ref.set({
    u'specializations': [u'Marksmanship', u'Beast Mastery', u'Survival']
})
doc_ref = db.collection(u'classes').document(u'Druid')
doc_ref.set({
    u'specializations': [ u'Balance', u'Feral', u'Guardian', u'Restoration']
})
doc_ref = db.collection(u'roles').document(u'Healer')
doc_ref.set({
    u'Healer Specializations': 
    [u'Restoration Druid', u'Mistweaver Monk', u'Holy Paladin', u'Holy Priest', 
    u'Restoration Shaman', u'Discipline Priest']
})
doc_ref = db.collection(u'roles').document(u'Tank')
doc_ref.set({
    u'Tank Specializations': 
    [u'Blood Death Knight', u'Vengeance Demon Hunter', u'Guardian Druid', 
    u'Brewmaster Monk', u'Protection Paladin', u'Protection Warrior']

})
doc_ref = db.collection(u'roles').document(u'DPS')
doc_ref.set({
    u'DPS Specalizations': 
    [u'Frost Death Knight', u'Unholy Death Knight', u'Havoc Demon Hunter', u'Balance Druid',
    u'Feral Druid', u'Beast Mastery Hunter', u'Marksmanship Hunter', u'Survival Hunter',
    u'Arcane Mage', u'Fire Mage', u'Frost Mage', u'Windwalker Monk', u'Retribution Paladin',
    u'Shadow Priest', u'Assassination Rogue', u'Outlaw Rogue', u'Subtlety Rogue', u'Elemental Shaman',
    u'Enhancement Shaman', u'Affliction Warlock', u'Demonology Warlock', u'Destruction Warlock',
    u'Arms Warrior', u'Fury Warrior']
})

## The Top DPS List collection, starts with adding a small
## dps_Data dictionary.
dps_Data = {u'enhancementshaman': 0,
            u'balancedruid': 0,
            u'frostmage': 0,
            u'elementalshaman': 0, 
            u'firemage': 0}
db.collection(u'Top DPS List').document(u'Specializations').set(dps_Data)
## Update Enhancement Shamans DPS value
### When updating the data or for this case the single target damage
### you can't have non alpha numeric characters in the name.
### I had to change Enhancement Shaman to EnhancementShaman to get it to work.
db.collection('Top DPS List').document('Specializations').update({"enhancementshaman" : 18900})
## Update the rest of the values
db.collection('Top DPS List').document('Specializations').update({"balancedruid" : 18097})
db.collection('Top DPS List').document('Specializations').update({"frostmage" : 17896})
db.collection('Top DPS List').document('Specializations').update({"elementalshaman" : 17642})
db.collection('Top DPS List').document('Specializations').update({"firemage" : 17619})

## Delete Frost Mage from the DPS List
#db.collection("Top DPS List").document("Specializations").update({"frostmage" : firestore.DELETE_FIELD})

## Add Unholy Death Knight to the DPS List
#db.collection("Top DPS List").document("Specializations").update({"unholydeathknight" : 16737})

## Query for Classes with their specializations
def displayClasses():
    ## Display Classes with their Specializations
        classes_ref = db.collection(u'classes')
        docs = classes_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

## View Top DPS
def displayTopDPS():
        topDPS_ref = db.collection(u'Top DPS List')
        docs = topDPS_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
## Update DPS function
def updateDPS():
    user_input_DPS_change = input("DPS to update \n> ").lower().replace(" ", "")
    user_input_damage_change = input("Updated damage value \n> ")
    exceptions = ['blooddeathknight','unholydeathknight','frostdeathknight',
    'havocdemonhunter', 'vengeancedemonhunter','balancedruid','feraldruid',
    'guardiandruid','restorationdruid','marksmanshiphunter','beastmasteryhunter',
    'survivalhunter','frostmage','arcanemage','firemage','windwalkermonk',
    'mistweavermonk','brewmastermonk','holypaladin','retributionpaladin',
    'protectionpaladin','holypriest','shadowpriest','disciplinepriest',
    'assassinationrogue','outlawrogue','subletyrogue','elementalshaman',
    'enhancementshaman','restorationshaman','destructionwarlock','demonologywarlock',
    'afflictionwarlock','protectionwarrior','furywarrior','armswarrior']
    if user_input_DPS_change in exceptions:
        db.collection("Top DPS List").document("Specializations").update({user_input_DPS_change : user_input_damage_change})
        print(f"{user_input_DPS_change} class updated with {user_input_damage_change} single target damage.")
    else:
        print("Invalid Entry: CHECK YOUR SPELLING")
## Delete DPS function
def deleteDPS():
    user_input_DPS_delete = input("DPS to delete \n> ").lower().replace(" ","")
    exceptions = ['blooddeathknight','unholydeathknight','frostdeathknight',
    'havocdemonhunter', 'vengeancedemonhunter','balancedruid','feraldruid',
    'guardiandruid','restorationdruid','marksmanshiphunter','beastmasteryhunter',
    'survivalhunter','frostmage','arcanemage','firemage','windwalkermonk',
    'mistweavermonk','brewmastermonk','holypaladin','retributionpaladin',
    'protectionpaladin','holypriest','shadowpriest','disciplinepriest',
    'assassinationrogue','outlawrogue','subletyrogue','elementalshaman',
    'enhancementshaman','restorationshaman','destructionwarlock','demonologywarlock',
    'afflictionwarlock','protectionwarrior','furywarrior','armswarrior']
    if user_input_DPS_delete in exceptions:
        db.collection("Top DPS List").document("Specializations").update({user_input_DPS_delete : firestore.DELETE_FIELD})
        print(f"{user_input_DPS_delete} removed from Top DPS List.")
    else:
        print("Invalid Entry: CHECK YOUR SPELLING")


    

## Display Roles
def displayRoles():
    roles_ref = db.collection(u'roles')
    docs = roles_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
## Attempt at simple interface
userResponse = 999
while userResponse != "0":
    print("0. Quit")
    print("1. View Classes with Specialization")
    print("2. Display Roles")
    print("3. View Top DPS")
    print("4. Add/Update Top DPS class")
    print("5. Remove Top DPS class")
    
    userResponse = input("Input Selection \n> ")
    if userResponse == "1":
        displayClasses()
    elif userResponse == "2":
        displayRoles()
    elif userResponse == "3":
        displayTopDPS()
    elif userResponse == "4":
        updateDPS()
    elif userResponse == "0":
        pass
    elif userResponse == "5":
        deleteDPS()
    else:
        print("Invalid Response")
        
# Display Roles with their associated classes
# roles_ref = db.collection(u'roles')
# docs = roles_ref.stream()