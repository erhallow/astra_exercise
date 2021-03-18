from connect_database import Connection


def add_new_player(player_id, team_id, year_id, lg_id, hr, triple, double, r, rbi):
    try:
        connection = Connection()

        # Insert entire new player into the table
        # Player Id = [5 characters from last name + 2 characters first name + number (01, 02, 03, etc)]
        # Frank Thomas => thomafr04
        entry = connection.session.execute(
            "INSERT INTO statistics.sample_batting_player_id (player_id, team_id, year_id, lg_id, hr, triple, double, r, rbi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", [player_id, team_id, year_id, lg_id, hr, triple, double, r, rbi])
        print('New Player Entered!')
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


def update_stat_line(player_id, team_id, year_id, lg_id, hr, triple, double, r, rbi):

    # Update query to update player statistics on table
    update_query = "UPDATE statistics.sample_batting_player_id SET  lg_id = ?, hr = ?, triple = ?, double = ?, r = ?, rbi = ? WHERE player_id = ? AND team_id = ? AND year_id = ?"

    try:
        connection = Connection()

        # Prepare update query
        prepared_update_query = connection.session.prepare(update_query)

        # Execute update query
        connection.session.execute(
            prepared_update_query, [lg_id, hr, triple, double, r, rbi, player_id, team_id, year_id])

    except Exception as e:
        print('Error: ', e)
    else:
        # No exception indicates that update was successful!
        print('Player Updated!!')
        connection.close()
        print('\n**Connection closed!**\n')


def delete_player(player_id):
    try:
        connection = Connection()

        # Delete Player Profile from test_batting
        connection.session.execute(
            "DELETE FROM statistics.sample_batting_player_id WHERE player_id = %s", [player_id])
    except Exception as e:
        print('Error: No Player!! / ', e)
    else:
        print('Player Deleted: ', player_id.capitalize())
        connection.close()
        print('\n**Connection closed!**\n')


add_new_player('konerpa01', 'CHA', 2005, 'AL',
               40, 0, 24, 98, 100)

# update_stat_line('konerpa01', 'CHA', 2005, 'AL',
#                  33, 33, 33, 33, 33)

# delete_player('konerpa01')
