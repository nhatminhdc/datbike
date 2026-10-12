cd /workspace/company/website
for p in index san-pham-era san-pham-quantum-s1 san-pham-quantum-s2 san-pham-quantum-s3 cua-hang lai-thu gioi-thieu; do
timeout 60 google-chrome --headless --no-sandbox --hide-scrollbars --virtual-time-budget=5000 --window-size=1440,6500 --screenshot=shots/${p}_desktop.png "file://$PWD/$p.html?shot" 2>/dev/null
timeout 60 google-chrome --headless --no-sandbox --hide-scrollbars --virtual-time-budget=5000 --window-size=390,11000 --screenshot=shots/${p}_mobile.png "file://$PWD/$p.html?shot" 2>/dev/null
done
python3 - <<'P'
from PIL import Image,ImageChops;import glob
for f in glob.glob('shots/*.png'):
    im=Image.open(f).convert('RGB');bb=ImageChops.difference(im,Image.new('RGB',im.size,(255,255,255))).getbbox()
    if bb:im.crop((0,0,im.width,bb[3])).save(f)
pairs={'home':'index','product_era':'san-pham-era','stores':'cua-hang','booking':'lai-thu','about':'gioi-thieu'}
for r,o in pairs.items():
  for v in['desktop','mobile']:
    try:a=Image.open(f'ref/{r}/full_{v}.png');b=Image.open(f'shots/{o}_{v}.png')
    except Exception as e:print(e);continue
    W=600 if v=='desktop' else 300;a=a.resize((W,int(a.height*W/a.width)));b=b.resize((W,int(b.height*W/b.width)))
    c=Image.new('RGB',(W*2+20,max(a.height,b.height)),'white');c.paste(a,(0,0));c.paste(b,(W+20,0));c.save(f'compare/{r}_vs_{o}_{v}.png')
P
echo ok
