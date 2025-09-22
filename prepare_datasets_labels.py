import json 
import yaml 

def format_txt(split_list, prefix, output_file):
    txt_list = []
    for entry in split_list:
        path = entry[0]
        label = entry[1]
        txt_list.append(f'{prefix}{path} {label} 1') # 1 means downstream data
    
    # sort txt_list by {label}
    txt_list.sort(key=lambda x: int(x.split(' ')[1]))
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(txt_list))
    print(f'Created {output_file}, {len(txt_list)} lines') 


def create_labels_eurosat():
    print('\nCreating labels for EuroSAT')

    file = f'{ROOT}/eurosat/split_zhou_EuroSAT.json'
    with open(file, 'r') as f:
        data = json.load(f)
    train_split = data['train']
    val_split = data['val']
    test_split = data['test']

    # create the train.txt, val.txt, test.txt
    prefix=f'eurosat/EuroSAT_RGB/'
    format_txt(train_split, prefix, 'data/eurosat/train.txt')
    format_txt(val_split, prefix, 'data/eurosat/val.txt')
    format_txt(test_split, prefix, 'data/eurosat/test.txt')

if __name__ == '__main__':
    
    # read the retrieved path from the config.yml
    with open('config.yml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        ROOT = config['dataset_path']  

    # create_labels_dtd()
    create_labels_eurosat()
    # create_labels_flowers()
    # create_labels_aircraft()
    # create_labels_aves()
        
    # create_labels_oxfordpets()
    # create_labels_food101()
    # create_labels_stanfordcars()
    print('Done')