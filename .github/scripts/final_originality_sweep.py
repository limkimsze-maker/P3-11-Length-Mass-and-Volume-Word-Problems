from pathlib import Path
import re

p=Path('index.html')
s=p.read_text(encoding='utf-8')

# Drink-station problem: remove old person/liquid remnants and align all working text to the new story.
s=re.sub(r'function qMilkLeft\(\)\{const people=\[.*?\],liquids=\[.*?\];const person=pick\(people\),liquid=pick\(liquids\),total=', 'function qDrinkStation(){const total=', s, count=1)
s=s.replace('type:"Two-step: drank and left"', 'type:"Two-step: served and left"')
s=s.replace('title:`How much ${liquid} was drunk and left?`', 'title:"How much drink was served and left?"')
s=s.replace('<div class="sectionTag">(i) Total drunk</div>', '<div class="sectionTag">(i) Total served</div>')
s=s.replace('${person} drank ${input("a4")} <span>ml over the two days.</span>', 'The team served ${input("a4")} <span>ml over the two breaks.</span>')

# Sports-drink powder problem: remove unused food/person source material.
s=re.sub(r'function qPackets\(\)\{const people=\[.*?\],foods=\[.*?\];const person=pick\(people\),food=pick\(foods\),packets=', 'function qPowderPackets(){const packets=', s, count=1)
s=s.replace('type:"Packed equally into packets"', 'type:"Share remaining powder equally"')
s=s.replace('title:"How much went into each packet?"', 'title:"How much powder went into each team packet?"')
s=s.replace('>packed<', '>shared<')
s=s.replace('Find how much was packed', 'Find how much powder remained')
s=s.replace('${person} packed ${input("b4")} <span>g.</span>', 'Powder remaining: ${input("b4")} <span>g.</span>')

# Water-station problem: remove old named-person wording.
s=re.sub(r'function qBottlesTotal\(\)\{const names1=\[.*?\],names2=\[.*?\];const p1=pick\(names1\),p2=pick\(names2\),each=', 'function qWaterStation(){const each=', s, count=1)
s=s.replace('title:"How much water do they drink in total?"', 'title:"How much water is at the station altogether?"')
s=s.replace("First find ${p1}'s total", 'First find the water in the blue bottles')
s=s.replace('${p1} drinks ${input("c4")} <span>ml.</span>', 'The blue bottles hold ${input("c4")} <span>ml.</span>')
s=s.replace('They drink ${input("c11","tiny")} <span>l</span> ${input("c12","small")} <span>ml in total.</span>', 'The station has ${input("c11","tiny")} <span>l</span> ${input("c12","small")} <span>ml altogether.</span>')

# Marker-bag problem: remove old food/person wording and update the bar-model labels.
s=re.sub(r'function qBagsLeft\(\)\{const people=\[.*?\],items=\[.*?\];const person=pick\(people\),item=pick\(items\),totalBags=', 'function qMarkerBags(){const totalBags=', s, count=1)
s=s.replace('given away', 'moved')
s=s.replace('type:"Equal bags left"', 'type:"Training-marker bags left"')
s=s.replace('title:"How much mass was left?"', 'title:"What mass of marker bags remained?"')
s=s.replace('${person} had ${input("d4","tiny")} <span>bags left.</span>', 'The team had ${input("d4","tiny")} <span>bags left.</span>')
s=s.replace('${person} had ${input("d10")} <span>g left.</span>', 'The marker bags left had a mass of ${input("d10")} <span>g.</span>')

# Route-comparison problem: remove old named-traveller wording.
s=re.sub(r'function qTimesDifference\(\)\{const peopleA=\[.*?\],peopleB=\[.*?\];const pa=pick\(peopleA\),pb=pick\(peopleB\),factor=', 'function qRouteCompare(){const factor=', s, count=1)
s=s.replace('type:"Times as much and difference"', 'type:"Compare two training routes"')
s=s.replace('title:"How much further?"', 'title:"How much longer is Route A?"')
s=s.replace('${pa} travelled ${input("e9")} <span>${unitWord} further than ${pb}.</span>', 'Route A is ${input("e9")} <span>${unitWord} longer than Route B.</span>')

# Rename the old question-family references in the builder.
s=s.replace('qMilkLeft()', 'qDrinkStation()')
s=s.replace('qPackets()', 'qPowderPackets()')
s=s.replace('qBottlesTotal()', 'qWaterStation()')
s=s.replace('qBagsLeft()', 'qMarkerBags()')
s=s.replace('qTimesDifference()', 'qRouteCompare()')

# Update model helper naming that still implied a person rather than an amount.
s=s.replace('function svgUnitsAndTotal(unit,n,other,person1)', 'function svgUnitsAndTotal(unit,n,other,firstAmount)')
s=s.replace('p1W=person1*scale', 'p1W=firstAmount*scale')
s=s.replace('${person1} ml', '${firstAmount} ml')

p.write_text(s,encoding='utf-8')
