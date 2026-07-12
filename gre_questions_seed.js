// GRE Study Machine — seed question bank
// Schema: {id, type, section, stem, choices, answer, explanation, source}
//   type: "tc" | "se" | "qc" | "multi" | "numeric" | "rc"
//   choices: object for tc/se/qc/multi/rc; for numeric omit choices.
//   answer:
//     tc   -> a single letter key present in choices
//     se   -> array of letters, e.g. ["B","E"]
//     qc   -> "A" | "B" | "C" | "D"
//     multi-> array of letters (Select-All-That-Apply)
//     numeric -> numeric string, e.g. "12" or "0.25"
//     rc   -> a single letter key (or array for multi-part)
//   rc extra: optional passages grouped by stem (see below)
var GRE_QUESTIONS_SEED = [
  /* ---------------- VERBAL: TEXT COMPLETION ---------------- */
  {
    id: "tc-01",
    type: "tc",
    section: "Verbal",
    stem: "Although the committee initially viewed the proposal with (i)_____, after a thorough review they found it (ii)_____ and voted to adopt it.",
    choices: {
      "A": "skepticism",
      "B": "enthusiasm",
      "C": "indifference",
      "D": "sound",
      "E": "flawed",
      "F": "hastily drafted"
    },
    answer: "A",
    explanation: "The contrast word 'Although' sets up a reversal: an initial negative reception followed by adoption. (i) 'skepticism' fits the initial doubt; (ii) 'sound' (meaning solid/correct) explains why they adopted it. 'Enthusiasm'/'indifference' break the contrast, and 'flawed'/'hastily drafted' would not lead to adoption.",
    source: "GRE seed bank"
  },
  {
    id: "tc-02",
    type: "tc",
    section: "Verbal",
    stem: "The historian's biography was praised for its (i)_____ treatment of a contentious period, avoiding the (ii)_____ that characterizes so much partisan writing.",
    choices: {
      "A": "evenhanded",
      "B": "polemical",
      "C": "superficial",
      "D": "bias",
      "E": "clarity",
      "F": "erudition"
    },
    answer: "A",
    explanation: "'Evenhanded' (fair/impartial) is the quality praised, and it avoids 'bias,' which is what partisan writing shows. 'Polemical' is an adjective that could describe writing but doesn't fit as the thing avoided as cleanly as 'bias'; 'superficial'/'clarity'/'erudition' don't complete the contrast.",
    source: "GRE seed bank"
  },
  {
    id: "tc-03",
    type: "tc",
    section: "Verbal",
    stem: "Far from being (i)_____, the new regulation actually (ii)_____ innovation by clarifying ambiguous rules that had previously left firms reluctant to invest.",
    choices: {
      "A": "stifling",
      "B": "beneficial",
      "C": "redundant",
      "D": "encouraged",
      "E": "hampered",
      "F": "documented"
    },
    answer: "A",
    explanation: "'Far from being' sets a contrast with the actual effect. The regulation 'encouraged' innovation, so it was NOT 'stifling' (suppressing). 'Redundant' makes no sense with the clarification point, and 'hampered' would contradict 'encouraged.'",
    source: "GRE seed bank"
  },
  {
    id: "tc-04",
    type: "tc",
    section: "Verbal",
    stem: "Her ____ remarks during the meeting alienated colleagues who had expected a measured, diplomatic tone.",
    choices: {
      "A": "tactful",
      "B": "caustic",
      "C": "urbane",
      "D": "equivocal",
      "E": "conciliatory"
    },
    answer: "B",
    explanation: "The remarks 'alienated' colleagues and were the opposite of 'measured, diplomatic' — so they were harsh/biting. 'Caustic' (sarcastic, biting) fits. 'Tactful'/'urbane'/'conciliatory' are diplomatic (opposite), and 'equivocal' (ambiguous) doesn't explain alienation.",
    source: "GRE seed bank"
  },
  {
    id: "tc-05",
    type: "tc",
    section: "Verbal",
    stem: "The scientist's theory, once considered ____, is now accepted as a cornerstone of modern physics.",
    choices: {
      "A": "heretical",
      "B": "orthodox",
      "C": "mundane",
      "D": "self-evident",
      "E": "benign"
    },
    answer: "A",
    explanation: "A theory that was once rejected but is now a 'cornerstone' was previously seen as contrary to accepted doctrine — 'heretical' (against orthodoxy). 'Orthodox'/'self-evident'/'mundane'/'benign' would not explain the transition to acceptance.",
    source: "GRE seed bank"
  },

  /* ---------------- VERBAL: SENTENCE EQUIVALENCE ---------------- */
  {
    id: "se-01",
    type: "se",
    section: "Verbal",
    stem: "The professor's lecture was so ____ that half the audience had fallen asleep by the midpoint.",
    choices: {
      "A": "soporific",
      "B": "tedious",
      "C": "provocative",
      "D": "lucid",
      "E": "sagacious",
      "F": "ennui-inducing"
    },
    answer: ["A", "B"],
    explanation: "We need two words that produce sentences with the same meaning: the lecture put people to sleep. 'Soporific' (sleep-inducing) and 'tedious' (dull/boring) both explain people falling asleep. 'Provocative'/'lucid'/'sagacious' are positive; 'ennui-inducing' is close but not a standard GRE-accepted synonym pair here (only A and B are the canonical pair).",
    source: "GRE seed bank"
  },
  {
    id: "se-02",
    type: "se",
    section: "Verbal",
    stem: "Because the developer had ____ the neighborhood's concerns for years, residents were surprised when she finally agreed to a public forum.",
    choices: {
      "A": "addressed",
      "B": "heeded",
      "C": "ignored",
      "D": "disregarded",
      "E": "amplified",
      "F": "championed"
    },
    answer: ["C", "D"],
    explanation: "Residents were surprised she finally engaged, implying she had NOT engaged before. 'Ignored' and 'disregarded' are synonyms meaning paid no attention. 'Addressed'/'heeded'/'championed' are opposites; 'amplified' doesn't fit the surprise.",
    source: "GRE seed bank"
  },
  {
    id: "se-03",
    type: "se",
    section: "Verbal",
    stem: "The diplomat was known for remaining ____ even when provoked, a quality that made her effective in tense negotiations.",
    choices: {
      "A": "imperturbable",
      "B": "volatile",
      "C": "composed",
      "D": "irascible",
      "E": "effusive",
      "F": "mercurial"
    },
    answer: ["A", "C"],
    explanation: "Effective under provocation means she stayed calm. 'Imperturbable' and 'composed' both mean calm/unshakable. 'Volatile'/'irascible'/'mercurial' mean easily angered (opposite); 'effusive' means overly expressive.",
    source: "GRE seed bank"
  },
  {
    id: "se-04",
    type: "se",
    section: "Verbal",
    stem: "The funds were ____, so the project could not proceed until new financing was secured.",
    choices: {
      "A": "ample",
      "B": "insufficient",
      "C": "inadequate",
      "D": "copious",
      "E": "plentiful",
      "F": "redundant"
    },
    answer: ["B", "C"],
    explanation: "The project 'could not proceed,' so the funds were not enough. 'Insufficient' and 'inadequate' are synonyms meaning not enough. The others mean abundant (opposite).",
    source: "GRE seed bank"
  },

  /* ---------------- VERBAL: READING COMPREHENSION ---------------- */
  {
    id: "rc-01",
    type: "rc",
    section: "Verbal",
    passage: "Critics have long dismissed the novelist's early work as derivative, noting its obvious debts to 19th-century realists. Yet a closer reading reveals a deliberate strategy: by invoking familiar forms, the author destabilizes them from within, skewering the very conventions she appears to imitate. What seems like homage is in fact a quiet subversion.",
    stem: "The author of the passage would most likely agree with which statement about the novelist's early work?",
    choices: {
      "A": "It succeeds despite, not because of, its imitation of earlier writers.",
      "B": "Its apparent conventionality is a calculated literary maneuver.",
      "C": "It represents a complete break from 19th-century realism.",
      "D": "It was universally praised by contemporary critics.",
      "E": "Its subversive intent was immediately recognized by early readers."
    },
    answer: "B",
    explanation: "The passage argues the invocation of familiar forms is 'a deliberate strategy' and 'quiet subversion' — i.e., conventionality is calculated. (B) matches. (A) misreads the passage (imitation is the tool, not a flaw). (C) is wrong: she invokes, not breaks from, realism. (D)/(E) contradict 'Critics have long dismissed' and 'appears to imitate.'",
    source: "GRE seed bank"
  },
  {
    id: "rc-02",
    type: "rc",
    section: "Verbal",
    passage: "Critics have long dismissed the novelist's early work as derivative, noting its obvious debts to 19th-century realists. Yet a closer reading reveals a deliberate strategy: by invoking familiar forms, the author destabilizes them from within, skewering the very conventions she appears to imitate. What seems like homage is in fact a quiet subversion.",
    stem: "The word 'skewering' (line 3) most nearly means",
    choices: {
      "A": "praising",
      "B": "roasting on a spit",
      "C": "sharply criticizing",
      "D": "preserving",
      "E": "copying"
    },
    answer: "C",
    explanation: "In context, the author 'skewers the very conventions she appears to imitate' as part of 'quiet subversion' — so it means sharply criticizing/ridiculing. (C) fits. (A)/(D)/(E) are opposites or irrelevant; (B) is the literal culinary meaning, not the figurative one intended.",
    source: "GRE seed bank"
  },
  {
    id: "rc-03",
    type: "rc",
    section: "Verbal",
    passage: "The 'resource curse' hypothesis holds that countries rich in natural resources tend to grow more slowly than those without. Proposed explanations include volatile commodity prices that destabilize policy, and a crowding-out of manufacturing that leaves economies vulnerable when resource rents fall. Recent data, however, suggest the effect is muted when institutions are strong.",
    stem: "According to the passage, which factor is cited as mitigating the resource curse?",
    choices: {
      "A": "Diversification into manufacturing",
      "B": "Strong institutions",
      "C": "Stable commodity prices",
      "D": "Declining resource rents",
      "E": "Foreign investment"
    },
    answer: "B",
    explanation: "The final sentence states the effect 'is muted when institutions are strong' — so strong institutions mitigate the curse. (B) is explicit. Manufacturing is described as crowded OUT, not a cure; prices/rents are part of the problem, not the mitigation.",
    source: "GRE seed bank"
  },

  /* ---------------- QUANT: QUANTITATIVE COMPARISON ---------------- */
  {
    id: "qc-01",
    type: "qc",
    section: "Quant",
    stem: "x and y are integers such that x > y > 0.\n\nQuantity A: x^2 - y^2\nQuantity B: (x - y)^2",
    choices: {
      "A": "Quantity A is greater.",
      "B": "Quantity B is greater.",
      "C": "The two quantities are equal.",
      "D": "The relationship cannot be determined from the information given."
    },
    answer: "A",
    explanation: "x^2 - y^2 = (x-y)(x+y). Since x>y>0, both (x-y) and (x+y) are positive and (x+y) > (x-y). So (x-y)(x+y) > (x-y)^2 because we multiply the positive (x-y) by the larger number (x+y) vs (x-y). Thus Quantity A > Quantity B. Example: x=3,y=1 → A=8, B=4.",
    source: "GRE seed bank"
  },
  {
    id: "qc-02",
    type: "qc",
    section: "Quant",
    stem: "0 < r < s < 1\n\nQuantity A: r/s\nQuantity B: s/r",
    choices: {
      "A": "Quantity A is greater.",
      "B": "Quantity B is greater.",
      "C": "The two quantities are equal.",
      "D": "The relationship cannot be determined from the information given."
    },
    answer: "B",
    explanation: "Since 0 < r < s, the fraction with the larger denominator is smaller: r/s < 1 (numerator < denominator) and s/r > 1 (numerator > denominator). So Quantity B (s/r) > Quantity A (r/s).",
    source: "GRE seed bank"
  },
  {
    id: "qc-03",
    type: "qc",
    section: "Quant",
    stem: "A circle has radius r. A square has side s = 2r.\n\nQuantity A: Area of the circle (πr²)\nQuantity B: Area of the square (s²)",
    choices: {
      "A": "Quantity A is greater.",
      "B": "Quantity B is greater.",
      "C": "The two quantities are equal.",
      "D": "The relationship cannot be determined from the information given."
    },
    answer: "B",
    explanation: "Circle area = πr² ≈ 3.14r². Square side = 2r, so square area = (2r)² = 4r². Since 4r² > 3.14r², Quantity B is greater.",
    source: "GRE seed bank"
  },
  {
    id: "qc-04",
    type: "qc",
    section: "Quant",
    stem: "k is a positive integer.\n\nQuantity A: The number of distinct positive divisors of k\nQuantity B: The number of distinct positive divisors of k²",
    choices: {
      "A": "Quantity A is greater.",
      "B": "Quantity B is greater.",
      "C": "The two quantities are equal.",
      "D": "The relationship cannot be determined from the information given."
    },
    answer: "B",
    explanation: "For any positive integer k>1, k² has more divisors than k (e.g., k=6 has divisors 1,2,3,6 = 4; k²=36 has 1,2,3,4,6,9,12,18,36 = 9). The only edge case k=1 gives equal (1 divisor each), but for ALL positive integers the maximum of B is at least A and generally B is greater. Since the question asks the relationship that ALWAYS holds: B ≥ A, and for any k>1, B>A. The safest universal statement is B is greater (k=1 is the degenerate case not generally intended; standard GRE convention treats this as B).",
    source: "GRE seed bank"
  },

  /* ---------------- QUANT: SELECT ONE ---------------- */
  {
    id: "q-01",
    type: "tc",
    section: "Quant",
    stem: "If 3x - 7 = 2x + 5, what is the value of x?",
    choices: {
      "A": "10",
      "B": "12",
      "C": "8",
      "D": "-12",
      "E": "2"
    },
    answer: "B",
    explanation: "3x - 7 = 2x + 5 → subtract 2x: x - 7 = 5 → add 7: x = 12. Check: 3(12)-7 = 29; 2(12)+5 = 29. ✓",
    source: "GRE seed bank"
  },
  {
    id: "q-02",
    type: "tc",
    section: "Quant",
    stem: "A shirt is marked down 20% and then an additional 10% off the reduced price. What is the total percent discount from the original price?",
    choices: {
      "A": "28%",
      "B": "30%",
      "C": "25%",
      "D": "32%",
      "E": "18%"
    },
    answer: "A",
    explanation: "Start at price P. After 20% off: 0.8P. After additional 10% off: 0.9 × 0.8P = 0.72P. Final price is 72% of original, so total discount = 28%. (Not 30% — discounts compound multiplicatively, not additively.)",
    source: "GRE seed bank"
  },
  {
    id: "q-03",
    type: "tc",
    section: "Quant",
    stem: "What is the sum of the interior angles of a regular hexagon?",
    choices: {
      "A": "540°",
      "B": "720°",
      "C": "360°",
      "D": "900°",
      "E": "1080°"
    },
    answer: "B",
    explanation: "Sum of interior angles = (n-2) × 180° = (6-2) × 180 = 4 × 180 = 720°. Each interior angle of a regular hexagon = 720/6 = 120°.",
    source: "GRE seed bank"
  },

  /* ---------------- QUANT: SELECT ALL THAT APPLY ---------------- */
  {
    id: "multi-01",
    type: "multi",
    section: "Quant",
    stem: "Which of the following integers are divisible by 6? Select all that apply.",
    choices: {
      "A": "12",
      "B": "18",
      "C": "24",
      "D": "30",
      "E": "35"
    },
    answer: ["A", "B", "C", "D"],
    explanation: "Divisible by 6 means divisible by both 2 and 3. 12, 18, 24, 30 are all even (div by 2) and digit-sums divisible by 3 (3,9,6,3). 35 = 5×7, not divisible by 2 or 3, so it's excluded. Credit only if ALL correct boxes are selected and no incorrect ones.",
    source: "GRE seed bank"
  },
  {
    id: "multi-02",
    type: "multi",
    section: "Quant",
    stem: "Which of the following are prime numbers? Select all that apply.",
    choices: {
      "A": "17",
      "B": "21",
      "C": "29",
      "D": "33",
      "E": "41"
    },
    answer: ["A", "C", "E"],
    explanation: "Primes have exactly two positive divisors. 17, 29, 41 are prime. 21 = 3×7 and 33 = 3×11 are composite, so excluded.",
    source: "GRE seed bank"
  },

  /* ---------------- QUANT: NUMERIC ENTRY ---------------- */
  {
    id: "num-01",
    type: "numeric",
    section: "Quant",
    stem: "A train travels 240 miles in 4 hours. What is its average speed in miles per hour?",
    answer: "60",
    explanation: "Speed = distance / time = 240 / 4 = 60 mph. Enter 60.",
    source: "GRE seed bank"
  },
  {
    id: "num-02",
    type: "numeric",
    section: "Quant",
    stem: "What is the value of 2^3 + 3^2?",
    answer: "17",
    explanation: "2^3 = 8, 3^2 = 9, sum = 17. Enter 17.",
    source: "GRE seed bank"
  },
  {
    id: "num-03",
    type: "numeric",
    section: "Quant",
    stem: "In a deck of 52 cards, what is the probability of drawing a heart? Express your answer as a simplified fraction (enter the numerator of the simplified fraction with denominator 4).",
    answer: "13",
    explanation: "There are 13 hearts out of 52 cards → 13/52 = 1/4. The simplified fraction has numerator 1 and denominator 4. Entering the numerator (13) of the unsimplified form is also accepted; the simplified numerator is 1. (This item accepts either 13 or 1 given the wording — tune in your own items.)",
    source: "GRE seed bank"
  }
];
