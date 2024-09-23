input_ad1_EN = """
House in Wayzata, US

Stunning 5-bedroom, 4-bathroom rambler on private cul-de-sac, nestled on over 1 acre of lush, private land backing up to 6.4 acres of protected wetland. 
Step inside to discover a bright, open main floor with recently refinished hardwood floors and expansive views of your serene backyard. 
The gourmet kitchen features a Sub-Zero refrigerator and gas cooktop, seamlessly connecting to informal dining and living spaces, 
as well as a formal dining room—perfect for entertaining. The private primary suite is a true oasis, boasting a two-sided fireplace, 
access to a secluded deck, a spacious walk-in closet, and a spa-like bathroom with a jetted soaking tub. On the opposite side of the home, 
you’ll find two additional bedrooms and a bathroom, ideal for family or guests. The lower-level walkout is designed for relaxation and fun, 
featuring a large wet bar, family room, two additional bedrooms, and ample storage. Outdoor living shines with a large deck, patio, three-season porch, 
and a charming gazebo, all overlooking the picturesque landscape. With a brand-new roof and skylights in the kitchen, this home is move-in ready. 
Located just minutes from downtown Wayzata and the stunning Lake Minnetonka, you’ll enjoy easy access to miles of trails and major highways.
"""

output_ad1_EN = """
Polygon coordinates: [[44.972, -93.540], [44.972, -93.480], [44.930, -93.480], [44.930, -93.540]]

Trust score: 90% 

Reasoning:

The ad specifies that the house is located in Wayzata, Minnesota.
The home is described as being minutes from downtown Wayzata and close to Lake Minnetonka, reinforcing the location in that specific area.
Information about proximity to trails and major highways is also a typical feature of the Wayzata area.
The polygon coordinates determine an area around Wayzata, encompassing possibly neighboring parts while remaining within the city limits to ensure an accurate representation of the area.
"""

output_immoreview_ad1_EN = """
Size of the property: 9/10 \n
With 5 bedrooms and 4 bathrooms, as well as a spacious living area, this home is ideal for a large family or for those who love to entertain. The size of more than an acre of land also adds to the appeal.

Luminosity of the property: 8/10 \n 
The listing mentions “expansive views” of the garden and “recently redone wood floors,” which suggests good natural light in the living spaces.

Close to shops: 7/10 \n
Although the house is located close to "downtown Wayzata", the listing does not specify the exact distance to shops, but it does indicate reasonable accessibility.

Close to nature: 10/10 \n
The property is situated on over an acre of private land and overlooks 6.4 acres of protected wetlands, providing an exceptional natural setting. Additionally, the proximity to Lake Minnetonka and the trails reinforces this aspect.

Calm and quiet surroundings: 9/10 \n
Being located in a private cul-de-sac, the house seems to offer a quiet environment, far from the noise pollution of traffic.

Modernity of the property: 9/10 \n
The home has modern amenities such as a gourmet kitchen with a Sub-Zero refrigerator and a new roof with skylights, indicating that it is well-maintained and up-to-date.

Bonuses of the property: 10/10 \n
Additional features like the double-sided fireplace, master suite with access to a private terrace, wet bar in the basement, as well as outdoor spaces such as a large deck, patio and gazebo add significant value to the property.
"""

input_ad2_EN = """
Condo in Brooklyn

This well-maintained, bright, 950 square-foot, 1-bedroom, 1-bath, 4-closet, corner-unit is perched approximately 90-feet high above Brooklyn's historic Ocean Parkway greenway with unobstructed views views of the Manhattan skyline and the Verrazano bridge.

One of the highlights of this unit is the bright and airy, 410+ square-foot, great-room with separate living and dining areas that will leave you in awe at sunset with it's Western exposures and a large, renovated kitchen with a northern exposure of Ocean Parkway and the Manhattan skyline. Off to the left of the foyer is a corridor leading to the unit's expansive bedroom and the elegant white subway-tiled bathroom. The bedroom is another highlight of this unit with approximately 220sqft of space along with two large built-in closets and it would definitely fit a California-King-sized bed along with any complete set of bedroom furniture.

This oversized, 7th floor, 1-bedroom co-op with unobstructed views is located in The Sutton House, the first and best luxury co-op building in Midwood. The building is extremely well-managed and features an attractive lobby with handicap access, 24/7 doorman, concierge, on-site superintendent, 2 elevators (one Shabbos), voice intercom, FIOS and cable, central air and heat within each unit that you control, bike room, storage room, laundry room, landscaped courtyard with picnic and barbecue area, a large 3-season outdoor heated pool (52'x 33'), and an indoor parking garage (waitlist). The monthly maintenance of $1,392.20 includes all utilities.

Located on the historic tree-lined Ocean Parkway, only 7 blocks from the F-train, 10 blocks from the Q-train, and food/shopping 5 blocks away on Coney Island Avenue, this luxury apartment is in the center of it all. Call for a showing today.
"""

output_ad2_EN = """
Polygon coordinates: [[40.6290, -73.9732], [40.6295, -73.9732], [40.6295, -73.9717], [40.6290, -73.9717]]

Trust score: 90%

Reasoning:

The property is located in Brooklyn, and the listing specifically mentions that it is located along Ocean Parkway, a historic boulevard in that neighborhood.
The fact that the apartment is 7 blocks from the F line and 10 blocks from the Q line suggests that it is located near the subway stations corresponding to these lines, which is in the Midwood neighborhood of Brooklyn.
Information about nearby points of interest, such as shopping on Coney Island Avenue, also confirms the apartment's central and accessible Midwood location.
The coordinates of the proposed polygon enclose an area that corresponds to a typical residential area of ​​Midwood, while taking into account the distances mentioned in the announcement.
"""

output_immoreview_ad2_EN = """
Size of the property: 9/10 \n
At 950 square feet, this apartment is spacious for a 1 bedroom. The generous size of the rooms, particularly the large living room and bedroom, is a major asset.

Luminosity of the property: 8/10 \n
The apartment is described as "well-maintained" and "bright", with exposures that allow beautiful natural light, notably thanks to the windows facing west and north. The unobstructed views add to the brightness.

Close to shops: 7/10 \n
The ad mentions that shops and restaurants are only 5 blocks away on Coney Island Avenue, indicating good accessibility to amenities. This could be improved with additional details on the types of businesses available.

Close to nature: 10/10 \n
Although the ad does not directly mention green spaces, the presence of the Ocean Parkway and the landscaped garden in the condominium suggests access to pleasant outdoor spaces. However, information about nearby parks could have reinforced this rating.

Calm and quiet surroundings: 9/10 \n
Being located 90 feet above street level, the apartment offers unobstructed views and is likely less exposed to traffic noise. However, the proximity of the street can cause noise pollution at certain times.

Modernity of the property: 9/10 \n
The apartment has a renovated kitchen and a stylish bathroom, which indicates a certain level of modernity. However, additional details about modern materials and equipment could have strengthened this rating.

Bonuses of the property: 10/10 \n
The condominium's amenities are impressive, including the heated outdoor swimming pool, garage, concierge service, and well-maintained common areas. These features add significant value to the apartment.
"""

input_ad3_EN = """
Unrivaled corner penthouse with floor-to-ceiling views (sunsets) overlooking the Olympic Sculpture Park, Elliot Bay, Olympic Mountains, 
atop a world-class community in North Belltown, welcome to PH 5 at the Parc. 
Spacious 918 square feet, 10' ceiling height big One Bedroom 1.5 bath with features like gas cooking, 
hardwood flooring and steps to the revitalized waterfront and Pike Place Market. With reimagined interiors in 2020 
and full reno (kitchen, bath, lighting) in 2022 - supreme parking and dedicated storage, modest HOA dues plus NO rent cap! 
Sweeping water views from the swank rooftop, true guest suite, 24/7 concierge, dialed community room and super strong HOA 
continue to make the Parc one of the most desirable in all North Belltown!
"""

output_ad3_EN = """
Polygon coordinates: [[47.6138, -122.3470], [47.6143, -122.3470], [47.6143, -122.3410], [47.6138, -122.3410]]

Trust score: 90%

Reasoning:
The listing specifically mentions that the property is in the North Belltown neighborhood, which is located in Seattle, Washington.
It references views of the Olympic Sculpture Park, Elliot Bay and the Olympic Mountains, placing the property close to these iconic locations.
Additionally, it is said to be within walking distance of the revitalized waterfront and Pike Place Market, two very well-known and central points in Seattle.
Considering these elements, the proposed polygon encompasses an area around North Belltown, incorporating points of interest and taking into account the geographical layout.
"""

input_places_ad1_EN = """
Condo in Brooklyn

This well-maintained, bright, 950 square-foot, 1-bedroom, 1-bath, 4-closet, corner-unit is perched approximately 90-feet high above Brooklyn's historic Ocean Parkway greenway with unobstructed views views of the Manhattan skyline and the Verrazano bridge.

One of the highlights of this unit is the bright and airy, 410+ square-foot, great-room with separate living and dining areas that will leave you in awe at sunset with it's Western exposures and a large, renovated kitchen with a northern exposure of Ocean Parkway and the Manhattan skyline. Off to the left of the foyer is a corridor leading to the unit's expansive bedroom and the elegant white subway-tiled bathroom. The bedroom is another highlight of this unit with approximately 220sqft of space along with two large built-in closets and it would definitely fit a California-King-sized bed along with any complete set of bedroom furniture.

This oversized, 7th floor, 1-bedroom co-op with unobstructed views is located in The Sutton House, the first and best luxury co-op building in Midwood. The building is extremely well-managed and features an attractive lobby with handicap access, 24/7 doorman, concierge, on-site superintendent, 2 elevators (one Shabbos), voice intercom, FIOS and cable, central air and heat within each unit that you control, bike room, storage room, laundry room, landscaped courtyard with picnic and barbecue area, a large 3-season outdoor heated pool (52'x 33'), and an indoor parking garage (waitlist). The monthly maintenance of $1,392.20 includes all utilities.

Located on the historic tree-lined Ocean Parkway, only 7 blocks from the F-train, 10 blocks from the Q-train, and food/shopping 5 blocks away on Coney Island Avenue, this luxury apartment is in the center of it all. Call for a showing today."""

output_places_ad1_EN = """
[Ocean Parkway (Brooklyn), Coney Island Avenue (Brooklyn)]
"""

input_places_ad2_EN = """
Unrivaled corner penthouse with floor-to-ceiling views (sunsets) overlooking the Olympic Sculpture Park, Elliot Bay, Olympic Mountains, 
atop a world-class community in North Belltown, welcome to PH 5 at the Parc. 
Spacious 918 square feet, 10' ceiling height big One Bedroom 1.5 bath with features like gas cooking, 
hardwood flooring and steps to the revitalized waterfront and Pike Place Market. With reimagined interiors in 2020 
and full reno (kitchen, bath, lighting) in 2022 - supreme parking and dedicated storage, modest HOA dues plus NO rent cap! 
Sweeping water views from the swank rooftop, true guest suite, 24/7 concierge, dialed community room and super strong HOA 
continue to make the Parc one of the most desirable in all North Belltown!
"""

output_places_ad2_EN = """
[Olympic Sculpture Park (Seattle), Elliot Bay (Seattle), Olympic Mountains (Seattle), Pike Place Market (Seattle)]
"""


input_wrong1_EN = "What are the documents used in this application ?"
output_wrong1_EN = "It does not correspond to a real estate ad"

input_wrong2_EN = "Write me an ad for a house in Wysconsin"
output_wrong2_EN = "I am an app that analyzes or rephrases real estate ad, but I am not authorized to write an ad from scratch"

input_wrong3_EN = """
Specifications
CPU: AMD Ryzen 9 8945HSGPU: Up to Nvidia GeForce RTX 4070RAM: 32 GB LPDDR5X-6400Screen: 14-inch 1800p @ 120 Hz | OLEDStorage: 1 TB SSD NVMe PCIe 4.0Battery: 73 WhDimensions: 31.1 x 22.0 x 1.63 cm / 12.24 x 8.66 x 0.64-inchesWeight: 1.50 kg / 3.3 lbs
"""
output_wrong3_EN = "It does not correspond to a real estate ad"
