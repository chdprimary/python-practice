import pygal

socializing =   (
                 2 + # Zilker Foodventure - 10/22
                 2 + # Wu Tang BDay - 10/22
                 2.5 + # CS Scary Movie - 10/22
                 3 + # Karaoke at Ciera's - 10/23
                 2 + # Meeting Matt - 10/25
                 3 + # Picking up / hanging with Matt at apt - 10/25
                 2 + # Nik at apt, watching anime - 10/27
                 5 # Halloween Parties - 10/28
                )

working =       (
                 2 + # Video editing at Ciera's - 10/23
                 2.25 + # Video w/ Kathy -10/24
                 2 # Video editing at Ciera's - 10/25
                )

# Want to do something outside, where kids can get out energy and I can do my own thing
kids =          (
                 2 # With kids at mall
                )

# Awake, solo time where we aren't working or on phones
quality_time =  (
                 2 + # Sex, hummus, vodka, tacorrido - 10/23
                 1 + # Alexis took me on sushi date - 10/25
                 1 + # At Canary Roost - 10/26
                 1 + # Watching Stranger Things (I was falling asleep) - 10/27
                 0.5 # Sex - 10/28
                )

fighting =      (
                 5 + # Missed Ciera's live podcast thing - 10/22
                 1 + # After sushi date (Alexis couldn't "share" about Andre or be herself) - 10/25
                 4 # Got mad because I didn't like how she was on phone? - 10/26
                )

alone =         (
                 2 + # Alexis was at Shay & Andre's - 10/22
                 3.5 + # Alexis at Speed Dating = 10/24
                 3 # Alexis at Scare for Cure = 10/27
                )

hours_in_week = 24 * 7 # => 168
waking_hours_in_week = 14.5 * 7 # => 101.5
logged_hours = 61.5 # total of factors above

bar = pygal.Bar()
bar.title = "Approx. Time Allocations (10/22 thru 10/28)"

bar.add('socializing', socializing)
bar.add('working', working)
bar.add('kids', kids)
bar.add('quality time', quality_time)
bar.add('fighting', fighting)
bar.add('alone', alone)
bar.add('news', 0.75 * 5 + 0.25 * 2)
bar.add('showers', 0.5 * 7)
bar.add('reading', 0)
bar.add('workout', 0)
# bar.add('biz learning', 0)
# bar.add('programming', 0)
# bar.add('guitar', 0)
# bar.add('bondange', 0)

bar.render_to_file("time_allocations_20171022_20171028.svg")