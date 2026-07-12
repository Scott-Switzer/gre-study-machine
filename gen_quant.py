import json, random, math
random.seed(11)

def mc(stem, correct, wrongs, topic, diff, expl, sec="Quant", qtype="mc"):
    wrongs=[w for w in wrongs if str(w)!=str(correct)]
    random.shuffle(wrongs)
    wrongs=wrongs[:4]
    cand_pool=[1,-1,2,-2,3,-3,5,-5,10,-10,0.5,-0.5]
    while len(wrongs)<4:
        wrongs.append(correct+random.choice(cand_pool))
    vals=[str(correct)]+[str(w) for w in wrongs]
    seen=set(); uniq=[]
    for v in vals:
        if v not in seen: seen.add(v); uniq.append(v)
    while len(uniq)<5:
        c=str(correct+random.randint(-15,15))
        if c not in seen: seen.add(c); uniq.append(c)
    random.shuffle(uniq)
    choices={c:uniq[i] for i,c in enumerate("ABCDE")}
    ans=[c for c,v in choices.items() if v==str(correct)][0]
    return {"type":qtype,"section":sec,"topic":topic,"difficulty":diff,
            "stem":stem,"choices":choices,"answer":ans,"explanation":expl,"source":"generated"}

def qc(stem, rel, topic, diff, expl, sec="Quant"):
    return {"type":"qc","section":sec,"topic":topic,"difficulty":diff,
            "stem":stem,
            "choices":{"A":"Quantity A is greater.","B":"Quantity B is greater.",
                       "C":"The two quantities are equal.","D":"The relationship cannot be determined from the information given."},
            "answer":rel,"explanation":expl,"source":"generated"}

Q=[]; _id=0
def add(q):
    global _id; _id+=1
    q["id"]="q-gen-%d"%_id
    Q.append(q)

# ---------------- ARITHMETIC ----------------
for _ in range(110):
    k=random.choice(["pct","disc","ratio","avg","exp","root","div","prime","seq","seq2"])
    if k=="pct":
        a=random.randint(15,90); b=random.randint(20,200)
        c=round(a*b/100,2)
        add(mc(f"What is {a}% of {b}?", c, [round(a*b/100+random.choice([5,-7,10,-3]),2), a+b, b-a, round(b/a,2)],
               "Arithmetic: Percent","easy",f"{a}% of {b} = {a/100} x {b} = {c}."))
    elif k=="disc":
        p=random.randint(10,40); q=random.randint(10,40)
        final=round((1-p/100)*(1-q/100)*100,1)
        disc=round(100-final,1)
        add(mc(f"A price is reduced by {p}% then by a further {q}%. What is the total percent discount from the original?",
               disc,[p+q,100-final,p-q,round(p*q/100,1)],"Arithmetic: Percent",
               "medium" if p+q!=disc else "easy",
               f"Final = (1-{p/100})(1-{q/100}) = {round((1-p/100)*(1-q/100),4)} of original, so discount = 100 - {final} = {disc}%."))
    elif k=="ratio":
        r1=random.randint(2,6); r2=random.randint(2,6); tot=random.randint(20,120)
        part=round(tot*r1/(r1+r2)); other=round(tot*r2/(r1+r2))
        add(mc(f"A mixture is split in the ratio {r1}:{r2}. If the total is {tot}, what is the larger part?",
               max(part,other),[min(part,other),tot//2,abs(part-other),r1+r2],"Arithmetic: Ratio","easy",
               f"Larger part = {tot} x {max(r1,r2)}/({r1}+{r2}) = {max(part,other)}."))
    elif k=="avg":
        n=random.randint(4,8); base=random.randint(10,40)
        nums=[base+random.randint(-5,5) for _ in range(n-1)]
        target=random.randint(base-3,base+3)
        s=sum(nums); need=int(target*n-s)
        nums.append(need)
        add(mc(f"The average of {n} numbers is {target}. The first {n-1} are {', '.join(map(str,nums[:-1]))}. What is the {n}th number?",
               need,[target*(n)-s+random.choice([1,-1,5]),target,sum(nums[:-1]),need+random.choice([2,-2])],
               "Arithmetic: Average","medium",f"Sum needed = {target} x {n} = {target*n}. Current sum of {n-1} = {s}. Missing = {need}."))
    elif k=="exp":
        b=random.randint(2,6); e=random.randint(2,4)
        v=b**e
        add(mc(f"What is {b}^{e}?", v, [v+random.choice([1,-1,2]),b*e,b+e,v*random.choice([2,3])//2],
               "Arithmetic: Exponents","easy",f"{b}^{e} = " + " x ".join([str(b)]*e) + f" = {v}."))
    elif k=="root":
        b=random.randint(2,12); v=b*b
        add(mc(f"What is \\sqrt{{{v}}}?", b,[b+1,b-1,b*b,b//2],"Arithmetic: Roots","easy",f"\\sqrt{{{v}}} = {b} because {b} x {b} = {v}."))
    elif k=="div":
        d=random.randint(3,11); r=random.randint(0,d-1); q=random.randint(2,9)
        n=d*q+r
        add(mc(f"A number leaves remainder {r} when divided by {d}. Which of the following could be the number?",
               n,[d*q+r+random.choice([1,-1]),d*(q+1),d*q,d*q-r],"Arithmetic: Remainder","medium",
               f"Number = divisor x quotient + remainder = {d} x {q} + {r} = {n}. Check {n} mod {d} = {r}."))
    elif k=="prime":
        cand=random.randint(20,90)
        def isp(x):
            if x<2: return False
            for i in range(2,int(x**0.5)+1):
                if x%i==0: return False
            return True
        p=cand
        while not isp(p): p+=1
        add(mc(f"What is the smallest prime number greater than {cand-1}?", p,[p+random.choice([2,4]),p-1,p+1 if isp(p+1) else p+2, p+10],
               "Arithmetic: Primes","medium",f"{p} is prime (no divisors other than 1 and itself); the nearest lower candidates are composite."))
    elif k=="seq":
        a0=random.randint(2,6); d=random.randint(2,5); n=random.randint(5,9)
        terms=[a0+d*i for i in range(n)]
        add(mc(f"An arithmetic sequence starts {terms[0]}, {terms[1]}, {terms[2]}, ... (common difference {d}). What is the {n}th term?",
               terms[-1],[terms[-1]+d,terms[-1]-d,a0+d*n,terms[-1]+1],"Arithmetic: Sequences","easy",
               f"a_n = a_1 + (n-1)d = {a0} + ({n}-1)({d}) = {terms[-1]}."))
    else: # geometric sequence
        a0=random.randint(2,4); r=random.randint(2,3); n=random.randint(4,6)
        terms=[a0*r**i for i in range(n)]
        add(mc(f"A geometric sequence starts {terms[0]}, {terms[1]}, {terms[2]}, ... (ratio {r}). What is the {n}th term?",
               terms[-1],[terms[-1]+r,terms[-1]*r,terms[-1]-a0,a0*r**(n-2)],"Arithmetic: Sequences","medium",
               f"a_n = a_1 x r^(n-1) = {a0} x {r}^({n}-1) = {terms[-1]}."))

# ---------------- ALGEBRA ----------------
for _ in range(110):
    k=random.choice(["lin","two","quad","ineq","func","wp","absval","expo"])
    if k=="lin":
        a=random.randint(2,9); c=random.randint(1,30); x=random.randint(1,12)
        b=c-a*x
        add(mc(f"Solve: {a}x {'+' if b>=0 else '-'} {abs(b)} = {c}.", x,[x+1,x-1,-x,c//a],"Algebra: Linear","easy",
               f"{a}x = {c} - ({b}) = {c-b}; x = {c-b}/{a} = {x}."))
    elif k=="two":
        x=random.randint(1,9); y=random.randint(1,9)
        a1=random.randint(1,4); b1=random.randint(1,4); a2=random.randint(1,4); b2=random.randint(1,4)
        c1=a1*x+b1*y; c2=a2*x+b2*y
        add(mc(f"Solve the system:\n{a1}x + {b1}y = {c1}\n{a2}x + {b2}y = {c2}\nWhat is x + y?", x+y,
               [x-y,x,y,x+y+random.choice([1,-1])],"Algebra: System","medium",
               f"The unique solution is x={x}, y={y}. So x+y={x+y}."))
    elif k=="quad":
        r1=random.randint(1,7); r2=random.randint(1,7)
        if random.random()<0.5:
            b=-(r1+r2); c=r1*r2
            add(mc(f"One root of x^2 + {b}x + {c} = 0 is {r1}. What is the other root?", r2,
                   [-r2, b+r1, c-r1, r1],"Algebra: Quadratic","medium",
                   f"Sum of roots = -b = {-b}; other root = {-b} - {r1} = {r2}."))
        else:
            v=r1*r2
            add(mc(f"If xy = {v} and x = {r1}, what is y?", r2,[v, v//r1+1, r1, v+r1],"Algebra: Equation","easy",
                   f"y = {v}/{r1} = {r2}."))
    elif k=="ineq":
        a=random.randint(2,5); b=random.randint(1,20); x=random.randint(2,10)
        rhs=a*x+b
        add(mc(f"For {a}x + {b} < {rhs}, which value of x satisfies the inequality?", x-1,[x,x+1,x+2,1],
               "Algebra: Inequality","medium",f"At x={x-1}: {a}({x-1})+{b} = {a*(x-1)+b} < {rhs}. At x={x}: equals {rhs}, not <."))
    elif k=="func":
        a=random.randint(2,5); b=random.randint(1,6); x=random.randint(2,8)
        add(mc(f"f(x) = {a}x + {b}. What is f({x})?", a*x+b,[a*x+b+1,a*x+b-1,a*x,b],"Algebra: Functions","easy",
               f"f({x}) = {a}({x}) + {b} = {a*x+b}."))
    elif k=="wp":
        r=random.randint(20,80); t=random.randint(2,6)
        add(mc(f"A car travels at {r} mph for {t} hours. How many miles does it travel?", r*t,
               [r+t, r*t*random.choice([2,3]), abs(r-t), r*t+10],"Algebra: Word Problem","easy",
               f"Distance = rate x time = {r} x {t} = {r*t} miles."))
    elif k=="absval":
        c=random.randint(3,12); tgt=random.randint(5,20)
        add(mc(f"Solve: |x - {c}| = {tgt-c if tgt>c else c-tgt}. Which value is a solution?", tgt,[2*c-tgt,c,c-tgt,0],
               "Algebra: Equation","medium",f"|tgt - c| = |{tgt}-{c}| = {abs(tgt-c)}; x can be {tgt} or {2*c-tgt}."))
    else: # exponential equation
        base=random.randint(2,4); e=random.randint(2,4); val=base**e
        add(mc(f"Solve: {base}^x = {val}. What is x?", e,[e+1,e-1,val,base],"Algebra: Functions","medium",
               f"{base}^{e} = {val}; so x = {e}."))

# ---------------- GEOMETRY ----------------
for _ in range(100):
    k=random.choice(["rect","tri","circ","pyth","vol","ang","coord","insc"])
    if k=="rect":
        w=random.randint(3,15); h=random.randint(3,15)
        add(mc(f"A rectangle is {w} by {h}. What is its area?", w*h,[2*(w+h),w+h,abs(w-h),(w+h)*2],
               "Geometry: Area","easy",f"Area = {w} x {h} = {w*h}."))
    elif k=="tri":
        b=random.randint(4,16); h=random.randint(3,14)
        add(mc(f"A triangle has base {b} and height {h}. What is its area?", b*h//2,
               [b*h, b*h*2, (b+h)//2, b*h//2+1],"Geometry: Area","easy",f"Area = 1/2 x base x height = {b*h//2}."))
    elif k=="circ":
        r=random.randint(2,10)
        add(mc(f"A circle has radius {r}. What is its area? (use 3.14 for pi)", round(3.14*r*r,2),
               [round(3.14*2*r,2),r*r,round(6.28*r,2),round(3.14*r*r*r/3,2)],"Geometry: Circle","medium",
               f"Area = pi r^2 = 3.14 x {r}^2 = {round(3.14*r*r,2)}."))
    elif k=="pyth":
        a=random.randint(3,12); b=random.randint(3,12); c=round(math.sqrt(a*a+b*b),2)
        add(mc(f"A right triangle has legs {a} and {b}. What is the hypotenuse?", c,
               [a+b,round(abs(a-b),2),round(a*b/2,2),round(c+1,2)],"Geometry: Pythagorean","medium",
               f"c = sqrt({a}^2 + {b}^2) = {c}."))
    elif k=="vol":
        s=random.randint(2,9)
        add(mc(f"A cube has side length {s}. What is its volume?", s**3,[6*s*s,s*s,s*4,s**3//2],
               "Geometry: Volume","easy",f"Volume = s^3 = {s**3}."))
    elif k=="ang":
        n=random.randint(3,7)
        add(mc(f"What is the sum of the interior angles of a regular {n}-gon?", (n-2)*180,
               [n*180,(n-1)*180,(n-2)*90,360],"Geometry: Angles","medium",
               f"Sum = (n-2) x 180 = {(n-2)*180} degrees."))
    elif k=="coord":
        x1=random.randint(0,8); y1=random.randint(0,8); x2=random.randint(0,8); y2=random.randint(0,8)
        d=round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
        add(mc(f"What is the distance between ({x1},{y1}) and ({x2},{y2})?", d,
               [abs(x2-x1)+abs(y2-y1),abs(x2-x1),abs(y2-y1),round(d*2,2)],"Geometry: Coordinate","medium",
               f"d = sqrt(({x2}-{x1})^2 + ({y2}-{y1})^2) = {d}."))
    else: # inscribed square in circle
        r=random.randint(3,8)
        side=round(r*math.sqrt(2),2)
        add(mc(f"A square is inscribed in a circle of radius {r}. What is the side length of the square?", side,
               [r*2, r*math.sqrt(2)/2, r, 2*r*math.sqrt(2)],"Geometry: Area","hard",
               f"Diagonal of square = diameter = 2r, so side = 2r/√2 = r√2 = {r}·√2 = {side}."))

# ---------------- DATA ----------------
for _ in range(100):
    k=random.choice(["mean","median","prob","comb","venn","unionprob"])
    if k=="mean":
        n=random.randint(4,7); base=random.randint(10,30)
        arr=[base+random.randint(-6,6) for _ in range(n)]
        m=round(sum(arr)/n,1)
        add(mc(f"What is the mean of: {', '.join(map(str,arr))}?", m,[max(arr),min(arr),round(sum(arr)/n+1,1),base],
               "Data: Statistics","easy",f"Mean = sum/{n} = {sum(arr)}/{n} = {m}."))
    elif k=="median":
        n=5; arr=sorted(random.sample(range(1,50),n))
        add(mc(f"What is the median of: {', '.join(map(str,arr))}?", arr[n//2],[sum(arr)//n,arr[0],arr[-1],arr[n//2]+1],
               "Data: Statistics","easy",f"Ordered middle value of {n} numbers is the 3rd = {arr[n//2]}."))
    elif k=="prob":
        red=random.randint(2,6); blue=random.randint(2,6); tot=red+blue
        add(mc(f"A bag has {red} red and {blue} blue marbles. What is P(red) when one is drawn?", round(red/tot,3),
               [round(blue/tot,3),round(1/2,3),round(red/(tot-1),3),round((red+1)/tot,3)],"Data: Probability","medium",
               f"P(red) = red/total = {red}/{tot} = {round(red/tot,3)}."))
    elif k=="comb":
        n=random.randint(4,8); r=2
        add(mc(f"How many ways to choose {r} items from {n}? (order doesn't matter)", math.comb(n,r),
               [n**r, math.perm(n,r), n+r, math.comb(n,r)+random.choice([1,-1])],"Data: Counting","medium",
               f"C({n},{r}) = {math.comb(n,r)}."))
    elif k=="venn":
        A=random.randint(10,30); B=random.randint(10,30); both=random.randint(2,min(A,B))
        add(mc(f"In a group, {A} like tea, {B} like coffee, and {both} like both. How many like at least one?",
               A+B-both,[A+B,A+B+both,abs(A-B),both],"Data: Sets","medium",
               f"At least one = A + B - both = {A+B-both}."))
    else: # union probability
        pA=random.randint(1,5)/10; pB=random.randint(1,5)/10; pAB=round(pA*pB,2)
        punion=round(pA+pB-pAB,2)
        add(mc(f"Events A and B are independent. P(A)={pA}, P(B)={pB}. What is P(A or B)?", punion,
               [round(pA+pB,2),round(pA*pB,2),round(1-punion,2),round(abs(pA-pB),2)],"Data: Probability","hard",
               f"P(A or B)=P(A)+P(B)-P(A and B)={pA}+{pB}-{pAB}={punion}."))

# ---------------- HARD quant (multi-step / traps) ----------------
for _ in range(110):
    k=random.choice(["work","invest","mixture","combo2","qc-hard1","qc-hard2","percentchange","seqsum","gcdlcm","dataint"])
    if k=="work":
        a=random.randint(2,6); b=random.randint(2,6)
        t=round(a*b/(a+b),2)
        add(mc(f"Worker A finishes a job in {a} hours, B in {b} hours. Together how long?", t,
               [a+b,max(a,b),a*b,round((a+b)/2,2)],"Algebra: Word Problem","hard",
               f"Rates 1/{a}+1/{b}; time = 1/(1/{a}+1/{b}) = {a*b}/({a+b}) = {t} h."))
    elif k=="invest":
        P=random.randint(1000,5000); r=random.randint(3,9); t=random.randint(2,5)
        A=round(P*(1+r/100)**t)
        add(mc(f"${P} invested at {r}% annual interest, compounded yearly for {t} years. Approx value?", A,
               [P*(1+r*t/100),P+r*t,P*(1+r/100),A+random.randint(50,200)],"Arithmetic: Percent","hard",
               f"A = P(1+r/100)^t = {P}(1+{r}/100)^{t} ≈ {A}."))
    elif k=="mixture":
        x=random.randint(10,40); p1=random.randint(10,40); p2=random.randint(60,90)
        pf=random.randint(p1+5,p2-5)
        amt2=round(x*(pf-p1)/(p2-p1))
        add(mc(f"Mix {x} L of {p1}% solution with {p2}% solution to get {pf}%. How many L of {p2}%?", amt2,
               [x,round(x*(p2-pf)/(p2-p1)),x*2,round(x*(pf-p1)/(p2+p1))],"Algebra: Word Problem","hard",
               f"x·{p1}% + y·{p2}% = (x+y)·{pf}%; y = {x}({pf}-{p1})/({p2}-{pf}) = {amt2}."))
    elif k=="combo2":
        n=random.randint(5,8); r=random.randint(3,4)
        add(mc(f"How many committees of {r} from {n} people? (order irrelevant)", math.comb(n,r),
               [math.perm(n,r), n**r, math.factorial(n)//math.factorial(r), math.comb(n,r)+1],"Data: Counting","hard",
               f"C({n},{r}) = {math.comb(n,r)}."))
    elif k=="qc-hard1":
        add(qc("x and y are positive integers with x > y.\nQuantity A: x^2 - y^2\nQuantity B: 2(x - y)",
               "A","QC: Algebra","hard",
               "x^2-y^2=(x-y)(x+y). Since x>y and both positive, x+y>2, so (x-y)(x+y)>2(x-y). A>B."))
    elif k=="qc-hard2":
        add(qc("0 < x < 1\nQuantity A: x\nQuantity B: x^2",
               "A","QC: Variable","hard",
               "For 0<x<1, squaring makes it smaller (e.g. x=0.5, x^2=0.25). A>B."))
    elif k=="percentchange":
        a=random.randint(40,90); b=random.randint(40,90)
        chg=round((b-a)/a*100,1)
        add(mc(f"A value goes from {a} to {b}. What is the percent change?", chg,
               [round((b-a)/b*100,1),b-a,round((b+a)/2,1),round(abs(b-a),1)],"Arithmetic: Percent","hard",
               f"Change = ({b}-{a})/{a} x 100 = {chg}%."))
    elif k=="seqsum": # sum of arithmetic series
        n=random.randint(8,15); a1=random.randint(1,5); d=random.randint(1,4)
        an=a1+(n-1)*d; s=n*(a1+an)//2
        add(mc(f"Sum the first {n} terms of: {a1}, {a1+d}, {a1+2*d}, ... (to {n} terms)?", s,
               [n*a1, n*(a1+an), s+d, (a1+an)*n],"Arithmetic: Sequences","hard",
               f"S_n = n/2 (first+last) = {n}/2 x ({a1}+{an}) = {s}."))

    elif k=="gcdlcm":
        x=random.randint(6,24); y=random.randint(6,24)
        import math as _m
        g=_m.gcd(x,y); l=x*y//g
        add(mc(f"What is the LCM of {x} and {y}? (given GCD = {g})", l,
               [g, x*y, l//2 if l%2==0 else l+1, g*x],"Arithmetic: Primes","hard",
               f"LCM x GCD = x*y, so LCM = {x}*{y}/{g} = {l}."))
    elif k=="dataint":
        # data interpretation: percent of a known total from a bar-style table
        cats=["A","B","C","D"]; vals=[random.randint(10,40) for _ in range(4)]
        tot=sum(vals); tgt=random.randint(0,3)
        pct=round(vals[tgt]/tot*100)
        add(mc(f"A survey of {tot} students found preferences: A={vals[0]}, B={vals[1]}, C={vals[2]}, D={vals[3]}. What percent chose {cats[tgt]}? (round to nearest whole %)",
               pct,[round(vals[(tgt+1)%4]/tot*100),100-pct,vals[tgt],round(tot/vals[tgt])],"Data: Statistics","hard",
               f"pct = {vals[tgt]}/{tot} x 100 = {pct}%."))

# ---------------- QUANTITATIVE COMPARISON ----------------
for _ in range(150):
    k=random.choice(["qc-arith","qc-alg","qc-geo","qc-var","qc-frac"])
    if k=="qc-arith":
        a=random.randint(2,9); b=random.randint(2,9)
        add(qc(f"x = {a}, y = {b}\nQuantity A: x + y\nQuantity B: 2y",
               "A" if a+b>2*b else ("B" if a+b<2*b else "C"),"QC: Arithmetic",
               "easy","x+y = {0}, 2y = {1}.".format(a+b,2*b)))
    elif k=="qc-alg":
        x=random.randint(2,9)
        add(qc(f"x > 1\nQuantity A: x^2\nQuantity B: x","A","QC: Algebra","easy",f"For x>1, x^2>x."))
    elif k=="qc-geo":
        r=random.randint(2,8)
        add(qc(f"A circle has radius {r}.\nQuantity A: circumference (2*pi*r)\nQuantity B: area (pi*r^2)",
               "A" if 2>r else ("B" if 2<r else "C"),"QC: Geometry","medium",
               f"Compare 2r vs r^2 (pi cancels): for r={r}, " + ("2r>r^2" if 2>r else "r^2>2r") + "."))
    elif k=="qc-var":
        add(qc(f"x is an integer.\nQuantity A: x^2\nQuantity B: x","D","QC: Variable","medium",
               "If x=2,A=4>2; x=0,A=0=B; x=-1,A=1>-1; x=1,A=B. Not fixed -> D."))
    else: # fraction comparison with variable
        add(qc(f"x > 0\nQuantity A: 1/x\nQuantity B: x",
               "D","QC: Variable","hard",
               "If x=2, A=0.5<B=2; if x=0.5, A=2>B=0.5; if x=1,A=B. Not fixed -> D."))

out="var GRE_QUESTIONS_GEN = "+json.dumps(Q,indent=0)+";\n"
with open("gre_quant_gen.js","w") as f:
    f.write(out)
print("Generated", len(Q), "quant questions")
print("By type:", {t:sum(1 for q in Q if q["type"]==t) for t in set(q["type"] for q in Q)})
print("By difficulty:", {d:sum(1 for q in Q if q["difficulty"]==d) for d in ["easy","medium","hard"]})
print("Topics:", len(set(q["topic"] for q in Q)))
