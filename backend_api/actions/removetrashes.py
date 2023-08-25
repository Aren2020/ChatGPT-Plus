def removeTrash(list,item):
    for item in list:
        if item == '':
            list.remove(item)
    return list