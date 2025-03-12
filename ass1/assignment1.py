"""
Name: Xiuhan Lin
Date started: 05/03/2025
GitHub URL:https://github.com/cp1404-students/a1-2025-1-LIN14263
"""

# Constants
LEARNED = "l"
UNLEARNED = "u"
SONG_FILE = "songs.csv"
MENU = """Menu:
D - Display songs
A - Add new song
C - Complete a song
Q - Quit
>>> """

def main():
    """Main function to manage the song list program."""
    print("Song List 1.0 - by [Your Name]")
    songs = load_songs()

    while True:
        print(MENU, end="")
        choice = input().strip().upper()
        if choice == "D":
            display_songs(songs)
        elif choice == "A":
            add_song(songs)
        elif choice == "C":
            complete_song(songs)
        elif choice == "Q":
            save_songs(songs)
            print(f"{len(songs)} songs saved to {SONG_FILE}")
            print("Make some music!")
            break
        else:
            print("Invalid menu choice")

def load_songs():
    """Load songs from CSV file into a list."""
    songs = []
    try:
        with open(SONG_FILE, "r") as file:
            for line in file:
                title, artist, year, status = line.strip().split(",")
                songs.append([title, artist, int(year), status])
        print(f"{len(songs)} songs loaded.")
    except FileNotFoundError:
        print("No songs file found. Starting with an empty list.")
    return songs

def save_songs(songs):
    """Save songs list to CSV file."""
    with open(SONG_FILE, "w") as file:
        for song in songs:
            file.write(",".join([song[0], song[1], str(song[2]), song[3]]) + "\n")

def display_songs(songs):
    """Display songs sorted by year and title with counts."""
    if not songs:
        print("No songs in list.")
        return

    sorted_songs = sorted(songs, key=lambda x: (x[2], x[0]))
    learned_count = sum(1 for song in songs if song[3] == LEARNED)
    unlearned_count = len(songs) - learned_count

    for i, song in enumerate(sorted_songs, 1):
        marker = "*" if song[3] == UNLEARNED else " "
        print(f"{i}. {marker} {song[0]:<30} - {song[1]:<25} ({song[2]})")
    print(f"{learned_count} songs learned, {unlearned_count} songs still to learn.")

def add_song(songs):
    """Add a new unlearned song to the list."""
    print("Enter details for a new song.")
    title = get_valid_string("Title: ")
    artist = get_valid_string("Artist: ")
    year = get_valid_year("Year: ")
    songs.append([title, artist, year, UNLEARNED])
    print(f"{title} by {artist} ({year}) added to song list.")

def complete_song(songs):
    """Mark an unlearned song as learned."""
    unlearned_indices = [i for i, song in enumerate(songs) if song[3] == UNLEARNED]
    if not unlearned_indices:
        print("No more songs to learn!")
        return

    display_songs(songs)
    song_number = get_valid_number("Enter the number of a song to mark as learned: ", 1, len(songs))
    song_index = song_number - 1

    if songs[song_index][3] == LEARNED:
        print(f"You have already learned {songs[song_index][0]}")
    else:
        songs[song_index][3] = LEARNED
        print(f"{songs[song_index][0]} by {songs[song_index][1]} learned.")

def get_valid_string(prompt):
    """Get a non-empty string from user input."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input can not be blank.")

def get_valid_number(prompt, min_value, max_value):
    """Get a valid integer within range from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Number must be >= {min_value}")
            elif value > max_value:
                print(f"Number must be <= {max_value}")
            else:
                return value
        except ValueError:
            print("Invalid input: enter a valid number.")

def get_valid_year(prompt):
    """Get a valid positive year from user input."""
    while True:
        try:
            year = int(input(prompt))
            if year <= 0:
                print("Number must be > 0.")
            else:
                return year
        except ValueError:
            print("Invalid input: enter a valid number.")

if __name__ == "__main__":
    main()



