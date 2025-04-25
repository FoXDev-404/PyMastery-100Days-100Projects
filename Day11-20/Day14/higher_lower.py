# The Hiher/Lower Game. This is a game where you compare the number of followers of two different Indian celebrities.
# The game is played in a loop until the user makes a wrong guess.
# The user is prompted to guess which celebrity has more followers, and the game keeps track of the score.
# The game ends when the user makes a wrong guess, and the final score is displayed.

import random
from higher_lower_art import logo, vs


def display_comparison(option_a, option_b):
    """Display the comparison between two options with nice formatting."""
    print(f"Compare A: {option_a}")
    print(vs)
    print(f"Compare B: {option_b}")


def clear_screen():
    """Clear the console screen for better visibility."""
    print("\n" * 3)


# Data dictionary with approx follower counts (in millions)
indian_celebrities = {
    # Actors
    "Shah Rukh Khan, an Actor, from India.": 42.5,
    "Deepika Padukone, an Actor, from India.": 77.2,
    "Alia Bhatt, an Actor, from India.": 73.1,
    "Salman Khan, an Actor, from India.": 58.9,
    "Priyanka Chopra, an Actor, from India.": 87.3,
    "Akshay Kumar, an Actor, from India.": 63.2,
    "Ranveer Singh, an Actor, from India.": 43.8,
    "Nawazuddin Siddiqui, an Actor, from India.": 1.8,
    "Dhanush, an Actor, from India.": 4.5,
    "Taapsee Pannu, an Actor, from India.": 26.4,
    "Hrithik Roshan, an Actor, from India.": 46.2,
    "Katrina Kaif, an Actor, from India.": 66.7,

    # Cricketers
    "Virat Kohli, a Cricketer, from India.": 270.5,
    "Rohit Sharma, a Cricketer, from India.": 35.2,
    "MS Dhoni, a Cricketer, from India.": 42.8,
    "Hardik Pandya, a Cricketer, from India.": 26.3,
    "Jasprit Bumrah, a Cricketer, from India.": 12.7,
    "KL Rahul, a Cricketer, from India.": 13.5,
    "Ravindra Jadeja, a Cricketer, from India.": 5.2,
    "Rishabh Pant, a Cricketer, from India.": 8.6,
    "Mohammed Siraj, a Cricketer, from India.": 2.1,
    "Smriti Mandhana, a Cricketer, from India.": 7.8,
    "Shubman Gill, a Cricketer, from India.": 9.3,

    # Musicians
    "A.R. Rahman, a Musician, from India.": 6.5,
    "Arijit Singh, a Singer, from India.": 15.3,
    "Neha Kakkar, a Singer, from India.": 74.2,
    "Badshah, a Musician, from India.": 11.4,
    "Shreya Ghoshal, a Singer, from India.": 28.5,
    "Jubin Nautiyal, a Singer, from India.": 12.6,
    "Armaan Malik, a Singer, from India.": 20.3,
    "Lata Mangeshkar, a Singer, from India.": 0.52,
    "Yo Yo Honey Singh, a Rapper, from India.": 7.5,
    "Divine, a Hip-Hop Artist, from India.": 2.9,

    # Sports Personalities (Non-Cricket)
    "Neeraj Chopra, an Olympic Gold Medalist, from India.": 9.2,
    "PV Sindhu, a Badminton Player, from India.": 4.1,
    "Sania Mirza, a Tennis Player, from India.": 11.8,
    "Mary Kom, a Boxer, from India.": 1.5,
    "Saina Nehwal, a Badminton Player, from India.": 2.7,
    "Dipa Karmakar, a Gymnast, from India.": 0.5,
    "Sunil Chhetri, a Footballer, from India.": 3.4,
    "Bajrang Punia, a Wrestler, from India.": 0.8,
    "Hima Das, a Sprinter, from India.": 1.3,

    # Business Leaders
    "Mukesh Ambani, a Business Tycoon, from India.": 1.2,
    "Ratan Tata, an Industrialist, from India.": 6.5,
    "Kiran Mazumdar-Shaw, a Businesswoman, from India.": 0.3,
    "Anand Mahindra, an Industrialist, from India.": 10.6,
    "Kunal Shah, a Fintech Entrepreneur, from India.": 0.8,
    "Falguni Nayar, Founder of Nykaa, from India.": 0.6,
    "Ritesh Agarwal, Founder of OYO, from India.": 0.7,
    "Byju Raveendran, an EdTech Entrepreneur, from India.": 0.2,

    # Organizations & Teams
    "ISRO, a Space Research Organization, from India.": 7.69,
    "DRDO, a Defense Research Organization, from India.": 1.2,
    "Chennai Super Kings, a Cricket Team, from India.": 10.3,
    "Mumbai Indians, a Cricket Team, from India.": 8.9,
    "Royal Challengers Bangalore, a Cricket Team, from India.": 7.5,
    "Kolkata Knight Riders, a Cricket Team, from India.": 3.2,
    "IIT Bombay, an Educational Institution, from India.": 0.2,
    "IIM Ahmedabad, an Educational Institution, from India.": 0.2,
    "Tata Consultancy Services, an IT Company, from India.": 0.9,
    "Infosys, an IT Company, from India.": 0.8,
    "Flipkart, an E-commerce Platform, from India.": 2.5,
    "Amul, a Dairy Brand, from India.": 1.5,
    "Reliance Industries, a Conglomerate, from India.": 1.4,
    "Make in India, a Government Initiative, from India.": 1.7,

    # Media & Entertainment
    "The Filmfare Awards, a Film Award Ceremony, from India.": 1.5,
    "IIFA Awards, a Film Award Ceremony, from India.": 1.1,
    "Zee Cine Awards, a Film Award Ceremony, from India.": 0.6,
    "SIIMA Awards, a Film Award Ceremony, from India.": 0.4,
    "Indian Idol, a Music Reality Show, from India.": 0.9,
    "The Voice India, a Singing Competition, from India.": 0.6,
    "Sunburn, a Music Festival, from India.": 0.55,
    "NH7 Weekender, a Music Festival, from India.": 0.3,
    "T-Series, a Music Label, from India.": 232.0,
    "YRF Music, a Music Company, from India.": 11.2,
    "Bollywood Hungama, an Entertainment Portal, from India.": 3.5,

    # Sports Organizations
    "BCCI, the Cricket Board, from India.": 17.2,
    "Kabaddi Pro League, a Sports Competition, from India.": 0.8,
    "ISL, a Club Football League, from India.": 0.7,
    "Hockey India, a Sports Federation, from India.": 0.5,
    "India Olympic Association, a Sports Body, from India.": 0.3,
    "Blue Tigers, the Indian National Football Team, from India.": 0.1,
    "Indian Arrows, a Football Team, from India.": 0.1,
    "FC Goa, a Football Club, from India.": 0.3,
    "Chennaiyin FC, a Football Club, from India.": 0.2,
    "Bengaluru FC, a Football Club, from India.": 0.4,

    # Political & Social
    "Narendra Modi, the Prime Minister, from India.": 90.2,
    "Rahul Gandhi, a Politician, from India.": 24.5,
    "Arvind Kejriwal, a Politician, from India.": 26.8,
    "Padma Awards, a Civilian Honor, from India.": 0.2,
    "Swachh Bharat Mission, a Cleanliness Campaign, from India.": 1.4,
    "Digital India, a Government Initiative, from India.": 2.2,

    # Technology
    "Byju's, an EdTech Company, from India.": 0.3,
    "Zomato, a Food Delivery App, from India.": 3.1,
    "Swiggy, a Food Delivery App, from India.": 1.7,
    "Paytm, a Fintech Company, from India.": 3.8,
    "PhonePe, a Payments App, from India.": 1.2,
    "Ola Cabs, a Ride-hailing Service, from India.": 2.9,
    "Myntra, a Fashion E-commerce, from India.": 1.3,
}


def play_game():
    print(logo)
    score = 0
    game_over = False
    current_celebrity = random.choice(list(indian_celebrities.keys()))

    while not game_over:
        # Select next celebrity (ensuring it's different from current)
        next_celebrity = current_celebrity
        while next_celebrity == current_celebrity:
            next_celebrity = random.choice(list(indian_celebrities.keys()))

        # Display comparison
        display_comparison(current_celebrity, next_celebrity)

        # Get followers
        current_followers = indian_celebrities[current_celebrity]
        next_followers = indian_celebrities[next_celebrity]

        # Debug info (comment out for production)
        # print(f"DEBUG - A: {current_followers}M, B: {next_followers}M")

        # Get user's guess
        while True:
            user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            if user_guess in ['a', 'b']:
                break
            print("Invalid input. Please type 'A' or 'B'.")

        # Check if user is correct
        is_correct = (user_guess == 'a' and current_followers > next_followers) or (
                    user_guess == 'b' and next_followers > current_followers)

        clear_screen()
        print(logo)

        # Display results
        if is_correct:
            score += 1
            print(f"✓ Correct! {current_celebrity.split(',')[0]} has {current_followers}M followers.")
            print(f"✓ {next_celebrity.split(',')[0]} has {next_followers}M followers.")
            print(f"Current score: {score}")
            # Winner becomes the new current celebrity for comparison
            current_celebrity = next_celebrity
        else:
            print(f"✗ Sorry, that's wrong!")
            print(f"{current_celebrity.split(',')[0]} has {current_followers}M followers.")
            print(f"{next_celebrity.split(',')[0]} has {next_followers}M followers.")
            print(f"Final score: {score}")
            game_over = True

        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    play_game()