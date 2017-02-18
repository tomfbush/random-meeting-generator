import random

# TODO: continue to add to these lists of terms

entity = ['project', 'campaign', 'business', 'media', 'brand', 'DR', 'performance', 'social', 'best practice', 'client', 'internal']
type = ['planning', 'strategy', 'status', 'audit', 'insights']
occasion = ['brainstorm', 'meeting', 'catch-up', 'workstream', 'update', 'discussion', 'chat']

loops = 0

while loops < 20:
    entityCurrent = random.choice(entity)
    typeCurrent = random.choice(type)
    occasionCurrent = random.choice(occasion)
    print(entityCurrent, typeCurrent, occasionCurrent, sep=" ")
    loops += 1