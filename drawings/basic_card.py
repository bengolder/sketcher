from sketcher import Surface, TextBlock
from sketcher.colors import *

png = Surface( 700, 400 )
png.fill( White )
text = TextBlock( "Thanks!" )
text.size = 24
png.add( text, "center" )
png.save( "drawings/basic_card.png" )










