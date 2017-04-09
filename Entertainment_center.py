import fresh_tomatoes
import media

toy_story = media.Movie("Toy story", "A story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc&t=2s")
# print(toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.show_trailer())
# avatar.show_trailer()

matrix = media.Movie("Matrix", "No one can be told what the matix is",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://www.youtube.com/watch?v=tGgCqGm_6Hs")

forest_gump = media.Movie("Forest Gump", "A marine on alien planet",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_UY268_CR10,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=bLvqoHBptjg")

harry_potter = media.Movie("Harry Potter", "A gifted boy, in the world of wizards and witches",
                           "http://vignette3.wikia.nocookie.net/harrypotter/images/0/0e/Philostone.jpg/revision/latest?cb=20101208171110",
                           "https://www.youtube.com/watch?v=PbdM1db3JbY")

star_wars = media.Movie("Star Wars", "A story of a boy and space travel",
                           "https://upload.wikimedia.org/wikipedia/en/4/40/Star_Wars_Phantom_Menace_poster.jpg",
                           "https://www.youtube.com/watch?v=bD7bpG-zDJQ")
movies = [toy_story, avatar, matrix, forest_gump, harry_potter, star_wars]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)