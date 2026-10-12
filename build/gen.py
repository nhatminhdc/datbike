import json,html
B=[("era","Dat Bike ERA",None),("quantum-s1","Dat Bike Quantum S1",None),("quantum-s2","Dat Bike Quantum S2",None),("quantum-s3","Dat Bike Quantum S3",None)]
CQ="Giá đã kèm pin + sạc + VAT (theo dat.bike)"
M={
"era":dict(name="ERA",price="Từ 29.900.000đ",cond="ERA E2 (đen) 29.900.000đ · ERA E1 (đen) 33.900.000đ · ERA E1 (đỏ, trắng, xám) 34.900.000đ. Giá xe đã bao gồm pin, chi phí nâng cấp pin và phần mềm nâng cao tính năng của xe Dat Bike.",
 chips=["Cốp 50 lít","200 km/lần sạc","Sạc tích hợp trên xe"],big=("200 km","Quãng đường mỗi lần sạc (theo công bố của Dat Bike)"),
 vers=[("ERA E2","29.900.000đ (màu đen)"),("ERA E1","33.900.000đ (đen) · 34.900.000đ (đỏ, trắng, xám)")],
 colors=["#111","#e9e9e9","#888","#c0392b"],
 cols=["ERA E2","ERA E1"],
 rows=[("Giá","29.900.000 VND (màu đen)","33.900.000 VND (màu đen) · 34.900.000 VND (đỏ, trắng, xám)"),("Màu sắc","1 màu (Đen)","4 màu (Đen, trắng, xám, đỏ)"),("Cốp","50 lít","50 lít"),("Pin","4.3 kWh","4.3 kWh"),("Quãng đường","200 km","200 km"),
 ("Thời gian sạc","~3h30' sạc đầy (Standard)","15' đi 30 km (Boost) · ~2h15' sạc đầy (Fast) · ~3h30' sạc đầy (Standard)"),("Hệ thống phanh","Phanh đĩa · phanh động cơ (tái sinh)","Phanh CBS · phanh động cơ (tái sinh)"),("Cổng USB","—","Có"),("Đèn định vị","—","Có"),
 ("Chuẩn chống nước","IP67: PCU, động cơ và pin · IP65: phần còn lại","IP67: PCU, động cơ và pin · IP65: phần còn lại"),("Động cơ","Side motor 5 kW","Side motor 5 kW"),("Tốc độ tối đa","82 km/h","82 km/h"),("Tăng tốc 0–40 km/h","3,0 s","3,0 s"),
 ("Bánh xe","12 inch","12 inch"),("Khối lượng bản thân","112 kg","112 kg"),("Dài × Rộng × Cao","1860 × 680 × 1115 mm","1860 × 680 × 1115 mm"),("Mức tiêu thụ năng lượng","38,91 Wh/km","41,31 Wh/km")]),
}
QR=[("Giá (kèm pin + sạc + VAT)",["49.900.000đ · Trắng & xám: 50.900.000đ","42.900.000đ · Trắng & xám: 43.900.000đ","34.900.000đ · Trắng & xám: 35.900.000đ"]),
("Quãng đường",["285 km","285 km","200 km"]),("Thời gian sạc",["4h – bộ sạc 1.800W","7h – bộ sạc 900W · 4h – bộ sạc 1.800W","5h – bộ sạc 900W · 2h30′ – bộ sạc 1.800W"]),
("Vận tốc",["100 km/h","90 km/h","90 km/h"]),("Màu sắc",["Đen, Trắng, Xám, Cam, Xanh Dương"]*3),("Hill Assist",["Có"]*3),("Cổng USB",["Có (USB-A, USB-C)","Có (USB-A, USB-C)","Không"]),
("Chuẩn chống nước",["IP54: cổng USB · IP67: động cơ, pin, cổng sạc, ECU · IP65: phần còn lại"]*2+["IP67: động cơ, pin, cổng sạc, ECU · IP65: phần còn lại"]),
("Pin",["6.4 kWh","6.4 kWh","4.3 kWh"]),("Vành / lốp",["Trước 90/80-16, sau 110/70-16 · lốp không săm Casumina · vành đúc 16 inch"]*3),("Công suất động cơ",["7000W","6000W","6000W"]),
("Hệ thống phanh",["CBS 2 piston, đĩa trước 245 mm · phanh động cơ (tái sinh) tích hợp tay ga","Phanh thủy lực, đĩa trước và sau, đĩa trước 245 mm · phanh động cơ (tái sinh)","Phanh thủy lực, đĩa trước và sau, đĩa trước 245 mm · phanh động cơ (tái sinh)"]),
("Tay ga",["Thể thao"]*3),("Khối lượng",["144 kg","144 kg","130 kg"]),("Tải trọng",["130 kg"]*3),("Kích thước (D-R-C)",["2010 × 710 × 1110 mm · yên 790 mm","2010 × 710 × 1110 mm · yên 760 mm","2010 × 710 × 1110 mm · yên 760 mm"])]
for i,(k,pr,km,kw) in enumerate([("quantum-s1","49.900.000đ","285 km","7000W"),("quantum-s2","42.900.000đ","285 km","6000W"),("quantum-s3","34.900.000đ","200 km","6000W")]):
    n="Quantum S"+str(i+1)
    M[k]=dict(name=n,price=pr,cond=f"Màu trắng & xám: {QR[0][1][i].split(': ')[1]}. "+CQ+".",chips=[km+"/lần sạc",kw,QR[3][1][i]],big=(km,"Quãng đường mỗi lần sạc (theo công bố của Dat Bike)"),
      vers=[("Màu thường",pr),("Trắng & xám",QR[0][1][i].split(': ')[1])],colors=["#111","#eee","#888","#f26a1b","#2e6fd8"],cols=["Quantum S1","Quantum S2","Quantum S3"],
      rows=[(a,*v) for a,v in QR],hl=i)
S=[["CN1","36-38 Trường Chinh","P. Tân Bình (Tân Bình)","0778 123 268"],["CN2","212 Hoà Bình","Tân Phú","0961 79 79 28"],["CN3","256B-C Nguyễn Văn Luông","Quận 6","0933 831 866"],["CN4","165 Phạm Văn Chiêu","Gò Vấp","0933 983 866"],["CN5","1236 Phạm Văn Đồng","Thủ Đức","079 8811 181"],["CN6","155 Lê Văn Quới","Bình Trị Đông (Bình Tân)","0933 792 866"],["CN7","658 Âu Cơ","Bảy Hiền (Tân Bình)","0933 969 396"]]
CSS=r'''
:root{--o:#f26a1b;--r:#e8450a;--rd:#c7360a;--k:#111;--g:#f4f4f4;--t:#555}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}body{font-family:"Be Vietnam Pro",system-ui,sans-serif;color:var(--k);line-height:1.55;font-size:16px}
a{color:inherit;text-decoration:none}img{max-width:100%;display:block}.w{max-width:1320px;margin:auto;padding:0 40px}
.draft{background:#ffe9a8;color:#5a4300;font-size:12px;text-align:center;padding:4px}
header{position:sticky;top:0;z-index:50;background:#fff;transition:.3s}header.sc{box-shadow:0 4px 20px rgba(0,0,0,.08)}
.nav{display:flex;align-items:center;height:64px;gap:34px}.nav .lg img{height:40px}
.menu{display:flex;gap:26px;font-size:15px;flex:1}.menu>div{position:relative}.menu>div>a{padding:20px 0;display:block}.menu>div>a:hover{color:var(--r)}
.dd>a:after{content:"⌄";font-size:12px;margin-left:5px;color:#999}
.sub{position:absolute;top:56px;left:-16px;background:#fff;min-width:210px;border-radius:12px;box-shadow:0 12px 32px rgba(0,0,0,.12);padding:10px 0;opacity:0;visibility:hidden;transform:translateY(8px);transition:.2s}
.menu>div:hover .sub{opacity:1;visibility:visible;transform:none}.sub a{display:flex;align-items:center;gap:10px;padding:9px 18px;font-size:14px}.sub a:hover{background:#fff3ec;color:var(--r)}.sub img{height:22px;width:30px;object-fit:contain}
.pill{display:inline-flex;align-items:center;justify-content:center;padding:8px 18px;border-radius:30px;font-size:14px;font-weight:600;transition:.2s;border:0;cursor:pointer;font-family:inherit}
.pill.f{background:linear-gradient(90deg,var(--rd),var(--r));color:#fff}.pill.f:hover{filter:brightness(1.1)}.pill.l{background:#fff;color:var(--r);border:1.5px solid var(--r)}.pill.l:hover{background:var(--r);color:#fff}.pill.big{padding:14px 30px;font-size:16px}
.hb{display:none;background:none;border:0;font-size:26px;margin-left:auto}
.mm{display:none}
section{padding:80px 0}.ttl{text-align:center;font-size:clamp(30px,4vw,52px);font-weight:800;line-height:1.15;letter-spacing:-.02em;margin-bottom:14px}.ttl em{font-style:normal;color:var(--r)}
.lead{text-align:center;color:var(--t);max-width:640px;margin:0 auto 44px;font-size:17px}
.ph{background:linear-gradient(135deg,#e9e9e9,#d5d5d5);display:flex;align-items:center;justify-content:center;flex-direction:column;color:#888;font-size:13px;text-align:center;position:relative;overflow:hidden}
.ph svg{width:62%;max-width:520px;color:#3a3a3a}.ph small{position:absolute;bottom:10px;left:0;right:0;font-size:11px;letter-spacing:.5px;text-transform:uppercase}
.ph.dk{background:linear-gradient(135deg,#2a2a2a,#151515);color:#777}.ph.dk svg{color:#ddd}
/* hero slider */
.hero{padding:30px 0 60px}.hs{position:relative}.slide{display:none}.slide.on{display:block;animation:fd .7s}
@keyframes fd{from{opacity:0;transform:scale(.98)}to{opacity:1}}
.sh{display:grid;grid-template-columns:1fr;position:relative;min-height:560px}
.sh .tx{position:relative;z-index:3;padding-top:20px}.sh .k{color:var(--r);font-weight:700;font-size:22px}.sh h1{font-size:clamp(40px,5vw,62px);line-height:1.08;font-weight:800;letter-spacing:-.03em}
.card-o{position:absolute;left:0;right:0;top:190px;bottom:0;border-radius:28px;background:radial-gradient(circle at 70% 30%,#ff8a3d,var(--r) 45%,var(--rd));overflow:hidden}
.card-o .wm{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:clamp(80px,13vw,200px);font-weight:900;color:transparent;-webkit-text-stroke:2px rgba(255,255,255,.35);letter-spacing:.05em;white-space:nowrap}
.sh .bike{position:absolute;z-index:2;left:22%;right:22%;bottom:-30px;top:60px;display:flex;align-items:flex-end}.sh .bike svg{width:100%;color:#222;filter:drop-shadow(0 30px 30px rgba(0,0,0,.35))}
.sh .cta{position:absolute;z-index:3;right:44px;top:240px}.sh .cta .pill{background:#fff;color:var(--r);font-style:italic;font-weight:800;font-size:18px;padding:14px 30px}
.sh .bl{position:absolute;z-index:3;right:20px;top:20px;height:56px}
.arw{position:absolute;z-index:4;top:62%;width:40px;height:40px;border-radius:50%;border:0;background:rgba(255,255,255,.25);color:#fff;font-size:20px;cursor:pointer}.arw:hover{background:var(--r)}.arw.p{left:20px}.arw.n{right:20px}
.dots{display:flex;gap:8px;justify-content:flex-end;padding:14px 40px 0}.dots i{width:9px;height:9px;border-radius:50%;background:#ccc;cursor:pointer}.dots i.on{background:var(--r)}
/* orange band */
.band{background:linear-gradient(180deg,#fff 0,#ff9a55 12%,var(--r) 55%,var(--rd));color:#fff;padding-top:110px}.band .ttl{color:#fff}
.bc{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.bc>div{background:#fff;color:var(--k);border-radius:22px;overflow:hidden;transition:.3s}.bc>div:hover{transform:translateY(-8px)}
.bc .ph{height:260px}.bc h4{color:var(--r);text-align:center;font-size:20px;padding:18px 20px 6px}.bc p{padding:0 24px 24px;font-size:14px;color:var(--t);text-align:center}
.st3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.sc3{background:#fff;border-radius:22px;padding:34px 30px;box-shadow:0 14px 40px rgba(0,0,0,.07)}.sc3 b{font-size:84px;line-height:1;font-weight:800;color:var(--rd);display:block}.sc3 span{font-weight:600;font-size:18px}
.spec3{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.sp{border-radius:22px;padding:30px;text-align:center;background:#fff;box-shadow:0 14px 40px rgba(0,0,0,.07);border-top:6px solid var(--r)}.sp .ic{font-size:30px}.sp b{display:block;font-size:56px;font-weight:800;color:var(--rd);line-height:1.1}.sp em{font-style:normal;font-weight:700;display:block}.f4{grid-template-columns:repeat(4,1fr)!important}@media(max-width:1000px){.f4{grid-template-columns:1fr 1fr!important}}.spec3 .sp em{font-size:17px}.sp p{color:var(--t);font-size:14px;margin-top:10px;border-top:1px dashed #ddd;padding-top:10px}
/* tech carousel */
.tc{position:relative;border-radius:26px;overflow:hidden;background:radial-gradient(circle at 80% 30%,#ff8a3d,var(--r) 50%,var(--rd));color:#fff;min-height:440px;display:grid;grid-template-columns:1fr 1.2fr;align-items:center}
.tc .tx{padding:50px}.tc h3{font-size:36px;font-weight:800;margin-bottom:12px}.tc .ph{height:100%;min-height:440px;background:transparent}.tc .ph svg{color:#fff}
.wmk{font-size:clamp(80px,17vw,250px);font-weight:900;text-align:center;line-height:.8;color:#f1f1f1;letter-spacing:.05em;margin-bottom:-60px;user-select:none}
.feat{display:grid;grid-template-columns:1.1fr 1fr;gap:50px;align-items:center;margin-bottom:80px}.feat.rev{grid-template-columns:1fr 1.1fr}.feat.rev .ph{order:2}
.feat .ph{height:420px;border-radius:24px}.feat .k{font-weight:700;font-size:20px}.feat h3{color:var(--r);font-size:40px;font-weight:800;line-height:1.1;margin-bottom:6px}.feat h4{font-size:18px;margin-bottom:16px}.feat ul{padding-left:20px;color:var(--t)}.feat li{margin:6px 0}
.brands{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}.brands a{background:var(--g);border-radius:20px;padding:14px 14px 22px;text-align:center;transition:.3s;font-weight:700}.brands a:hover{background:#fff;box-shadow:0 14px 34px rgba(0,0,0,.1);transform:translateY(-6px)}
.brands .ph{height:200px;border-radius:14px}.brands .bl{height:84px;display:flex;align-items:center;justify-content:center;margin-bottom:12px}.brands img{max-height:84px;max-width:100%;object-fit:contain}.txl{font-size:26px;font-weight:900;color:var(--r)}
.offer{background:var(--k);color:#fff;border-radius:26px;padding:50px;display:flex;justify-content:space-between;align-items:center;gap:30px;flex-wrap:wrap}.offer h3{font-size:38px;font-weight:800}.offer h3 em{font-style:normal;color:var(--o)}
/* footer */
footer{background:#0b0b0b;color:#bbb;padding:60px 0 0;font-size:14px}.fg{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:34px}
.fb{background:var(--o);color:#fff;padding:30px;border-radius:4px}.fb img{height:70px;margin-bottom:20px}.fb p{margin:8px 0}.fb b{display:block;margin-top:16px}
footer h5{color:#fff;font-size:18px;margin-bottom:14px}footer h5:before{content:"• "}footer ul{list-style:none}footer li{margin:7px 0}footer li a{color:var(--o)}footer li a:hover{color:#fff}
.cp{border-top:1px solid #222;margin-top:50px;padding:20px 0;text-align:center;color:#777}
.fab{position:fixed;right:20px;bottom:20px;z-index:60;display:flex;flex-direction:column;gap:10px}.fab a{width:52px;height:52px;border-radius:50%;background:var(--r);color:#fff;display:flex;align-items:center;justify-content:center;font-size:22px;box-shadow:0 8px 20px rgba(0,0,0,.25);animation:pl 2s infinite}
@keyframes pl{0%{box-shadow:0 0 0 0 rgba(232,69,10,.5)}70%{box-shadow:0 0 0 14px rgba(232,69,10,0)}}
.rv{opacity:0;transform:translateY(50px);transition:opacity .9s,transform .9s}.rv.in{opacity:1;transform:none}
/* product */
.pimg{width:100%;height:100%;object-fit:cover;display:block}.ihero{position:relative;border-radius:28px;overflow:hidden;height:600px}.ihero .ov{position:absolute;left:0;bottom:0;right:0;padding:50px;color:#fff;background:linear-gradient(0deg,rgba(0,0,0,.7),transparent)}.ihero h1{font-size:clamp(40px,5vw,64px);font-weight:800;line-height:1.1}.ihero .k{color:#ffb07a;font-weight:700}.ihero p{margin-bottom:16px}
.vimg{background:#f0f0f0;height:300px;display:flex;align-items:center;justify-content:center;overflow:hidden}.vimg .pimg{object-fit:contain}.pvi{height:520px;border-radius:24px}.fimg{height:420px;border-radius:24px;overflow:hidden}
.badge{display:flex;align-items:center;gap:8px;border-left:1px solid #ddd;padding-left:14px;font-size:11px;color:#777;line-height:1.15;margin-left:-20px}.badge img{height:22px}
@media(max-width:1000px){.ihero{height:420px}.ihero .ov{padding:24px}.fimg{height:260px}.vimg{height:220px}.pvi{height:300px}.badge span{display:none}.badge img{height:16px}}
.pv{display:grid;grid-template-columns:1.4fr 1fr;gap:40px;align-items:start}.pv .ph{height:520px;border-radius:24px}
.chips{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}.chips span{background:#fff3ec;color:var(--r);padding:8px 14px;border-radius:10px;font-weight:700;font-size:14px}
.pbox{border:1px solid #eee;border-radius:20px;padding:24px;margin-top:16px}.pbox h5{font-size:14px;color:var(--t);margin-bottom:10px}
.vers{display:grid;grid-template-columns:1fr 1fr;gap:10px}.vers label{border:1.5px solid #ddd;border-radius:12px;padding:12px;cursor:pointer;font-size:14px}.vers input{display:none}.vers input:checked+label{border-color:var(--r);background:#fff3ec}
.sw{display:flex;gap:10px}.sw i{width:30px;height:30px;border-radius:50%;border:3px solid #fff;box-shadow:0 0 0 1.5px #ccc;cursor:pointer}.sw i.on{box-shadow:0 0 0 2px var(--r)}
.price{font-size:40px;font-weight:800;color:var(--r)}.price small{font-size:15px;color:var(--t);font-weight:500}
.big{background:var(--k);color:#fff;text-align:center;border-radius:26px;padding:70px 30px}.big b{font-size:clamp(70px,12vw,150px);font-weight:900;line-height:1;background:linear-gradient(90deg,#ffb07a,var(--r));-webkit-background-clip:text;color:transparent}
.tbl{width:100%;border-collapse:collapse;font-size:15px}.tbl th{background:var(--r);color:#fff;text-align:left;padding:14px 18px}.tbl td{padding:13px 18px;border-bottom:1px solid #eee}.tbl tr:nth-child(even) td{background:#fafafa}.tbl td:first-child{font-weight:600;width:40%}
.tbl .na{color:#b07a00;font-style:italic}
.grp{margin-bottom:34px}.grp h4{font-size:20px;margin-bottom:10px;color:var(--r)}
/* stores */
.sbar{display:grid;grid-template-columns:2fr 1fr auto;gap:10px;background:#fff;padding:16px;border-radius:12px;box-shadow:0 8px 24px rgba(0,0,0,.08);margin-bottom:20px}
.sbar input,.sbar select{padding:12px;border:1px solid #ddd;border-radius:8px;font-family:inherit;font-size:15px}
.sl{display:grid;grid-template-columns:420px 1fr;gap:20px;height:620px}.sl .ls{overflow:auto;border:1px solid #eee;border-radius:12px}
.si{padding:18px 20px;border-bottom:1px solid #eee;cursor:pointer}.si:hover,.si.on{background:#fff3ec}.si h4{color:var(--r);font-size:15px;text-transform:uppercase}.si p{font-size:14px;color:var(--t);margin-top:4px}.si .a{display:flex;gap:16px;margin-top:8px;font-size:13px;font-weight:600;color:var(--r)}
.map{border-radius:12px;overflow:hidden;background:#e8e8e8}.map iframe{width:100%;height:100%;border:0}
.pt{background:var(--k);color:#fff;padding:34px 0}.pt h1{font-size:28px;text-transform:uppercase}
/* booking */
.bkp{background:#0b0b0b;color:#fff;padding:40px 0 80px}.bkg{display:grid;grid-template-columns:1fr 1.9fr;gap:40px}.bkg h1{font-size:30px;margin-bottom:14px}.bkg p{color:#ccc;margin-bottom:20px}
.of{background:var(--o);border-radius:22px;padding:30px;display:grid;gap:6px}.of label{font-weight:700;color:#111;font-size:14px;margin-top:8px}.of input,.of select{padding:12px;border:0;font-family:inherit;font-size:15px;width:100%}
.of button{background:#000;color:#fff;border:0;padding:16px 18px;font-weight:700;width:max-content;margin-top:12px;cursor:pointer;font-family:inherit}.tq{display:none;color:#111;padding:40px 0;text-align:center}.tq b{font-size:26px;display:block}
.sq{background:var(--o);color:#fff;padding:14px 22px;font-weight:700;text-transform:uppercase;display:inline-block;border-radius:4px}
/* about */
.ah{text-align:center;padding:50px 0 0}.ah h1{font-size:clamp(40px,5vw,64px);font-weight:800}.ah .ph{height:360px;margin-top:20px;background:transparent}
.ab2{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center}.ab2 .k{color:var(--r);font-weight:700}.ab2 h2{font-size:42px;font-weight:800;margin-bottom:14px}.ab2 .ph{height:380px;border-radius:24px}
.icn{display:flex;gap:14px;margin-top:22px}.icn div{background:var(--g);border-radius:14px;padding:14px;text-align:center;font-size:13px;flex:1}.icn i{font-style:normal;font-size:26px;display:block;color:var(--r)}
.og{background:linear-gradient(180deg,var(--r),var(--rd) 70%,#8e2205);color:#fff}.og h2{font-size:clamp(34px,4vw,54px);font-weight:800;line-height:1.1}
.og .row{display:grid;grid-template-columns:1fr 1.6fr;gap:30px;align-items:center;margin-bottom:50px}.og .row.rv2{grid-template-columns:1.6fr 1fr}.og .ph{height:300px;border-radius:20px;background:rgba(255,255,255,.15)}.og .ph svg{color:#fff}
.vb{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.vb div{background:rgba(255,255,255,.12);border-radius:20px;padding:26px}.vb b{font-size:34px;display:block}
.ceo{display:grid;grid-template-columns:300px 1fr;gap:50px;align-items:center}.ceo .ph{height:340px;border-radius:12px}
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}.gal .ph{height:220px;border-radius:18px}.gal .ph:first-child{grid-column:span 4;height:380px}
@media(max-width:1000px){.w{padding:0 18px}.menu,.nav>.pill{display:none}.hb{display:block}
.mm.op{display:block;position:fixed;top:64px;left:0;right:0;bottom:0;background:#fff;overflow:auto;padding:20px;z-index:49}.mm a{display:block;padding:12px 0;border-bottom:1px solid #eee;font-weight:600}.mm .s2 a{padding-left:16px;font-weight:400}
.sh{min-height:520px}.card-o{top:200px}.sh .bike{left:2%;right:2%;bottom:30px;top:200px}.sh .cta{right:auto;left:20px;top:auto;bottom:20px}.sh .bl{height:36px}.arw{display:none}
.bc,.st3,.spec3,.spec3[style],.bc[style],.tc,.feat,.feat.rev,.pv,.ab2,.og .row,.og .row.rv2,.vb,.ceo,.bkg,.fg{grid-template-columns:1fr}.feat.rev .ph{order:0}.brands{grid-template-columns:repeat(2,1fr)}
.sc3 b{font-size:64px}.feat .ph,.pv .ph{height:280px}.feat h3{font-size:30px}.sl{grid-template-columns:1fr;height:auto}.sl .ls{max-height:420px}.map{height:360px}.sbar{grid-template-columns:1fr}
.gal{grid-template-columns:1fr 1fr}.gal .ph:first-child{grid-column:span 2;height:240px}section{padding:56px 0}.tc .ph{min-height:260px}.tc .tx{padding:30px}.wmk{margin-bottom:-24px}}
'''
BIKE='<svg viewBox="0 0 400 240"><circle cx="85" cy="175" r="48" fill="none" stroke="currentColor" stroke-width="14"/><circle cx="315" cy="175" r="48" fill="none" stroke="currentColor" stroke-width="14"/><path d="M85 175 L150 110 L270 110 L315 175" fill="none" stroke="currentColor" stroke-width="10" stroke-linejoin="round"/><path d="M130 120 Q160 80 250 85 L285 105 L270 140 L150 140Z" fill="#f26a1b"/><path d="M270 110 L300 50 L330 45" stroke="currentColor" stroke-width="10" fill="none" stroke-linecap="round"/><rect x="150" y="70" width="80" height="16" rx="8" fill="currentColor"/></svg>'
def ph(label,cls=""): return f'<div class="ph {cls}">{BIKE}<small>Ảnh placeholder · {label}</small></div>'
def blogo(b,h=22):
    return f'<img src="{b[2]}" alt="{b[1]}">' if b[2] else ''
def head(title):
    sub="".join(f'<a href="san-pham-{b[0]}.html">{blogo(b)}{b[1]}</a>' for b in B)
    msub="".join(f'<a href="san-pham-{b[0]}.html">{b[1]}</a>' for b in B)
    return f'''<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{title} – Sài Thành Group</title><link rel="preconnect" href="https://fonts.gstatic.com"><link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,800&display=swap" rel="stylesheet"><link rel="stylesheet" href="style.css"></head><body>
<div class="draft">BẢN NHÁP NỘI BỘ – chưa xuất bản</div>
<header id="hd"><div class="w nav"><a class="lg" href="index.html"><img src="saithanh.png" alt="Sai Thanh Group"></a><div class="badge"><span>Đại lý ủy quyền</span><img src="assets/web/logo_db.png" alt="Đại lý ủy quyền Dat Bike"></div>
<nav class="menu"><div class="dd"><a href="index.html#xe">Sản phẩm</a><div class="sub">{sub}</div></div>
<div class="dd"><a href="#">Chăm sóc khách hàng</a><div class="sub"><a href="#">Chính sách thanh toán</a><a href="#">Giao nhận &amp; kiểm hàng</a><a href="#">Bảo hành &amp; bảo dưỡng</a></div></div>
<div><a href="gioi-thieu.html">Về Sài Thành</a></div><div><a href="cua-hang.html">Danh sách cửa hàng</a></div></nav>
<a class="pill f" href="lai-thu.html">Mua ngay</a><a class="pill l" href="lai-thu.html">Lái thử miễn phí</a><button class="hb" id="hb" aria-label="Menu">☰</button></div>
<div class="mm" id="mm"><a href="index.html#xe">Sản phẩm</a><div class="s2">{msub}</div><a href="gioi-thieu.html">Về Sài Thành</a><a href="cua-hang.html">Danh sách cửa hàng</a><a href="lai-thu.html">Lái thử miễn phí</a><a href="lai-thu.html">Mua ngay</a></div></header>'''
def foot():
    pl="".join(f'<li><a href="san-pham-{b[0]}.html">{b[1]}</a></li>' for b in B)
    return f'''<footer><div class="w fg"><div class="fb"><img src="saithanh_white.png" alt="Sai Thanh Group"><p>☎ Hotline CN1: 0778 123 268</p><p>✉ [email – cần bổ sung]</p><p>🌐 [website – cần bổ sung]</p>
<p style="margin-top:14px">Đại lý ủy quyền</p><img src="assets/web/logo_db_w.png" alt="Dat Bike" style="height:34px;margin:6px 0 0"><b>CÔNG TY [TÊN PHÁP LÝ – CẦN BỔ SUNG]</b><p>Mã số doanh nghiệp: [cần bổ sung]</p><p>Trụ sở: [cần bổ sung]</p></div>
<div><h5>Sản phẩm</h5><ul>{pl}</ul></div><div><h5>Về Sài Thành</h5><ul><li><a href="gioi-thieu.html">Giới thiệu</a></li><li><a href="cua-hang.html">Hệ thống 7 cửa hàng</a></li><li><a href="lai-thu.html">Đăng ký lái thử</a></li></ul></div>
<div><h5>Chính sách</h5><ul><li><a href="#">Thanh toán</a></li><li><a href="#">Giao nhận &amp; kiểm hàng</a></li><li><a href="#">Bảo hành &amp; bảo dưỡng</a></li></ul></div></div>
<div class="w cp">© 2026 Sai Thanh Group · Tín – Tâm – Trí – Tốc – Tinh – Nhân</div></footer>
<div class="fab"><a href="tel:0778123268" title="Gọi">☎</a><a href="lai-thu.html" title="Lái thử">🛵</a></div>
<script src="main.js"></script></body></html>'''
JS=r'''
const hd=document.getElementById('hd');addEventListener('scroll',()=>hd.classList.toggle('sc',scrollY>10));
document.getElementById('hb').onclick=()=>document.getElementById('mm').classList.toggle('op');
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(x=>io.observe(x));if(/shot/.test(location.search))document.querySelectorAll('.rv').forEach(x=>x.classList.add('in'));
document.querySelectorAll('.hs').forEach(h=>{const s=h.querySelectorAll('.slide'),d=h.querySelector('.dots');let i=0;
d.innerHTML=[...s].map(()=>'<i></i>').join('');const g=n=>{i=(n+s.length)%s.length;s.forEach((x,k)=>x.classList.toggle('on',k==i));d.querySelectorAll('i').forEach((x,k)=>{x.classList.toggle('on',k==i);x.onclick=()=>g(k)})};
h.querySelector('.p').onclick=()=>g(i-1);h.querySelector('.n').onclick=()=>g(i+1);g(0);if(!/shot/.test(location.search))setInterval(()=>g(i+1),5000)});
document.querySelectorAll('form[data-ty]').forEach(f=>f.onsubmit=e=>{e.preventDefault();f.querySelector('.fi').style.display='none';f.querySelector('.tq').style.display='block'});
document.querySelectorAll('.sw').forEach(s=>s.onclick=e=>{if(e.target.tagName=='I'){s.querySelectorAll('i').forEach(x=>x.classList.remove('on'));e.target.classList.add('on')}});
document.querySelectorAll('.si').forEach(x=>x.onclick=()=>{document.querySelectorAll('.si').forEach(y=>y.classList.remove('on'));x.classList.add('on');const m=document.getElementById('mf');if(m)m.src='https://maps.google.com/maps?q='+encodeURIComponent(x.dataset.q)+'&output=embed'});
const q=document.getElementById('sq');if(q)q.oninput=q.onchange=()=>{const v=q.value.toLowerCase(),d=document.getElementById('sd').value;document.querySelectorAll('.si').forEach(x=>x.style.display=(x.textContent.toLowerCase().includes(v)&&(!d||x.textContent.includes(d)))?'':'none')};
const sd=document.getElementById('sd');if(sd)sd.onchange=q.oninput;
'''
open('style.css','w').write(CSS);open('main.js','w').write(JS)
OUT={}
def img(f,alt,st=""):return f'<img class="pimg" src="assets/web/{f}" alt="{alt}" loading="lazy" style="{st}">'
# ---------- HOME
HS={"era":"era_s1.jpg","quantum-s1":"s1_hero.jpg","quantum-s2":"s2_hero.jpg","quantum-s3":"s3_hero.jpg"}
slides="".join(f'''<div class="slide"><a href="san-pham-{b[0]}.html" class="ihero" style="display:block">{img(HS[b[0]],b[1])}<div class="ov"><div class="k">Sài Thành · Đại lý ủy quyền Dat Bike</div><h1>{b[1]}</h1><p>{M[b[0]]["price"]}</p><span class="pill f big">Tư vấn ngay</span></div></a></div>''' for b in B)
_old="".join(f'''<div class="slide"><div class="sh"><div class="tx"><div class="k">Sài Thành phân phối · {M[b[0]]["price"]}</div><h1>{b[1]}</h1></div>
<div class="card-o"><div class="wm">SÀI THÀNH</div></div><div class="bike">{BIKE}</div>{('<img class="bl" src="'+b[2]+'" alt="">') if b[2] else ''}
<div class="cta"><a class="pill" href="san-pham-{b[0]}.html">Tư vấn ngay</a></div></div></div>''' for b in B)
MI={"era":"era_main.png","quantum-s1":"s1_main.jpg","quantum-s2":"s2_main.jpg","quantum-s3":"s3_main.jpg"}
brands="".join(f'<a class="rv" href="san-pham-{b[0]}.html"><div class="vimg" style="height:200px;border-radius:14px;background:#fff">{img(MI[b[0]],b[1])}</div><div style="padding:14px 4px 0;font-size:20px">{b[1]}</div><div style="color:var(--r);font-size:18px">{M[b[0]]["price"]}</div><div style="font-weight:400;font-size:13px;color:var(--t)">{" · ".join(M[b[0]]["chips"][:2])}</div><span class="pill f" style="margin-top:12px">Xem chi tiết</span></a>' for b in B)
home=head("Chuỗi cửa hàng xe điện")+f'''
<section class="hero"><div class="w hs">{slides}<button class="arw p">‹</button><button class="arw n">›</button><div class="dots"></div></div></section>
<section class="band"><div class="w"><h2 class="ttl rv">Mua xe dễ dàng<br>Đi xe yên tâm</h2><p class="lead" style="color:#ffe3d1">Từ chọn xe, lái thử đến bảo dưỡng – Sài Thành lo cùng bạn.</p>
<div class="bc"><div class="rv"><div class="fimg" style="height:260px;border-radius:0">{img("era_f2.jpg","")}</div><h4>Xem tận nơi</h4><p>Đủ các mẫu Dat Bike trưng bày để so sánh trực tiếp.</p></div>
<div class="rv"><div class="fimg" style="height:260px;border-radius:0">{img("s1_f1.jpg","")}</div><h4>Lái thử miễn phí</h4><p>Ngồi thử, chạy thử rồi mới quyết định.</p></div>
<div class="rv"><div class="fimg" style="height:260px;border-radius:0">{img("s2_f1.jpg","")}</div><h4>Chăm xe tận tâm</h4><p>Kiểm tra pin, phanh, lốp tại cả 7 cửa hàng.</p></div></div></div></section>
<section><div class="w"><h2 class="ttl rv">Sài Thành <em>qua con số</em></h2><p class="lead">[Placeholder – bổ sung số liệu thật khi có]</p>
<div class="st3"><div class="sc3 rv"><b>7</b><span>Cửa hàng tại TP.HCM</span></div><div class="sc3 rv"><b>4</b><span>Mẫu xe Dat Bike</span></div><div class="sc3 rv"><b>0đ</b><span>Trả trước khi trả góp</span></div></div></div></section>
<section style="padding-top:0"><div class="w"><h2 class="ttl rv">Mua xe theo cách <em>của bạn</em></h2><p class="lead">Ba lựa chọn để bắt đầu.</p>
<div class="spec3"><div class="sp rv"><div class="ic">💳</div><b>0đ</b><em>Trả trước</em><p>Không trả trước, trả góp 0đ.*</p></div><div class="sp rv"><div class="ic">🛵</div><b>7</b><em>Điểm lái thử</em><p>Đặt lịch tại cửa hàng gần bạn.</p></div><div class="sp rv"><div class="ic">🔧</div><b>[?]</b><em>Tháng bảo hành</em><p>[Cần bổ sung chính sách thật]</p></div></div>
<p style="font-size:12px;color:#999;margin-top:14px">*Điều kiện áp dụng theo từng đợt, liên hệ cửa hàng.</p></div></section>
<section id="xe" style="padding-top:0"><div class="w"><h2 class="ttl rv">Xe điện <em>Dat Bike</em></h2><p class="lead">Sài Thành là đại lý phân phối. Giá theo dat.bike ngày 12/10/2026, đã kèm pin + sạc + VAT.</p><div class="brands">{brands}</div></div></section>
<section style="padding-top:0"><div class="w"><h2 class="ttl rv">Dịch vụ <em>trọn gói</em></h2><p class="lead">Mọi thứ cần cho chiếc xe đầu tiên của bạn.</p>
<div class="tc rv"><div class="tx"><h3>Lái thử – nhận xe – bảo dưỡng</h3><p>Một nơi lo trọn: tư vấn, thủ tục giấy tờ, giao xe và chăm sóc định kỳ.</p><br><a class="pill big" style="background:#fff;color:var(--r)" href="lai-thu.html">Đăng ký lái thử</a></div><div class="fimg" style="height:100%;min-height:440px;border-radius:0">{img("s3_hero.jpg","")}</div></div></div></section>
<div class="wmk">SÀI THÀNH</div>
<section><div class="w"><h2 class="ttl rv">Vì sao chọn <em>Sài Thành</em></h2><p class="lead">Tín – Tâm – Trí – Tốc – Tinh – Nhân</p>
<div class="feat rv"><div class="fimg">{img("s2_f2.jpg","")}</div><div><div class="k">Tín · Tâm · Trí</div><h3>Tư vấn thật</h3><h4>Đúng nhu cầu, đúng túi tiền</h4><ul><li>Giá và thông số rõ ràng</li><li>Gợi ý xe theo độ tuổi, quãng đường</li><li>Không ép mua</li></ul></div></div>
<div class="feat rev rv"><div class="fimg">{img("s3_f2.jpg","")}</div><div><div class="k">Tốc · Tinh · Nhân</div><h3>Phục vụ nhanh</h3><h4>Giao xe gọn, chăm xe kỹ</h4><ul><li>Kiểm tra kỹ trước khi giao</li><li>Hỗ trợ giấy tờ</li><li>Đồng hành suốt thời gian dùng xe</li></ul></div></div></div></section>
<section style="padding-top:0"><div class="w"><div class="offer rv"><div><h3>Không trả trước, <em>trả góp 0đ</em></h3><p style="color:#aaa">Ghé cửa hàng gần nhất để được tư vấn.</p></div><div style="display:flex;gap:12px;flex-wrap:wrap"><a class="pill f big" href="lai-thu.html">Đăng ký tư vấn</a><a class="pill l big" href="cua-hang.html">Tìm cửa hàng</a></div></div></div></section>
'''+foot()
OUT['index.html']=home
# ---------- PRODUCTS
A="assets/web/"
IM={"era":dict(slides=["era_s1.jpg","era_s2.jpg","era_s3.jpg","era_s4.jpg"],main="era_main.png",vers=["era_e2.png","era_e1.png"],f=["era_f1.jpg","era_f2.jpg"],baked=True)}
for k in("s1","s2","s3"):IM["quantum-"+k]=dict(slides=[k+"_hero.jpg"],main=k+"_main.jpg",vers=[k+"_main.jpg",k+"_main.jpg"],f=[k+"_f1.jpg",k+"_f2.jpg"],baked=False)

def tblh(m):
    hl=m.get('hl',-1)
    th="".join(f'<th{" style=background:var(--rd)" if i==hl else ""}>{c}</th>' for i,c in enumerate(m["cols"]))
    tr="".join('<tr><td>'+r[0]+'</td>'+"".join(f'<td{" style=font-weight:700" if i==hl else ""}>{v}</td>' for i,v in enumerate(r[1:]))+'</tr>' for r in m["rows"])
    return f'<div class="rv" style="overflow-x:auto"><table class="tbl"><tr><th>Thông số</th>{th}</tr>{tr}</table></div>'
for b in B:
    m=M[b[0]];n=m["name"];I=IM[b[0]]
    if I["baked"]: hero='<section class="hero"><div class="w hs">'+"".join(f'<div class="slide">{img(x,"Dat Bike "+n,"border-radius:28px;width:100%")}</div>' for x in I["slides"])+'<button class="arw p">‹</button><button class="arw n">›</button><div class="dots"></div></div></section>'
    else: hero=f'<section class="hero"><div class="w hs"><div class="slide"><div class="ihero">{img(I["slides"][0],"Dat Bike "+n)}<div class="ov"><div class="k">Dat Bike · Sài Thành – đại lý ủy quyền</div><h1>{n}</h1><p>{m["price"]} · {" · ".join(m["chips"][:2])}</p><a class="pill f big" href="lai-thu.html">Tư vấn ngay</a></div></div></div><button class="arw p">‹</button><button class="arw n">›</button><div class="dots"></div></div></section>'

    vers="".join(f'<input type="radio" name="v" id="v{i}" {"checked" if i==0 else ""}><label for="v{i}"><b>{v[0]}</b><br>{v[1]}</label>' for i,v in enumerate(m["vers"]))
    p=head(n)+f"""
{hero}
<section style="padding:0 0 40px"><div class="w"><div class="spec3 f4">{"".join(f'<div class="sp rv" style="padding:18px;border-top-width:4px"><em>{c}</em></div>' for c in m["chips"])}<div class="sp rv" style="padding:18px;border-top-width:4px"><em>Trả góp 0đ</em><p style="margin-top:6px">Không trả trước*</p></div></div></div></section>
<section style="padding-top:0"><div class="w"><h2 class="ttl rv">Phiên bản</h2><div class="bc" style="grid-template-columns:1fr 1fr">{"".join(f'<div class="rv" style="background:var(--g)"><div class="vimg">{img(I["vers"][i],n+" "+v[0])}</div><h4>{v[0]}</h4><p>{v[1]}</p></div>' for i,v in enumerate(m["vers"]))}</div></div></section>
<section style="padding-top:20px"><div class="w pv"><div class="rv vimg pvi">{img(I["main"],"Dat Bike "+n)}</div><div class="rv"><div class="k" style="color:var(--r);font-weight:700">Dat Bike · Sài Thành phân phối</div><h2 style="font-size:34px;font-weight:800">{n}</h2>
<div class="chips">{"".join(f"<span>{c}</span>" for c in m["chips"])}</div>
<div class="pbox"><h5>Phiên bản</h5><div class="vers">{vers}</div></div>
<div class="pbox"><h5>Màu sắc</h5><div class="sw">{"".join(f'<i{" class=on" if i==0 else ""} style="background:{c}"></i>' for i,c in enumerate(m["colors"]))}</div></div>
<div class="pbox"><h5>Giá</h5><div class="price">{m["price"]}</div><p style="font-size:13px;color:var(--t);margin-top:6px">{m["cond"]}</p><p style="font-size:13px;margin-top:6px;font-weight:600">Không trả trước, trả góp 0đ*</p></div>
<div style="display:flex;gap:10px;margin-top:18px"><a class="pill f big" href="lai-thu.html">Mua ngay</a><a class="pill l big" href="lai-thu.html">Lái thử miễn phí</a></div></div></div></section>
<section style="padding-top:20px"><div class="w"><div class="feat rv"><div class="fimg">{img(I["f"][0],n)}</div><div><div class="k">Dat Bike {n}</div><h3>{m["chips"][0]}</h3><h4>{m["chips"][1]} · {m["chips"][2]}</h4><p style="color:var(--t)">[Nội dung tính năng – chờ tài liệu đại lý từ Dat Bike]</p></div></div>
<div class="feat rev rv"><div class="fimg">{img(I["f"][1],n)}</div><div><div class="k">Sài Thành</div><h3>Lái thử miễn phí</h3><h4>Tại 7 cửa hàng TP.HCM</h4><ul><li>Không trả trước, trả góp 0đ*</li><li>Tư vấn 1:1</li></ul></div></div>
<div class="big rv"><b>{m["big"][0]}</b><h3 style="font-size:22px;margin-top:10px">{m["big"][1]}</h3></div></div></section>
<section style="padding-top:0"><div class="w"><h2 class="ttl rv">Thông số <em>kỹ thuật</em></h2><p class="lead">Nguồn: dat.bike, lấy ngày 12/10/2026. Giá và thông số có thể thay đổi theo hãng.</p>{tblh(m)}</div></section>
<section style="padding-top:0"><div class="w"><div class="offer rv"><div><h3>Không trả trước, <em>trả góp 0đ</em></h3><p style="color:#aaa">Lái thử {n} miễn phí tại 7 cửa hàng Sài Thành. *Điều kiện theo từng đợt.</p></div><a class="pill f big" href="lai-thu.html">Đăng ký lái thử</a></div></div></section>"""+foot()
    OUT[f'san-pham-{b[0]}.html']=p
# ---------- STORES
items="".join(f'<div class="si{" on" if i==0 else ""}" data-q="{s[1]}, {s[2]}, TP. Hồ Chí Minh"><h4>{s[0]} · Sài Thành {s[2]}</h4><p>📍 {s[1]}, {s[2]}, TP.HCM</p><p>☎ {s[3]} · 🕘 [Giờ mở cửa – cần bổ sung]</p><div class="a"><a href="tel:{s[3].replace(" ","")}">Gọi ngay</a><a target="_blank" href="https://www.google.com/maps/search/{html.escape(s[1]+", "+s[2]+", TP.HCM")}">Chỉ đường</a></div></div>' for i,s in enumerate(S))
opts="".join(f'<option>{d}</option>' for d in sorted({s[2].split(" (")[0] for s in S}))
OUT['cua-hang.html']=head("Danh sách cửa hàng")+f'''<div class="pt"><div class="w"><h1>Danh sách cửa hàng</h1></div></div>
<section style="padding-top:30px"><div class="w"><div class="sbar"><input id="sq" placeholder="Tìm theo tên đường, quận..."><select id="sd"><option value="">Tất cả khu vực</option>{opts}</select><button class="pill f">Tìm kiếm</button></div>
<div class="sl"><div class="ls">{items}</div><div class="map"><iframe id="mf" loading="lazy" src="https://maps.google.com/maps?q={html.escape(S[0][1]+", Tân Bình, TP. Hồ Chí Minh")}&output=embed"></iframe></div></div></div></section>'''+foot()
# ---------- BOOKING
bo="".join(f'<option>{b[1]}</option>' for b in B);so="".join(f'<option>{s[0]} – {s[1]}, {s[2]}</option>' for s in S)
OUT['lai-thu.html']=head("Đăng ký lái thử")+f'''<div class="bkp"><div class="w bkg"><div><h1>Tư vấn và lái thử miễn phí</h1><p>Chọn xe, chọn cửa hàng – nhân viên Sài Thành sẽ gọi lại hẹn giờ.</p><a class="sq" href="cua-hang.html">Danh sách cửa hàng</a>
<p style="margin-top:30px;color:#fff;font-weight:700;font-size:20px">Không trả trước, trả góp 0đ*</p><p style="font-size:12px">*Điều kiện theo từng đợt.</p></div>
<form class="of" data-ty><div class="fi" style="display:grid;gap:6px"><label>Họ và tên *</label><input required placeholder="Nhập họ và tên"><label>Số điện thoại *</label><input required type="tel" pattern="[0-9 ]{{9,12}}" placeholder="Nhập số điện thoại">
<label>Mẫu xe quan tâm *</label><select required><option value="">Chọn mẫu xe</option>{bo}</select><label>Cửa hàng *</label><select required><option value="">Chọn cửa hàng</option>{so}</select><label>Ngày muốn lái thử</label><input type="date"><button>ĐĂNG KÝ LÁI THỬ</button></div>
<div class="tq"><b>Cảm ơn bạn!</b>Cửa hàng sẽ gọi lại để hẹn lịch lái thử.</div></form></div></div>'''+foot()
# ---------- ABOUT
vals=[("Tín","Nói đúng, bán đúng."),("Tâm","Tư vấn vì khách."),("Trí","Hiểu xe, giải thích dễ hiểu."),("Tốc","Nhanh gọn từng việc."),("Tinh","Kỹ từng chi tiết."),("Nhân","Đối xử tử tế.")]
OUT['gioi-thieu.html']=head("Về Sài Thành")+f'''<section class="ah"><div class="w"><h1>Về Sài Thành Group</h1>{ph("Ảnh dàn xe / cửa hàng")}</div></section>
<section><div class="w ab2"><div class="rv"><div class="k">Câu chuyện</div><h2>[Tiêu đề câu chuyện thương hiệu]</h2><p style="color:var(--t)">[Placeholder – năm thành lập, hành trình mở 7 cửa hàng, cần anh Minh cung cấp.]</p>
<div class="icn"><div><i>🏬</i>7 cửa hàng</div><div><i>🛵</i>Đại lý Dat Bike</div><div><i>🤝</i>Tư vấn 1:1</div></div></div><div class="rv">{ph("Ảnh cửa hàng")}</div></div></section>
<section class="og"><div class="w"><div class="k" style="font-weight:700">Giá trị cốt lõi</div><div class="row rv"><h2>Khách hàng<br>là trung tâm</h2>{ph("Ảnh tư vấn")}</div>
<div class="row rv2 rv">{ph("Ảnh đội ngũ")}<h2 style="text-align:right">Đội ngũ<br>hiểu xe</h2></div>
<h2 style="text-align:center;margin-bottom:30px" class="rv">Tín – Tâm – Trí – Tốc – Tinh – Nhân</h2><div class="vb">{"".join(f'<div class="rv"><b>{a}</b>{c}</div>' for a,c in vals)}</div></div></section>
<section><div class="w ceo"><div class="rv">{ph("Ảnh người sáng lập")}<p style="text-align:center;margin-top:10px"><b>Trần Nhật Minh</b><br><small>[Chức danh – xác nhận]</small></p></div><div class="rv"><div class="k" style="color:var(--r);font-weight:700">Lời nhắn từ người sáng lập</div><p style="font-size:18px;margin-top:12px">[Placeholder – lời nhắn của anh Minh, cần anh viết/duyệt.]</p></div></div></section>
<section style="padding-top:0"><div class="w"><div class="k" style="color:var(--r);font-weight:700">Hệ thống</div><h2 class="ttl" style="text-align:left">7 cửa hàng tại TP.HCM</h2><div class="gal">{"".join(ph(f"Ảnh {s[0]} – {s[2]}") for s in S[:5])}</div></div></section>
<section style="padding-top:0"><div class="w"><div class="offer rv"><div><h3>Ghé <em>Sài Thành</em> gần bạn</h3></div><a class="pill f big" href="cua-hang.html">Xem 7 cửa hàng</a></div></div></section>'''+foot()
for k,v in OUT.items(): open(k,'w').write(v)
print(list(OUT))
