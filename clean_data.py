import os 
import pandas as pd 

fds = ['classic_table', 'color_rock']


for i in fds:
    data = {'image_file':[], 'caption':[]}
    for j in os.listdir(i):
        if j.endswith(('.png', '.webp')):
            data['image_file'].append(j)
            data['caption'].append(j.split('_')[0])

    df = pd.DataFrame.from_dict(data)
    df.to_csv(i + '/caption.csv', index=None)
    
