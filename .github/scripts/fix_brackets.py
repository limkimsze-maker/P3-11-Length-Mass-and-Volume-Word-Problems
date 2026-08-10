from pathlib import Path

p=Path('index.html')
s=p.read_text(encoding='utf-8')

def rep(a,b,label):
    global s
    if a not in s:
        raise SystemExit(f'missing {label}')
    s=s.replace(a,b,1)

rep('''    <rect x="${80+packedW}" y="32" width="${usedW}" height="28" fill="#f7ae2b" stroke="#222" stroke-width="2"/>\n    <text x="${80+(packedW+usedW)/2}" y="17"''','''    <rect x="${80+packedW}" y="32" width="${usedW}" height="28" fill="#f7ae2b" stroke="#222" stroke-width="2"/>\n    <path d="M80 26 v-8 h${packedW+usedW} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M80 66 v8 h${packedW} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M${80+packedW} 66 v8 h${usedW} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${80+(packedW+usedW)/2}" y="17"''','packets upper')

rep('''    ${divs}\n    <text x="${80+packedW/2}" y="115"''','''    ${divs}\n    <path d="M80 120 v-8 h${packedW} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M80 160 v8 h${unitW} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${80+packedW/2}" y="115"''','packets lower')

rep('''    ${top}\n    <text x="${72+unitW/2}" y="20"''','''    ${top}\n    <path d="M72 28 v-8 h${unitW} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M72 66 v8 h${firstW} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${72+unitW/2}" y="20"''','bottle unit')

rep('''    <rect x="${72+p1W}" y="130" width="${p2W}" height="28" fill="#9ec6ea" stroke="#222" stroke-width="2"/>\n    <text x="${72+p1W/2}" y="122"''','''    <rect x="${72+p1W}" y="130" width="${p2W}" height="28" fill="#9ec6ea" stroke="#222" stroke-width="2"/>\n    <path d="M72 124 v-8 h${p1W} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M${72+p1W} 124 v-8 h${p2W} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M72 164 v8 h${p1W+p2W} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${72+p1W/2}" y="122"''','bottle total')

rep('''    ${units}\n    <text x="${72+unitW/2}" y="20"''','''    ${units}\n    <path d="M72 32 v-8 h${unitW} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M72 72 v8 h${unitW*given} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M${72+unitW*given} 72 v8 h${unitW*left} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${72+unitW/2}" y="20"''','bags')

rep('''    ${top}\n    <rect x="120" y="80" width="${unitW}" height="28" fill="#f0ae3c" stroke="#222" stroke-width="2"/>\n    <text x="${120+unitW*factor/2}" y="19"''','''    ${top}\n    <rect x="120" y="80" width="${unitW}" height="28" fill="#f0ae3c" stroke="#222" stroke-width="2"/>\n    <path d="M120 28 v-8 h${unitW*factor} v8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <path d="M${120+unitW} 66 v8 h${unitW*(factor-1)} v-8" fill="none" stroke="#000" stroke-width="1.8"/>\n    <text x="${120+unitW*factor/2}" y="19"''','times')

p.write_text(s,encoding='utf-8')
