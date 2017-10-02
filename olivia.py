####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Olivia'
strategy_name = 'Copycat'
strategy_description = 'Always copy previous opponents move.'
    
def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history:
        return 'b'
    elif 'c' in their_history:
        return 'c'
    else:
        return '-1'
