from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')


def patch(old, new, label):
    global s
    if new in s:
        print(f'{label}: already fixed')
        return
    if old not in s:
        raise SystemExit(f'missing expected section: {label}')
    s = s.replace(old, new, 1)
    print(f'{label}: fixed')


# Equal packets: whole amount, packed/used parts, packed group, and one packet.
old = '''<rect x="${80+packedW}" y="32" width="${usedW}" height="28" fill="#f7ae2b" stroke="#222" stroke-width="2"/><text x="${80+(packedW+usedW)/2}" y="17"'''
new = '''<rect x="${80+packedW}" y="32" width="${usedW}" height="28" fill="#f7ae2b" stroke="#222" stroke-width="2"/><path d="M80 26 v-8 h${packedW+usedW} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M80 66 v8 h${packedW} v-8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M${80+packedW} 66 v8 h${usedW} v-8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${80+(packedW+usedW)/2}" y="17"'''
patch(old, new, 'packets upper brackets')

old = '''${divs}<text x="${80+packedW/2}" y="115"'''
new = '''${divs}<path d="M80 120 v-8 h${packedW} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M80 160 v8 h${unitW} v-8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${80+packedW/2}" y="115"'''
patch(old, new, 'packets lower brackets')

# Bottles: one bottle, first person's total, both people, and grand total.
old = '''${top}<text x="${72+unitW/2}" y="20"'''
new = '''${top}<path d="M72 28 v-8 h${unitW} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M72 66 v8 h${firstW} v-8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${72+unitW/2}" y="20"'''
patch(old, new, 'bottle unit brackets')

old = '''<rect x="${72+p1W}" y="130" width="${p2W}" height="28" fill="#9ec6ea" stroke="#222" stroke-width="2"/><text x="${72+p1W/2}" y="122"'''
new = '''<rect x="${72+p1W}" y="130" width="${p2W}" height="28" fill="#9ec6ea" stroke="#222" stroke-width="2"/><path d="M72 124 v-8 h${p1W} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M${72+p1W} 124 v-8 h${p2W} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M72 164 v8 h${p1W+p2W} v-8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${72+p1W/2}" y="122"'''
patch(old, new, 'bottle total brackets')

# Equal bags: add the missing one-unit bracket. The group brackets already exist.
old = '''${units}<text x="${72+unitW/2}" y="20"'''
new = '''${units}<path d="M72 32 v-8 h${unitW} v8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${72+unitW/2}" y="20"'''
patch(old, new, 'bag unit bracket')

# Times-as-much: whole amount and difference portion.
old = '''<rect x="120" y="80" width="${unitW}" height="28" fill="#f0ae3c" stroke="#222" stroke-width="2"/><text x="${120+unitW*factor/2}" y="19"'''
new = '''<rect x="120" y="80" width="${unitW}" height="28" fill="#f0ae3c" stroke="#222" stroke-width="2"/><path d="M120 28 v-8 h${unitW*factor} v8" fill="none" stroke="#000" stroke-width="1.8"/><path d="M${120+unitW} 66 v8 h${unitW*(factor-1)} v-8" fill="none" stroke="#000" stroke-width="1.8"/><text x="${120+unitW*factor/2}" y="19"'''
patch(old, new, 'times-as-much brackets')

p.write_text(s, encoding='utf-8')
print('Bracket repair complete.')
