"""
Retrieved from
https://en.wikipedia.org/wiki/List_of_municipalities_in_New_Jersey using Chrome
developer tools.
"""

counties = ('Atlantic',
            'Bergen',
            'Burlington',
            'Camden',
            'Cape May',
            'Cumberland',
            'Essex',
            'Gloucester',
            'Hudson',
            'Hunterdon',
            'Mercer',
            'Middlesex',
            'Monmouth',
            'Morris',
            'Ocean',
            'Passaic',
            'Salem',
            'Somerset',
            'Sussex',
            'Union',
            'Warren',)

municipalities = (('Absecon', 'Atlantic'),
                  ('Atlantic City', 'Atlantic'),
                  ('Brigantine', 'Atlantic'),
                  ('Buena', 'Atlantic'),
                  ('Buena Vista Township', 'Atlantic'),
                  ('Corbin City', 'Atlantic'),
                  ('Egg Harbor City', 'Atlantic'),
                  ('Egg Harbor Township', 'Atlantic'),
                  ('Estell Manor', 'Atlantic'),
                  ('Folsom', 'Atlantic'),
                  ('Galloway Township', 'Atlantic'),
                  ('Hamilton Township (2)', 'Atlantic'),
                  ('Hammonton', 'Atlantic'),
                  ('Linwood', 'Atlantic'),
                  ('Longport', 'Atlantic'),
                  ('Margate City', 'Atlantic'),
                  ('Mullica Township', 'Atlantic'),
                  ('Northfield', 'Atlantic'),
                  ('Pleasantville', 'Atlantic'),
                  ('Port Republic', 'Atlantic'),
                  ('Somers Point', 'Atlantic'),
                  ('Ventnor City', 'Atlantic'),
                  ('Weymouth Township', 'Atlantic'),
                  ('Allendale', 'Bergen'),
                  ('Alpine', 'Bergen'),
                  ('Bergenfield', 'Bergen'),
                  ('Bogota', 'Bergen'),
                  ('Carlstadt', 'Bergen'),
                  ('Cliffside Park', 'Bergen'),
                  ('Closter', 'Bergen'),
                  ('Cresskill', 'Bergen'),
                  ('Demarest', 'Bergen'),
                  ('Dumont', 'Bergen'),
                  ('East Rutherford', 'Bergen'),
                  ('Edgewater', 'Bergen'),
                  ('Elmwood Park', 'Bergen'),
                  ('Emerson', 'Bergen'),
                  ('Englewood', 'Bergen'),
                  ('Englewood Cliffs', 'Bergen'),
                  ('Fair Lawn', 'Bergen'),
                  ('Fairview', 'Bergen'),
                  ('Fort Lee', 'Bergen'),
                  ('Franklin Lakes', 'Bergen'),
                  ('Garfield', 'Bergen'),
                  ('Glen Rock', 'Bergen'),
                  ('Hackensack', 'Bergen'),
                  ('Harrington Park', 'Bergen'),
                  ('Hasbrouck Heights', 'Bergen'),
                  ('Haworth', 'Bergen'),
                  ('Hillsdale', 'Bergen'),
                  ('Ho-Ho-Kus', 'Bergen'),
                  ('Leonia', 'Bergen'),
                  ('Little Ferry', 'Bergen'),
                  ('Lodi', 'Bergen'),
                  ('Lyndhurst', 'Bergen'),
                  ('Mahwah', 'Bergen'),
                  ('Maywood', 'Bergen'),
                  ('Midland Park', 'Bergen'),
                  ('Montvale', 'Bergen'),
                  ('Moonachie', 'Bergen'),
                  ('New Milford', 'Bergen'),
                  ('North Arlington', 'Bergen'),
                  ('Northvale', 'Bergen'),
                  ('Norwood', 'Bergen'),
                  ('Oakland', 'Bergen'),
                  ('Old Tappan', 'Bergen'),
                  ('Oradell', 'Bergen'),
                  ('Palisades Park', 'Bergen'),
                  ('Paramus', 'Bergen'),
                  ('Park Ridge', 'Bergen'),
                  ('Ramsey', 'Bergen'),
                  ('Ridgefield', 'Bergen'),
                  ('Ridgefield Park', 'Bergen'),
                  ('Ridgewood', 'Bergen'),
                  ('River Edge', 'Bergen'),
                  ('River Vale', 'Bergen'),
                  ('Rochelle Park', 'Bergen'),
                  ('Rockleigh', 'Bergen'),
                  ('Rutherford', 'Bergen'),
                  ('Saddle Brook', 'Bergen'),
                  ('Saddle River', 'Bergen'),
                  ('South Hackensack', 'Bergen'),
                  ('Teaneck', 'Bergen'),
                  ('Tenafly', 'Bergen'),
                  ('Teterboro', 'Bergen'),
                  ('Upper Saddle River', 'Bergen'),
                  ('Waldwick', 'Bergen'),
                  ('Wallington', 'Bergen'),
                  ('Washington Township (1)', 'Bergen'),
                  ('Westwood', 'Bergen'),
                  ('Wood-Ridge', 'Bergen'),
                  ('Woodcliff Lake', 'Bergen'),
                  ('Wyckoff', 'Bergen'),
                  ('Bass River Township', 'Burlington'),
                  ('Beverly', 'Burlington'),
                  ('Bordentown', 'Burlington'),
                  ('Bordentown Township', 'Burlington'),
                  ('Burlington', 'Burlington'),
                  ('Burlington Township', 'Burlington'),
                  ('Chesterfield Township', 'Burlington'),
                  ('Cinnaminson Township', 'Burlington'),
                  ('Delanco Township', 'Burlington'),
                  ('Delran Township', 'Burlington'),
                  ('Eastampton Township', 'Burlington'),
                  ('Edgewater Park', 'Burlington'),
                  ('Evesham Township', 'Burlington'),
                  ('Fieldsboro', 'Burlington'),
                  ('Florence Township', 'Burlington'),
                  ('Hainesport Township', 'Burlington'),
                  ('Lumberton Township', 'Burlington'),
                  ('Mansfield Township (2)', 'Burlington'),
                  ('Maple Shade Township', 'Burlington'),
                  ('Medford', 'Burlington'),
                  ('Medford Lakes', 'Burlington'),
                  ('Moorestown', 'Burlington'),
                  ('Mount Holly', 'Burlington'),
                  ('Mount Laurel', 'Burlington'),
                  ('New Hanover Township', 'Burlington'),
                  ('North Hanover Township', 'Burlington'),
                  ('Palmyra', 'Burlington'),
                  ('Pemberton', 'Burlington'),
                  ('Pemberton Township', 'Burlington'),
                  ('Riverside Township', 'Burlington'),
                  ('Riverton', 'Burlington'),
                  ('Shamong Township', 'Burlington'),
                  ('Southampton Township', 'Burlington'),
                  ('Springfield Township (2)', 'Burlington'),
                  ('Tabernacle Township', 'Burlington'),
                  ('Washington Township (5)', 'Burlington'),
                  ('Westampton Township', 'Burlington'),
                  ('Willingboro Township', 'Burlington'),
                  ('Woodland Township', 'Burlington'),
                  ('Wrightstown', 'Burlington'),
                  ('Audubon', 'Camden'),
                  ('Audubon Park', 'Camden'),
                  ('Barrington', 'Camden'),
                  ('Bellmawr', 'Camden'),
                  ('Berlin', 'Camden'),
                  ('Berlin Township', 'Camden'),
                  ('Brooklawn', 'Camden'),
                  ('Camden', 'Camden'),
                  ('Cherry Hill', 'Camden'),
                  ('Chesilhurst', 'Camden'),
                  ('Clementon', 'Camden'),
                  ('Collingswood', 'Camden'),
                  ('Gibbsboro', 'Camden'),
                  ('Gloucester City', 'Camden'),
                  ('Gloucester Township', 'Camden'),
                  ('Haddon Heights', 'Camden'),
                  ('Haddon Township', 'Camden'),
                  ('Haddonfield', 'Camden'),
                  ('Hi-Nella', 'Camden'),
                  ('Laurel Springs', 'Camden'),
                  ('Lawnside', 'Camden'),
                  ('Lindenwold', 'Camden'),
                  ('Magnolia', 'Camden'),
                  ('Merchantville', 'Camden'),
                  ('Mount Ephraim', 'Camden'),
                  ('Oaklyn', 'Camden'),
                  ('Pennsauken Township', 'Camden'),
                  ('Pine Hill', 'Camden'),
                  ('Pine Valley', 'Camden'),
                  ('Runnemede', 'Camden'),
                  ('Somerdale', 'Camden'),
                  ('Stratford', 'Camden'),
                  ('Tavistock', 'Camden'),
                  ('Voorhees Township', 'Camden'),
                  ('Waterford Township', 'Camden'),
                  ('Winslow Township', 'Camden'),
                  ('Woodlynne', 'Camden'),
                  ('Avalon', 'Cape May'),
                  ('Cape May', 'Cape May'),
                  ('Cape May Point', 'Cape May'),
                  ('Dennis Township', 'Cape May'),
                  ('Lower Township', 'Cape May'),
                  ('Middle Township', 'Cape May'),
                  ('North Wildwood', 'Cape May'),
                  ('Ocean City', 'Cape May'),
                  ('Sea Isle City', 'Cape May'),
                  ('Stone Harbor', 'Cape May'),
                  ('Upper Township', 'Cape May'),
                  ('West Cape May', 'Cape May'),
                  ('West Wildwood', 'Cape May'),
                  ('Wildwood', 'Cape May'),
                  ('Wildwood Crest', 'Cape May'),
                  ('Woodbine', 'Cape May'),
                  ('Bridgeton', 'Cumberland'),
                  ('Commercial Township', 'Cumberland'),
                  ('Deerfield Township', 'Cumberland'),
                  ('Downe Township', 'Cumberland'),
                  ('Fairfield Township (2)', 'Cumberland'),
                  ('Greenwich Township (3)', 'Cumberland'),
                  ('Hopewell Township (2)', 'Cumberland'),
                  ('Lawrence Township (2)', 'Cumberland'),
                  ('Maurice River Township', 'Cumberland'),
                  ('Millville', 'Cumberland'),
                  ('Shiloh', 'Cumberland'),
                  ('Stow Creek Township', 'Cumberland'),
                  ('Upper Deerfield Township', 'Cumberland'),
                  ('Vineland', 'Cumberland'),
                  ('Belleville', 'Essex'),
                  ('Bloomfield', 'Essex'),
                  ('Caldwell', 'Essex'),
                  ('Cedar Grove', 'Essex'),
                  ('City of Orange', 'Essex'),
                  ('East Orange', 'Essex'),
                  ('Essex Fells', 'Essex'),
                  ('Fairfield Township (1)', 'Essex'),
                  ('Glen Ridge', 'Essex'),
                  ('Irvington', 'Essex'),
                  ('Livingston', 'Essex'),
                  ('Maplewood', 'Essex'),
                  ('Millburn', 'Essex'),
                  ('Montclair', 'Essex'),
                  ('Newark', 'Essex'),
                  ('North Caldwell', 'Essex'),
                  ('Nutley', 'Essex'),
                  ('Roseland', 'Essex'),
                  ('South Orange Village', 'Essex'),
                  ('Verona', 'Essex'),
                  ('West Caldwell', 'Essex'),
                  ('West Orange', 'Essex'),
                  ('Clayton', 'Gloucester'),
                  ('Deptford Township', 'Gloucester'),
                  ('East Greenwich Township', 'Gloucester'),
                  ('Elk Township', 'Gloucester'),
                  ('Franklin Township (4)', 'Gloucester'),
                  ('Glassboro', 'Gloucester'),
                  ('Greenwich Township (2)', 'Gloucester'),
                  ('Harrison Township', 'Gloucester'),
                  ('Logan Township', 'Gloucester'),
                  ('Mantua Township', 'Gloucester'),
                  ('Monroe Township (2)', 'Gloucester'),
                  ('National Park', 'Gloucester'),
                  ('Newfield', 'Gloucester'),
                  ('Paulsboro', 'Gloucester'),
                  ('Pitman', 'Gloucester'),
                  ('South Harrison Township', 'Gloucester'),
                  ('Swedesboro', 'Gloucester'),
                  ('Washington Township (4)', 'Gloucester'),
                  ('Wenonah', 'Gloucester'),
                  ('West Deptford Township', 'Gloucester'),
                  ('Westville', 'Gloucester'),
                  ('Woodbury', 'Gloucester'),
                  ('Woodbury Heights', 'Gloucester'),
                  ('Woolwich Township', 'Gloucester'),
                  ('Bayonne', 'Hudson'),
                  ('East Newark', 'Hudson'),
                  ('Guttenberg', 'Hudson'),
                  ('Harrison', 'Hudson'),
                  ('Hoboken', 'Hudson'),
                  ('Jersey City', 'Hudson'),
                  ('Kearny', 'Hudson'),
                  ('North Bergen', 'Hudson'),
                  ('Secaucus', 'Hudson'),
                  ('Union City', 'Hudson'),
                  ('Weehawken', 'Hudson'),
                  ('West New York', 'Hudson'),
                  ('Alexandria Township', 'Hunterdon'),
                  ('Bethlehem Township', 'Hunterdon'),
                  ('Bloomsbury', 'Hunterdon'),
                  ('Califon', 'Hunterdon'),
                  ('Clinton', 'Hunterdon'),
                  ('Clinton Township', 'Hunterdon'),
                  ('Delaware Township', 'Hunterdon'),
                  ('East Amwell Township', 'Hunterdon'),
                  ('Flemington', 'Hunterdon'),
                  ('Franklin Township (2)', 'Hunterdon'),
                  ('Frenchtown', 'Hunterdon'),
                  ('Glen Gardner', 'Hunterdon'),
                  ('Hampton', 'Hunterdon'),
                  ('High Bridge', 'Hunterdon'),
                  ('Holland Township', 'Hunterdon'),
                  ('Kingwood Township', 'Hunterdon'),
                  ('Lambertville', 'Hunterdon'),
                  ('Lebanon', 'Hunterdon'),
                  ('Lebanon Township', 'Hunterdon'),
                  ('Milford', 'Hunterdon'),
                  ('Raritan Township', 'Hunterdon'),
                  ('Readington Township', 'Hunterdon'),
                  ('Stockton', 'Hunterdon'),
                  ('Tewksbury Township', 'Hunterdon'),
                  ('Union Township (2)', 'Hunterdon'),
                  ('West Amwell Township', 'Hunterdon'),
                  ('East Windsor Township', 'Mercer'),
                  ('Ewing Township', 'Mercer'),
                  ('Hamilton Township (1)', 'Mercer'),
                  ('Hightstown', 'Mercer'),
                  ('Hopewell', 'Mercer'),
                  ('Hopewell Township (1)', 'Mercer'),
                  ('Lawrence Township (1)', 'Mercer'),
                  ('Pennington', 'Mercer'),
                  ('Princeton', 'Mercer'),
                  ('Robbinsville Township', 'Mercer'),
                  ('Trenton', 'Mercer'),
                  ('West Windsor Township', 'Mercer'),
                  ('Carteret', 'Middlesex'),
                  ('Cranbury', 'Middlesex'),
                  ('Dunellen', 'Middlesex'),
                  ('East Brunswick', 'Middlesex'),
                  ('Edison', 'Middlesex'),
                  ('Helmetta', 'Middlesex'),
                  ('Highland Park', 'Middlesex'),
                  ('Jamesburg', 'Middlesex'),
                  ('Metuchen', 'Middlesex'),
                  ('Middlesex', 'Middlesex'),
                  ('Milltown', 'Middlesex'),
                  ('Monroe Township (1)', 'Middlesex'),
                  ('New Brunswick', 'Middlesex'),
                  ('North Brunswick', 'Middlesex'),
                  ('Old Bridge Township', 'Middlesex'),
                  ('Perth Amboy', 'Middlesex'),
                  ('Piscataway', 'Middlesex'),
                  ('Plainsboro Township', 'Middlesex'),
                  ('Sayreville', 'Middlesex'),
                  ('South Amboy', 'Middlesex'),
                  ('South Brunswick', 'Middlesex'),
                  ('South Plainfield', 'Middlesex'),
                  ('South River', 'Middlesex'),
                  ('Spotswood', 'Middlesex'),
                  ('Woodbridge Township', 'Middlesex'),
                  ('Aberdeen Township', 'Monmouth'),
                  ('Allenhurst', 'Monmouth'),
                  ('Allentown', 'Monmouth'),
                  ('Asbury Park', 'Monmouth'),
                  ('Atlantic Highlands', 'Monmouth'),
                  ('Avon-by-the-Sea', 'Monmouth'),
                  ('Belmar', 'Monmouth'),
                  ('Bradley Beach', 'Monmouth'),
                  ('Brielle', 'Monmouth'),
                  ('Colts Neck Township', 'Monmouth'),
                  ('Deal', 'Monmouth'),
                  ('Eatontown', 'Monmouth'),
                  ('Englishtown', 'Monmouth'),
                  ('Fair Haven', 'Monmouth'),
                  ('Farmingdale', 'Monmouth'),
                  ('Freehold Borough', 'Monmouth'),
                  ('Freehold Township', 'Monmouth'),
                  ('Hazlet', 'Monmouth'),
                  ('Highlands', 'Monmouth'),
                  ('Holmdel Township', 'Monmouth'),
                  ('Howell Township', 'Monmouth'),
                  ('Interlaken', 'Monmouth'),
                  ('Keansburg', 'Monmouth'),
                  ('Keyport', 'Monmouth'),
                  ('Lake Como', 'Monmouth'),
                  ('Little Silver', 'Monmouth'),
                  ('Loch Arbour', 'Monmouth'),
                  ('Long Branch', 'Monmouth'),
                  ('Manalapan Township', 'Monmouth'),
                  ('Manasquan', 'Monmouth'),
                  ('Marlboro Township', 'Monmouth'),
                  ('Matawan', 'Monmouth'),
                  ('Middletown Township', 'Monmouth'),
                  ('Millstone Township', 'Monmouth'),
                  ('Monmouth Beach', 'Monmouth'),
                  ('Neptune City', 'Monmouth'),
                  ('Neptune Township', 'Monmouth'),
                  ('Ocean Township (1)', 'Monmouth'),
                  ('Oceanport', 'Monmouth'),
                  ('Red Bank', 'Monmouth'),
                  ('Roosevelt', 'Monmouth'),
                  ('Rumson', 'Monmouth'),
                  ('Sea Bright', 'Monmouth'),
                  ('Sea Girt', 'Monmouth'),
                  ('Shrewsbury', 'Monmouth'),
                  ('Shrewsbury Township', 'Monmouth'),
                  ('Spring Lake', 'Monmouth'),
                  ('Spring Lake Heights', 'Monmouth'),
                  ('Tinton Falls', 'Monmouth'),
                  ('Union Beach', 'Monmouth'),
                  ('Upper Freehold Township', 'Monmouth'),
                  ('Wall Township', 'Monmouth'),
                  ('West Long Branch', 'Monmouth'),
                  ('Boonton', 'Morris'),
                  ('Boonton Township', 'Morris'),
                  ('Butler', 'Morris'),
                  ('Chatham Borough', 'Morris'),
                  ('Chatham Township', 'Morris'),
                  ('Chester Borough', 'Morris'),
                  ('Chester Township', 'Morris'),
                  ('Denville Township', 'Morris'),
                  ('Dover', 'Morris'),
                  ('East Hanover Township', 'Morris'),
                  ('Florham Park', 'Morris'),
                  ('Hanover Township', 'Morris'),
                  ('Harding Township', 'Morris'),
                  ('Jefferson Township', 'Morris'),
                  ('Kinnelon', 'Morris'),
                  ('Lincoln Park', 'Morris'),
                  ('Long Hill Township', 'Morris'),
                  ('Madison', 'Morris'),
                  ('Mendham Borough', 'Morris'),
                  ('Mendham Township', 'Morris'),
                  ('Mine Hill Township', 'Morris'),
                  ('Montville', 'Morris'),
                  ('Morris Plains', 'Morris'),
                  ('Morris Township', 'Morris'),
                  ('Morristown', 'Morris'),
                  ('Mount Arlington', 'Morris'),
                  ('Mount Olive Township', 'Morris'),
                  ('Mountain Lakes', 'Morris'),
                  ('Netcong', 'Morris'),
                  ('Parsippany-Troy Hills', 'Morris'),
                  ('Pequannock Township', 'Morris'),
                  ('Randolph', 'Morris'),
                  ('Riverdale', 'Morris'),
                  ('Rockaway', 'Morris'),
                  ('Rockaway Township', 'Morris'),
                  ('Roxbury Township', 'Morris'),
                  ('Victory Gardens', 'Morris'),
                  ('Washington Township (2)', 'Morris'),
                  ('Wharton', 'Morris'),
                  ('Barnegat Light', 'Ocean'),
                  ('Barnegat Township', 'Ocean'),
                  ('Bay Head', 'Ocean'),
                  ('Beach Haven', 'Ocean'),
                  ('Beachwood', 'Ocean'),
                  ('Berkeley Township', 'Ocean'),
                  ('Brick Township', 'Ocean'),
                  ('Eagleswood Township', 'Ocean'),
                  ('Harvey Cedars', 'Ocean'),
                  ('Island Heights', 'Ocean'),
                  ('Jackson Township', 'Ocean'),
                  ('Lacey Township', 'Ocean'),
                  ('Lakehurst', 'Ocean'),
                  ('Lakewood Township', 'Ocean'),
                  ('Lavallette', 'Ocean'),
                  ('Little Egg Harbor Township', 'Ocean'),
                  ('Long Beach Township', 'Ocean'),
                  ('Manchester Township', 'Ocean'),
                  ('Mantoloking', 'Ocean'),
                  ('Ocean Gate', 'Ocean'),
                  ('Ocean Township (2)', 'Ocean'),
                  ('Pine Beach', 'Ocean'),
                  ('Plumsted Township', 'Ocean'),
                  ('Point Pleasant', 'Ocean'),
                  ('Point Pleasant Beach', 'Ocean'),
                  ('Seaside Heights', 'Ocean'),
                  ('Seaside Park', 'Ocean'),
                  ('Ship Bottom', 'Ocean'),
                  ('South Toms River', 'Ocean'),
                  ('Stafford Township', 'Ocean'),
                  ('Surf City', 'Ocean'),
                  ('Toms River', 'Ocean'),
                  ('Tuckerton', 'Ocean'),
                  ('Bloomingdale', 'Passaic'),
                  ('Clifton', 'Passaic'),
                  ('Haledon', 'Passaic'),
                  ('Hawthorne', 'Passaic'),
                  ('Little Falls', 'Passaic'),
                  ('North Haledon', 'Passaic'),
                  ('Passaic', 'Passaic'),
                  ('Paterson', 'Passaic'),
                  ('Pompton Lakes', 'Passaic'),
                  ('Prospect Park', 'Passaic'),
                  ('Ringwood', 'Passaic'),
                  ('Totowa', 'Passaic'),
                  ('Wanaque', 'Passaic'),
                  ('Wayne', 'Passaic'),
                  ('West Milford', 'Passaic'),
                  ('Woodland Park', 'Passaic'),
                  ('Alloway Township', 'Salem'),
                  ('Carneys Point Township', 'Salem'),
                  ('Elmer', 'Salem'),
                  ('Elsinboro Township', 'Salem'),
                  ('Lower Alloways Creek Township', 'Salem'),
                  ('Mannington Township', 'Salem'),
                  ('Oldmans Township', 'Salem'),
                  ('Penns Grove', 'Salem'),
                  ('Pennsville Township', 'Salem'),
                  ('Pilesgrove Township', 'Salem'),
                  ('Pittsgrove Township', 'Salem'),
                  ('Quinton Township', 'Salem'),
                  ('Salem', 'Salem'),
                  ('Upper Pittsgrove Township', 'Salem'),
                  ('Woodstown', 'Salem'),
                  ('Bedminster', 'Somerset'),
                  ('Bernards Township', 'Somerset'),
                  ('Bernardsville', 'Somerset'),
                  ('Bound Brook', 'Somerset'),
                  ('Branchburg', 'Somerset'),
                  ('Bridgewater Township', 'Somerset'),
                  ('Far Hills', 'Somerset'),
                  ('Franklin Township (3)', 'Somerset'),
                  ('Green Brook Township', 'Somerset'),
                  ('Hillsborough Township', 'Somerset'),
                  ('Manville', 'Somerset'),
                  ('Millstone', 'Somerset'),
                  ('Montgomery', 'Somerset'),
                  ('North Plainfield', 'Somerset'),
                  ('Peapack and Gladstone', 'Somerset'),
                  ('Raritan', 'Somerset'),
                  ('Rocky Hill', 'Somerset'),
                  ('Somerville', 'Somerset'),
                  ('South Bound Brook', 'Somerset'),
                  ('Warren Township', 'Somerset'),
                  ('Watchung', 'Somerset'),
                  ('Andover', 'Sussex'),
                  ('Andover Township', 'Sussex'),
                  ('Branchville', 'Sussex'),
                  ('Byram Township', 'Sussex'),
                  ('Frankford Township', 'Sussex'),
                  ('Franklin', 'Sussex'),
                  ('Fredon Township', 'Sussex'),
                  ('Green Township', 'Sussex'),
                  ('Hamburg', 'Sussex'),
                  ('Hampton Township', 'Sussex'),
                  ('Hardyston Township', 'Sussex'),
                  ('Hopatcong', 'Sussex'),
                  ('Lafayette Township', 'Sussex'),
                  ('Montague Township', 'Sussex'),
                  ('Newton', 'Sussex'),
                  ('Ogdensburg', 'Sussex'),
                  ('Sandyston Township', 'Sussex'),
                  ('Sparta Township', 'Sussex'),
                  ('Stanhope', 'Sussex'),
                  ('Stillwater Township', 'Sussex'),
                  ('Sussex', 'Sussex'),
                  ('Vernon Township', 'Sussex'),
                  ('Walpack Township', 'Sussex'),
                  ('Wantage Township', 'Sussex'),
                  ('Berkeley Heights', 'Union'),
                  ('Clark', 'Union'),
                  ('Cranford', 'Union'),
                  ('Elizabeth', 'Union'),
                  ('Fanwood', 'Union'),
                  ('Garwood', 'Union'),
                  ('Hillside', 'Union'),
                  ('Kenilworth', 'Union'),
                  ('Linden', 'Union'),
                  ('Mountainside', 'Union'),
                  ('New Providence', 'Union'),
                  ('Plainfield', 'Union'),
                  ('Rahway', 'Union'),
                  ('Roselle', 'Union'),
                  ('Roselle Park', 'Union'),
                  ('Scotch Plains', 'Union'),
                  ('Springfield Township (1)', 'Union'),
                  ('Summit', 'Union'),
                  ('Union Township (1)', 'Union'),
                  ('Westfield', 'Union'),
                  ('Winfield Township', 'Union'),
                  ('Allamuchy Township', 'Warren'),
                  ('Alpha', 'Warren'),
                  ('Belvidere', 'Warren'),
                  ('Blairstown', 'Warren'),
                  ('Franklin Township (1)', 'Warren'),
                  ('Frelinghuysen Township', 'Warren'),
                  ('Greenwich Township (1)', 'Warren'),
                  ('Hackettstown', 'Warren'),
                  ('Hardwick Township', 'Warren'),
                  ('Harmony Township', 'Warren'),
                  ('Hope Township', 'Warren'),
                  ('Independence Township', 'Warren'),
                  ('Knowlton Township', 'Warren'),
                  ('Liberty Township', 'Warren'),
                  ('Lopatcong Township', 'Warren'),
                  ('Mansfield Township (1)', 'Warren'),
                  ('Oxford Township', 'Warren'),
                  ('Phillipsburg', 'Warren'),
                  ('Pohatcong Township', 'Warren'),
                  ('Washington', 'Warren'),
                  ('Washington Township (3)', 'Warren'),
                  ('White Township', 'Warren'),)