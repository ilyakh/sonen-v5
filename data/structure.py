# -*- coding: utf-8 -*-

class Category:
    def __init__( self, name, priority=1.0 ):
        self.name = name
        self.priority = priority


class Entry:
    def __init__( self, title, category_names=None ):
        self.title = title
        self.categories = category_names

    def set_categories( self, category_names ):
        self.categories = category_names


    def __str__( self ):
        return "[Entry: \"{title}\"] -> ({categories})".format(title=self.title, categories=self.categories)


class Categories:

    def __init__( self ):
        self.categories = {}

    def __setitem__( self, key, value ):
        self.categories[key] = value

    def __getitem__( self, category_name ):
        self( category_name )

    def __call__( self, category_name ):
        return self.categories.get( category_name )



class Entries:
    def __init__( self ):
        self.entries = []

    def __lt__( self, entry ):
        self.entries.append( entry )

    def __iter__( self ):
        return self.entries.__iter__()

    def __len__( self ):
        return len( self.entries )

    def create_in_categories( self, category_names, *args ):
        if len(args):
            for entry in args:
                entry.set_categories( category_names )
                self.entries.append( entry )

class E(Entry):
    pass

class C(Category):
    pass


if __name__ == "__main__":

    categories = Categories()

    category_definitions = [
        ( "prosjekter",                 0.625 ),
        ( "utviklingsplaformer",        0.625 ),
        ( "funksjonelle områder",       0.625 ),
        ( "arrangementer",              0.625 ),
        ( "instrumenter/verktøy",       0.625 ),

        ( "programvare",                0.250 ),
        ( "samarbeidspartnere",         0.250 ),
        ( "foredragsholdere",           0.250 ),
        ( "severdigheter",              0.250 ),

        ( "medlemmer",                  0.125 ),
        ( "prosjektideer",              0.125 ),
        ( "materialer",                 0.125 ),
        ( "spesielle komponenter",      0.125 )
    ]


    print "Number of categories: ", len( category_definitions )


    for name, priority in category_definitions:
        categories[name] = C(name, priority)

    entries = Entries()

    entries.create_in_categories(

        ['prosjektideer'],

        E(
            'OpenRC'
        ),

        E(
            'Husroboten'
        ),

        E(
            'Gigakaeder'
        ),

        E(
            'Gear train'
        ),

    )


    entries.create_in_categories(

        ['funksjonelle områder'],

        E(
            'Loddestasjon'
        ),

        E(
            'Wiki'
        ),

        E(
            'Blader, papers og bøker'
        ),

        E(
            'Sofahjørnet'
        ),

        E(
            'Roteboksen'
        ),

        E(
            'Utstilling'
        ),

    )

    entries.create_in_categories(

        ['programvare'],

        E(
            'Arduino'
        ),

        E(
            'Illustrator/Adobe Creative Suite'
        ),

        E(
            'Processing'
        ),

        E(
            'Android'
        ),

        E(
            'FinalCut Pro'
        ),

        E(
            'NetLogo'
        ),

    )


    entries.create_in_categories(

        ['medlemmer'],

        E(
            'Ilya Kostolomov'
        ),

        E(
            'Bao Marianna Nguyen'
        ),

        E(
            'Persijn D. Kwekkeboom'
        ),

        E(
            'Srod Karim'
        ),

        E(
            'Fredrik Hov'
        ),

        E(
            'Asgeir Mortensen'
        ),

        E(
            'Jan Ole Skotterud'
        ),

        E(
            'Fredrik Hov'
        ),

    )

    entries.create_in_categories(

        ['medlemmer', 'foredragsholdere'],

        E(
            'Kyrre Havik Eriksen'
        ),

        E(
            'Sigmund Hansen'
        ),

        E(
            'Veronika Heimsbak'
        ),

        E(
            'Jonathan Ringstad'
        ),

        E(
            'Roger Antonsen'
        ),

    )




    entries.create_in_categories(

        ['foredragsholdere'],

        E(
            'Tom Igoe'
        ),

    )



    entries.create_in_categories(

        ['prosjekter'],

        E(
            'Den fullstendige maskinen'
        ),

        E(
            'Krydderino'
        ),

        E(
            'Pink Ardubot'
        ),

        E(
            'Babybot'
        ),

        E(
            'B.L.I.M.P.'
        ),

    )


    entries.create_in_categories(

        ['prosjekter', 'utviklingsplatformer'],

        E(
            'Arkademaskina'
        ),

        E(
            'Game of Light'
        ),

        E(
            'Turtlebot'
        ),

    )


    entries.create_in_categories(

        ['utviklingsplatformer'],

        E(
            'Pleo'
        ),

        E(
            'Quadcopter'
        ),

        E(
            'E-puck'
        ),

        E(
            'DFRobot / Thinkee Winkee'
        ),

        E(
            'Commodore64'
        ),

        E(
            'Energy Micro'
        ),

        E(
            'Arduino'
        ),

        E(
            'Raspberry Pi'
        ),

        E(
            'Fignition'
        ),

        E(
            'Gameduino'
        ),

        E(
            'Diverse robotplatformer'
        ),

        E(
            'Emotiv'
        ),

        E(
            'Infoskjerm'
        ),

    )


    entries.create_in_categories(

        ['instrumenter/verktøy'],

        E(
            'Weller WD-1'
        ),

        E(
            'Rigol 1102A'
        ),

        E(
            'Ultimaker'
        ),

        E(
            'Makerbot'
        ),

        E(
            'Printrbot'
        ),

        E(
            'Plastknekker'
        ),

        E(
            'Foto- og videoutstyr'
        ),

        E(
            'GoPro'
        ),

        E(
            'Lydutstyr'
        ),

    )


    entries.create_in_categories(

        ['materialer'],

        E(
            'Tøy'
        ),

        E(
            'MakerBeam'
        ),

        E(
            'Mecano'
        ),

        E(
            'Plast'
        ),

        E(
            'Generiske El-komponenter'
        ),

        E(
            'PCB/stripeboards'
        ),

    )


    entries.create_in_categories(

        ['samarbeidspartnere'],

        E(
            'Robotica Osloensis'
        ),

        E(
            'Statoil'
        ),

        E(
            'The Gathering'
        ),

        E(
            'Lær kidsa kode'
        ),

        E(
            'Teknisk museum'
        ),

        E(
            'Telemuseet'
        ),

    )


    entries.create_in_categories(

        ['severdigheter'],

        E(
            'Eggbot'
        ),

        E(
            'Rubiks kube'
        ),

        E(
            'Singularity Chess'
        ),

        E(
            'LittleBits'
        ),

        E(
            'Romo'
        ),

        E(
            'Sifteo'
        ),

        E(
            'Zome'
        ),

    )

    entries.create_in_categories(

        ['spesielle komponenter'],

        E(
            'Sensorer'
        ),

        E(
            'Motorer/aktuatorer'
        ),

        E(
            'Batterier'
        ),

    )

    entries.create_in_categories(

        ['arrangementer'],

        E(
            'GameJam'
        ),

        E(
            'Campus TG'
        ),

    )

    print "Number of entries: ", len( entries )


    for e in entries:
        print e