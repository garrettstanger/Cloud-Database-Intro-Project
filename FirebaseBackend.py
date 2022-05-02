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
    u'spec1': u'Protection',
    u'spec2': u'Fury',
    u'spec3': u'Arms'
})
doc_ref = db.collection(u'classes').document(u'Demon Hunter')
doc_ref.set({
    u'spec1': u'Havoc',
    u'spec2': u'Vengeance'
})
doc_ref = db.collection(u'classes').document(u'Paladin')
doc_ref.set({
    u'spec1': u'Holy',
    u'spec2': u'Retribution',
    u'spec3': u'Protection'
})
doc_ref = db.collection(u'classes').document(u'Death Knight')
doc_ref.set({
    u'spec1': u'Blood',
    u'spec2': u'Unholy',
    u'spec3': u'Frost'
})
doc_ref = db.collection(u'classes').document(u'Mage')
doc_ref.set({
    u'spec1': u'Frost',
    u'spec2': u'Arcane',
    u'spec3': u'Fire'
})
doc_ref = db.collection(u'classes').document(u'Warlock')
doc_ref.set({
    u'spec1': u'Destruction',
    u'spec2': u'Demonology',
    u'spec3': u'Affliction'
})
doc_ref = db.collection(u'classes').document(u'Priest')
doc_ref.set({
    u'spec1': u'Holy',
    u'spec2': u'Shadow',
    u'spec3': u'Discipline'
})
doc_ref = db.collection(u'classes').document(u'Shaman')
doc_ref.set({
    u'spec1': u'Elemental',
    u'spec2': u'Enhancement',
    u'spec3': u'Restoration'
})
doc_ref = db.collection(u'classes').document(u'Rogue')
doc_ref.set({
    u'spec1': u'Assassination',
    u'spec2': u'Outlaw',
    u'spec3': u'Subtlety'
})
doc_ref = db.collection(u'classes').document(u'Monk')
doc_ref.set({
    u'spec1': u'Windwalker',
    u'spec2': u'Mistweaver',
    u'spec3': u'Brewmaster'
})
doc_ref = db.collection(u'classes').document(u'Hunter')
doc_ref.set({
    u'spec1': u'Marksmanship',
    u'spec2': u'Beast Mastery',
    u'spec3': u'Survival'
})
doc_ref = db.collection(u'classes').document(u'Druid')
doc_ref.set({
    u'spec1': u'Balance',
    u'spec2': u'Feral',
    u'spec3': u'Guardian',
    u'spec4': u'Restoration'
})
## The Roles collection will probably remain static
doc_ref = db.collection(u'roles').document(u'Healer')
doc_ref.set({
    u'option1': u'Restoration Druid',
    u'option2': u'Mistweaver Monk',
    u'option3': u'Holy Paladin',
    u'option4': u'Holy Priest',
    u'option5': u'Restoration Shaman',
    u'option6': u'Discipline Priest'
})
doc_ref = db.collection(u'roles').document(u'Tank')
doc_ref.set({
    u'option1': u'Blood Death Knight',
    u'option2': u'Vengeance Demon Hunter',
    u'option3': u'Guardian Druid',
    u'option4': u'Brewmaster Monk',
    u'option5': u'Protection Paladin',
    u'option6': u'Protection Warrior'

})
doc_ref = db.collection(u'roles').document(u'DPS')
doc_ref.set({
    u'option1': u'Frost Death Knight',
    u'option2': u'Unholy Death Knight',
    u'option3': u'Havoc Demon Hunter',
    u'option4': u'Balance Druid',
    u'option5': u'Feral Druid',
    u'option6': u'Beast Mastery Hunter',
    u'option7': u'Marksmanship Hunter',
    u'option8': u'Survival Hunter',
    u'option9': u'Arcane Mage',
    u'option10': u'Fire Mage',
    u'option11': u'Frost Mage',
    u'option12': u'Windwalker Monk',
    u'option13': u'Retribution Paladin',
    u'option14': u'Shadow Priest',
    u'option15': u'Assassination Rogue',
    u'option16': u'Outlaw Rogue',
    u'option17': u'Subtlety Rogue',
    u'option18': u'Elemental Shaman',
    u'option19': u'Enhancement Shaman',
    u'option20': u'Affliction Warlock',
    u'option21': u'Demonology Warlock',
    u'option22': u'Destruction Warlock',
    u'option23': u'Arms Warrior',
    u'option24': u'Fury Warrior'
})

## The Top 5 DPS List collection will be dynamic because
## the list will could change with each patch. This is where
## I will implement the insert, modify, and delete ability.
dps_Data = {u'EnhancementShaman': 0,
            u'BalanceDruid': 0,
            u'FrostMage': 0,
            u'ElementalShaman': 0, 
            u'FireMage': 0}
db.collection(u'Top 5 DPS List').document(u'Specializations').set(dps_Data)
## Update Enhancement Shamans DPS value
db.collection('Top 5 DPS List').document('Specializations').update({"EnhancementShaman" : 18900})
## Update the rest of the values
db.collection('Top 5 DPS List').document('Specializations').update({"BalanceDruid" : 18097})
db.collection('Top 5 DPS List').document('Specializations').update({"FrostMage" : 17896})
db.collection('Top 5 DPS List').document('Specializations').update({"ElementalShaman" : 17642})
db.collection('Top 5 DPS List').document('Specializations').update({"FireMage" : 17619})

## Delete Frost Mage from the DPS List
db.collection("Top 5 DPS List").document("Specializations").update({"FrostMage" : firestore.DELETE_FIELD})

## Add Unholy Death Knight to the DPS List
db.collection("Top 5 DPS List").document("Specializations").update({"UnholyDeathKnight" : 16737})

## Attempt at simple interface
# userResponse = 0
# while userResponse != 4:
#     print("1. View Classes with Specialization\n2. View Top 5 DPS\n3. Update Top DPS Damage Value")
#     userResponse = input("Input Selection \n>")
#     if userResponse == 1:
#         ## Display Classes with their Specializations
#         classes_ref = db.collection(u'classes')
#         docs = classes_ref.stream()

#         for doc in docs:
#             print(f'{doc.id} => {doc.to_dict()}')

#         # Display Roles with their associated classes
#         roles_ref = db.collection(u'roles')
#         docs = roles_ref.stream()
#     elif userResponse == 2:
#         topDPS_ref = db.collection(u'Top 5 DPS List')
#         docs = classes_ref.stream()

#         for doc in docs:
#             print(f'{doc.id} => {doc.to_dict()}')
#     else:
#         print("Invalid Response")

## Updates the top DPS with best single target damage.
### When updating the data or for this case the single target damage
### you can't have non alpha numeric characters in the name.
### I had to change Enhancement Shaman to EnhancementShaman to get it to work.

# def updateDPS():


#for doc in docs:
#    print(f'{doc.id} => {doc.to_dict()}')