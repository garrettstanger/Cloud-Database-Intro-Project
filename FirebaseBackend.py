from abc import update_abstractmethods
from re import L
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Using a service account with path to JSON file
cred = credentials.Certificate('cloud-database-intro-project-27c80c0f9082.json')
firebase_admin.initialize_app(cred)
# Create the database
db = firestore.client()
## The Classes collection will probably remain static.
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

## Query for Classes with their specializations
def displayClasses(db):
    ## Display Classes with their Specializations
        classes_ref = db.collection(u'classes')
        docs = classes_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
## Display Roles
def displayRoles(db):
    roles_ref = db.collection(u'roles')
    docs = roles_ref.stream()
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
## View Top DPS
def displayTopDPS(db):
        topDPS_ref = db.collection(u'Top DPS List')
        docs = topDPS_ref.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')
## Update DPS function
def updateDPS(db):
    dps_spec = input("DPS to update \n> ").lower().replace(" ", "")
    damage = float(input("Updated damage value \n> "))
    dps_role = str(input("Role of Specialization (Tank, DPS, Healer)\n> "))
    data = {"damage" : damage, "dps_role" : dps_role}
    exceptions = ['blooddeathknight','unholydeathknight','frostdeathknight',
    'havocdemonhunter', 'vengeancedemonhunter','balancedruid','feraldruid',
    'guardiandruid','restorationdruid','marksmanshiphunter','beastmasteryhunter',
    'survivalhunter','frostmage','arcanemage','firemage','windwalkermonk',
    'mistweavermonk','brewmastermonk','holypaladin','retributionpaladin',
    'protectionpaladin','holypriest','shadowpriest','disciplinepriest',
    'assassinationrogue','outlawrogue','subletyrogue','elementalshaman',
    'enhancementshaman','restorationshaman','destructionwarlock','demonologywarlock',
    'afflictionwarlock','protectionwarrior','furywarrior','armswarrior']
    if dps_spec in exceptions:
        db.collection("Top DPS List").document(dps_spec).set(data)
        change_notification(db, f"{dps_spec} class updated with {damage} single target damage.")
    else:
        print("Invalid Entry: CHECK YOUR SPELLING")
## Delete DPS function
def deleteDPS(db):
    dps_spec = input("Select Class \n> ").lower().replace(" ","")
    user_delete = input("Remove dps_role or damage? \n> ").lower().replace(" ","")
    exceptions = ['blooddeathknight','unholydeathknight','frostdeathknight',
    'havocdemonhunter', 'vengeancedemonhunter','balancedruid','feraldruid',
    'guardiandruid','restorationdruid','marksmanshiphunter','beastmasteryhunter',
    'survivalhunter','frostmage','arcanemage','firemage','windwalkermonk',
    'mistweavermonk','brewmastermonk','holypaladin','retributionpaladin',
    'protectionpaladin','holypriest','shadowpriest','disciplinepriest',
    'assassinationrogue','outlawrogue','subletyrogue','elementalshaman',
    'enhancementshaman','restorationshaman','destructionwarlock','demonologywarlock',
    'afflictionwarlock','protectionwarrior','furywarrior','armswarrior']
    if user_delete == "dps_role":
        if dps_spec in exceptions:
            db.collection("Top DPS List").document(dps_spec).update({user_delete : firestore.DELETE_FIELD})
            change_notification(db, f"Removed {user_delete} from {dps_spec}")
        else:
            print("Invalid Entry: CHECK YOUR SPELLING")
    elif user_delete == "damage":
        if dps_spec in exceptions:
            db.collection("Top DPS List").document(dps_spec).update({user_delete : firestore.DELETE_FIELD})
            change_notification(db, f"{user_delete} from {dps_spec} deleted")
        else:
            print("Invalid Entry: CHECK YOUR SPELLING")

def queryDPS(db):
    damage = float(input("Damage value parameter: \n> "))
    boolean = str(input("Greater than or less than? (> or <)\n-- "))
    results = db.collection("Top DPS List").where("damage", boolean, damage).get()
    print()
    print("Results:")
    for result in results:
        data = result.to_dict()
        print(f"{result.id:<10} {data['damage']}")

def change_notification(db, notification):
    data = {"notification" : notification, "timestamp" : firestore.SERVER_TIMESTAMP}
    db.collection("log").add(data)


## Attempt at simple interface
userResponse = 999
while userResponse != "0":
    print("0. Quit")
    print("1. View Classes with Specialization")
    print("2. Display Roles")
    print("3. View Top DPS")
    print("4. Add/Update Top DPS class")
    print("5. Remove Top DPS damage or role")
    print("6. View DPS above or below value")
    
    userResponse = input("Input Selection \n> ")
    if userResponse == "1":
        displayClasses(db)
    elif userResponse == "2":
        displayRoles(db)
    elif userResponse == "3":
        displayTopDPS(db)
    elif userResponse == "4":
        updateDPS(db)
    elif userResponse == "0":
        pass
    elif userResponse == "5":
        deleteDPS(db)
    elif userResponse == "6":
        queryDPS(db)
    else:
        print("Invalid Response")



## The Top DPS List collection, starts with adding a small
## dps_Data dictionary.
# dps_Data = {u'enhancementshaman': 0,
#             u'balancedruid': 0,
#             u'frostmage': 0,
#             u'elementalshaman': 0, 
#             u'firemage': 0}
# db.collection(u'Top DPS List').document(u'Specializations').set(dps_Data)
# ## Update Enhancement Shamans DPS value
# ### When updating the data or for this case the single target damage
# ### you can't have non alpha numeric characters in the name.
# ### I had to change Enhancement Shaman to EnhancementShaman to get it to work.
# db.collection('Top DPS List').document('Specializations').update({"enhancementshaman" : 18900})
# ## Update the rest of the values
# db.collection('Top DPS List').document('Specializations').update({"balancedruid" : 18097})
# db.collection('Top DPS List').document('Specializations').update({"frostmage" : 17896})
# db.collection('Top DPS List').document('Specializations').update({"elementalshaman" : 17642})
# db.collection('Top DPS List').document('Specializations').update({"firemage" : 17619})

## Delete Frost Mage from the DPS List
#db.collection("Top DPS List").document("Specializations").update({"frostmage" : firestore.DELETE_FIELD})

## Add Unholy Death Knight to the DPS List
#db.collection("Top DPS List").document("Specializations").update({"unholydeathknight" : 16737})
        
# Display Roles with their associated classes
# roles_ref = db.collection(u'roles')
# docs = roles_ref.stream()