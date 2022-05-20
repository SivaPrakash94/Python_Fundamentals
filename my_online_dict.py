import json
from urllib.request import urlopen

def define(word, include_synonyms=False):
    word = word.casefold()
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    meanings_listDict =[]
    with urlopen(url) as f:
        info = json.load(f)
        #print(type(info))
        num_senses = len(info)
        #print(num_senses)
        for j in info:
            for key, value in j.items():
                if key.casefold() == 'meanings':
                    meanings_listDict.append(value)

        for i, senses in enumerate(meanings_listDict, start=1):
            print(f"Sense #{i}:")
            for meaning in senses:
                PoS = meaning['partOfSpeech']
                #print(PoS)
                lenOfDefn = len(meaning['definitions'])
                #print(lenOfDefn)
                #print(meaning['definitions'])
                defn_Dict = meaning['definitions']
                for all_defs in defn_Dict:
                    #print(all_defs)
                    defn = all_defs['definition']
                    synList = all_defs['synonyms']
                    #print(synList)
                    if (len(synList) != 0):
                        all_syns_str = ''
                        for s in synList:
                            all_syns_str += ', ' + s 
                        all_syns_str = all_syns_str[1:]
                    else:
                        all_syns_str = "NONE"
                    print(f"{word} ({PoS}) : {defn}")
                    if(include_synonyms is True):
                        if (len(synList) != 0):
                            print(f"{word} (synonyms) : {all_syns_str}")
                    else:
                        pass
                
            
        
                    
if __name__ == '__main__':
    define('python')
    #define('python', include_synonyms=True)
    #define('FORTE')
    #define('whiff', include_synonyms=True)
    #define('prograM', include_synonyms=True)
    #define('party', include_synonyms=True)
    #define('FORTE', include_synonyms=True)
    #define('SYNONYM', include_synonyms=True)
    define('SYNONYM')
