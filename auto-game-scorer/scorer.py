import openai

msg_list = list()
contents = list()

msg_obj = dict()
msg_obj["role"] = "system"
msg_obj["content"] = "you are an assistant to keep track of the score for a game, displaying the results in a table with player names as the columns, with rounds and total score per player as the rows. only display the table, no other text."

msg_list.append(msg_obj)

game_name = input("What game? ")
num_players = input("How many players? ")

player_names = ""
round = 0

for i in range(int(num_players)):

    player_names += input("Player {}: ".format(i + 1))
    player_names += " "

player_names = player_names[:-1]

setup_msg = "keep track of the score for a game of {} in a table with {} players named {}. only display the table and no other text. also make sure to show the total score per round for each player in the table.".format(game_name, num_players, player_names)

msg_obj = dict()
msg_obj["role"] = "user"
msg_obj["content"] = setup_msg

msg_list.append(msg_obj)

while True:

    round += 1
    round_msg = "\nRound {}: ".format(round)
    content = input(round_msg)

    if content != "game over":

        content += " in round {}".format(round)

        msg_obj = dict()
        msg_obj["role"] = "user"
        msg_obj["content"] = content

        msg_list.append(msg_obj)

        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=0, messages=msg_list)

        print()
        print(chat_completion.choices[0].message.content)

    else:

        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", temperature=0, messages=msg_list)

        print()
        print("\nFinal Score:")
        print(chat_completion.choices[0].message.content)
        print()

        break