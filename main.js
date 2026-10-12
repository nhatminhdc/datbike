const hd=document.getElementById('hd');
if(hd)addEventListener('scroll',()=>hd.classList.toggle('sc',scrollY>10));
const hb=document.getElementById('hb');
if(hb)hb.onclick=()=>document.getElementById('mm').classList.toggle('op');
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.12});
document.querySelectorAll('.rv').forEach(x=>io.observe(x));if(/shot/.test(location.search))document.querySelectorAll('.rv').forEach(x=>x.classList.add('in'));
document.querySelectorAll('.hs').forEach(h=>{const s=h.querySelectorAll('.slide'),d=h.querySelector('.dots');if(!d||!s.length)return;let i=0;
d.innerHTML=[...s].map(()=>'<i></i>').join('');const g=n=>{i=(n+s.length)%s.length;s.forEach((x,k)=>x.classList.toggle('on',k==i));d.querySelectorAll('i').forEach((x,k)=>{x.classList.toggle('on',k==i);x.onclick=()=>g(k)})};
const prev=h.querySelector('.p'),next=h.querySelector('.n');if(prev)prev.onclick=()=>g(i-1);if(next)next.onclick=()=>g(i+1);g(0);if(!/shot/.test(location.search))setInterval(()=>g(i+1),5000)});
document.querySelectorAll('form[data-ty]').forEach(f=>f.onsubmit=e=>{e.preventDefault();f.querySelector('.fi').style.display='none';f.querySelector('.tq').style.display='block'});
document.querySelectorAll('.sw').forEach(s=>s.onclick=e=>{if(e.target.tagName=='I'){s.querySelectorAll('i').forEach(x=>x.classList.remove('on'));e.target.classList.add('on')}});
document.querySelectorAll('.si').forEach(x=>x.onclick=()=>{document.querySelectorAll('.si').forEach(y=>y.classList.remove('on'));x.classList.add('on');const m=document.getElementById('mf');if(m)m.src='https://maps.google.com/maps?q='+encodeURIComponent(x.dataset.q)+'&output=embed'});
const q=document.getElementById('sq');if(q)q.oninput=q.onchange=()=>{const v=q.value.toLowerCase(),d=document.getElementById('sd').value;document.querySelectorAll('.si').forEach(x=>x.style.display=(x.textContent.toLowerCase().includes(v)&&(!d||x.textContent.includes(d)))?'':'none')};
const sd=document.getElementById('sd');if(sd)sd.onchange=q.oninput;

if(document.body.classList.contains('home')){
  const toggle=document.getElementById('menuToggle');
  const closeBtn=document.getElementById('menuClose');
  const overlay=document.getElementById('menuOverlay');
  const menu=document.getElementById('mobileMenu');
  const openMenu=()=>{if(menu){menu.classList.add('is-open');document.body.style.overflow='hidden'}};
  const closeMenu=()=>{if(menu){menu.classList.remove('is-open');document.body.style.overflow=''}};
  if(toggle)toggle.addEventListener('click',openMenu);
  if(closeBtn)closeBtn.addEventListener('click',closeMenu);
  if(overlay)overlay.addEventListener('click',closeMenu);
  document.querySelectorAll('.mobile-nav-item.has-sub .mobile-nav-item__trigger').forEach(btn=>{
    btn.addEventListener('click',()=>{
      const item=btn.closest('.mobile-nav-item');
      const isOpen=item.classList.contains('is-open');
      document.querySelectorAll('.mobile-nav-item.is-open').forEach(el=>el.classList.remove('is-open'));
      if(!isOpen)item.classList.add('is-open');
    });
  });
  const slides=[...document.querySelectorAll('.section-tech-eco__slider .swiper-slide')];
  const dots=document.querySelector('.section-tech-eco__dots');
  if(slides.length&&dots){
    let ti=0;
    dots.innerHTML=slides.map((_,i)=>`<button type="button" class="swiper-pagination-bullet" aria-label="Slide ${i+1}"></button>`).join('');
    const bullets=[...dots.querySelectorAll('button')];
    const show=n=>{ti=(n+slides.length)%slides.length;slides.forEach((s,i)=>s.classList.toggle('is-on',i===ti));bullets.forEach((b,i)=>b.classList.toggle('swiper-pagination-bullet-active',i===ti))};
    bullets.forEach((b,i)=>b.onclick=()=>show(i));
    const p=document.querySelector('.section-tech-eco__nav--prev');
    const n=document.querySelector('.section-tech-eco__nav--next');
    if(p)p.onclick=()=>show(ti-1);
    if(n)n.onclick=()=>show(ti+1);
    show(0);
  }
  const items=[...document.querySelectorAll('.testimonial__item')];
  if(items.length){
    let cur=Math.max(0,items.findIndex(el=>el.classList.contains('is-active')));
    const show=idx=>{items[cur].classList.remove('is-active');cur=(idx+items.length)%items.length;items[cur].classList.add('is-active')};
    const prev=document.getElementById('testimonial-prev');
    const next=document.getElementById('testimonial-next');
    if(prev)prev.addEventListener('click',()=>show(cur-1));
    if(next)next.addEventListener('click',()=>show(cur+1));
  }
  document.querySelectorAll('.stat-top-card__plus').forEach(btn=>{
    btn.addEventListener('click',e=>{
      e.stopPropagation();
      const card=btn.closest('.stat-top-card');
      const popup=card.querySelector('.stat-top-card__popup');
      const isOpen=card.classList.contains('is-open');
      document.querySelectorAll('.stat-top-card.is-open').forEach(c=>{c.classList.remove('is-open');c.querySelector('.stat-top-card__popup').classList.remove('is-open')});
      if(!isOpen){card.classList.add('is-open');popup.classList.add('is-open')}
    });
  });
  document.addEventListener('click',()=>{document.querySelectorAll('.stat-top-card.is-open').forEach(c=>{c.classList.remove('is-open');const p=c.querySelector('.stat-top-card__popup');if(p)p.classList.remove('is-open')})});
  document.querySelectorAll('.stat-top-card__popup').forEach(popup=>popup.addEventListener('click',e=>e.stopPropagation()));
}
