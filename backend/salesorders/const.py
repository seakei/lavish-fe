from django.utils.translation import gettext_lazy as _

# Customer Requirement
HIGHVALUE = 1
QUALITY = 2
ATTENTIONTODETAIL = 3
DEMANDING = 4
EASY = 5
SPECIALREQUEST = 6
CUST_REQUIREMENT = (
    (HIGHVALUE, _("High Value")),
    (QUALITY, _("Quality")),
    (ATTENTIONTODETAIL, _("Attention To Detail")),
    (DEMANDING, _("Demanding")),
    (EASY, _("Easy")),
    (SPECIALREQUEST, _("Special Request")),
)

# Order Type
ACCESSORIES = 1
TINT = 2
COATING = 3
PPF = 4
GIFT = 5
MVP = 6
ESSENTIAL = 7
DELUXE = 8
ULTIMATE = 9
XCA1 = 10
XCA2 = 11
XCA3 = 12
XCA5 = 13
BASICCOATINGMAINT = 14
PERFORMANCERECOATMAINT = 15
ULTRARECOATMAINT = 16
ORDER_TYPE = (
    (ACCESSORIES, _("Accessories")),
    (TINT, _("Tint")),
    (COATING, _("Coating")),
    (PPF, _("PPF")),
    (GIFT, _("Gift")),
    (MVP, _("MVP")),
    (ESSENTIAL, _("Essential")),
    (DELUXE, _("Deluxe")),
    (ULTIMATE, _("Ultimate")),
    (XCA1, _("XCA1")),
    (XCA2, _("XCA2")),
    (XCA3, _("XCA3")),
    (XCA5, _("XCA5")),
    (BASICCOATINGMAINT, _("Basic Coating Maintenance")),
    (PERFORMANCERECOATMAINT, _("Performance Coating Maintenance")),
    (ULTRARECOATMAINT, _("Ultra Coat Maintenance")),
)

# Tint, Coating, PPF
ALACARTE = 1
CONTINUELASTORDER = 2
PACKAGE = 3
ORDER_MODE = (
    (ALACARTE, _("Ala-carte")),
    (CONTINUELASTORDER, _("Continue Last Order")),
    (PACKAGE, _("Package")),
)

# Tint, Coating, PPF Package
TITAN = 1
BRONZE = 2
SILVER = 3
GOLD = 4
PLATINUM = 5
ROYAL = 6
ROYALPLUS = 7
ROYALPLUSSAFETY = 8
ELEMENTAL = 9
ECOBONZ9H = 10
CRYSTALLGLOSS9H = 11
MULTIQUARTZ9H = 12
AVANTGARDE = 13
KOSMOSI = 14
KOSMOSII = 15
KOSMOSIII = 16
KLEIO = 17
MORPHEUS = 18
MATTHIAS = 19
MAXIMUS = 20
PRODUCT_PACKAGE = (
    (TITAN, _("Titan")),
    (BRONZE, _("Bronze")),
    (SILVER, _("Silver")),
    (GOLD, _("Gold")),
    (PLATINUM, _("Platinum")),
    (ROYAL, _("Royal")),
    (ROYALPLUS, _("Royal Plus")),
    (ROYALPLUSSAFETY, _("Royal Plus Safety")),
    (ELEMENTAL, _("Elemental")),
    (ECOBONZ9H, _("Eco Bonz 9H")),
    (CRYSTALLGLOSS9H, _("Crystal Gloss 9H")),
    (MULTIQUARTZ9H, _("Multi Quartz 9H")),
    (AVANTGARDE, _("Avantgarde")),
    (KOSMOSI, _("Kosmos I")),
    (KOSMOSII, _("Kosmos II")),
    (KOSMOSIII, _("Komsos III")),
    (KLEIO, _("Kleio")),
    (MORPHEUS, _("Morpheus")),
    (MATTHIAS, _("Matthias")),
    (MAXIMUS, _("Maximus")),
)

# Items and Addons
# Gift Items
DOORVISOR = 1
COILMATB = 2
COILMATVIPRED = 3
COILMATVIPBLACK = 4
COILMATVIPGREY = 5
COILMAT3DRED = 6
COILMAT3DBLACK = 7
COILMAT3DGREY = 8
SANDBLASTING = 9
HEADLIGHTCOATINGLEFT = 10
HEADLIGHTCOATINGRIGHT = 11
HEADLIGHTPPFLEFT = 12
HEADLIGHTPPFRIGHT = 13
REARHEADLIGHTPPFLEFT = 14
REARHEADLIGHTPPFRIGHT = 15
DOORCUPLEFTONEGIFT = 16
DOORCUPLEFTTWOGIFT = 17
DOORCUPRIGHTONEGIFT = 18
DOORCUPRIGHTTWOGIFT = 19
TWOPCDOOREDGELEFT = 20
TWOPCDOOREDGERIGHT = 21
SIDEMIRRORLEFTGIFT = 22
SIDEMIRRORRIGHTGIFT = 23
BACTERIAODOREXTERMINATORGIFT = 24
WINDSCREENCOATINGGIFT = 25
FRONTPARTCOATING = 26
FULLCARWINDOWCOATING = 27
NORMALSUNVISOR = 28
PERFORMANCESUNVISOR = 29
OLDTINTREMOVAL = 30
DIYMAINTENANCEKIT = 31
PERFORMANCEMAINTENANCE = 32
REARCOILMATB = 33
REARBOOTEDGE = 34
REARBUMPEREDGE = 35
SIDESTEPLEFTONE = 36
SIDESTEPLEFTTWO = 37
SIDESTEPRIGHTONE = 38
SIDESTEPRIGHTTWO = 39
FUELCAPGIFT = 40
INTERIORSILICACOATING = 41
# Tint Items
CARBONFILM_BK50_2MIL = 42
CARBONFILM_BK70_2MIL = 43
CARBONFILM_BK80_2MIL = 44
CARBONFILM_BK90_2MIL = 45
SAFETYFILM_4MIL_CLEAR= 46
JASPER_2MIL = 47
TITANBLACK_2MIL = 48
CERAMIC_2MIL = 49
CERAMICBLACK_2MIL = 50
CERAMICBLACK_DK_2MIL = 51
PRONANO_2MIL = 52
NANOSHIELD_2MIL = 53
NANOSHIELD_DK_2MIL = 54
BLACKRAINBOW_SUPERCLEAR_3MIL = 55
BLACKRAINBOW_3MIL = 56
BLACKRAINBOW_DK_3MIL = 57
BLACKRAINBOW_DR_3MIL = 58
# Coating Items
SILICA_COATING = 59
ITEM_NAME = (
    (DOORVISOR, _("Door Visor")),
    (COILMATB, _("Coil Mat (B)")),
    (COILMATVIPRED, _("Coil Mat VIP (Red)")),
    (COILMATVIPBLACK, _("Coil Mat VIP (Black)")),
    (COILMATVIPGREY, _("Coil Mat VIP (Grey)")),
    (COILMAT3DRED, _("Coil Mat 3D (Red)")),
    (COILMAT3DBLACK, _("Coil Mat 3D (Black)")),
    (COILMAT3DGREY, _("Coil Mat 3D (Grey)")),
    (SANDBLASTING, _("Sand Blasting")),
    (HEADLIGHTCOATINGLEFT, _("Headlight Coating L")),
    (HEADLIGHTCOATINGRIGHT, _("Headlight Coating R")),
    (HEADLIGHTPPFLEFT, _("Headlight PPF L")),
    (HEADLIGHTPPFRIGHT, _("Headlight PPF R")),
    (REARHEADLIGHTPPFLEFT, _("Rear Headlight PPF L")),
    (REARHEADLIGHTPPFRIGHT, _("Rear Headlight PPF R")),
    (DOORCUPLEFTONEGIFT, _("Door Cup L1")),
    (DOORCUPLEFTTWOGIFT, _("Door Cup L2")),
    (DOORCUPRIGHTONEGIFT, _("Door Cup R1")),
    (DOORCUPRIGHTTWOGIFT, _("Door Cup R2")),
    (TWOPCDOOREDGELEFT, _("2pc Door Edge L")),
    (TWOPCDOOREDGERIGHT, _("2pc Door Edge R")),
    (SIDEMIRRORLEFTGIFT, _("Side Mirror L")),
    (SIDEMIRRORRIGHTGIFT, _("Side Mirror R")),
    (BACTERIAODOREXTERMINATORGIFT, _("Bacteria Odor Exterminator")),
    (WINDSCREENCOATINGGIFT, _("Windscreen Coating")),
    (FRONTPARTCOATING, _("Front Windscreen Coating and Driver Side Coating")),
    (FULLCARWINDOWCOATING, _("Full Car Window Coating")),
    (NORMALSUNVISOR, _("Normal Sunvisor")),
    (PERFORMANCESUNVISOR, _("Performance Sunvisor")),
    (OLDTINTREMOVAL, _("Old Tint Removal")),
    (DIYMAINTENANCEKIT, _("DIY Maintenance Kit")),
    (PERFORMANCEMAINTENANCE, _("1 Time Performance Maintenance")),
    (REARCOILMATB, _("Rear Coil Mat B")),
    (REARBOOTEDGE, _("Rear Boot Edge")),
    (REARBUMPEREDGE, _("Rear Bumper Edge")),
    (SIDESTEPLEFTONE, _("Side Step L1")),
    (SIDESTEPLEFTTWO, _("Side Step L2")),
    (SIDESTEPRIGHTONE, _("Side Step R1")),
    (SIDESTEPRIGHTTWO, _("Side Step R2")),
    (FUELCAPGIFT, _("Fuel Cap")),
    (INTERIORSILICACOATING, _("Interior Silica Coating")),
    (CARBONFILM_BK50_2MIL, _("Carbon Film - BK-50 2MIL")),
    (CARBONFILM_BK70_2MIL, _("Carbon Film - BK-70 2MIL")),
    (CARBONFILM_BK80_2MIL, _("Carbon Film - BK-80 2MIL")),
    (CARBONFILM_BK90_2MIL, _("Carbon Film - BK-90 2MIL")),
    (JASPER_2MIL, _("Jasper 2MIL")),
    (TITANBLACK_2MIL, _("Titan Black 2MIL")),
    (CERAMIC_2MIL, _("Ceramic 2MIL")),
    (CERAMICBLACK_2MIL, _("Ceramic Black 2MIL")),
    (CERAMICBLACK_DK_2MIL, _("Ceramic Black DK 2MIL")),
    (PRONANO_2MIL, _("PRO Nano 2MIL")),
    (NANOSHIELD_2MIL, _("Nano Shield 2MIL")),
    (NANOSHIELD_DK_2MIL, _("Nano Shield DK 2MIL")),
    (BLACKRAINBOW_SUPERCLEAR_3MIL, _("Black Rainbow (Super Clear) 3MIL")),
    (BLACKRAINBOW_3MIL, _("Black Rainbow 3MIL")),
    (BLACKRAINBOW_DK_3MIL, _("Black Rainbow DK 3MIL")),
    (BLACKRAINBOW_DR_3MIL, _("Black Rainbow DR 3MIL")),
    (SILICA_COATING, _("Silica Coating")),
)

"""
ADD-ON FILM
ADD_ON_FILM = (
    (CARBONFILM_BK50_2MIL, _("Carbon Film - BK-50 2MIL")),
    (CARBONFILM_BK70_2MIL, _("Carbon Film - BK-70 2MIL")),
    (CARBONFILM_BK80_2MIL, _("Carbon Film - BK-80 2MIL")),
    (CARBONFILM_BK90_2MIL, _("Carbon Film - BK-90 2MIL")),
)
"""

# Status - used on gifts
NIL = 0
ADD = 1
CHANGEFOC = 2
REMAIN = 3
SELLING = 4
UPGRADE = 5
PART_STATUS = (
    (NIL, _("NIL")),
    (ADD, _("ADD")),
    (CHANGEFOC, _("Change (FOC)")),
    (REMAIN, _("Remain")),
    (SELLING, _("Selling")),
    (UPGRADE, _("Upgrade")),
)

# Team
TEAM_A = 1
TEAM_B = 2
TEAM_C = 3
TEAM_COATING = 4
TEAM_TYPE = (
    (TEAM_A, _("Team A")),
    (TEAM_B, _("Team B")),
    (TEAM_C, _("Team C")),
    (TEAM_COATING, _("Coating Team")),
)

"""
# To Accessories
# This enum can technically be item_name also
DOORVISOR = 1
COILMATB = 2
COILMATVIPRED = 3
COILMATVIPBLACK = 4
COILMATVIPGREY = 5
COILMAT3DRED = 6
COILMAT3DBLACK = 7
COILMAT3DGREY = 8
SANDBLASTING = 9
ACCESSORIES = (
    (DOORVISOR, _("Door Visor")),
    (COILMATB, _("Coil Mat (B)")),
    (COILMATVIPRED, _("Coil Mat VIP (Red)")),
    (COILMATVIPBLACK, _("Coil Mat VIP (Black)")),
    (COILMATVIPGREY, _("Coil Mat VIP (Grey)")),
    (COILMAT3DRED, _("Coil Mat 3D (Red)")),
    (COILMAT3DBLACK, _("Coil Mat 3D (Black)")),
    (COILMAT3DGREY, _("Coil Mat 3D (Grey)")),
    (SANDBLASTING, _("Sand Blasting")),
)
"""

# Surcharge Types
NIL = 0
FOURXFOUR = 1
LUXURYSUPER = 2
MPV = 3
SUV = 4
SURCHARGE_VEHICLE_TYPE = (
    (NIL, _("NIL")),
    (FOURXFOUR, _("4X4")),
    (LUXURYSUPER, _("Luxury/Super")),
    (MPV, _("MPV")),
    (SUV, _("SUV")),
)

# Discount Types
FIVEPC = 1
SECONDCAR10PC = 2
REFERRALVOUCHER15PC = 3
OTHERS = 4
DISCOUNT_TYPE = (
    (FIVEPC, _("Discount 5%")),
    (SECONDCAR10PC, _("2nd Car Discount 10%")),
    (REFERRALVOUCHER15PC, _("Referral Voucher 15%")),
    (OTHERS, _("Others")),
)

# Part types
# Common Parts for Tint & Coating
FRONTWINDSCREEN = 1
REARWINDSCREEN = 2
# Common Parts for Coating & PPF
INTERIOR = 3
HEADLIGHTLEFT = 4
HEADLIGHTRIGHT = 5
# Tint Parts
CANOPYWINDOWLEFT = 6
CANOPYWINDOWRIGHT = 7
SIDEWINDOWLEFTONE = 8
SIDEWINDOWLEFTTWO = 9
SIDEWINDOWLEFTTHREE = 10
SIDEWINDOWRIGHTONE = 11
SIDEWINDOWRIGHTTWO = 12
SIDEWINDOWRIGHTTHREE = 13
SUNROOFONE = 14
SUNROOFTWO = 15
SUNVISOR = 16
# Coating Parts
BODYPAINT = 17
FRONTPART = 18
DOORLEFTONE = 19
DOORLEFTTWO = 20
PARTLEFTTHREE = 21
DOORRIGHTONE = 22
DOORRIGHTTWO = 23
PARTRIGHTTHREE = 24
ROOFTOP = 25
REARPART = 26
SPORTRIM = 27
WINDOWS = 28
# PPF Parts
DOORCUPLEFTONE = 29
DOORCUPLEFTTWO = 30
DOORCUPRIGHTONE = 31
DOORCUPRIGHTTWO = 32
DOOREDGELEFTONE = 33
DOOREDGELEFTTWO = 34
DOOREDGERIGHTONE = 35
DOOREDGERIGHTTWO = 36
FUELCAP = 37
FRONTFENDERLEFT = 38
FRONTFENDERRIGHT = 39
FRONTDOORLEFT = 40
FRONTDOORRIGHT = 41
FRONTFOGLAMP = 42
FRONTGRILLE = 43
PILLARANDREARFENDERLEFT = 44
PILLARANDREARFENDERRRIGHT = 45
REARHEADLIGHTLEFT = 46
REARHEADLIGHTRIGHT = 47
SKIRTINGLEFT = 48
SKIRTINGRIGHT = 49
REARBOOTEDGE = 50
REARBUMPER = 51
REARBUMPEREDGE = 52
REARBONNET = 53
REARDOORLEFT = 54
REARDOORRIGHT = 55
SIDEMIRRORLEFT = 56
SIDEMIRRORRIGHT = 57
SPOILER = 58
SIDESTEPLEFTONE = 59
SIDESTEPLEFTTWO = 60
SIDESTEPRIGHTONE = 61
SIDESTEPRIGHTTWO = 62
FREEGIFT = 63
FRONT_BUMPER = 64
FRONT_HOOD = 65

# Possible dupes
# HEADLIGHTCOATINGLEFT = 0
# HEADLIGHTCOATINGRIGHT = 0
# HEADLIGHTPOLISHLEFT = 0
# HEADLIGHTPOLISHRIGHT = 0
# SPORTRIMPOLISH = 28
# WINDOWCOATING = 28
# REMOVEWATERMARK = 0
# INTERIORPPF = 0
VEHICLE_PART = (
    (FRONTWINDSCREEN, _("Front Windscreen")),
    (REARWINDSCREEN, _("Rear Windscreen")),
    (INTERIOR, _("Interior")),
    (HEADLIGHTLEFT, _("Headlight L")),
    (HEADLIGHTRIGHT, _("Headlight R")),
    (CANOPYWINDOWLEFT, _("Canopy Window L")),
    (CANOPYWINDOWRIGHT, _("Canopy Window R")),
    (SIDEWINDOWLEFTONE, _("Side Window L1")),
    (SIDEWINDOWLEFTTWO, _("Side Window L2")),
    (SIDEWINDOWLEFTTHREE, _("Side Window L3")),
    (SIDEWINDOWRIGHTONE, _("Side Window R1")),
    (SIDEWINDOWRIGHTTWO, _("Side Window R2")),
    (SIDEWINDOWRIGHTTHREE, _("Side Window R3")),
    (SUNROOFONE, _("Sunroof 1")),
    (SUNROOFTWO, _("Sunroof 2")),
    (SUNVISOR, _("Sunvisor")),
    (BODYPAINT, _("Bodypaint")),
    (FRONTPART, _("Front Part")),
    (DOORLEFTONE, _("Door L1")),
    (DOORLEFTTWO, _("Door L2")),
    (PARTLEFTTHREE, _("Door L3")),
    (DOORRIGHTONE, _("Door R1")),
    (DOORRIGHTTWO, _("Door R2")),
    (PARTRIGHTTHREE, _("Door R3")),
    (ROOFTOP, _("Rooftop")),
    (REARPART, _("Rear Part")),
    (SPORTRIM, _("Sport Rim")),
    (WINDOWS, _("Windows")),
    (DOORCUPLEFTONE, _("Door Cup L1")),
    (DOORCUPLEFTTWO, _("Door Cup L2")),
    (DOORCUPRIGHTONE, _("Door Cup R1")),
    (DOORCUPRIGHTTWO, _("Door Cup R2")),
    (DOOREDGELEFTONE, _("Door Edge L1")),
    (DOOREDGELEFTTWO, _("Door Edge L2")),
    (DOOREDGERIGHTONE, _("Door Edge R1")),
    (DOOREDGERIGHTTWO, _("Door Edge R2")),
    (FUELCAP, _("Fuel Cap")),
    (FRONTFENDERLEFT, _("Front Fender L")),
    (FRONTFENDERRIGHT, _("Front Fender R")),
    (FRONTDOORLEFT, _("Front Door L")),
    (FRONTDOORRIGHT, _("Front Door R")),
    (FRONTFOGLAMP, _("Front Foglamp")),
    (FRONTGRILLE, _("Front Grille")),
    (PILLARANDREARFENDERLEFT, _("Pillar and Rear Fender L")),
    (PILLARANDREARFENDERRRIGHT, _("Pillar and Rear Fender R")),
    (REARHEADLIGHTLEFT, _("Rear Headlight L")),
    (REARHEADLIGHTRIGHT, _("Rear Headlight R")),
    (SKIRTINGLEFT, _("Skirting L")),
    (SKIRTINGRIGHT, _("Skirting R")),
    (REARBOOTEDGE, _("Rear Boot Edge")),
    (REARBUMPER, _("Rear Bumper")),
    (REARBUMPEREDGE, _("Rear Bumper Edge")),
    (REARBONNET, _("Rear Bonnet")),
    (REARDOORLEFT, _("Rear Door L")),
    (REARDOORRIGHT, _("Rear Door R")),
    (SIDEMIRRORLEFT, _("Side Mirror L")),
    (SIDEMIRRORRIGHT, _("Side Mirror R")),
    (SPOILER, _("Spoiler")),
    (SIDESTEPLEFTONE, _("Side Step L1")),
    (SIDESTEPLEFTTWO, _("Side Step L2")),
    (SIDESTEPRIGHTONE, _("Side Step R1")),
    (SIDESTEPRIGHTTWO, _("Side Step R2")),
    (FREEGIFT, _("Gift")),
    (FRONT_BUMPER, _("Front Bumper")),
    (FRONT_HOOD, _("Front Hood")),
)

# Job types
DO_NOW = 1
PENDING = 2
INSTALL = 3
REMOVE_OLD = 4
JOB_TYPE = (
    (DO_NOW, _("Do It Now")),
    (PENDING, _("Pending")),
    (INSTALL, _("Install")),
    (REMOVE_OLD, _("Remove Old")),
)
