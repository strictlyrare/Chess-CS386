
# Requirements

_Group 09 – “[Chess with Friends!]”\
Date and location: Sep. 29, 2024\
Group Members: Noah Carges, Elliott Kinsley, Tristen Calder, Ryan Todd, David Gold-Matejka_

## 1. Positioning
### 1.1 Problem statement


The problem of chess not being typically customizable affects beginner players the impact of which make new chess players less interested in playing.


### 1.2. Product Position Statement


For anyone who wants to play chess online, Chess with Friends! is a free, online accessible application that allows you to play with your buddies, random people, or AI to test your skills! Unlike Chess.com, our product is simple to use and allows the user to customize their preferences however they like.


### 1.3. Value proposition


“Chess with friends is an online chess application that will provide anyone with an interest in chess hours of fun with friends or a computer.”


Customer segment: People with an interest in chess


## 2. Stakeholders


**Users**: Casual Players, Chess Enthusiasts, Beginner Learners, Competitive Gamers, Coaches/Trainers, Children/Young Learners
**Competitors**: www.chess.com , www.sparkChess.com , www.247chess.com, www.lichess.org 
**Detractors**: Traditional chess players or people who don’t have an interest in chess
**Developers**: Noah Carges, Elliott Kinsley, Tristen Calder, Ryan Todd, David Gold-Matejka


## 3. Functional requirements (features)


- Personalization/Preferences:Being able to customize your board and piece colors
- Ease of Use: Simple menu and board system that isn’t confusing to players.
- Chess online with friends: Being able to have the ability to play chess anywhere with anyone.
- Chess against AI:: Being able to play chess against an artificial intelligence.
- Optimization: The chess app will have manual memory allocation so the game will be well optimized.


## 4. Non-functional requirements
- Availability
- Usability
- Reliability
- Response Time


## 5. MVP
- The feature we plan on implementing early on would be the simple GUI and customization preferences.
- When building the GUI we try to keep in mind that anyone can use this app, so we are trying to make it very simple and intuitive.
- During our interviews, the most requested feature was being able to filter out the info they receive. If they were going to get notifications for things they didn't care about, they didn't want the app. So to deal with this we are planning on having categories, or a “tag” system to help people choose what they want to see.

## 6. Use cases
### 6.1. Use case diagram
**![](https://i.ibb.co/rZ5nm7K/image-2024-09-29-220848407.png)**


### 6.2. Use case descriptions


**Use Case**: New Game (pass and play)   
**Actor**: Player
**Description**: * User selects a new game for pass and play.
*Preconditions**:    User has opened the application and the game has been set up.
**Postconditions**:  The system now knows which game function to initialize.
**Main Flow**:
1. The actors accesses www.chessWithFriends.com  
2. After the game has accessed the server, the game should load. 
3. The actor either wins, forfeits, loses or stalemates
4. Back to main menu 
**Alternative Flow**
The user does not have access to the internet and the game cannot access the server.  


**Use Case**: New Game (online)   
**Actor**:  User
**Description**:   The user selects a new game for online play with friends.
**Preconditions**:    User has opened the application and the game has been set up
**Postconditions**:   The system now knows to initialize a game over another server and to output results to both.
**Main Flow**:
1. The actors accesses www.chessWithFriends.com 
After the game has accessed the server, the game should load. 
The actor either wins, forfeits, loses or stalemates
Back to main menu
**Alternative Flow**:
1. The user does not have access to the internet.
2. The servers are down.
3. The user connecting has no access to the internet.
4. Error displayed




**Use Case**: New Game (AI)  
**Actor**: User  
**Description**: The user selects a new game to play against an artificial intelligence (AI).
**Preconditions**:    User has opened the application and the game has been set up
**Postconditions**:   The system knows to initialize the artificial intelligence and ask the user the difficulty.
**Main Flow**:
The actors accesses www.chessWithFriends.com 
The actor selects new game with ai
The actor selects the difficulty level
The actor either wins, forfeits, loses or stalemates
Back to main menu
**Alternative Flow**:
1. The user does no have access to the internet.
2. The servers are down.
3. The user doesn’t select difficulty.
4. Error displayed


**Use Case**: Setup Game (pass and play)  
**Actor**: System   
**Description**: The system sets up pass and play by initiating both sides as players.   
**Preconditions**:  The user has accessed the website and chose the pass and play option.
**Postconditions**:   a setup board waiting for input
**Main Flow**:
1. The system creates a chess board
2. The system assigns both sides to the chess board.
3. The system outputs the board in a format to website
4. The system waits for player input to select


**Alternative Flow**:
Game board initialization problem
Report error back to user 


**Use Case**: Setup Game (online)
**Actor**: System  
**Description**:   The system sets up online functionality by connecting servers to each other.
**Preconditions**:   The user has accessed the website and play online option.
**Postconditions**:   a setup board waiting for user input.
**Main Flow**:
1. The system creates a chess board
2. The system assigns both sides to the chess board.
3. The system outputs the board in a format to website
4. The system waits for player input to select 
5. After user input, the player input is sent to a server
6. Board is displayed
**Alternative Flow**:
1.Game board initialization problem
2. Report error back to user   


**Use Case**: Initialize Artificial Intelligence  
**Actor**: System  
**Description**: The system sets up an artificial intelligence with variable difficulty.
**Preconditions**:   The user has accessed the website and play against computer option..
**Postconditions**:     a setup board waiting for user input.
**Main Flow**:
1. The system creates a chess board
2. The system assigns both sides to the chess board, one being AI.
3. The system outputs the board in a format to website
4. The system waits for player input to select 
5. After user input, the artificial intelligence will chose a option
6. Board is displayed
**Alternative Flow**:
1.Game board initialization problem
2. Report error back to user   


# 7. User stories


**User story 1**:  “As a player, I want to play a game of chess against another player so that I can enjoy a competitive match.”
Priority: HIGH
Estimated Hours: 8 hours


**User story 2**:  “As a beginner chess player, I want tutorials and tips within the game so that I can learn the rules and improve my skills.”
Priority: MEDIUM
Estimated Hours: 5 hours


**User story 3**:  “As a player, I want to move my pieces by clicking and dragging so that the gameplay feels intuitive and user-friendly.”
Priority: HIGH
Estimated Hours: 3 hours


**User story 4**:  “As a competitive player, I want to play against a basic AI opponent so that I can practice my strategies without needing another human player.”
Priority: MEDIUM
Estimated Hours: 8 hours


**User story 5**:  “As a player, I want the option to restart the game at any time so that I can play again without closing and reopening the program.”
Priority: MEDIUM
Estimated Hours: 2 hours


**User story 6**:  “As a player, I want to see a history of my moves during the game so that I can analyze my decisions and learn from my mistakes.”
Priority: MEDIUM
Estimated Hours: 5 hours


**User story 7**:  “As a player, I want the game to highlight valid moves when I select a piece so that I can easily see my options and make better decisions.”
Priority: HIGH
Estimated Hours: 5 hours


**User story 8**:  “As a player, I want to have an option to undo my last move so that I can correct mistakes without losing progress.”
Priority: MEDIUM
Estimated Hours:  3 hours


**User story 9**:  “As a player, I want to receive notifications when the game ends with a victory or draw so that I know the result of the match immediately.”
Priority: LOW
Estimated Hours:  2 hours


**User story 10**:  “As a player, I want the chessboard and pieces to be visually appealing so that I have an enjoyable and engaging experience while playing.”
Priority: LOW
Estimated Hours:  5 hours


## 8. Issue Tracker
**![](https://i.ibb.co/xHFyYmW/image-2024-09-29-215834767.png)**

https://github.com/Ekinsley02/Chess-CS386/issues 

