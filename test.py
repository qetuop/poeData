import poeq
import poed
import json

if __name__ == '__main__':
    config = json.loads(open('config.json').read())
    account = config['account']
    getStandard = config['getStandard']
    league = config['league']
    poesessid = config['poesessid']
    character = config['character']
    SLEEP = config['sleep']

    poeq.setup(league, account, poesessid)

    out = poeq.getCharacterInventory(character)
    charDict = poeq.readFromFile(character)
    print(charDict)
    characterDict = charDict['character']

    characterDict['__class__'] = 'CharacterInfo'
    characterDict['__module__'] = 'poed'
    if 'class' in characterDict:
        characterDict['class_'] = characterDict.pop('class')
    data2 = json.dumps(characterDict)
    charInfo = json.loads(data2, object_hook=poed.dict_to_obj)

    print(charInfo)

    #charInfo = poed.dict_to_obj(characterDict)