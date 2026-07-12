/* ================= GRE Study Machine — engine (part B) ================= */
/* ================= VOCAB (SRS) ================= */
var fcDeck=[], fcI=0, fcFlipped=false;
function vstate(w){ if(!state['v:'+w]) state['v:'+w]={known:false,box:0,due:0,last:0}; return state['v:'+w]; }
function vocabKnown(w){ return vstate(w).known; }
function fcStart(mode){
  var pool=GRE_VOCAB.slice();
  if(mode==='unknown') pool=pool.filter(v=>!vocabKnown(v.word));
  if(mode==='due') pool=pool.filter(v=>!vocabKnown(v.word) && vstate(v.word).due<=Date.now());
  if(!pool.length){ toast(mode==='due'?'Nothing due right now':'All known — browse A–Z'); document.getElementById('fc-area').classList.add('hidden'); return; }
  fcDeck=shuff(pool); fcI=0;
  document.getElementById('vlist-area').innerHTML='';
  document.getElementById('fc-area').classList.remove('hidden');
  fcRender();
}
function fcRender(){
  var v=fcDeck[fcI]; fcFlipped=false; var st=vstate(v.word);
  document.getElementById('fc-w').textContent=v.word;
  document.getElementById('fc-pos').textContent=v.pos+(st.box?' · box '+st.box:'');
  document.getElementById('fc-d').textContent=v.def;
  document.getElementById('fc-e').textContent='“'+v.ex+'”';
  document.getElementById('fc-d').classList.add('hidden');
  document.getElementById('fc-e').classList.add('hidden');
  document.getElementById('fc-flip').textContent='click to reveal';
  document.getElementById('fc-poscount').textContent=(fcI+1)+' / '+fcDeck.length+(vocabKnown(v.word)?'  ✓':'');
}
function fcFlip(){ fcFlipped=!fcFlipped; document.getElementById('fc-d').classList.toggle('hidden',!fcFlipped); document.getElementById('fc-e').classList.toggle('hidden',!fcFlipped); document.getElementById('fc-flip').textContent=fcFlipped?'click to hide':'click to reveal'; }
function fcKnown(){ var st=vstate(fcDeck[fcI].word); st.known=true; st.box=Math.min(5,(st.box||0)+1); st.due=Date.now()+boxInterval(st.box); st.last=Date.now(); saveState(); fcNext(); }
function fcAgain(){ var st=vstate(fcDeck[fcI].word); st.known=false; st.box=0; st.due=Date.now(); st.last=Date.now(); saveState(); fcNext(); }
function boxInterval(box){ // spaced intervals in ms
  var days=[0,1,3,7,16,35]; var d=days[Math.min(box,5)]; return d*24*3600*1000;
}
function fcNext(){ if(fcI<fcDeck.length-1){fcI++;fcRender();} else { toast('Deck done'); document.getElementById('fc-area').classList.add('hidden'); } }
function fcPrev(){ if(fcI>0){fcI--;fcRender();} }
function renderVocabList(){
  document.getElementById('fc-area').classList.add('hidden');
  var known=GRE_VOCAB.filter(v=>vocabKnown(v.word)).length;
  var due=GRE_VOCAB.filter(v=>!vocabKnown(v.word)&&vstate(v.word).due<=Date.now()).length;
  var html='<p class="small">'+known+' / '+GRE_VOCAB.length+' known · '+due+' due for review</p><div class="vlist">';
  GRE_VOCAB.forEach(v=>{ var kn=vocabKnown(v.word); html+='<div class="vchip '+(kn?'known':'')+'" onclick="quickFlip(\''+v.word.replace(/'/g,"\\'")+'\')"><b>'+esc(v.word)+'</b>'+(kn?' ✓':'')+'</div>'; });
  html+='</div>';
  document.getElementById('vlist-area').innerHTML=html;
}
function quickFlip(w){ var v=GRE_VOCAB.find(x=>x.word===w); if(!v) return; alert(v.word+'  '+v.pos+'\n\n'+v.def+'\n\n“'+v.ex+'”'); }

/* ================= MOCK SECTION ================= */
var SECTION_TIME={verbal:30*60,quant:35*60};
function renderMockSetup(){
  document.getElementById('mock-run-wrap').innerHTML='';
}
function startMock(kind){
  var sec=kind==='quant'?'Quant':'Verbal';
  var pool=GRE_QUESTIONS.filter(q=>q.section===sec);
  if(pool.length<10){ toast('Need ≥10 '+sec+' questions; have '+pool.length, true); return; }
  var n=Math.min(20,pool.length);
  startRunner({qs:shuff(pool).slice(0,n), label:sec+' Section', sectionLabel:sec, mode:'mock', showTimer:true, timeLimit:SECTION_TIME[kind],
    onDone:function(r){ if(r.__next){ r.__next(); } }});
  if(n<20) toast('Short: '+n+' '+sec+' questions (add more for full 20)', true);
}

/* ================= FULL TEST ================= */
var FULL=null;
var AWA_PROMPTS={
  issue:[
    "As people rely more and more on technology to solve problems, the ability of humans to think for themselves will surely deteriorate. Develop your perspective on the issue below, using relevant reasons and examples to support your views.",
    "Governments should place few, if any, restrictions on scientific research and development. Develop your perspective, using examples to support your views.",
    "The best way to teach is to praise positive actions and ignore negative ones. Develop your perspective, using examples to support your views.",
    "Society should make efforts to save endangered species only if the potential extinction of those species is the result of human activities. Develop your perspective.",
    "Colleges and universities should require their students to spend at least one semester studying abroad. Develop your perspective."
  ],
  argument:[
    "The following appeared in a memo from the vice president of a food company: 'Our competitor's low-price approach has cut into our market share. The best way to regain customers is to slash prices by 20% and launch a national ad campaign. We will thus reverse the sales decline.' Discuss what questions would need to be answered to evaluate this recommendation.",
    "The following appeared in a letter to the editor: 'Two years ago, the town of Seaside opened a new ferry line, and tourism rose 30%. Therefore, the nearby town ofNorthgate should build a ferry line to boost its own tourism.' Discuss what is needed to evaluate the argument.",
    "The following appeared in an article on local schools: 'Since Oak City implemented a laptop program for all students, test scores rose 12%. Clearly, providing laptops to students improves academic performance.' Discuss how well the evidence supports the conclusion.",
    "A bike-rental company concluded: 'Because our downtown location had 40% more rentals than our university location, we should close the university branch and expand downtown.' Discuss what questions would need to be answered.",
    "The following recommendation appeared in a business review: 'To increase profits, our company should reduce its workforce by 15%. Our competitor did this and saw profits rise.' Discuss the assumptions and what would be needed to evaluate the claim."
  ]
};
function startFullTest(){
  FULL={stage:0, results:{}, started:Date.now()};
  document.getElementById('full-status').innerHTML='<p class="small">Starting full test…</p>';
  awaStart('issue', function(){ awaStart('argument', function(){ runFullSection('Verbal', 1); }); });
}
function runFullSection(sec, n){
  var pool=GRE_QUESTIONS.filter(q=>q.section===sec);
  var cnt=Math.min(20,pool.length);
  startRunner({qs:shuff(pool).slice(0,cnt), label:sec+' '+n, sectionLabel:sec+' '+n, mode:'full', showTimer:true, timeLimit:SECTION_TIME[sec==='Quant'?'quant':'verbal'],
    onDone:function(r){
      FULL.results[sec+' '+n]=(r.correct||0)+'/'+r.qs.length;
      var vDone=Object.keys(FULL.results).filter(k=>k.indexOf('Verbal')>=0).length;
      var qDone=Object.keys(FULL.results).filter(k=>k.indexOf('Quant')>=0).length;
      if(vDone>=2 && qDone>=2){ finishFullTest(); }
      else {
        var nextSec = (sec==='Verbal') ? 'Quant' : 'Verbal';
        var nextN = (nextSec==='Verbal') ? vDone+1 : qDone+1;
        toast(nextSec+' '+nextN+' next'); runFullSection(nextSec, nextN);
      }
    }});
  if(cnt<20) toast('Short '+sec+' section ('+cnt+' Q)', true);
}
function finishFullTest(){
  var v=qsplit('Verbal'), q=qsplit('Quant');
  var ve=estFromRaw(v.c, v.t), qe=estFromRaw(q.c, q.t);
  var html='<div class="card"><h2>Full Test Complete</h2>'+
    '<div class="stats">'+
    '<div class="stat"><div class="n">'+v.txt+'</div><div class="l">Verbal est.</div></div>'+
    '<div class="stat"><div class="n">'+q.txt+'</div><div class="l">Quant est.</div></div>'+
    '<div class="stat"><div class="n">'+(ve+qe)+'</div><div class="l">Total (340)</div></div></div>'+
    '<p class="small">Raw: Verbal '+v.c+'/'+v.t+', Quant '+q.c+'/'+q.t+'. Scaled figures are a rough linear model; the real GRE is adaptive.</p>'+
    '<div class="row"><button class="btn primary" onclick="show(\'dash\')">Dashboard</button></div></div>';
  document.getElementById('run').innerHTML=html; enterRun('full');
  renderDash();
}
function qsplit(sec){ var ks=Object.keys(FULL.results).filter(k=>k.indexOf(sec)>=0); var c=0,t=0; ks.forEach(k=>{var p=FULL.results[k].split('/');c+=+p[0];t+=+p[1];}); return {c:c,t:t,txt:t?Math.round(c/t*100)+'%':'-'}; }
function estFromRaw(c,t){ if(!t) return 150; return Math.max(130,Math.min(170,Math.round(130+(c/t)*40))); }
function showFullStatus(){
  if(!FULL){ document.getElementById('full-status').innerHTML='<p class="muted">No full test in progress. Start one above.</p>'; return; }
  var html='<div class="card"><h2>Current Full Test</h2><div class="small">';
  ['Verbal','Quant'].forEach(s=>{ var ks=Object.keys(FULL.results).filter(k=>k.indexOf(s)>=0); html+=s+': '+(ks.length?ks.map(k=>FULL.results[k]).join(', '):'not started')+'<br>'; });
  html+='</div></div>'; document.getElementById('full-status').innerHTML=html;
}

/* ================= AWA ================= */
var awaTimer=null, awaDeadline=0, awaRunning=false, AWA_CUR=null;
function awaStart(kind, after){
  AWA_CUR={kind:kind, after:after, prompt: AWA_PROMPTS[kind][Math.floor(Math.random()*AWA_PROMPTS[kind].length)]};
  document.getElementById('awa-area').classList.remove('hidden');
  document.getElementById('awa-bank').innerHTML='';
  document.getElementById('awa-type').textContent=kind==='issue'?'Issue Task':'Argument Task';
  document.getElementById('awa-prompt').textContent=AWA_CUR.prompt;
  document.getElementById('awa-text').value='';
  document.getElementById('awa-info').textContent='';
  awaDeadline=Date.now()+30*60*1000; awaRunning=false;
  var t=document.getElementById('awa-timer'); t.textContent='30:00'; t.className='timer';
  document.getElementById('awa-rubric').classList.add('hidden');
}
function awaToggleTimer(){
  var t=document.getElementById('awa-timer');
  if(awaRunning){ if(awaTimer) clearInterval(awaTimer); awaTimer=null; awaRunning=false; return; }
  awaRunning=true; var tick=function(){ var left=Math.max(0,Math.round((awaDeadline-Date.now())/1000)); t.textContent=Math.floor(left/60)+':'+('0'+(left%60)).slice(-2); t.className='timer'+(left<=300?' crit':(left<=600?' warn':'')); if(left<=0){clearInterval(awaTimer);awaTimer=null;awaRunning=false;} }; tick(); awaTimer=setInterval(tick,1000);
}
function awaWordCount(){ var txt=document.getElementById('awa-text').value.trim(); var n=txt?txt.split(/\s+/).length:0; document.getElementById('awa-info').textContent=n+' words'+(n<400?' (aim for 400–600)':''); }
function showRubric(){
  var el=document.getElementById('awa-rubric'); el.classList.toggle('hidden');
  el.innerHTML='<h3>Self-Grade Rubric (0–6)</h3>'+
    '<p class="small"><b>6</b> Insightful, well-organized, compelling; few errors.<br><b>5</b> Strong, generally thoughtful; minor flaws.<br><b>4</b> Competent; adequate development, some lapses.<br><b>3</b> Limited; weak development or organization.<br><b>2</b> Seriously flawed; poor control.<br><b>1</b> Fundamentally deficient.<br><b>0</b> Off-topic / blank.</p>'+
    '<p class="small">Score yourself, then note it mentally. Tip: Issue = take a clear position + reasons + examples. Argument = identify logical flaws (assumptions, alternatives, data gaps), don\'t agree/disagree.</p>';
}
function awaFinish(){ if(awaTimer){clearInterval(awaTimer);awaTimer=null;} awaRunning=false; var n=document.getElementById('awa-text').value.trim().split(/\s+/).filter(Boolean).length; toast('Essay saved locally ('+n+' words). Self-grade via rubric.'); if(AWA_CUR&&AWA_CUR.after) AWA_CUR.after(); }
function renderAwaBank(){
  document.getElementById('awa-area').classList.add('hidden');
  var html='<div class="card"><h2>Prompt Bank</h2>';
  ['issue','argument'].forEach(k=>{ html+='<h3>'+ (k==='issue'?'Issue':'Argument') +'</h3>'; AWA_PROMPTS[k].forEach(p=>{ html+='<div class="awa-prompt">'+esc(p)+'</div>'; }); });
  html+='</div>'; document.getElementById('awa-bank').innerHTML=html;
}

/* ================= STUDY PLAN ================= */
function genPlan(){
  var date=document.getElementById('plan-date').value;
  var hrs=parseInt(document.getElementById('plan-hours').value)||10;
  var level=document.getElementById('plan-level').value;
  if(!date){ toast('Pick a test date', true); return; }
  var days=Math.ceil((new Date(date)-new Date())/86400000);
  if(days<1){ toast('Test date is in the past', true); return; }
  // weight: weak topics
  var weak=GRE_QUESTIONS.map(q=>{ var s=state[q.id]; var a=s?(s.correct||0)/((s.correct||0)+(s.wrong||0)||1):0; return {tp:q.topic||'General', a:a, seen:s?(s.seen||0):0}; })
    .reduce((m,x)=>{ if(!m[x.tp]) m[x.tp]={a:1,seen:0,n:0}; m[x.tp].a=Math.min(m[x.tp].a,x.a); m[x.tp].seen+=x.seen; m[x.tp].n++; return m; },{});
  var weakTopics=Object.keys(weak).sort((a,b)=>weak[a].a-weak[b].a).slice(0,6);
  var weeks=Math.ceil(days/7);
  var html='<div class="card"><h2>Your '+weeks+'-Week Plan ('+days+' days, '+hrs+' h/week)</h2>';
  html+='<p class="small">Level: '+level+' · Focus topics: '+(weakTopics.length?weakTopics.map(esc).join(', '):'take a diagnostic first')+'</p>';
  var phase=level==='beginner'?'Foundations':(level==='advanced'?'Sharpening':'Building');
  for(var w=1; w<=weeks; w++){
    var focus = w<=2 ? 'Diagnose + '+weakTopics.slice(0,2).join(' / ') : (w>=weeks-1 ? 'Full tests + weak review' : 'Topic drills + vocab SRS');
    html+='<div class="secrow"><span class="name"><b>Week '+w+'</b></span><span class="pct">'+hrs+'h</span></div>'+
      '<div class="small" style="margin:-4px 0 8px">'+focus+' · '+'Custom-quiz the weak topics, 30 min vocab/day, 1 timed section.</div>';
  }
  html+='<div class="row" style="margin-top:10px"><button class="btn primary" onclick="show(\'custom\')">Open Custom Quiz</button><button class="btn" onclick="show(\'vocab\')">Vocab Drill</button><button class="btn" onclick="show(\'mock\')">Timed Section</button></div></div>';
  document.getElementById('plan-out').innerHTML=html;
  // default date = today+56 if empty handled above
}

/* ================= IMPORT / EXPORT ================= */
var GRE_TYPES=['mc','tc','se','qc','multi','numeric','rc'];
function validateQuestion(q){
  if(!q || typeof q!=='object' || Array.isArray(q)) return ['not an object'];
  if(!q.type || !GRE_TYPES.includes(q.type)) return ['type must be one of '+GRE_TYPES.join('/')];
  if(!q.stem || !String(q.stem).trim()) return ['missing stem'];
  if(q.type==='rc'){ if(!q.passage || !String(q.passage).trim()) return ['rc needs passage']; }
  if(q.type==='qc'){ if(!'ABCD'.includes(q.answer)) return ['qc answer must be A-D']; return []; }
  if(q.type==='numeric'){ if(q.answer==null || q.answer==='') return ['numeric answer missing']; return []; }
  if(!q.choices || typeof q.choices!=='object' || Object.keys(q.choices).length<2) return ['needs >=2 choices'];
  var ans=Array.isArray(q.answer)?q.answer:[q.answer];
  if((q.type==='se'||q.type==='multi') && !Array.isArray(q.answer)) return [q.type+' needs array answer'];
  var bad=ans.filter(a=>!(a in q.choices));
  if(bad.length) return ['answer '+bad.join(',')+' not in choices'];
  // duplicate option labels?
  var vals=Object.values(q.choices);
  if(vals.length!==new Set(vals).size) return ['duplicate choice text'];
  return [];
}
function looksLikeVocab(arr){
  return Array.isArray(arr) && arr.length>0 && arr.every(o=>o && (o.word||o.term) && (o.def||o.definition) && !o.stem);
}
function parsePlainText(txt){
  // Best-effort parser for copy-paste MCQ blocks, e.g.:
  //   Q: What is 2+2?
  //   A) 3   B) 4   C) 5
  //   Answer: B
  var out=[], i=0, lines=txt.split(/\r?\n/);
  function letterOf(s){ var m=s.match(/^\s*([A-E])[\.\)\:]/); return m?m[1]:null; }
  while(i<lines.length){
    var ln=lines[i];
    if(/^\s*(q|question|\d+[\.\)]\s|stem)/i.test(ln) || (ln.trim() && letterOf(ln)===null && i+1<lines.length && letterOf(lines[i+1]))){
      // start of a question: gather stem until first option line
      var stem='', opts={}, ans=[];
      stem=ln.replace(/^\s*(q|question|\d+[\.\)]\s|\:)\s*/i,'').trim();
      i++;
      while(i<lines.length){
        var l=lines[i];
        if(/answer\s*[:=]/i.test(l)){ var am=l.match(/answer\s*[:=]\s*(.+)/i); if(am){ am[1].split(/[\s,]+/).forEach(x=>{var L=x.trim().toUpperCase(); if(L&&'ABCDE'.includes(L)) ans.push(L);}); } i++; break; }
        var ll=letterOf(l);
        if(ll){ l.replace(/([A-E])[\.\)\:]\s*([^\sA-E][^A-E]*?)(?=\s+[A-E][\.\)\:]|$)/g,function(_,L,text){ opts[L]=text.trim(); }); if(!opts[ll]){ var t=l.replace(/^\s*[A-E][\.\)\:]\s*/,'').trim(); if(t) opts[ll]=t; } i++; }
        else if(!l.trim()){ i++; break; } // blank line ends block
        else { stem+=' '+l.trim(); i++; }
      }
      if(stem && Object.keys(opts).length>=2){
        var type = ans.length>1 ? 'multi' : 'mc';
        out.push({type:type, section: ans.length>1?'Verbal':'Verbal', topic:'Imported', difficulty:'medium', stem:stem, choices:opts, answer: type==='multi'?ans:ans[0], explanation:''});
      }
      continue;
    }
    i++;
  }
  return out;
}
function parseInput(txt){
  txt=txt.trim();
  // JSON array?
  if(txt[0]==='['){
    try{ var a=JSON.parse(txt); if(Array.isArray(a)) return {parsed:a, kind:'json'}; }catch(e){}
    return {parsed:[], kind:'json', parseError:e?e.message:''};
  }
  // .js assignment: var X = [...]; or X = [...]
  var m=txt.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
  if(m){ try{ var a=JSON.parse(m[1]); if(Array.isArray(a)) return {parsed:a, kind:'js'}; }catch(e){ return {parsed:[], kind:'js', parseError:e.message}; } }
  // plain text MCQ
  var pt=parsePlainText(txt);
  if(pt.length) return {parsed:pt, kind:'text'};
  return {parsed:[], kind:'unknown', parseError:'Unrecognized format (need JSON array, .js bank, or text MCQ blocks).'};
}
function doImport(previewOnly){
  var txt=document.getElementById('imp-text').value.trim();
  var msg=document.getElementById('imp-msg'), rep=document.getElementById('imp-report');
  if(!txt){ msg.textContent='Paste JSON, a .js bank, or text questions first.'; if(rep) rep.innerHTML=''; return; }
  var res=parseInput(txt);
  if(!res.parsed.length){ msg.textContent='Parse error: '+(res.parseError||'nothing parsed'); if(rep) rep.innerHTML=''; return; }
  // vocab?
  if(looksLikeVocab(res.parsed)){
    var added=0, skipped=0; var known=new Set(GRE_VOCAB.map(w=>w.word.toLowerCase()));
    res.parsed.forEach(o=>{ var w=(o.word||o.term).trim(); if(known.has(w.toLowerCase())){skipped++;return;} GRE_VOCAB.push({word:w, pos:o.pos||'n.', def:o.def||o.definition, ex:o.ex||''}); known.add(w.toLowerCase()); added++; });
    if(!previewOnly){ localStorage.setItem('gre_vocab', JSON.stringify(GRE_VOCAB)); }
    msg.textContent=(previewOnly?'Preview: ':'Imported ')+added+' vocab words'+(skipped?', skipped '+skipped+' duplicates.':'.')+' Bank vocab now '+GRE_VOCAB.length+'.';
    if(rep) rep.innerHTML=''; renderDash(); return;
  }
  // questions: validate + dedup
  var ok=[], rejected=[], seen=new Set(GRE_QUESTIONS.map(q=>q.id));
  res.parsed.forEach((q,idx)=>{
    var q2=Object.assign({},q);
    if(!q2.id) q2.id='imp-'+Date.now()+'-'+idx;
    if(q2.type==='qc'||q2.type==='numeric') q2.section='Quant';
    else if(!q2.section) q2.section='Verbal';
    if(!q2.topic) q2.topic='Imported';
    if(!q2.difficulty) q2.difficulty='medium';
    // numeric may legitimately have no choices
    var errs=validateQuestion(q2);
    if(errs.length){ rejected.push({id:q2.id, reason:errs.join('; ')}); return; }
    if(seen.has(q2.id)){ rejected.push({id:q2.id, reason:'duplicate id'}); return; }
    seen.add(q2.id); ok.push(q2);
  });
  if(previewOnly){
    msg.textContent='Preview: '+ok.length+' valid, '+rejected.length+' rejected (not added).';
  } else {
    GRE_IMPORTED=GRE_IMPORTED.concat(ok);
    localStorage.setItem('gre_imported_bank', JSON.stringify(GRE_IMPORTED));
    GRE_QUESTIONS=GRE_QUESTIONS.concat(ok);
    msg.textContent='Imported '+ok.length+' questions. Bank now '+GRE_QUESTIONS.length+'.'+(rejected.length?' '+rejected.length+' rejected.':'');
    renderDash();
  }
  if(rep){
    rep.innerHTML = (rejected.length? '<div class="small" style="margin-top:8px;color:var(--bad)">Rejected ('+rejected.length+'):</div>'+
      rejected.slice(0,12).map(r=>'<div class="small">• '+r.id+': '+r.reason+'</div>').join('') : '<div class="small" style="margin-top:8px;color:var(--good)">All '+ok.length+' passed validation.</div>');
  }
}
function exportBank(){ var data=JSON.stringify({questions:GRE_QUESTIONS, vocab:GRE_VOCAB},null,2); var b=new Blob([data],{type:'application/json'}); var u=URL.createObjectURL(b); var a=document.createElement('a'); a.href=u; a.download='gre_export.json'; a.click(); URL.revokeObjectURL(u); toast('Exported'); }
function loadFile(ev){ var f=ev.target.files[0]; if(!f) return; var r=new FileReader(); r.onload=function(){ var txt=String(r.result).trim(); var m=txt.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/); if(m) txt=m[1]; document.getElementById('imp-text').value=txt; doImport(true); }; r.readAsText(f); ev.target.value=''; }

/* ================= INIT ================= */
window.addEventListener('DOMContentLoaded', function(){
  renderDash(); renderPracQuick(); renderCustom(); renderVocabList();
  // default plan date 60 days out
  var d=new Date(Date.now()+60*86400000); document.getElementById('plan-date').value=d.toISOString().slice(0,10);
});
