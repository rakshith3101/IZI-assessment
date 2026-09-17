from pathlib import Path
from collections import Counter
import xml.etree.ElementTree as ET
root=Path(__file__).parents[1]; xs=list((root/'data/voc_extracted').rglob('*.xml')); c=Counter()
for x in xs:
    for o in ET.parse(x).getroot().findall('object'): c[o.findtext('name')]+=1
print('XML files:',len(xs)); print('Instances by class:'); print(*sorted(c.items()),sep='\n')
