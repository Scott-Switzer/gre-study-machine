/* ================= GRE Study Machine — engine (part A) ================= */
/* Bank assembly: generated quant + curated + seed + persisted imports */
var GRE_IMPORTED = [];
try { GRE_IMPORTED = JSON.parse(localStorage.getItem('gre_imported_bank')||'[]')||[]; } catch(e){ GRE_IMPORTED=[]; }
var GRE_QUESTIONS = [];
if (typeof GRE_QUESTIONS_GEN !== "undefined") GRE_QUESTIONS = GRE_QUESTIONS.concat(GRE_QUESTIONS_GEN);
if (typeof GRE_VERBAL_GEN !== "undefined") GRE_QUESTIONS = GRE_QUESTIONS.concat(GRE_VERBAL_GEN);
if (typeof GRE_QUESTIONS_CURATED !== "undefined") GRE_QUESTIONS = GRE_QUESTIONS.concat(GRE_QUESTIONS_CURATED);
if (typeof GRE_QUESTIONS_SEED !== "undefined") GRE_QUESTIONS = GRE_QUESTIONS.concat(GRE_QUESTIONS_SEED);
GRE_QUESTIONS = GRE_QUESTIONS.concat(GRE_IMPORTED);
if (document.getElementById('side-count')) document.getElementById('side-count').textContent = GRE_QUESTIONS.length + ' questions · ' + (typeof GRE_VOCAB!=='undefined'?GRE_VOCAB.length:'—') + ' words';

var TYPE_LABEL = {mc:"Multiple Choice", tc:"Text Completion", se:"Sentence Equivalence",
  qc:"Quant Comparison", multi:"Select All", numeric:"Numeric Entry", rc:"Reading Comp"};
var ALL_TYPES = ["mc","tc","se","qc","multi","numeric","rc"];
var ALL_DIFFS = ["easy","medium","hard"];
var DIFF_RANK = {easy:0, medium:1, hard:2};

/* ================= STATE ================= */
var STORE_KEY = "gre_study_machine_v2";
var state = loadState();
function loadState(){ try{ return JSON.parse(localStorage.getItem(STORE_KEY))||{}; }catch(e){ return {}; } }
function saveState(){ try{ localStorage.setItem(STORE_KEY, JSON.stringify(state)); }catch(e){} }
/* state[qid] = {seen,correct,wrong,flagged}
   state['v:'+word] = {known, box(1-5), due(timestamp ms), last} */

/* ================= HELPERS ================= */
function shuff(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;} return a; }
function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function toast(msg,err){ var t=document.getElementById('toast'); t.textContent=msg; t.className='toast show'+(err?' err':''); clearTimeout(window._tt); window._tt=setTimeout(function(){t.className='toast'+(err?' err':'');},1700); }
function sections(){ var o={}; GRE_QUESTIONS.forEach(q=>o[q.section]=1); return Object.keys(o); }
function topics(){ var o={}; GRE_QUESTIONS.forEach(q=>o[q.topic||'General']=1); return Object.keys(o).sort(); }
function qOf(id){ return GRE_QUESTIONS.find(q=>q.id===id); }
function diffBadge(d){ return '<span class="diffbadge diff-'+d+'">'+d+'</span>'; }
function typeBadge(t){ return '<span class="typebadge">'+TYPE_LABEL[t]+'</span>'; }

/* ================= NAV ================= */
var PAGES=['dash','prac','custom','vocab','mock','full','awa','plan','imp','res','learn'];
function show(page){
  PAGES.forEach(p=>{
    var el=document.getElementById(p); if(el) el.classList.toggle('hidden', p!==page);
    var nav=document.getElementById('nav-'+p); if(nav) nav.classList.toggle('active', p===page);
  });
  document.getElementById('run').classList.add('hidden');
  if(page==='dash') renderDash();
  if(page==='prac') renderPracQuick();
  if(page==='custom') renderCustom();
  if(page==='vocab'){ document.getElementById('fc-area').classList.add('hidden'); document.getElementById('vlist-area').innerHTML=''; }
  if(page==='mock') renderMockSetup();
  if(page==='full') showFullStatus();
  if(page==='awa'){ document.getElementById('awa-area').classList.add('hidden'); document.getElementById('awa-bank').innerHTML=''; }
  if(page==='plan'){ /* keep plan-out */ }
  if(page==='res') renderResources();
  if(page==='learn') renderLearn();
}
function enterRun(navPage){
  PAGES.forEach(p=>{ var el=document.getElementById(p); if(el) el.classList.add('hidden'); var nav=document.getElementById('nav-'+p); if(nav) nav.classList.toggle('active', p===navPage); });
  document.getElementById('run').classList.remove('hidden');
  document.getElementById('run').scrollIntoView();
}

/* ================= DASHBOARD ================= */
function accFor(filterFn){
  var ids=Object.keys(state).filter(k=>GRE_QUESTIONS.some(q=>q.id===k));
  var c=0,t=0;
  ids.forEach(id=>{ if(filterFn && !filterFn(qOf(id))) return; var s=state[id]; c+=(s.correct||0); t+=(s.correct||0)+(s.wrong||0); });
  return t? c/t : 0;
}
// Real GRE raw->scaled shape (ETS). Values approximate the published
// conversion curves: verbal is harsher per-correct, quant is generous.
// Keyed by raw correct out of 20 (a standard section length); interpolated.
var GRE_SCORE_TABLE = {
  Verbal: [ // raw 0..20 -> scaled 130..170
    130,131,133,135,137,138,140,141,143,144,146,147,149,150,152,153,155,158,160,163,170],
  Quant: [ // raw 0..20
    130,131,132,134,135,137,138,140,141,143,144,146,147,149,150,152,153,155,157,160,170]
};
function estScore(section){
  var seen=GRE_QUESTIONS.filter(q=>q.section===section && state[q.id]);
  if(!seen.length) return null;
  var c=seen.reduce((s,q)=>s+((state[q.id].correct||0)>0?1:0),0);
  var t=seen.reduce((s,q)=>s+((state[q.id].correct||0)+(state[q.id].wrong||0)),0);
  if(t===0) return null;
  // Normalize to a 20-question section so the table applies, then interpolate.
  var raw = Math.min(20, Math.round(c / t * 20));
  var tbl = GRE_SCORE_TABLE[section] || GRE_SCORE_TABLE.Verbal;
  var lo = Math.floor(raw), hi = Math.min(20, lo+1), frac = raw-lo;
  var score = tbl[lo] + (tbl[hi]-tbl[lo])*frac;
  return Math.max(130, Math.min(170, Math.round(score)));
}
function renderDash(){
  document.getElementById('st-total').textContent=GRE_QUESTIONS.length;
  var ids=Object.keys(state).filter(k=>GRE_QUESTIONS.some(q=>q.id===k));
  var seen=ids.length, c=0,t=0;
  ids.forEach(id=>{ c+=(state[id].correct||0); t+=(state[id].correct||0)+(state[id].wrong||0); });
  document.getElementById('st-seen').textContent=seen;
  document.getElementById('st-acc').textContent=t?Math.round(c/t*100)+'%':'0%';
  var mastered=ids.filter(id=>state[id].wrong===0 && (state[id].seen||0)>=2).length;
  document.getElementById('st-mastered').textContent=mastered;
  var flagged=ids.filter(id=>state[id].flagged).length;
  document.getElementById('st-flagged').textContent=flagged;
  var vknown=Object.keys(state).filter(k=>k.indexOf('v:')===0 && state[k].known).length;
  document.getElementById('st-vocab').textContent=vknown+' / '+GRE_VOCAB.length;

  var ev=estScore('Verbal'), eq=estScore('Quant');
  document.getElementById('est-v').textContent=ev==null?'—':ev;
  document.getElementById('est-q').textContent=eq==null?'—':eq;
  document.getElementById('est-o').textContent=(ev==null&&eq==null)?'—':((ev==null?150:ev)+(eq==null?150:eq));

  // topic bars
  var tcount={}; GRE_QUESTIONS.forEach(q=>{ var tp=q.topic||'General'; tcount[tp]=(tcount[tp]||0)+1; });
  var th='';
  topics().forEach(tp=>{
    var qs=GRE_QUESTIONS.filter(q=>q.topic===tp);
    var sc=0,tt=0;
    qs.forEach(q=>{ var s=state[q.id]; if(s){ sc+=(s.correct||0); tt+=(s.correct||0)+(s.wrong||0);} });
    var a=tt?Math.round(sc/tt*100):0;
    var col=a>=70?'var(--good)':(tt===0?'var(--mut)':'var(--bad)');
    th+='<div class="secrow"><span class="name">'+esc(tp)+'</span><div class="bar" style="flex:2"><i style="width:'+a+'%;background:'+col+'"></i></div><span class="pct">'+a+'% · '+qs.length+'</span></div>';
  });
  document.getElementById('topicbars').innerHTML=th;

  // difficulty bars
  var dh='';
  ALL_DIFFS.forEach(d=>{
    var qs=GRE_QUESTIONS.filter(q=>q.difficulty===d);
    if(!qs.length) return;
    var sc=0,tt=0;
    qs.forEach(q=>{ var s=state[q.id]; if(s){ sc+=(s.correct||0); tt+=(s.correct||0)+(s.wrong||0);} });
    var a=tt?Math.round(sc/tt*100):0;
    dh+='<div class="secrow"><span class="name">'+d+' ('+qs.length+')</span><div class="bar" style="flex:2"><i style="width:'+a+'%"></i></div><span class="pct">'+a+'%</span></div>';
  });
  document.getElementById('diffbars').innerHTML=dh;

  // weak areas
  var weak=GRE_QUESTIONS.map(q=>{ var s=state[q.id]; var a=s?(s.correct||0)/((s.correct||0)+(s.wrong||0)||1):0; var sv=s?(s.seen||0):0; return {q,a,sv}; })
    .filter(x=>x.sv===0||x.a<0.7).sort((x,y)=>x.a-y.a).slice(0,10);
  var wh=weak.length?'':'<p class="muted">No weak areas yet — start a quiz.</p>';
  weak.forEach(x=>{ var tag=x.sv===0?'UNSEEN':Math.round(x.a*100)+'%'; wh+='<div class="secrow"><span class="name">'+esc(x.q.stem.slice(0,64))+'…</span><span class="pill" style="border-color:'+(x.sv===0?'var(--mut)':'var(--bad)')+';color:'+(x.sv===0?'var(--mut)':'var(--bad)')+'">'+tag+'</span><span class="small">'+esc(x.q.topic||'')+'</span></div>'; });
  document.getElementById('weak').innerHTML=wh;
}

/* ================= PRACTICE (quick) ================= */
function renderPracQuick(){
  var html='';
  sections().forEach(s=>{ html+='<button class="btn" data-k="sec" data-v="'+esc(s)+'">'+esc(s)+' ('+GRE_QUESTIONS.filter(q=>q.section===s).length+')</button>'; });
  Object.keys(TYPE_LABEL).forEach(t=>{ if(GRE_QUESTIONS.some(q=>q.type===t)) html+='<button class="btn" data-k="type" data-v="'+t+'">'+TYPE_LABEL[t]+'</button>'; });
  topics().forEach(tp=>{ html+='<button class="btn" data-k="topic" data-v="'+esc(tp)+'">'+esc(tp)+'</button>'; });
  var box=document.getElementById('prac-buttons'); box.innerHTML=html;
  box.querySelectorAll('.btn').forEach(b=>b.onclick=function(){ box.querySelectorAll('.btn').forEach(x=>x.classList.remove('active')); b.classList.add('active'); });
}
function beginQuick(){
  var btns=document.querySelectorAll('#prac-buttons .btn');
  var sel=null; btns.forEach(b=>{ if(b.classList.contains('active')) sel=b; });
  if(!sel){ toast('Pick a section, type, or topic first', true); return; }
  var k=sel.getAttribute('data-k'), v=sel.getAttribute('data-v');
  startQuizWith(k+':'+v);
}

/* ================= CUSTOM QUIZ BUILDER ================= */
function renderCustom(){
  var cs=document.getElementById('cust-sec'); cs.innerHTML='';
  ['Verbal','Quant'].forEach(s=>{ cs.innerHTML+='<label class="chk"><input type="checkbox" value="'+s+'" checked> '+s+'</label>'; });
  var ct=document.getElementById('cust-type'); ct.innerHTML='';
  ALL_TYPES.forEach(t=>{ if(GRE_QUESTIONS.some(q=>q.type===t)) ct.innerHTML+='<label class="chk"><input type="checkbox" value="'+t+'" checked> '+TYPE_LABEL[t]+'</label>'; });
  var cd=document.getElementById('cust-diff'); cd.innerHTML='';
  ALL_DIFFS.forEach(d=>{ cd.innerHTML+='<label class="chk"><input type="checkbox" value="'+d+'" checked> '+d+'</label>'; });
  var ctp=document.getElementById('cust-topics'); ctp.innerHTML='';
  topics().forEach(t=>{ ctp.innerHTML+='<label class="chk"><input type="checkbox" value="'+esc(t)+'" checked> '+esc(t)+'</label>'; });
}
function buildCustom(){
  var secs=[...document.querySelectorAll('#cust-sec input:checked')].map(i=>i.value);
  var types=[...document.querySelectorAll('#cust-type input:checked')].map(i=>i.value);
  var diffs=[...document.querySelectorAll('#cust-diff input:checked')].map(i=>i.value);
  var tps=[...document.querySelectorAll('#cust-topics input:checked')].map(i=>i.value);
  var pool=GRE_QUESTIONS.filter(q=> secs.indexOf(q.section)>=0 && types.indexOf(q.type)>=0 && diffs.indexOf(q.difficulty)>=0 && tps.indexOf(q.topic||'General')>=0 );
  if(!pool.length){ toast('No questions match those filters', true); document.getElementById('cust-info').textContent='0 match'; return; }
  var n=document.getElementById('cust-count').value;
  if(n==='all') n=pool.length; else n=Math.min(parseInt(n),pool.length);
  document.getElementById('cust-info').textContent=pool.length+' match · starting '+n;
  startRunner({qs:shuff(pool).slice(0,n), label:'Custom Quiz ('+n+')', mode:'practice'});
}

/* ================= UNIFIED QUIZ RUNNER ================= */
var RUN=null, runTimer=null, runDeadline=0;
function startQuizWith(sel, fixedN){
  var pool=GRE_QUESTIONS.slice();
  if(sel && sel!=='all'){
    var parts=sel.split(':'), k=parts[0], v=parts.slice(1).join(':');
    if(k==='sec') pool=pool.filter(q=>q.section===v);
    else if(k==='type') pool=pool.filter(q=>q.type===v);
    else if(k==='topic') pool=pool.filter(q=>(q.topic||'General')===v);
  }
  if(document.getElementById('onlyweak') && document.getElementById('onlyweak').checked){
    var w=pool.filter(q=>{ var s=state[q.id]; return !s||(s.wrong||0)>0||(s.seen||0)===0; });
    if(w.length) pool=w;
  }
  var n=fixedN||document.getElementById('qcount').value;
  if(n==='all') n=pool.length; else n=Math.min(parseInt(n),pool.length);
  startRunner({qs:shuff(pool).slice(0,n), label:'Practice ('+n+')', mode:'practice'});
}
function startWeakDrill(){
  var ranked=sections().map(s=>({s,score:accFor(q=>q.section===s)*100 - unseenCount(s)*50})).sort((a,b)=>a.score-b.score);
  var pool=[];
  ranked.forEach(({s})=>{
    var qs=GRE_QUESTIONS.filter(q=>q.section===s);
    var wrong=qs.filter(q=>{var st=state[q.id];return st&&(st.wrong||0)>0;});
    var unseen=qs.filter(q=>{var st=state[q.id];return !st||(st.seen||0)===0;});
    var rest=qs.filter(q=>{var st=state[q.id];return st&&(st.wrong||0)===0&&(st.seen||0)>0;});
    pool=pool.concat(wrong,unseen,rest);
  });
  if(!pool.length){ toast('No questions yet — run a quiz first'); return; }
  startRunner({qs:pool.slice(0,Math.min(40,pool.length)), label:'Weak Drill', mode:'practice'});
}
function startMistakes(){
  var wrong=GRE_QUESTIONS.filter(q=>{var st=state[q.id];return st&&(st.wrong||0)>0;});
  if(!wrong.length){ toast('No mistakes yet'); return; }
  startRunner({qs:shuff(wrong), label:'Mistakes', mode:'practice'});
}
function startSRS(){
  // Spaced repetition: due (overdue or due now) questions, oldest due first.
  var now=Date.now();
  var due=GRE_QUESTIONS.filter(q=>{ var st=state[q.id]; return st && st.seen>0 && (st.due||0)<=now; });
  if(!due.length){ toast('Nothing due — all reviewed. Drill more to build a queue.'); return; }
  due.sort((a,b)=>(state[a.id].due||0)-(state[b.id].due||0));
  startRunner({qs:due.slice(0,Math.min(40,due.length)), label:'SRS Review ('+due.length+' due)', mode:'practice'});
}
function unseenCount(sec){ var u=0; GRE_QUESTIONS.filter(q=>q.section===sec).forEach(q=>{var st=state[q.id]; if(!st||(st.seen||0)===0)u++;}); return u; }
function startRunner(opts){
  RUN=Object.assign({idx:0,correct:0,answers:{},flagged:{},mode:'practice',showTimer:false,timeLimit:0,sectionLabel:'',onDone:null},opts);
  RUN.qs=opts.qs||[];
  enterRun('prac');
  if(opts.mode==='mock'||opts.mode==='full'){ enterRun('mock'); }
  if(opts.mode==='full'){ enterRun('full'); }
  renderRunQ();
  if(RUN.showTimer && RUN.timeLimit){ startRunTimer(); } else { stopRunTimer(); }
}
function stopRunTimer(){ if(runTimer){ clearInterval(runTimer); runTimer=null; } }
function startRunTimer(){
  runDeadline=Date.now()+RUN.timeLimit*1000;
  var tick=function(){
    var left=Math.max(0,Math.round((runDeadline-Date.now())/1000));
    var t=document.getElementById('run-timer'); if(!t) return;
    t.textContent=Math.floor(left/60)+':'+('0'+(left%60)).slice(-2);
    t.className='timer'+(left<=30?' crit':(left<=60?' warn':''));
    if(left<=0){ stopRunTimer(); finishRun(true); }
  };
  tick(); runTimer=setInterval(tick,1000);
}
function renderRunQ(){
  var q=RUN.qs[RUN.idx];
  var mock=RUN.mode==='mock'||RUN.mode==='full';
  var gridHtml = mock ? '<div class="qgrid" id="run-grid"></div>' : '';
  var flagHtml = '<button class="flagbtn" id="run-flag" onclick="toggleRunFlag()">⚑ Flag</button>';
  var navHtml='';
  if(mock){
    navHtml='<button class="btn" onclick="runPrev()">← Prev</button>'+
      '<button class="btn primary" id="run-nextbtn" onclick="runNext()">Next →</button>'+
      '<button class="btn primary hidden" id="run-submitbtn" onclick="finishRun(false)">Submit</button>';
  } else {
    navHtml='<button class="btn primary hidden" id="run-nextbtn" onclick="runNext()">Next →</button>'+
      '<button class="btn hidden" id="run-finishbtn" onclick="finishRun(false)">Finish</button>';
  }
  var timerHtml = RUN.showTimer ? '<span class="timer" id="run-timer">--:--</span>' : '';
  var html='<div class="card">'+
    '<div class="exambar"><span class="pill" id="run-label">'+esc(RUN.label)+'</span>'+timerHtml+'</div>'+
    gridHtml+
    (mock?'<div class="qmeta"><span id="run-sec" class="pill"></span><span id="run-flagstat"></span></div>':'')+
    '<div id="run-passage"></div>'+
    '<div class="qstem" id="run-stem"></div>'+
    '<div id="run-choices"></div>'+
    '<div class="exp hidden" id="run-exp"></div>'+
    '<div class="row" style="margin-top:14px">'+flagHtml+navHtml+'</div>'+
    '</div>';
  document.getElementById('run').innerHTML=html;
  // fill question
  document.getElementById('run-section-pill')&&0;
  if(mock){ document.getElementById('run-sec').innerHTML=typeBadge(q.type)+(q.topic?' <span class="tag">'+esc(q.topic)+'</span>':''); }
  else { document.getElementById('run-label').innerHTML=esc(RUN.label)+typeBadge(q.type)+diffBadge(q.difficulty||'easy'); }
  var pg=document.getElementById('run-passage'); pg.innerHTML=q.passage?'<div class="passage">'+esc(q.passage)+'</div>':'';
  document.getElementById('run-stem').textContent=q.stem;
  var c=document.getElementById('run-choices'); c.innerHTML=''; window._rsel={};
  if(q.type==='numeric'){
    var wrap=document.createElement('div'); wrap.className='numeric-wrap';
    var inp=document.createElement('input'); inp.type='text'; inp.id='r-num'; inp.value=RUN.answers[RUN.idx]||''; inp.autocomplete='off';
    var sub=document.createElement('button'); sub.className='btn primary'; sub.textContent='Submit'; sub.onclick=function(){ answerRun(q); };
    wrap.appendChild(inp); wrap.appendChild(sub); c.appendChild(wrap); setTimeout(()=>inp.focus(),40);
  } else {
    Object.keys(q.choices).forEach(k=>{
      var b=document.createElement('button'); b.className='choice';
      if(mock && RUN.answers[RUN.idx] && RUN.answers[RUN.idx].indexOf(k)>=0) b.classList.add('sel');
      b.innerHTML='<span class="lk">'+k+'</span>'+esc(q.choices[k]);
      b.onclick=function(){
        if(q.type==='multi'||q.type==='se'){ if(window._rsel[k]){delete window._rsel[k];b.classList.remove('sel');} else {window._rsel[k]=true;b.classList.add('sel');} }
        else { document.querySelectorAll('#run-choices .choice').forEach(x=>x.classList.remove('sel')); window._rsel={}; window._rsel[k]=true; b.classList.add('sel'); }
      };
      c.appendChild(b);
    });
    if(q.type==='multi'||q.type==='se'){ var go=document.createElement('button'); go.className='btn primary'; go.textContent='Submit'; go.onclick=function(){answerRun(q);}; c.appendChild(go); }
  }
  if(mock) renderRunGrid();
  var fb=document.getElementById('run-flag'); if(fb){ fb.classList.toggle('on',!!RUN.flagged[RUN.idx]); }
  document.getElementById('run-exp').classList.add('hidden');
}
function renderRunGrid(){
  var g=document.getElementById('run-grid'); if(!g) return; g.innerHTML='';
  RUN.qs.forEach((q,idx)=>{
    var b=document.createElement('button'); b.textContent=idx+1;
    if(idx===RUN.idx) b.classList.add('cur');
    if(RUN.answers[idx]!=null && !(Array.isArray(RUN.answers[idx])&&RUN.answers[idx].length===0)) b.classList.add('answered');
    if(RUN.flagged[idx]) b.classList.add('flag');
    b.onclick=function(){ recordRun(); RUN.idx=idx; renderRunQ(); };
    g.appendChild(b);
  });
  var fs=document.getElementById('run-flagstat'); if(fs) fs.textContent=Object.keys(RUN.flagged).filter(k=>RUN.flagged[k]).length+' flagged';
}
function toggleRunFlag(){
  RUN.flagged[RUN.idx]=!RUN.flagged[RUN.idx];
  var fb=document.getElementById('run-flag'); if(fb) fb.classList.toggle('on',!!RUN.flagged[RUN.idx]);
  renderRunGrid();
}
function recordRun(){
  var q=RUN.qs[RUN.idx];
  if(q.type==='numeric'){ var el=document.getElementById('r-num'); RUN.answers[RUN.idx]=el?el.value:''; }
  else { RUN.answers[RUN.idx]=Object.keys(window._rsel).filter(k=>window._rsel[k]); }
}
function correctKeys(q){
  if(q.type==='multi'||q.type==='se') return (Array.isArray(q.answer)?q.answer:[q.answer]).slice().sort();
  if(q.type==='qc') return [q.answer];
  if(q.type==='numeric') return null;
  return [q.answer];
}
// Enrich an explanation into a teaching note (pulls vocab definitions for verbal answers).
function wordDef(w){
  var key=String(w||'').replace(/[^A-Za-z]/g,'').toLowerCase();
  if(!key) return '';
  for(var i=0;i<GRE_VOCAB.length;i++){ var v=GRE_VOCAB[i]; if(v.word.replace(/[^A-Za-z]/g,'').toLowerCase()===key) return v.word+' ('+v.pos+'): '+v.def+'.'; }
  return '';
}
function teachNote(q){
  var base=(q.explanation||'').trim();
  if((q.type==='tc'||q.type==='se') && q.choices){
    var ans=Array.isArray(q.answer)?q.answer:[q.answer];
    var defs=ans.map(function(k){ return wordDef(q.choices[k]); }).filter(Boolean);
    if(defs.length){ base += (base? ' ' : '') + 'Word meaning — ' + defs.join(' '); }
  }
  return base || 'No explanation on file — review the answer and topic.';
}
function answerRun(q){
  if(!document.getElementById('run-exp').classList.contains('hidden')) return;
  var isCorrect;
  if(q.type==='numeric'){ var raw=document.getElementById('r-num').value.trim(); isCorrect=(raw===String(q.answer)); window._rsel={__num:raw}; }
  else if(q.type==='multi'||q.type==='se'){ var picked=Object.keys(window._rsel).filter(k=>window._rsel[k]).sort(); var ans=correctKeys(q); isCorrect=picked.length===ans.length&&picked.every(k=>ans.indexOf(k)>=0); }
  else { var ps=Object.keys(window._rsel).filter(k=>window._rsel[k]); isCorrect=ps.length===1&&ps[0]===q.answer; }
  // UI mark
  if(q.type!=='numeric'){
    document.querySelectorAll('#run-choices .choice').forEach(b=>{ var lk=b.querySelector('.lk'); var l=lk?lk.textContent:''; if(correctKeys(q).indexOf(l)>=0) b.classList.add('correct'); else if(window._rsel[l]) b.classList.add('wrong'); b.onclick=null; });
    document.querySelectorAll('#run-choices .btn').forEach(b=>b.onclick=null);
  }
  // state
  if(!state[q.id]) state[q.id]={seen:0,correct:0,wrong:0,box:0,due:0};
  state[q.id].seen++; if(isCorrect){state[q.id].correct++;RUN.correct++;} else state[q.id].wrong++;
  // Spaced repetition: correct -> promote box + longer interval; wrong -> reset to box 1 (due now)
  var st=state[q.id];
  if(isCorrect){ st.box=Math.min(5,(st.box||0)+1); }
  else { st.box=1; }
  var intervals=[0,0,1,3,7,16]; // days for box 1..5
  st.due=Date.now()+ (intervals[st.box]||0)*86400000;
  saveState();
  // explanation
  var e=document.getElementById('run-exp');
  var ansTxt,youTxt;
  if(q.type==='numeric'){ youTxt=window._rsel.__num||'(blank)'; ansTxt=String(q.answer); }
  else if(q.type==='qc'){ youTxt=(Object.keys(window._rsel).filter(k=>window._rsel[k])[0])||'(none)'; ansTxt=q.choices[q.answer]||q.answer; }
  else { var pk=Object.keys(window._rsel).filter(k=>window._rsel[k]); youTxt=pk.length?pk.map(k=>k+'. '+q.choices[k]).join('; '):'(none)'; ansTxt=(q.type==='multi'||q.type==='se')?correctKeys(q).map(k=>k+'. '+q.choices[k]).join('; '):(q.choices[q.answer]||q.answer); }
  e.innerHTML='<div class="exp-head '+(isCorrect?'ok':'no')+'">'+(isCorrect?'✓ Correct':'✗ Incorrect')+'</div>'+
    '<div class="exp-why"><b>You:</b> '+esc(youTxt)+'</div>'+
    '<div class="exp-why"><b>Answer:</b> '+esc(ansTxt)+'</div>'+
    '<div class="exp-why"><b>Why:</b> '+esc(teachNote(q))+'</div>'+
    '<div class="exp-src muted">Source: '+(q.source||'bank')+(q.topic?' · '+esc(q.topic):'')+'</div>';
  e.classList.remove('hidden');
  if(RUN.mode==='practice'){
    if(RUN.idx===RUN.qs.length-1) document.getElementById('run-finishbtn').classList.remove('hidden');
    else document.getElementById('run-nextbtn').classList.remove('hidden');
  } else {
    document.getElementById('run-nextbtn').classList.toggle('hidden', RUN.idx===RUN.qs.length-1);
    document.getElementById('run-submitbtn').classList.toggle('hidden', RUN.idx!==RUN.qs.length-1);
  }
  toast(isCorrect?'Correct ✓':'Incorrect ✗');
}
function runNext(){ recordRun(); if(RUN.idx<RUN.qs.length-1){ RUN.idx++; renderRunQ(); } }
function runPrev(){ recordRun(); if(RUN.idx>0){ RUN.idx--; renderRunQ(); } }
function finishRun(auto){
  recordRun(); stopRunTimer();
  // grade all answered
  RUN.qs.forEach((q,idx)=>{
    var a=RUN.answers[idx]; if(a==null||(Array.isArray(a)&&a.length===0)) return;
    var ok;
    if(q.type==='numeric') ok=(String(a).trim()===String(q.answer));
    else if(q.type==='multi'||q.type==='se'){ var ans=correctKeys(q); var p=(Array.isArray(a)?a:[]).slice().sort(); ok=p.length===ans.length&&p.every(k=>ans.indexOf(k)>=0); }
    else ok=(Array.isArray(a)?a[0]:a)===q.answer;
    if(!state[q.id]) state[q.id]={seen:0,correct:0,wrong:0};
    state[q.id].seen++; if(ok) state[q.id].correct++; else state[q.id].wrong++;
  });
  saveState();
  if(RUN.mode==='practice'){ showPracticeResult(); }
  else { showRunReview(auto); }
}
function showPracticeResult(){
  var pct=RUN.qs.length?Math.round(RUN.correct/RUN.qs.length*100):0;
  var html='<div class="card"><div class="result-big"><div class="score" style="font-size:46px;font-weight:800">'+pct+'%</div>'+
    '<div class="muted">'+RUN.correct+' / '+RUN.qs.length+' correct</div></div>'+
    '<div class="row" style="justify-content:center;margin-top:12px">'+
    '<button class="btn primary" onclick="retryRun()">Retry</button>'+
    '<button class="btn" onclick="show(\'dash\')">Dashboard</button></div></div>';
  document.getElementById('run').innerHTML=html;
  renderDash();
}
function retryRun(){ startRunner({qs:shuff(RUN.qs), label:RUN.label, mode:RUN.mode}); }
function showRunReview(auto){
  var correct=RUN.qs.filter((q,idx)=>{ var a=RUN.answers[idx]; if(a==null||(Array.isArray(a)&&a.length===0)) return false;
    if(q.type==='numeric') return String(a).trim()===String(q.answer);
    if(q.type==='multi'||q.type==='se'){ var ans=correctKeys(q); var p=(Array.isArray(a)?a:[]).slice().sort(); return p.length===ans.length&&p.every(k=>ans.indexOf(k)>=0); }
    return (Array.isArray(a)?a[0]:a)===q.answer; }).length;
  var pct=Math.round(correct/RUN.qs.length*100);
  var rows='';
  RUN.qs.forEach((q,idx)=>{
    var a=RUN.answers[idx]; var ok=false;
    if(a!=null&&!(Array.isArray(a)&&a.length===0)){
      if(q.type==='numeric') ok=String(a).trim()===String(q.answer);
      else if(q.type==='multi'||q.type==='se'){ var ans=correctKeys(q); var p=(Array.isArray(a)?a:[]).slice().sort(); ok=p.length===ans.length&&p.every(k=>ans.indexOf(k)>=0); }
      else ok=(Array.isArray(a)?a[0]:a)===q.answer;
    }
    var ansTxt=q.type==='numeric'?String(q.answer):(q.type==='multi'||q.type==='se')?correctKeys(q).map(k=>k+'. '+q.choices[k]).join('; '):(q.choices[q.answer]||q.answer);
    var youTxt=a==null?'(blank)':q.type==='numeric'?String(a):(Array.isArray(a)?a:[a]).map(k=>k+'. '+(q.choices[k]||k)).join('; ');
    var teach=teachNote(q);
    rows+='<div class="revrow"><span class="'+(ok?'ok':'no')+'">'+(ok?'✓':'✗')+'</span><div style="flex:1"><div class="muted small">'+esc(q.section)+' · '+TYPE_LABEL[q.type]+(q.topic?' · '+esc(q.topic):'')+'</div>'+
      '<div>'+esc(q.stem.slice(0,110))+(q.stem.length>110?'…':'')+'</div>'+
      '<div class="small">You: '+esc(youTxt)+'</div>'+
      '<div class="small" style="color:var(--good)">Answer: '+esc(ansTxt)+'</div>'+
      (teach?'<div class="small exp-teach">💡 '+esc(teach)+'</div>':'')+
      (!ok?'<button class="btn small" style="margin-top:5px" onclick="markUnderstood(\''+q.id+'\')">I understand this ✓</button>':'')+
      '</div></div>';
  });
  var html='<div class="card"><div class="result-big"><div class="score" style="font-size:46px;font-weight:800">'+pct+'%</div>'+
    '<div class="muted">'+correct+' / '+RUN.qs.length+' · '+(RUN.sectionLabel||RUN.label)+(auto?' (time up)':'')+'</div></div>'+
    '<div class="row" style="justify-content:center;margin-top:12px"><button class="btn" onclick="renderRunReviewList()">Review answers</button>'+
    '<button class="btn primary" onclick="runDone()">Continue</button></div></div>'+
    '<div class="card hidden" id="run-reviewlist"><h2>Review</h2>'+rows+'</div>';
  document.getElementById('run').innerHTML=html;
  window._runReviewRows=rows;
  if(RUN.onDone && !auto) RUN.onDone(RUN);
}
function renderRunReviewList(){ var el=document.getElementById('run-reviewlist'); if(el){ el.classList.remove('hidden'); el.innerHTML='<h2>Review</h2>'+window._runReviewRows; } }
function runDone(){ if(RUN.onDone) RUN.onDone(RUN); else show('dash'); }
function markUnderstood(qid){
  if(!state[qid]) state[qid]={seen:0,correct:0,wrong:0,box:0,due:0};
  // understood => keep progress but resurface in ~10 min for reinforcement, bump box lightly
  state[qid].box=Math.min(5,(state[qid].box||0)+1);
  state[qid].due=Date.now()+10*60000;
  saveState();
  toast('Added to review queue (resurfaces soon) ✓');
}

/* ================= LEARN CONCEPTS ================= */
var CONCEPT_NOTES={
  'Arithmetic':{t:'Arithmetic',n:'Percents, ratios, averages, exponents, roots, primes, remainders, sequences. Core quant floor — most errors come from careless arithmetic, not concepts. Drill daily.'},
  'Algebra':{t:'Algebra',n:'Solve linear/quadratic equations, manipulate inequalities, work with functions and systems. Isolate the variable; check domain restrictions on functions.'},
  'Geometry':{t:'Geometry',n:'Lines, angles, triangles, circles, area, volume, coordinate geometry. Memorize the Pythagorean triples and circle formulas; most GRE geometry is plug-and-chug after you see the shape.'},
  'Data':{t:'Data Analysis',n:'Probability, counting (permutations/combinations), sets, statistics (mean/median/mode/SD). For probability, count favorable / total outcomes; watch "with vs without replacement".'},
  'QC':{t:'Quant Comparison',n:'Decide A > B, B > A, equal, or cannot determine. Try to prove they could differ before picking "cannot determine". Plug in 0, 1, a negative, and a fraction.'},
  'tc':{t:'Text Completion',n:'Read for the logic signal (contrast "but"/"yet", support "therefore"). Predict the blank before looking at choices; pick the word whose meaning fits your prediction.'},
  'se':{t:'Sentence Equivalence',n:'Find TWO words that fit the blank AND are near-synonyms. If the two answers don\'t mean roughly the same thing, one is wrong. Build vocab daily.'},
  'rc':{t:'Reading Comp',n:'Read the first/last sentence of each paragraph for structure. Questions test main point, inference, and detail — go back to the text; don\'t rely on memory.'},
  'verbal-strategy':{t:'Verbal Strategy',n:'Your likely weaker section (quant majors). Spend 60% of verbal time on vocab SRS; learn 15 words/day. TC/SE reward pattern recognition, not deep reading.'}
};
function conceptAccFor(prefix){
  var qs=GRE_QUESTIONS.filter(q=>{ var tp=q.topic||''; return tp.indexOf(prefix)===0 || (prefix==='tc'&&q.type==='tc') || (prefix==='se'&&q.type==='se') || (prefix==='rc'&&q.type==='rc'); });
  if(!qs.length) return null;
  var c=0,t=0; qs.forEach(q=>{var s=state[q.id]; if(s){c+=s.correct||0; t+=(s.correct||0)+(s.wrong||0);}});
  return t? c/t : null;
}
function renderLearn(){
  var groups=[
    {label:'Quant Concepts', keys:['Arithmetic','Algebra','Geometry','Data','QC']},
    {label:'Verbal Concepts', keys:['tc','se','rc','verbal-strategy']}
  ];
  var html='';
  groups.forEach(function(g){
    html+='<h2 style="margin:16px 0 8px">'+g.label+'</h2>';
    g.keys.forEach(function(k){
      var note=CONCEPT_NOTES[k]; if(!note) return;
      var acc=conceptAccFor(k);
      var flag = acc===null ? '' : (acc<0.6 ? ' <span class="pill" style="background:var(--bad);color:#fff">weak ('+Math.round(acc*100)+'%)</span>' : ' <span class="pill" style="background:var(--good);color:#fff">'+Math.round(acc*100)+'%</span>');
      var drill = k==='tc'||k==='se'||k==='rc' ? 'startQuizWith(\'type:'+k+'\')' : 'startQuizWith(\'topic:'+k+'\')';
      html+='<div class="card" style="margin-bottom:10px"><div style="display:flex;justify-content:space-between;align-items:center"><b>'+note.t+'</b>'+flag+'</div>'+
        '<p class="small" style="margin:6px 0 10px">'+note.n+'</p>'+
        '<button class="btn small" onclick="'+drill+'">Drill '+note.t+' →</button></div>';
    });
  });
  document.getElementById('learn-body').innerHTML=html;
}

/* ================= RESOURCES ================= */
function renderResources(){
  var RES=[
    {cat:'official', items:[
      ['POWERPREP Online (free practice tests)', 'https://www.ets.org/gre/test-takers/general-test/prepare/powerprep.html', 'Two free full-length adaptive tests from ETS - the gold standard for calibrating your real score.'],
      ['ETS GRE Paper Practice Book (PDF)', 'https://www.ets.org/content/dam/ets-india/pdfs/gre/paper-delivered-test-practice-book.pdf', 'Free official practice test with real questions and scoring guide.'],
      ['ETS Quantitative Reasoning Practice Questions', 'https://hiast.edu.sy/sites/default/files/general/ETS-GRE%20Quantitative%20Reasoning.pdf', 'Official 150 quant questions with explanations (mirrors the paid book).']
    ]},
    {cat:'practice', items:[
      ['GregMat (free + low-cost)', 'https://www.gregmat.com/', 'Extremely popular GRE prep - free vocab groups, study plans, and video walkthroughs.'],
      ['Magoosh GRE eBook (free)', 'https://gre.magoosh.com/gre-ebook', 'Complete free strategy guide covering all sections.'],
      ['Magoosh 1000-Word GRE List (PDF)', 'https://s3.amazonaws.com/magoosh.resources/magoosh-gre-1000-words_oct01.pdf', 'Free high-frequency vocab list - pair with this app’s flashcards.'],
      ['The GRE Big Book (27 tests)', 'https://drive.google.com/drive/u/0/folders/0Bwy2T5wsuholfmtwMEJDN1JLZXd6UmhEd1dXWW10cTYwV3d4dkJ3UHF5czNVeThMaWg4WWc', 'Out-of-print ETS old tests - tons of real practice questions (use for drilling, not scoring).'],
      ['Mometrix Free Quant Practice', 'https://www.mometrix.com/academy/gre-quantitative-practice-test/', 'Free practice test with answer explanations.'],
      ['Kaplan Free GRE Questions', 'https://www.kaptest.com/gre/free/gre-20-minute-workout', 'Short free workout of mixed questions.']
    ]},
    {cat:'vocab', items:[
      ['Magoosh Vocabulary Builder (app)', 'https://play.google.com/store/apps/details?id=com.magoosh.gre.quiz.vocabulary', 'Free spaced-repetition vocab app from Magoosh.'],
      ['Quizlet 500 GRE Words', 'https://quizlet.com/14840887/500-practice-gre-vocabulary-words-flash-cards/', 'Free community flashcard deck of 500 words.'],
      ['Barron’s 800 Essential (Memrise)', 'https://www.memrise.com/course/121215/barrons-800-essential-word-list-gre/', 'Free public deck of Barron’s 800 core words.'],
      ['Kaplan Top 500 GRE Words (video)', 'https://www.youtube.com/watch?v=9fz456TIdJs', 'Free video list of 500 words with definitions.']
    ]},
    {cat:'video', items:[
      ['Awesome GRE Materials (curated index)', 'https://github.com/rishiloyola/Awesome-GRE-Materials', 'Community list of free blogs, apps, books, and video lectures.'],
      ['ETS GRE YouTube', 'https://www.youtube.com/user/GREtestprep', 'Official ETS channel with question walkthroughs.'],
      ['Khan Academy (math foundations)', 'https://www.khanacademy.org/math', 'Free refresher on the algebra/geometry/arithmetic the quant section tests.']
    ]}
  ];
  var map={official:'res-official', practice:'res-practice', vocab:'res-vocab', video:'res-video'};
  RES.forEach(function(g){
    var html='';
    g.items.forEach(function(it){
      html+='<div class="revrow" style="border-color:var(--line)"><div style="flex:1"><a href="'+it[1]+'" target="_blank" rel="noopener" style="font-weight:700;font-size:13.5px">'+it[0]+'</a><div class="small" style="margin-top:3px">'+it[2]+'</div><div class="small" style="margin-top:2px;opacity:.7">'+it[1]+'</div></div></div>';
    });
    document.getElementById(map[g.cat]).innerHTML=html;
  });
  document.getElementById('res-banksize').textContent='This app currently holds '+GRE_QUESTIONS.length+' questions and '+GRE_VOCAB.length+' vocabulary words, all generated and free to use.';
}
