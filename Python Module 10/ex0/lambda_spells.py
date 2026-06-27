#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x : x['power'])

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x['power'] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '* ' + x + ' *', spells))

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(map(lambda x: x['power'], mages))
    min_power = min(map(lambda x: x['power'], mages))
    avg_power = round(sum(map(lambda x: x['power'], mages))/len(mages),2)
    return({'max_power': max_power, 'min_power': min_power, 'avg_power': avg_power})


if __name__ == "__main__":
    artifact = [
        {'name': 'Lam','power': 10, 'type' : 'Human'},
        {'name':'Vang','power': 20, 'type' :'Cho'},
        {'name':'Miu','power': 5, 'type' : 'Meo'},
        {'name':'Coc','power': 3, 'type' : 'half'},
        {'name':'Voi','power': 40, 'type' : 'animal'}
    ]
    
    spell = ['hello', 'this', 'is', 'magical', 'spell']
    
    print(artifact_sorter(artifact))
    print(power_filter(artifact, 5))
    print(spell_transformer(spell))
    print(mage_stats(artifact))
