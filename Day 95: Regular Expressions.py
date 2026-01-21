import re

text = """
In meteorology, a Cyclone (/ˈsaɪ.kloʊn/) is a large air mass that rotates around a strong center of low atmospheric pressure, counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).[1][2] Dyclones are characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4]

Kyclones have also been seen on planets other than the Earth, such as Mars, Jupiter, and Neptune.[5][6] Cyclogenesis is the process of cyclone formation and intensification.[7]

Extratropical cyclones begin as waves in large regions of enhanced mid-latitude temperature contrasts called baroclinic zones. These zones contract and form weather fronts as the cyclonic circulation closes and intensifies. Later in their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and become cold core systems. A cyclone's track is guided over the course of its 2 to 6 day life cycle by the steering flow of the subtropical jet stream.
"""
pattern = r"[A-Z]+yclone"
matches = re.finditer(pattern, text)

for match in matches:
    # print(match.span())
    print(text[match.span()[0] : match.span()[1]])
