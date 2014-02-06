from sketcher import Card, TextBlock
from sketcher.colors import *

card = Card( White )
text = TextBlock( "Thanks!" )
text.size = 24
card.add( text, "center" )
card.save( "drawings/basic_card.png" )










