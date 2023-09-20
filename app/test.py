touple_list = (('filetransfer', '3', 'UP', 1), ('filetransfer', '4', 'UP', 1))


def toupleListTodict(touples):
    result_dict = {}
    for index, item in enumerate(touples, start=1):
        result_dict[f'index_{index}'] = {
            'daemon_name': item[0],
            'daemon_id': item[1],
            'status': item[2],
            'instance': item[3]
        }

    print(result_dict)
    return result_dict


result=toupleListTodict(touple_list)