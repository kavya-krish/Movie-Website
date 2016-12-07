import media
import fresh_tomatos


mini = media.Movie("Minions","Minions embark on a global trip and meet Scarlett Overkill, a female super-villain who recruits them and hatches a plan to take over the world.","https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg","https://www.youtube.com/watch?v=7AFUch5JZaQ")

inception = media.Movie("Inception","The implantation of another person's idea into a target's subconscious","https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg","https://www.youtube.com/watch?v=8hP9D6kZseM")

Twilight= media.Movie("Twilight","seventeen-year-old Isabella Bella Swan falls in love with Edward Cullen, a vampire","https://upload.wikimedia.org/wikipedia/en/8/89/Newmooncover.jpg","https://www.youtube.com/watch?v=fFLrRlPBg0A")

ps = media.Movie("P.S. I Love You","Holly Kennedy receives letters from her late husband that bring her hope, strength and inspiration and make her feel as if he is standing by her side each step of the way.","https://upload.wikimedia.org/wikipedia/en/7/7f/PS_I_Love_You_%28film%29.jpg","https://www.youtube.com/watch?v=CZzW6_hR068")

stars = media.Movie("Fault in our stars","Teenager Hazel Grace's life changes when she meets Augustus Waters at a cancer support group. The two then embark on a life-changing journey which brings them even closer.","https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%28Official_Film_Poster%29.png","https://www.youtube.com/watch?v=9ItBvH5J6ss")

movies = [mini,inception,Twilight,ps,stars]



fresh_tomatos.open_movies_page(movies)
