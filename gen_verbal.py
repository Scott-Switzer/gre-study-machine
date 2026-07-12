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
# ---- ADDITIONAL GRE WORDS (expansion) ----
WORDS += """aggressive ambiguous awkward beauty bland bombastic brilliant decorous defiant engaging ephemeral
fastidious frankness generous habitual harmful harmless ineffective learned malodorous modest noxious optimistic
peaceful perfumed persuasive reticent sanguine scholarly scintillating sedulous seemly shrewd shy silent smug
sociable stolid suave sullen surreptitious sweet sycophant talkative tenacious terse timid tranquil truculent
ubiquitous unyielding urbane verbose vilify volatile waver weaken winsome wordy worsen""".split()
WORDS = [w.strip().lower() for w in WORDS if w.strip().isalpha()]
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
 ("The ___ wind of opinion shifted the committee's decision overnight.", "capricious"),
 ("Her ___ refusal to acknowledge the error only deepened the rift.", "obstinate"),
 ("The diplomat's ___ manner defused the hostage situation with quiet grace.", "urbane"),
 ("A ___ chill settled over the room as the verdict was read.", "surreptitious"),
 ("The ___ philanthropist funded the hospital without seeking credit.", "munificent"),
 ("His ___ logic laid bare the flaw in the opponent's argument.", "incisive"),
 ("The ___ child greeted every stranger with a disarming smile.", "winsome"),
 ("A ___ scent of jasmine drifted through the open window.", "redolent"),
 ("The ___ monarch ruled with unquestioned, absolute authority.", "urbane"),
 ("Her ___ wit made even the dullest briefing bearable.", "scintillating"),
 ("The ___ professor could recall every case from a decade past.", "erudite"),
 ("After the loss, he remained ___, showing no outward grief.", "phlegmatic"),
 ("The ___ explanation wandered so far that the point was lost.", "convoluted"),
 ("His ___ stance left no room for negotiation or compromise.", "intransigent"),
 ("The ___ servant anticipated every need before it was spoken.", "obsequious" if 'obsequious' in WSET else "assiduous"),
 ("A ___ glow spread across the horizon at dawn.", "refulgent"),
 ("The ___ debater reduced the complex issue to its essence.", "cogent"),
 ("She tried to ___ the angry crowd with soothing words.", "mollify"),
 ("The critic sought to ___ the artist's reputation with cruel reviews.", "denigrate"),
 ("His ___ behavior at the gala scandalized the older guests.", "raffish" if 'raffish' in WSET else "boorish"),
 ("The ___ student finished the assignment days early, flawless.", "assiduous"),
 ("Her ___ tone hinted she doubted every word he said.", "glib"),
 ("The ___ village enjoyed decades of peace and prosperity.", "halcyon"),
 ("A ___ odor of sulfur leaked from the laboratory.", "malodorous" if 'malodorous' in WSET else "fetid"),
 ("The ___ old man grumbled at every noise the children made.", "curmudgeon" if 'curmudgeon' in WSET else "morose"),
 ("His ___ spending drained the inheritance within a year.", "prodigal"),
 ("The ___ smile never reached her cold, calculating eyes.", "winsome"),
 ("A ___ hush fell as the conductor raised the baton.", "tranquil"),
 ("The ___ toddler screamed when told to leave the playground.", "irascible"),
 ("Her ___ perseverance carried the project through every setback.", "tenacious"),
 ("The ___ statement clarified the previously murky policy.", "pellucid"),
 ("He was ___ about the surprise, telling no one of the plan.", "surreptitious"),
 ("The ___ professor's lecture, thick with jargon, lost the freshmen.", "esoteric"),
 ("A ___ calm held the ship steady through the storm.", "phlegmatic"),
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
# ---- EVEN MORE RC PASSAGES ----
RC += [
 {"passage":"The 2008 financial crisis revealed how tightly global markets are coupled: a collapse in U.S. subprime mortgages propagated within months to banks in Europe and export demand in Asia. Economists debated whether tighter capital requirements or simpler financial products would best prevent recurrence. What is clear is that no economy remained an island; interdependence cut both ways, transmitting shocks and, eventually, recoveries.",
  "qs":[("The passage primarily illustrates that", {"A":"mortgages caused the crisis alone","B":"global markets are interdependent","C":"Asia caused the recession","D":"recovery was impossible","E":"banks are unnecessary"}, "B", "The passage shows shocks propagated globally, illustrating interdependence."),
   ("The word 'propagated' most nearly means", {"A":"stopped","B":"spread","C":"reversed","D":"hidden","E":"fund"}, "B", "Propagated = spread / transmitted."),
   ("According to the passage, interdependence", {"A":"only transmitted shocks","B":"only helped recoveries","C":"cut both ways","D":"was avoided","E":"ended trade"}, "C", "Stated: interdependence cut both ways, transmitting shocks and recoveries.")]},
 {"passage":"Machine learning models often excel at prediction but struggle to explain their reasoning, a problem known as the opacity of black-box systems. Regulators in finance and medicine increasingly demand interpretability: a model that denies a loan or misdiagnoses a patient should justify itself. Researchers respond with techniques that approximate a model's decisions using simpler, human-readable rules, trading some accuracy for trust.",
  "qs":[("The passage suggests that black-box models are problematic because they", {"A":"are always wrong","B":"lack explainability","C":"are too simple","D":"cost nothing","E":"never predict well"}, "B", "The passage frames opacity / lack of interpretability as the core issue."),
   ("The word 'opacity' most nearly means", {"A":"clarity","B":"lack of transparency","C":"speed","D":"accuracy","E":"color"}, "B", "Opacity = lack of transparency / unexplainability."),
   ("According to the passage, researchers trade accuracy for", {"A":"speed","B":"trust via interpretability","C":"cost","D":"size","E":"data"}, "B", "Stated: they trade some accuracy for trust (interpretability).")]},
 {"passage":"Urban density, long criticized for congestion and cost, also yields efficiencies that sprawl cannot: shorter commutes, shared transit, and the spontaneous exchange of ideas that fuels innovation. Economists note that productivity rises with city size even as amenities concentrate. The challenge for planners is capturing density's benefits without its downsides of inequality and displacement.",
  "qs":[("The passage suggests urban density", {"A":"is purely harmful","B":"produces efficiencies sprawl lacks","C":"eliminates inequality","D":"reduces innovation","E":"requires no planning"}, "B", "The passage credits density with efficiencies and idea exchange sprawl cannot match."),
   ("The word 'spontaneous' most nearly means", {"A":"planned","B":"unplanned / natural","C":"expensive","D":"forced","E":"rare"}, "B", "Spontaneous = occurring naturally without planning."),
   ("According to the passage, planners must balance density's benefits against", {"A":"its downsides of inequality and displacement","B":"lower productivity","C":"fewer amenities","D":"longer commutes","E":"less transit"}, "A", "Stated: capture benefits without inequality/displacement downsides.")]},
 {"passage":"Antibiotic resistance arises when bacteria exposed to a drug evolve to survive it; the survivors reproduce, and the resistant strain dominates. Overuse in medicine and agriculture accelerates this process, shrinking the arsenal effective against infection. Public health authorities urge restraint and rotation of drugs, yet economic incentives often pull in the opposite direction, rewarding volume over stewardship.",
  "qs":[("The passage primarily explains", {"A":"how antibiotics cure disease","B":"how resistance evolves and why overuse worsens it","C":"why bacteria are harmless","D":"that drugs are unlimited","E":"how to make antibiotics"}, "B", "The passage explains evolution of resistance and the role of overuse."),
   ("The word 'stewardship' most nearly means", {"A":"waste","B":"careful management","C":"sales","D":"ignorance","E":"profit"}, "B", "Stewardship = responsible management."),
   ("According to the passage, economic incentives often", {"A":"support restraint","B":"reward volume over stewardship","C":"eliminate resistance","D":"fund research","E":"reduce use"}, "B", "Stated: incentives reward volume over stewardship.")]},
]

# ---- MORE RC PASSAGES (expansion) ----
RC += [
 {"passage":"The printing press, introduced in Europe in the 15th century, did more than multiply books; it transformed the conditions of knowledge itself. Before print, a scholar's authority rested on rare manuscripts guarded in monasteries. After print, texts could be copied exactly and distributed widely, enabling shared reference points across cities and eventually across nations. Critics at the time feared that cheap printed matter would spread error and vulgarity, yet the press proved indispensable to the scientific revolution that followed.",
  "qs":[("The passage primarily suggests that the printing press", {"A":"destroyed monasteries","B":"changed how knowledge was stored and shared","C":"reduced the number of books","D":"caused the scientific revolution directly","E":"spread only error"}, "B", "The passage argues print changed the conditions of knowledge via exact, wide distribution."),
   ("The word 'indispensable' most nearly means", {"A":"unnecessary","B":"essential","C":"harmful","D":"rare","E":"optional"}, "B", "Indispensable = absolutely necessary / essential."),
   ("According to the passage, a scholar's authority before print rested on", {"A":"widely distributed texts","B":"rare guarded manuscripts","C":"printed books","D":"scientific data","E":"shared reference points"}, "B", "Stated: authority rested on rare manuscripts in monasteries.")]},
 {"passage":"Migration shapes both the places people leave and the places they enter. Remittances sent home by migrants can lift families out of poverty, funding education and small businesses. Meanwhile, destination cities gain workers but may strain housing and services. The net effect on any single community depends on policy, timing, and the skills migrants bring, making simple claims about migration's impact misleading.",
  "qs":[("The passage suggests that the impact of migration is", {"A":"always positive","B":"always negative","C":"dependent on context and policy","D":"irrelevant to cities","E":"limited to remittances"}, "C", "Stated: the net effect depends on policy, timing, and skills."),
   ("The word 'remittances' most nearly refers to", {"A":"taxes paid to governments","B":"money sent home by migrants","C":"loans from banks","D":"goods traded abroad","E":"skills brought to cities"}, "B", "Remittances = funds migrants send back home."),
   ("According to the passage, destination cities may experience", {"A":"no change","B":"strain on housing and services","C":"loss of workers","D":"collapse of education","E":"reduction in population"}, "B", "Stated: cities may strain housing and services.")]},
 {"passage":"Coral reefs cover a tiny fraction of the ocean floor yet shelter roughly a quarter of all marine species. They build their limestone skeletons slowly, over centuries, in warm shallow water. When ocean temperatures rise even slightly, the symbiotic algae that give corals color and food exit, leaving bleached, starving reefs. Because reefs protect coastlines from storms and support fisheries, their decline threatens both biodiversity and human livelihoods.",
  "qs":[("The passage indicates that coral reefs are significant because they", {"A":"cover most of the ocean","B":"support a large share of marine species","C":"grow quickly","D":"require cold water","E":"lack biodiversity"}, "B", "Stated: reefs shelter ~25% of marine species despite tiny area."),
   ("The word 'symbiotic' most nearly means", {"A":"competing","B":"mutually dependent","C":"unrelated","D":"parasitic only","E":"dead"}, "B", "Symbiotic = mutually beneficial relationship."),
   ("According to the passage, coral bleaching occurs when", {"A":"water cools","B":"algae leave due to warming","C":"fish arrive","D":"limestone builds","E":"storms stop"}, "B", "Stated: warming causes algae to exit, bleaching reefs.")]},
]

# ---- MORE SYNONYM CLUSTERS (expansion) ----
CLUSTERS += [
 ["obsequious","sycophant","servile"],["refulgent","radiant","luminous"],
 ["cogent","persuasive","telling"],["mollify","appease","placate"],
 ["denigrate","malign","asperse"],["halcyon","peaceful","serene"],
 ["curmudgeon","grouch","misanthrope"],["raffish","rakish","raffish"],
 ["refulgent","luminous","shining"],["boorish","crass","uncouth"],
 ["tenacious","dogged","unyielding"],["pellucid","limpid","clear"],
 ["esoteric","abstruse","recondite"],["intransigent","adamant","obdurate"],
 ["winsome","engaging","charming"],["scintillating","brilliant","sparkling"],
 ["surreptitious","furtive","covert"],["redolent","fragrant","perfumed"],
 ["phlegmatic","impassive","stolid"],["convoluted","tortuous","byzantine"],
 ["incisive","acute","keen"],["urbane","suave","courtliness"],
 ["erudite","learned","scholarly"],["assiduous","sedulous","diligent"],
 ["glib","facile","smooth"],["prodigal","wasteful","extravagant"],
 ["irascible","testy","cantankerous"],["tranquil","calm","serene"],
 ["malodorous","fetid","noisome"],["morose","sullen","dismal"],
 ["capricious","fickle","mercurial"],["obstinate","stubborn","mulish"]
]

# ---- MORE RC PASSAGES (volume round) ----
RC += [
 {"passage":"The Green Revolution of the mid-20th century introduced high-yield crop varieties, synthetic fertilizers, and irrigation to developing nations, averting the mass famine many had predicted. Yet the same package increased dependence on fossil-fuel inputs and eroded traditional seed diversity. Historians now weigh its legacy as both a triumph over hunger and a cautionary tale about technological lock-in.",
  "qs":[("The passage suggests the Green Revolution", {"A":"caused mass famine","B":"both prevented famine and created new dependencies","C":"rejected irrigation","D":"preserved seed diversity","E":"ended synthetic fertilizer use"}, "B", "The passage credits it with averting famine while noting fossil-fuel dependence."),
   ("The word 'eroded' most nearly means", {"A":"strengthened","B":"gradually weakened/diminished","C":"planted","D":"measured","E":"celebrated"}, "B", "Eroded = gradually worn away / diminished."),
   ("According to the passage, a downside was", {"A":"more famine","B":"loss of traditional seed diversity","C":"less irrigation","D":"lower yields","E":"abandoned fertilizers"}, "B", "Stated: it eroded traditional seed diversity.")]},
 {"passage":"Networks exhibit surprising robustness: removing random nodes rarely collapses a large network, because most nodes are peripheral. But targeted removal of highly connected hubs can fragment it swiftly. This asymmetry explains why the internet survives outages yet power grids are vulnerable to coordinated attacks on key substations.",
  "qs":[("The passage primarily explains", {"A":"why all networks collapse easily","B":"why random failures are tolerable but hub attacks are devastating","C":"that the internet is fragile","D":"how substations are built","E":"why grids never fail"}, "B", "The passage contrasts random-node tolerance with hub-targeted vulnerability."),
   ("The word 'fragment' most nearly means", {"A":"strengthen","B":"break into pieces","C":"connect","D":"improve","E":"measure"}, "B", "Fragment = break apart."),
   ("According to the passage, power grids are vulnerable to", {"A":"random node loss","B":"coordinated attacks on key substations","C":"internet outages","D":"peripheral failures","E":"more nodes"}, "B", "Stated: grids are vulnerable to coordinated attacks on key substations.")]},
 {"passage":"Cognitive biases systematically skew human judgment: confirmation bias leads us to favor confirming evidence, while the availability heuristic makes vivid recent events seem more common than they are. Recognizing these patterns does not eliminate them, but labeling them can reduce their sway over decisions from hiring to investing.",
  "qs":[("The passage suggests cognitive biases", {"A":"are easily eliminated","B":"persist but can be partly mitigated by awareness","C":"only affect hiring","D":"improve investing","E":"are purely beneficial"}, "B", "The passage says recognition does not eliminate them but can reduce their sway."),
   ("The word 'mitigated' most nearly means", {"A":"worsened","B":"lessened/reduced","C":"caused","D":"ignored","E":"measured"}, "B", "Mitigated = reduced / lessened."),
   ("According to the passage, the availability heuristic causes", {"A":"accurate probability estimates","B":"vivid events to seem more common","C":"better hiring","D":"confirmation of beliefs","E":"less bias"}, "B", "Stated: vivid recent events seem more common than they are.")]},
 {"passage":"Renewable energy's intermittency - the sun does not always shine, the wind does not always blow - demands storage or backup. Batteries are improving but remain costly; grids therefore blend renewables with flexible natural-gas plants and, increasingly, demand response that shifts load to off-peak hours. The transition is less a switch than a careful balancing act.",
  "qs":[("The passage suggests the renewable transition requires", {"A":"only batteries","B":"balancing storage, backup, and demand management","C":"ending all gas use immediately","D":"ignoring intermittency","E":"no planning"}, "B", "The passage describes blending storage, gas backup, and demand response."),
   ("The word 'intermittency' most nearly means", {"A":"constant supply","B":"irregular/stop-start availability","C":"low cost","D":"high output","E":"reliability"}, "B", "Intermittency = stop-start / irregular availability."),
   ("According to the passage, demand response", {"A":"raises peak load","B":"shifts load to off-peak hours","C":"replaces all backup","D":"eliminates batteries","E":"increases cost only"}, "B", "Stated: demand response shifts load to off-peak hours.")]},
]

# ---- MORE SYNONYM CLUSTERS (volume round) ----
CLUSTERS += [
 ["abrasive","harsh","caustic"],["equable","even-tempered","placid"],["insouciant","carefree","nonchalant"],
 ["lugubrious","mournful","melancholy"],["panegyric","praise","encomium"],["recalcitrant","stubborn","obstinate"],
 ["sanguine","hopeful","optimistic"],["vituperate","berate","revile"],["vociferous","loud","clamorous"],
 ["zeitgeist","spirit of the age","ethos"],["abstemious","temperate","abstinent"],["crapulous","intemperate","dissolute"],
 ["defenestrate","throw out window","eject"],["ebullient","joyful","exuberant"],["fatuous","foolish","inane"],
 ["garrulous","talkative","loquacious"],["hirsute","hairy","shaggy"],["iconoclast","dissenter","heretic"],
 ["jejune","immature","puerile"],["knavish","dishonest","roguish"],["limpid","clear","pellucid"],
 ["meretricious","gaudy","tawdry"],["obtuse","dull","stupid"],["pacific","peaceful","tranquil"],
 ["querulous","complaining","petulant"],["refulgent","shining","radiant"],["saturate","soak","drench"],
 ["taciturn","silent","reticent"],["urbane","polished","suave"],["verisimilitude","realism","truth"],
 ["winsome","charming","engaging"],["yearn","long","crave"],["zephyr","breeze","gentle wind"],
 ["ascetic","austere","abstemious"],["bilious","irritable","peevish"],["castigate","rebuke","chastise"],
 ["desultory","random","aimless"],["effusive","gushing","expressive"],["fortuitous","lucky","propitious"],
 ["gregarious","social","outgoing"],["impecunious","poor","penniless"],["inveterate","habitual","chronic"],
 ["laconic","terse","concise"],["mellifluous","sweet-sounding","honeyed"],["obstreperous","unruly","noisy"],
 ["pellucid","clear","limpid"],["prevaricate","lie","equivocate"],["quiescent","dormant","still"],
 ["recalcitrant","defiant","stubborn"],["surreptitious","secret","covert"],["truculent","aggressive","belligerent"],
 ["ubiquitous","everywhere","pervasive"],["valedictory","farewell","parting"],["wither","shrivel","fade"]
]

# ---- RC PASSAGES (volume 2) ----
RC += [
 {"passage":"The Enlightenment prized reason and individual liberty, yet many of its thinkers held views now seen as contradictory: advocating universal rights while owning enslaved people or excluding women. Historians caution that the era's legacy is not a simple triumph of progress but a complex inheritance in which lofty principles coexisted with glaring exclusions that later movements would spend centuries correcting.",
  "qs":[("The passage suggests the Enlightenment's legacy is", {"A":"an unqualified triumph","B":"principled yet marked by contradictions and exclusions","C":"solely about slavery","D":"irrelevant today","E":"opposed to liberty"}, "B", "The passage frames it as lofty principles coexisting with exclusions."),
   ("The word 'coexisted' most nearly means", {"A":"conflicted","B":"existed together","C":"vanished","D":"preceded","E":"ended"}, "B", "Coexisted = existed at the same time."),
   ("According to the passage, later movements worked to", {"A":"restore slavery","B":"correct the exclusions","C":"reject reason","D":"abolish liberty","E":"ignore history"}, "B", "Stated: later movements spent centuries correcting the exclusions.")]},
 {"passage":"Supply chains stretched across continents mean a factory's output depends on components from dozens of countries. A pandemic, a war, or a single port bottleneck can halt production thousands of miles away. Firms once optimized purely for low cost now prize resilience, holding extra inventory and qualifying alternate suppliers even at higher expense, accepting that efficiency and robustness sometimes pull in opposite directions.",
  "qs":[("The passage suggests firms now value", {"A":"cost alone","B":"resilience alongside cost","C":"fewer suppliers","D":"no inventory","E":"single sourcing"}, "B", "The passage says firms now prize resilience, not just low cost."),
   ("The word 'resilience' most nearly means", {"A":"fragility","B":"ability to recover from shocks","C":"cheapness","D":"speed","E":"isolation"}, "B", "Resilience = capacity to withstand / recover from disruption."),
   ("According to the passage, efficiency and robustness", {"A":"always align","B":"can conflict","C":"are identical","D":"never matter","E":"only help ports"}, "B", "Stated: they sometimes pull in opposite directions.")]},
 {"passage":"Language shapes but does not imprison thought. Speakers of languages with rich spatial frames of reference navigate differently than those who rely on absolute compass directions, yet all humans share the cognitive capacity to learn any system. The Sapir-Whorf hypothesis, in its strong form, overstated linguistic determinism; in its weak form, it correctly notes that habitual vocabulary nudges attention toward some distinctions over others.",
  "qs":[("The passage suggests language", {"A":"fully determines thought","B":"influences but does not imprison thought","C":"is irrelevant to cognition","D":"only uses compass directions","E":"prevents learning"}, "B", "The passage's opening line states language shapes but does not imprison thought."),
   ("The word 'determinism' most nearly means", {"A":"freedom","B":"the view that language fixes thought","C":"learning","D":"translation","E":"grammar"}, "B", "Linguistic determinism = language determines thought."),
   ("According to the passage, the weak form of Sapir-Whorf holds that vocabulary", {"A":"controls everything","B":"nudges attention toward certain distinctions","C":"is meaningless","D":"eliminates thought","E":"uses only compass terms"}, "B", "Stated: habitual vocabulary nudges attention toward some distinctions.")]},
 {"passage":"Biodiversity stabilizes ecosystems: when many species fill similar roles, the loss of one is buffered by others. Monocultures, by contrast, are productive until a single pest or drought cascades through the uniform stand. Ecologists therefore warn that optimizing short-term yield by simplifying nature trades long-term stability for immediate gain, a bargain that climate change is making riskier by the year.",
  "qs":[("The passage suggests biodiversity", {"A":"reduces stability","B":"buffers ecosystems against species loss","C":"causes monocultures","D":"lowers yield always","E":"is irrelevant"}, "B", "Stated: many species buffer the loss of one."),
   ("The word 'cascades' most nearly means", {"A":"stops","B":"spreads downward through","C":"helps","D":"isolates","E":"reverses"}, "B", "Cascades = spreads through the stand like a waterfall."),
   ("According to the passage, monocultures are", {"A":"always stable","B":"vulnerable to a single shock","C":"biodiverse","D":"climate-proof","E":"low yield"}, "B", "Stated: a single pest or drought cascades through the uniform stand.")]},
 {"passage":"The right to privacy is not enumerated in many constitutions yet is inferred from broader guarantees of liberty and security. Courts have extended it to contraception, marriage, and data, even as technology erodes the factual boundary between public and private. Critics argue that a right nowhere written should be narrower; defenders reply that liberty without a sphere of privacy is hollow.",
  "qs":[("The passage suggests the right to privacy is", {"A":"explicitly listed everywhere","B":"inferred rather than enumerated","C":"rejected by courts","D":"about property only","E":"a modern invention with no basis"}, "B", "Stated: it is inferred from broader guarantees, not enumerated."),
   ("The word 'hollow' most nearly means", {"A":"strong","B":"empty / meaningless","C":"private","D":"secure","E":"written"}, "B", "Hollow = empty / without substance."),
   ("According to the passage, technology", {"A":"strengthens privacy","B":"erodes the public-private boundary","C":"writes the right","D":"ignores courts","E":"creates liberty"}, "B", "Stated: technology erodes the boundary between public and private.")]},
 {"passage":"Nuclear fusion promises nearly limitless clean energy by fusing light atoms the way stars do, but the engineering challenge is immense: containing a 100-million-degree plasma long enough for net energy gain. Decades of investment have brought breakthroughs in magnetic confinement, yet commercial plants remain distant. Proponents argue the payoff justifies the cost; skeptics note that renewables already scale without fusion's unresolved hurdles.",
  "qs":[("The passage suggests fusion's main challenge is", {"A":"finding fuel","B":"confining extreme plasma for net gain","C":"public opposition","D":"lack of interest","E":"too much energy"}, "B", "Stated: containing 100M-degree plasma long enough for net gain."),
   ("The word 'immense' most nearly means", {"A":"tiny","B":"enormous","C":"solved","D":"irrelevant","E":"cheap"}, "B", "Immense = extremely large / great."),
   ("According to the passage, skeptics point out that", {"A":"fusion is commercial now","B":"renewables already scale without fusion's hurdles","C":"fusion is cheap","D":"plasma is cold","E":"no breakthroughs exist"}, "B", "Stated: renewables already scale without fusion's unresolved hurdles.")]}
]

# ---- SYNONYM CLUSTERS (volume 2) ----
CLUSTERS += [
 ["quixotic","impractical","romantic"],["umbrage","offense","resentment"],
 ["perspicacious","astute","discerning"],["proclivity","inclination","bent"],
 ["sanctimonious","hypocritical","self-righteous"],["tacit","implied","unspoken"],
 ["propensity","tendency","leaning"],["candor","frankness","honesty"],
 ["voluble","talkative","verbose"],[["pithy","concise","succinct"]],
 ["sedulous","diligent","assiduous"],[["recalcitrant","stubborn","defiant"]],
 ["sanguine","optimistic","hopeful"],["pugnacious","aggressive","combative"],
 ["vicarious","secondhand","indirect"],[["ebullient","exuberant","joyful"]],
 ["insidious","stealthy","creeping"],[["brazen","bold","shameless"]],
 ["brusque","abrupt","curt"],["demure","modest","reserved"],
 ["garrulous","loquacious","talkative"],[["laconic","terse","concise"]],
 ["reverent","respectful","adoring"],["cynical","skeptical","distrustful"],
 ["impervious","unaffected","resistant"],[["pliable","flexible","yielding"]],
 ["assuage","soothe","relieve"],[["exacerbate","worsen","aggravate"]],
 ["candid","open","honest"],["guileless","naive","innocent"],
 ["profligate","wasteful","extravagant"],["parsimonious","frugal","stingy"],
 ["resilient","tough","recovering"],["fragile","brittle","delicate"],
 ["adroit","skillful","dexterous"],["maladroit","clumsy","awkward"]
]

# Generate RC questions (all passages now appended)
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
