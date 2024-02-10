import pandas as pd
import os 
from PIL import Image
import numpy as np 

dict = {'file_name':[], 'prompt':[]}

for i in os.listdir('paper'):
    if i.endswith('.webp') and not os.path.exists(i.split('.webp')[0] + '.png'):
        img = Image.open('paper/'+i)
        img.save('paper/'+ i.split('.webp')[0] + '.png')

for i in os.listdir('paper'):  
    if i.endswith('.png'):
        prompt = i.split('_')[0]
        dict['file_name'].append(i)
        dict['prompt'].append(prompt)

df = pd.DataFrame.from_dict(dict)
df.to_csv('paper/metadata.csv', index=None)


for i in os.listdir('paper'):
    if i.endswith('.png'):
        try:
            img = Image.open('paper/' + i)
            print(np.array(img).shape)
        except:
            print(i)