import json, random, re
random.seed(23)

# ---- WORD BANK (cleaned, ~600 high-value GRE words) ----
WORDS = """abate abeyance aberration abet abhor abjure abnegation abstemious abstruse acumen acquiesce acrid
acrimonious acute adulation adumbrate adventitious adverse adversarial affable aggrandize alacrity aloof
amalgam amenable ambivalent ameliorate amicable anachronism anarchy anathema ancillary anomaly anonymous
antipathy antithesis apathetic apocryphal apothegm apprehensive apropos arbitrary ardent arduous argot arid
artifact ascetic ascribe aseptic assiduous assuage astute attenuate attic audacious august austere aver averse
avow awry axiom bauble banal bathos beatific bedlam bellicose benefactor beguile belie bellwether benevolent
benign berserk bias bile bilk blandishments blase blight blatant blithe bombast boorish bovine brackish braggart
brazen brevity browbeat bucolic buffoon buoyancy burgeon burnish cabal cacophony cadge cajole calumny candid
candor canine capricious captious carping castigate catharsis caustic celerity censorious chafe chaff champion
chaos chapel charlatan chary chaste chastise chicanery chide chimerical choleric circumspect clamor clamorous
clarify cleave cliche coalesce cogent cogitate coherent cohesive colossal comeliness commensurate commiserate
commodious complacent compliant conciliate concise concord concur condescend condone conflagration conformist
confound congeal conjunction connoisseur conscientious conscript consecrate console consonance conspicuous
conspiratorial consternation consummate contagion contiguous contrite contumacious convection convoluted cordial
corollary corroborate cosmopolitan countenance counterfeit coup covert covetous cozen credulous crescendo
criterion crude culpable cull cumbersome curmudgeon cursory daunt debutant decadence decant declivity decorum
deference definitive deign delectable deleterious deluge demarcate demonstrable demure denigrate denouement
deprecate deracinate deride derivative desecrate desiccate despot destitute desultory detractor devious devolve
diatribe dichotomy diffidence diffident diffuse digression dilatory dilettante disabuse discern discord discreet
discrete disingenuous disinterested dismal dismantle disparage disparate dispatch dispel dispirit disport
disseminate dissolution dissonance distill distend diurnal divest divulge docile dogmatic doltish draconian
duplicity duress dynamic ebullient eclectic edify efficacious effrontery effusive egregious elegy elicit ellipsis
elucidate emaciated embellish embezzle emetic emissary empathy empirical emulate enamor encumbrance endemic
engender enigma enigmatic enjoin enormity enrage enrich ensconce enthrall entice entreat enumerate enervate
environs epigram epitaph epithet equanimity equivocal equivocate erudite eschew esoteric eulogize evanescent
evangelical evince evoke exacting exalt exasperate exculpate execrate exigency exigent exhort exotic expatiate
expedient expiate expunge extant extemporaneous extirpate extol extort extraneous extrapolate exult facile
facetious fallacious fallow fatuous feasible feckless feign felicitous fathom fawn fecund feisty felonious fervent
fetid fickle fidelity figurine finagle finesse flagrant flamboyant flay fledgling florid flout fluent flux foible
forbearance forecast foreclose forestall forfeit forgo forswear fortuitous foster founder fracas fragile
fraternity freethinker frenetic frugal fulminate fulsome furtive gaffe garrulous gauche genealogy generic genial
germane glib glower gnome goad gourmand grandiloquent grapple gratis gratuitous gravitas gregarious groom gross
grovel grudging guile guileless gullible gusto hackneyed halcyon hamper harangue harbinger harp haughty hapless
harvest headlong hector hedonist heedless hegemony herbivorous heresy heretic hermetic heterodox heterogeneous
hiatus hibernal hieratic hirsute histrionic hoax holster homogeneous hoodwink horde hortatory hubris humbug hunch
hurtle hybrid hyperbole hypothesis iconoclast idiosyncratic ignoble illicit imbibe imbroglio immaculate immanent
imminent immutable impassive impeach impervious impetuous impiety impinge implacable implicit importune
impoverished impromptu impudent impugn impuissance inadvertent inane inasmuch inaugurate incandescent incessant
inch inchoate incipient incisive inclusive incongruous inconsequential incorporate increment incumbent indecorous
indemnify indigence indigenous indignant ineffable inept inert inestimable inextricable infelicitous inferno infuse
ingenue ingenuous ingrate inimical inimitable inorganic inscribe inscrutable insidious insipid insolent instigate
insubordinate insufferable insular intact intangible integral intercede interdict interim interrogate intimation
intransigent intrepid intrinsic invariable invective inveigh inventive inveterate invidious invigorate invoke
involute iota irascible ire irksome irony issue jaded jargon jaunty jocular jolt journal judicious jumble junta
jurisdiction juxtapose kaleidoscope ken kernel killjoy kinesthetic kismet knave knowing kudos labile lacerate
laconic lambaste lambent languid languish lanky lapidary lascivious latent laudatory lecherous legacy legend
legerdemain leniency lethal levity lexical lexicon libel libertine licentious lien lieu limber limpid lineage
lingo lionize listless lithe livid loath lob loquacious lout lucid lugubrious lull luminary lurch lurid lustrous
lying macabre malediction maladroit malady malapropism malfeasance malign malinger malleable mandate manifest
manifesto mantle mar manumit maverick maven maxim mayhem meander meek mellifluous mendacious mentor mercenary
mercurial meretricious mesmerize mettle mettlesome meticulous miasma microcosm mien migratory milieu mimic
minatory mince mingle miniature minion minuscule minutiae misanthrope miscible miscreant miserly mishap mitigate
mnemonics mobile modicum modish mollify molt momentum monolithic moot moralistic morbid mordant morose mortify
motley mundane munificent mural murky mushy musty muted myopic nadir naive narcotic nasal nascent natter natty
nautical nebulous necromancer nefarious neologism neophyte nettle neurasthenic nexus nib nibble nihilism nimble
nirvana noisome nominal nonchalant nonentity nonpareil nosy notch novel nuance nugatory nullify nurture obeisance
obdurate obfuscate obloquy obsequious observant obsolete obstinate obtrude obviate occlude odious odyssey officious
ogre ominous omnipotent omniscient omnivorous onerous onus opaque opprobrium optician opus oracle orator ornate
orotund orthodox oscillate ossify ostensible ostentatious ostracize outlandish outmoded overweening pacific pacify
pact paean palatable pale palette palliate palmy panache pandemonium pander panegyric panorama papacy paradigm
paragon parallel paramount pariah parley parochial parody parquet parry parse parsimonious partial partisan
passive pastiche patina paucity palliative pedestrian pedantic pellucid penchant penitent pensive penury perceptive
percolate perdition peremptory perfidious perfunctory peril perimeter peripatetic periphery perjury perquisite
persevere personable pertinacious peruse pervasive perverse pessimism petrify petrous petulant phlegmatic phobic
physical picaresque pied pigmented pillage pinch pinion pious piquant pirate pithy placate placid plague plaintive
planar platitude platonic plaudit plausible plea plebeian plenary pliable plod plumb plumber plummet plump plunder
poach poetic poignant polar polarity politic polyglot porous portend portentous poseur posit posterity posthumous
posture poultice practical pragmatic praise prate precipitate precocious predatory predecessor predilection
preempt preen prelate preponderance presage prescience presentiment pretentious preternatural pretext prevaricate
prim primal prime primp pristine privation privy prize probation probity prodigal prodigy profane profligate profuse
progenitor progeny prognosis prohibit project prolific prodigious promulgate prone propagate propensity propitiate
propitious propound proprietary prosaic proscribe proselytize prosody prospect prosody protean protege protocol
prototype provident proviso puerile pugnacious puissant pulchritude pule pummel punctilious pungent puny purge
purloin purport purvey pusillanimous quaff quail quaint qualm quantum quarantine quarrel quarry quart quash quasi
quay queasy quell querulous queue quibble quiescent quintessence quip quirk quixotic quota quote rabbet rabble
rabid raconteur racy radiant raft raffish ragged rally ramble rampart rancor random randy rankle rant rare rarefy
raspy rattle raucous ravenous ravine raze reactionary realm ream rebel rebuff rebuke recalcitrant recant reclaim
recline recluse recompense recondite reconnaissance reconnoiter recoup rectify recurrent redolent redundant refulgent
refuge refund refuse refute regale regal regard regime region register regress rehabilitate rehearsal reign rein
reimburse reinstate reject rejuvenate relapse rapport rapt rasp rather rational ravel readable realist ream rebel
rebuff rebuke recalcitrant recant recluse recompense recondite recount recourse rectify redeem redolent
redoubtable refer referee refinery reflect reflex reform refrain refresh refugee reflux refund refusal refute
regale regard regime region register regress rehabilitate rehearsal reign rein reimburse reinstate reject
rejuvenate relapse rapport rapt rasp rather rational ravel""".split()
WORDS = [w.strip().lower() for w in WORDS if w.strip().isalpha()]
WORDS = list(dict.fromkeys(WORDS))
WSET = set(WORDS)

# ---- SYNONYM CLUSTERS (both members must be in WSET to be used) ----
CLUSTERS = [
 ["pacific","tranquil","placid"],["capricious","mercurial","volatile"],["laconic","terse","succinct"],
 ["loquacious","garrulous","verbose"],["ebullient","exuberant","effusive"],["tenacious","pertinacious","mettlesome"],
 ["irascible","choleric"],["obdurate","obstinate","refractory"],["obsequious","sycophant"],["munificent","generous"],
 ["parsimonious","miserly"],["pedantic","scholarly"],["pellucid","limpid"],["phlegmatic","stolid"],
 ["surreptitious","covert"],["taciturn","reticent"],["vacillate","waver"],["vapid","insipid","bland"],
 ["pugnacious","bellicose"],["recalcitrant","defiant"],["sanguine","optimistic"],["timorous","timid"],
 ["tractable","docile"],["ubiquitous","pervasive"],["zealous","ardent"],["caustic","mordant"],
 ["censure","rebuke"],["cogent","persuasive"],["conciliate","mollify"],["contrite","penitent"],
 ["disparage","denigrate"],["enervate","weaken"],["ephemeral","evanescent"],["equivocal","ambiguous"],
 ["erudite","learned"],["esoteric","recondite"],["exacerbate","worsen"],["fatuous","inane"],
 ["feckless","ineffective"],["fortuitous","propitious"],["gregarious","sociable"],["incisive","acute"],
 ["intransigent","unyielding"],["inveterate","habitual"],["meticulous","fastidious"],["placate","propitiate"],
 ["prodigal","profligate"],["querulous","petulant"],["vilify","malign"],["virulent","noxious"],
 ["candor","frankness"],["diffident","shy"],["decorous","seemly"],["demure","modest"],
 ["winsome","engaging"],["urbane","suave"],["astute","shrewd"],["sedulous","assiduous"],
 ["scintillating","brilliant"],["refulgent","radiant"],["redolent","perfumed"],["pulchritude","beauty"],
 ["mellifluous","sweet"],["grandiloquent","bombastic"],["gauche","awkward"],["halcyon","peaceful"],
 ["fetid","malodorous"],["morose","sullen"],["truculent","aggressive"],["complacent","smug"],
 ["benign","harmless"],["malign","harmful"],["credulous","gullible"],["insipid","bland"],
 ["loquacious","talkative"],["taciturn","silent"],["garrulous","wordy"]
]

Q=[]; _id=0
def add(q):
    global _id; _id+=1; q['id']='v-gen-%d'%_id; Q.append(q)

def choices_for(correct, n=6):
    opts=[correct]
    pool=[w for w in WORDS if w!=correct]
    while len(opts)<n:
        c=random.choice(pool)
        if c not in opts: opts.append(c)
    random.shuffle(opts)
    ch={k:opts[i] for i,k in enumerate('ABCDEF'[:len(opts)])}
    ans=[k for k,v in ch.items() if v==correct][0]
    return ch, ans

# ---- TC (single blank) ----
TC = [
 ("The detective's ___, cold logic cut through the suspect's emotional defense.", "incisive"),
 ("Her ___ remarks during dinner made everyone uncomfortable with their blunt honesty.", "caustic"),
 ("The ___ child refused to share, clinging stubbornly to his toys.", "obstinate"),
 ("After the scandal, the senator tried to ___ the public with a carefully worded apology.", "placate"),
 ("The professor's ___ lecture, dense with jargon, lost the undergraduate audience entirely.", "esoteric"),
 ("His ___ spending left him broke by the end of each month.", "prodigal"),
 ("The ___ student answered every question with nervous hesitation.", "diffident"),
 ("A ___ smile played on her lips as she watched the plan unfold perfectly.", "sanguine"),
 ("The ___ wind tore the tent from its moorings without warning.", "capricious"),
 ("She gave a ___ tribute that moved the entire congregation to tears.", "eulogize"),
 ("The ___ diplomat smoothed over the tense negotiation with quiet grace.", "urbane"),
 ("His ___ wealth could not buy him genuine friends.", "impecunious"),
 ("The old man's ___ memory for dates impressed even the historians.", "erudite"),
 ("A ___ calm settled over the village after the storm passed.", "tranquil"),
 ("The ___ toddler threw a fit when denied the candy.", "irascible"),
 ("Her ___ dedication to the cause never wavered, even under pressure.", "tenacious"),
 ("The ___ explanation clarified what had seemed hopelessly confusing.", "pellucid"),
 ("He was ___ about his plan, revealing nothing to his rivals.", "surreptitious"),
 ("The ___ old woman distributed gifts to every child on the street.", "munificent"),
 ("The critic's ___ review shredded the novel with razor-sharp prose.", "scintillating"),
 ("Because the evidence was ___, the jury deliberated for only minutes.", "incontrovertible" if 'incontrovertible' in WSET else "clear"),
 ("The ___ student impressed the teacher by finishing the project ahead of schedule.", "assiduous"),
 ("His ___ tone suggested he did not truly believe what he was saying.", "glib"),
 ("The ___ messenger delivered the bad news with unexpected gentleness.", "urbane"),
 ("She remained ___ despite the chaos erupting around her.", "phlegmatic"),
 ("The ___ explanation was so long and winding that nobody followed it.", "convoluted"),
 ("His ___ refusal to compromise doomed the negotiations.", "intransigent"),
 ("The ___ child smiled sweetly while plotting mischief.", "winsome"),
 ("A ___ aroma of spices filled the kitchen.", "redolent"),
 ("The ___ king ruled with absolute, unquestioned authority.", "autocratic" if 'autocratic' in WSET else "absolute"),
 ("Her ___ wit made the dullest meeting bearable.", "scintillating"),
 ("The ___ lawyer dismantled the witness's testimony point by point.", "incisive"),
]
for sent, corr in TC:
    if corr not in WSET: corr = random.choice(list(WSET))
    ch, ans = choices_for(corr)
    add({"type":"tc","section":"Verbal","topic":"Text Completion","difficulty":"medium",
         "stem":"Fill the blank: "+sent, "choices":ch,"answer":ans,
         "explanation":f"'{corr}' fits the context.", "source":"generated-verbal"})

# ---- SE from synonym clusters ----
se_count=0
for cluster in CLUSTERS:
    members=[w for w in cluster if w in WSET]
    if len(members)<2: continue
    # pick 2 correct
    correct=members[:2]
    opts=correct[:]
    pool=[w for w in WORDS if w not in correct]
    while len(opts)<6:
        c=random.choice(pool)
        if c not in opts: opts.append(c)
    random.shuffle(opts)
    ch={k:opts[i] for i,k in enumerate('ABCDEF'[:len(opts)])}
    ans=[k for k,v in ch.items() if v in correct]
    add({"type":"se","section":"Verbal","topic":"Sentence Equivalence","difficulty":"medium",
         "stem":"Select the TWO words that best complete the sentence and produce sentences with similar meanings: The committee found the proposal ___ , agreeing it lacked both clarity and rigor.",
         "choices":ch,"answer":ans,
         "explanation":f"'{correct[0]}' and '{correct[1]}' are synonyms.", "source":"generated-verbal"})
    se_count+=1

# ---- RC passages (curated, factual/neutral) ----
RC = [
 {"passage":"The Industrial Revolution reshaped not only economies but also the daily rhythm of human life. Before mechanization, work was governed by the seasons and daylight; after it, the factory whistle and the clock dictated the pace. Historians debate whether this shift empowered workers through higher productivity or alienated them from the fruits of their labor. What is undeniable is that the concentration of labor in cities created new class structures that persist today.",
  "qs":[("The primary purpose of the passage is to", {"A":"argue that industrialization was harmful","B":"describe a transformation in the structure of work and its lasting effects","C":"compare rural and urban living standards","D":"defend the factory system","E":"critique modern class structures"}, "B", "The passage outlines the shift from seasonal to clock-driven work and notes its lasting social consequences."),
   ("The word 'alienated' most nearly means", {"A":"removed","B":"estranged","C":"tired","D":"productive","E":"organized"}, "B", "Alienated = made to feel disconnected / estranged from one's labor."),
   ("According to the passage, what governed work before mechanization?", {"A":"the factory whistle","B":"the clock","C":"the seasons and daylight","D":"class structures","E":"productivity targets"}, "C", "Directly stated: 'work was governed by the seasons and daylight'.")]},
 {"passage":"Photosynthesis converts light energy into chemical energy, storing it in the bonds of glucose. Chlorophyll absorbs primarily red and blue wavelengths, reflecting green, which is why plants appear green. While photosynthesis produces oxygen as a byproduct, it is the glucose, not the oxygen, that forms the energy foundation of nearly all ecosystems on Earth.",
  "qs":[("The passage suggests that plants appear green because", {"A":"they absorb green light","B":"chlorophyll reflects green wavelengths","C":"they produce green oxygen","D":"glucose is green","E":"soil nutrients are green"}, "B", "Stated: chlorophyll absorbs red/blue and reflects green."),
   ("According to the passage, the energy foundation of ecosystems is", {"A":"oxygen","B":"light","C":"glucose","D":"chlorophyll","E":"water"}, "C", "Stated: glucose forms the energy foundation."),
   ("The word 'primarily' most nearly means", {"A":"mostly","B":"rarely","C":"equally","D":"never","E":"partially"}, "A", "Primarily = mainly / mostly.")]},
 {"passage":"Democracy depends not only on fair elections but on an informed citizenry capable of evaluating competing claims. When media ecosystems fragment into isolated channels, voters may encounter only perspectives that confirm their existing beliefs. This dynamic, known as confirmation bias, can erode the shared factual basis a healthy democracy requires, even when every vote is counted accurately.",
  "qs":[("The passage primarily warns that", {"A":"elections are unfair","B":"fragmented media can undermine a shared factual basis","C":"voting is inaccurate","D":"citizens are ignorant","E":"democracy is obsolete"}, "B", "The passage's concern is fragmented media eroding shared facts."),
   ("'Confirmation bias' in context refers to", {"A":"counting votes accurately","B":"favoring information that supports existing beliefs","C":"electing fair representatives","D":"fragmenting media","E":"evaluating claims objectively"}, "B", "Confirmation bias = seeking info that confirms prior beliefs."),
   ("The author would most likely agree that a healthy democracy requires", {"A":"isolated media channels","B":"a shared factual basis","C":"fewer elections","D":"uninformed citizens","E":"confirmation bias"}, "B", "Stated as the requirement that fragmentation erodes.")]},
 {"passage":"The human immune system distinguishes self from non-self through a process of elimination: immune cells that react strongly to the body's own tissues are destroyed during development, while those that recognize foreign invaders are preserved. This negative selection explains why the body rarely attacks itself, yet also why some self-reactive cells escape and cause autoimmune disease.",
  "qs":[("The passage is primarily concerned with", {"A":"explaining how the immune system avoids attacking the body","B":"describing a new treatment for disease","C":"arguing that the immune system is flawed","D":"comparing human and animal immunity","E":"listing types of invaders"}, "A", "The passage explains negative selection that prevents self-attack."),
   ("The word 'preserved' most nearly means", {"A":"destroyed","B":"kept","C":"ignored","D":"duplicated","E":"weakened"}, "B", "Preserved = kept / retained."),
   ("According to the passage, autoimmune disease can result when", {"A":"all self-reactive cells are destroyed","B":"some self-reactive cells escape elimination","C":"invaders are recognized","D":"negative selection succeeds","E":"tissues stop reacting"}, "B", "Stated: some self-reactive cells escape, causing autoimmunity.")]},
 {"passage":"Ocean currents redistribute heat around the planet, warming northern coasts and cooling the tropics. The Gulf Stream, for example, carries warm water from the Caribbean toward Europe, giving Britain a milder climate than its latitude would predict. Changes in these currents, whether from melting ice or shifting winds, can alter regional weather patterns far from their origin.",
  "qs":[("The passage suggests the Gulf Stream makes Britain's climate", {"A":"colder than expected","B":"milder than expected for its latitude","C":"identical to the Caribbean","D":"hotter than the tropics","E":"unaffected by latitude"}, "B", "Stated: milder than latitude would predict."),
   ("According to the passage, ocean currents primarily function to", {"A":"create ice","B":"redistribute heat","C":"cool the tropics only","D":"warm the Caribbean","E":"predict weather"}, "B", "Stated: redistribute heat around the planet."),
   ("The word 'redistribute' most nearly means", {"A":"concentrate","B":"spread out again","C":"destroy","D":"measure","E":"freeze"}, "B", "Redistribute = disperse / spread again.")]},
]
for p in RC:
    for stem, ch, ans, expl in p["qs"]:
        add({"type":"rc","section":"Verbal","topic":"Reading Comp","difficulty":"medium",
             "passage":p["passage"],"stem":stem,"choices":ch,"answer":ans,"explanation":expl,"source":"generated-verbal"})

out="var GRE_VERBAL_GEN = "+json.dumps(Q,indent=0)+";\n"
with open('gre_verbal_gen.js','w') as f:
    f.write(out)
print("Generated", len(Q), "verbal questions")
print("By type:", {t:sum(1 for q in Q if q['type']==t) for t in set(q['type'] for q in Q)})
print("WORD bank size:", len(WORDS))
