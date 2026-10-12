
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
