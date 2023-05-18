from CONFIG import LABEL_MAP_FILE

def createMap(labels):
    with open(LABEL_MAP_FILE, 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')
    print(f'Successfully created {LABEL_MAP_FILE}')