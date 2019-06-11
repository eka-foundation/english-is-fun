import requests
import json

def similar(s, n=10, minimum_score=10000):
    
    '''Find similar words or phrases
    
    s : str
        Either a word or a phrase.
    n : int
        Number of results to return
    minimum_score : int
        The minimum similarity score
        
    Example:
    
        # single word 
        similar('now', 20)
    
        # phrase
        similar('how are you', 10, 20000)
        
    NOTE: In case of phrase, spaces will be replaced with '+'
    
    '''
    
    s = s.replace(' ', '+')
    
    r = requests.get('http://api.datamuse.com/words?ml=' + s)
    results = json.loads(r.content)
    
    out = []
    for word in results[:n]:
        if word['score'] >= minimum_score:
            out.append(word['word'])
            
    return out
