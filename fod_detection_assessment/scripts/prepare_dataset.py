from pathlib import Path
import argparse, shutil, random, zipfile, xml.etree.ElementTree as ET
from PIL import Image

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--voc_zip',required=True); ap.add_argument('--seed',type=int,default=42); a=ap.parse_args()
    root=Path(__file__).parents[1]; ex=root/'data/voc_extracted'
    if not ex.exists():
        with zipfile.ZipFile(a.voc_zip) as z: z.extractall(ex)
    ims=list({p.resolve() for p in ex.rglob('*') if p.is_file() and p.suffix.lower() in ('.jpg','.jpeg','.png')}); xm={p.stem:p for p in ex.rglob('*.xml')}; items=[(p,xm[p.stem]) for p in ims if p.stem in xm]
    names=sorted({o.findtext('name') for _,x in items for o in ET.parse(x).getroot().findall('object')}); ids={n:i for i,n in enumerate(names)}; random.seed(a.seed); random.shuffle(items); n=len(items)
    splits={'train':items[:int(.7*n)],'val':items[int(.7*n):int(.85*n)],'test':items[int(.85*n):]}; out=root/'data/fod_clean'
    for sp,vals in splits.items():
        for im,xp in vals:
            (out/'images'/sp).mkdir(parents=True,exist_ok=True); (out/'labels'/sp).mkdir(parents=True,exist_ok=True); shutil.copy2(im,out/'images'/sp/(im.stem+'.jpg')); iw,ih=Image.open(im).size; ls=[]
            for o in ET.parse(xp).getroot().findall('object'):
                b=o.find('bndbox'); x1,y1,x2,y2=[float(b.findtext(k)) for k in ('xmin','ymin','xmax','ymax')]; ls.append(f"{ids[o.findtext('name')]} {(x1+x2)/(2*iw):.6f} {(y1+y2)/(2*ih):.6f} {(x2-x1)/iw:.6f} {(y2-y1)/ih:.6f}")
            (out/'labels'/sp/(im.stem+'.txt')).write_text('\n'.join(ls))
    (out/'fod.yaml').write_text(f"path: {out.as_posix()}\ntrain: images/train\nval: images/val\ntest: images/test\nnames: {names!r}\n")
    print('Prepared',n,'images:',{k:len(v) for k,v in splits.items()},'classes:',names)
if __name__=='__main__': main()
