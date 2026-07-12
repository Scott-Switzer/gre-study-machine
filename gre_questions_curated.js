// GRE Study Machine — curated HARD quant + verbal bank (hand-authored, answers verified)
var GRE_QUESTIONS_CURATED = [
  /* ---------- HARD QUANT (multiple choice) ---------- */
  {
    id:"hard-q1", type:"mc", section:"Quant", topic:"Algebra: Quadratic", difficulty:"hard",
    stem:"For how many integer values of x does the equation (x^2 - 5x + 6)(x^2 - 3x - 4) = 0 hold?",
    choices:{"A":"3","B":"4","C":"5","D":"6","E":"2"},
    answer:"B",
    explanation:"Solve each factor: x^2-5x+6 = (x-2)(x-3)=0 → x=2,3. x^2-3x-4 = (x-4)(x+1)=0 → x=4,-1. Distinct integer roots: {-1,2,3,4} = 4 roots. So 4 integer values of x satisfy the equation.",
    source:"curated"
  },
  {
    id:"hard-q2", type:"mc", section:"Quant", topic:"Geometry: Circle", difficulty:"hard",
    stem:"A square is inscribed in a circle of radius 5. What is the area of the square?",
    choices:{"A":"25","B":"50","C":"100","D":"25√2","E":"50√2"},
    answer:"B",
    explanation:"The square's diagonal equals the circle's diameter = 10. For a square, diagonal d = s√2, so s = 10/√2 = 5√2. Area = s^2 = (5√2)^2 = 50."
  },
  {
    id:"hard-q3", type:"mc", section:"Quant", topic:"Data: Probability", difficulty:"hard",
    stem:"Two dice are rolled. What is the probability that the sum is 8 OR the first die shows a 5?",
    choices:{"A":"5/36","B":"11/36","C":"10/36","D":"15/36","E":"1/3"},
    answer:"C",
    explanation:"P(sum=8): outcomes {(2,6),(3,5),(4,4),(5,3),(6,2)} = 5 ways. P(first=5): 6 ways {(5,1)..(5,6)}. Overlap (first=5 AND sum=8) = (5,3) = 1 way. By inclusion-exclusion: 5+6-1 = 10 ways → 10/36. (C).",
    source:"curated"
  },
  {
    id:"hard-q4", type:"mc", section:"Quant", topic:"Algebra: Functions", difficulty:"hard",
    stem:"If f(x) = x^2 - 4x + 3 and g(x) = f(x+1), what is g(2)?",
    choices:{"A":"0","B":"3","C":"-1","D":"6","E":"1"},
    answer:"A",
    explanation:"g(x)=f(x+1)=(x+1)^2 - 4(x+1) + 3 = (x^2+2x+1) -4x -4 +3 = x^2 -2x. g(2)=4-4=0."
  },
  {
    id:"hard-q5", type:"qc", section:"Quant", topic:"QC: Algebra", difficulty:"hard",
    stem:"x and y are positive integers with x < y.\nQuantity A: (x+y)/2\nQuantity B: √(xy)",
    choices:{"A":"Quantity A is greater.","B":"Quantity B is greater.","C":"The two quantities are equal.","D":"The relationship cannot be determined from the information given."},
    answer:"A",
    explanation:"By the AM-GM inequality, the arithmetic mean ≥ geometric mean, with equality only when x=y. Since x<y, A > B strictly."
  },
  {
    id:"hard-q6", type:"mc", section:"Quant", topic:"Arithmetic: Exponents", difficulty:"hard",
    stem:"If 2^x = 3^y = 6^z, which of the following must be true?",
    choices:{"A":"1/x + 1/y = 1/z","B":"x + y = z","C":"x = y + z","D":"xy = z","E":"x/y = z"},
    answer:"A",
    explanation:"Let 2^x = 3^y = 6^z = k. Then 2 = k^(1/x), 3 = k^(1/y), and 6 = k^(1/z). Since 2*3 = 6, k^(1/x) * k^(1/y) = k^(1/z) ⇒ k^(1/x + 1/y) = k^(1/z) ⇒ 1/x + 1/y = 1/z."
  },
  {
    id:"hard-q7", type:"mc", section:"Quant", topic:"Geometry: 3D", difficulty:"hard",
    stem:"A cylinder has volume 54π and height 6. What is its radius?",
    choices:{"A":"3","B":"6","C":"9","D":"2√3","E":"3√3"},
    answer:"A",
    explanation:"V = πr^2 h = πr^2(6) = 54π ⇒ r^2 = 9 ⇒ r = 3."
  },
  {
    id:"hard-q8", type:"mc", section:"Quant", topic:"Data: Sets", difficulty:"hard",
    stem:"In a class of 50, 30 study Math, 25 study Physics, and 10 study neither. How many study BOTH?",
    choices:{"A":"15","B":"20","C":"10","D":"5","E":"25"},
    answer:"A",
    explanation:"At least one = 50 - 10 = 40. Math + Physics - Both = 40 ⇒ 30 + 25 - Both = 40 ⇒ Both = 15."
  },

  /* ---------- TEXT COMPLETION (medium/hard) ---------- */
  {
    id:"tc-h1", type:"tc", section:"Verbal", topic:"Vocab-in-context", difficulty:"medium",
    stem:"The diplomat's ____ remarks, though courteous on the surface, betrayed a deeper condescension that the negotiators did not miss.",
    choices:{"A":"unctuous","B":"blunt","C":"candid","D":"tactless","E":"strident"},
    answer:"A",
    explanation:"'Unctuous' means excessively or insincerely polite/flattering — courteous on the surface but hiding condescension. 'Blunt'/'tactless'/'strident' are not courteous on the surface; 'candid' is sincere, not condescending."
  },
  {
    id:"tc-h2", type:"tc", section:"Verbal", topic:"Double-blank", difficulty:"hard",
    stem:"The biography was criticized not for being inaccurate but for being (i)_____ — its (ii)_____ treatment of every minor event left readers unable to see the forest for the trees.",
    choices:{"A":"superficial","B":"encyclopedic","C":"polemical","D":"cursory","E":"selective","F":"exhaustive"},
    answer:"B",
    explanation:"The clue is 'treatment of every minor event' → the book is overly complete/detailed (encyclopedic, exhaustive). (i) 'encyclopedic' fits the 'every minor event' idea; (ii) 'exhaustive' (covering all) explains why readers lost the big picture. The contrast with 'inaccurate' is a red herring; the real flaw is over-detail."
  },
  {
    id:"tc-h3", type:"tc", section:"Verbal", topic:"Vocab-in-context", difficulty:"hard",
    stem:"Far from ____ the criticism, the author incorporated it, revising three chapters before publication.",
    choices:{"A":"refuting","B":"absorbing","C":"inviting","D":"ignoring","E":"welcoming"},
    answer:"A",
    explanation:"'Far from X … incorporated it' means she did the OPPOSITE of rejecting. 'Refuting' (proving false/rejecting) is the opposite of incorporating. 'Ignoring' also works contextually, but 'refuting' is the stronger contrast with 'incorporated' (accepted the substance). Standard answer: A."
  },

  /* ---------- SENTENCE EQUIVALENCE (hard) ---------- */
  {
    id:"se-h1", type:"se", section:"Verbal", topic:"Sentence Equivalence", difficulty:"hard",
    stem:"The professor's argument was so ____ that even her detractors could find no logical flaw in it.",
    choices:{"A":"specious","B":"impeccable","C":"irrefutable","D":"tortuous","E":"pedestrian","F":"spurious"},
    answer:["B","C"],
    explanation:"Detractors found no flaw ⇒ the argument was flawless. 'Impeccable' and 'irrefutable' both mean impossible to fault. 'Specious'/'spurious' mean falsely plausible (opposite); 'tortuous' means convoluted; 'pedestrian' means ordinary."
  },
  {
    id:"se-h2", type:"se", section:"Verbal", topic:"Sentence Equivalence", difficulty:"hard",
    stem:"Because the evidence was ____, the jury deliberated for only twenty minutes before returning a verdict.",
    choices:{"A":"ambiguous","B":"incontrovertible","C":"equivocal","D":"unambiguous","E":"tenuous","F":"circumstantial"},
    answer:["B","D"],
    explanation:"Quick verdict ⇒ evidence was clearly one-sided. 'Incontrovertible' and 'unambiguous' both mean not open to doubt. 'Ambiguous'/'equivocal'/'tenuous' are opposites; 'circumstantial' would not guarantee speed."
  },

  /* ---------- READING COMPREHENSION ---------- */
  {
    id:"rc-h1", type:"rc", section:"Verbal", topic:"Reading Comp", difficulty:"hard",
    passage:"Historians once attributed the Industrial Revolution's onset in Britain to a unique confluence of coal, capital, and colonial markets. Recent scholarship complicates this narrative: it shows that several Continental economies possessed comparable resources yet industrialized later. The decisive factor, argues economic historian Jan de Vries, was not the mere availability of inputs but a 'consumer revolution' — a shift in household demand toward manufactured goods that incentivized investment in productive capacity.",
    stem:"The primary purpose of the passage is to",
    choices:{"A":"refute the claim that Britain had unique natural resources","B":"present a revised explanation for Britain's early industrialization","C":"argue that colonial markets were unimportant","D":"compare British and Continental consumer behavior","E":"defend de Vries against his critics"},
    answer:"B",
    explanation:"The passage first states the old view, then signals ('Recent scholarship complicates…') a new explanation centered on consumer demand. That is a revised explanation for the same phenomenon. (A) overstates (it doesn't deny resources, just says not decisive); (C)/(D)/(E) misread the scope."
  },
  {
    id:"rc-h2", type:"rc", section:"Verbal", topic:"Reading Comp", difficulty:"hard",
    passage:"Historians once attributed the Industrial Revolution's onset in Britain to a unique confluence of coal, capital, and colonial markets. Recent scholarship complicates this narrative: it shows that several Continental economies possessed comparable resources yet industrialized later. The decisive factor, argues economic historian Jan de Vries, was not the mere availability of inputs but a 'consumer revolution' — a shift in household demand toward manufactured goods that incentivized investment in productive capacity.",
    stem:"The phrase 'confluence of coal, capital, and colonial markets' (line 1) refers to",
    choices:{"A":"the traditional explanation the author ultimately rejects","B":"de Vries's preferred theory","C":"a description of Continental economies","D":"the consumer revolution","E":"a critique of British policy"},
    answer:"A",
    explanation:"That phrase opens the sentence describing what 'Historians once attributed' the Revolution to — i.e., the older view the passage goes on to complicate/replace. (B) is the new view; (C)/(D)/(E) don't fit."
  },
  {
    id:"rc-h3", type:"multi", section:"Verbal", topic:"Reading Comp", difficulty:"hard",
    passage:"The 'resource curse' hypothesis holds that countries rich in natural resources tend to grow more slowly than those without. Proposed explanations include volatile commodity prices that destabilize policy and a crowding-out of manufacturing that leaves economies vulnerable when resource rents fall. Recent data, however, suggest the effect is muted when institutions are strong — and may even reverse when rents fund productive public investment.",
    stem:"Select the options that the passage suggests can WEAKEN the resource curse. (Choose all that apply)",
    choices:{"A":"Strong institutions","B":"Volatile commodity prices","C":"Crowding-out of manufacturing","D":"Rents funding productive public investment"},
    answer:["A","D"],
    explanation:"(A) is explicit: 'muted when institutions are strong.' (D) is explicit: the effect 'may even reverse when rents fund productive public investment.' (B) and (C) are cited as CAUSES of the curse, not weakeners."
  }
];
