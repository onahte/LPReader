from CONFIG import LABEL_MAP

labels = [{'name': 'license', 'id': '1'},]

def createMap():
    with open(LABEL_MAP, 'w') as f:
        for label in labels:
            f.write('item { \n')
            f.write('\tname:\'{}\'\n'.format(label['name']))
            f.write('\tid:{}\n'.format(label['id']))
            f.write('}\n')
