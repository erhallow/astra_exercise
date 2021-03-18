from connect_database import Connection


def read_table_salary_by_player_id():
    try:
        connection = Connection()

        # Select salary query on salary_by_player_id
        salary_results = connection.session.execute(
            "SELECT * FROM statistics.salary_by_player_id limit 10")

        # Print out Salary Results
        idx = 1
        print('============================================SALARY TOTALS TABLE======================================')
        for row in salary_results:
            print("Index: ", "{0:02d}".format(idx), ' | Player: ', "{:<9}".format(row.player_id), ' | Year: ', row.year_id,
                  ' | Team: ', row.team_id, ' | League: ', row.lg_id, ' | Salary: $', "{:,}".format(row.salary))
            idx += 1
        print('=====================================================================================================')
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


def read_table_batting_by_player_id():
    try:
        connection = Connection()

        # Batting select query on batting_by_player_id
        batting_results = connection.session.execute(
            "SELECT * FROM statistics.batting_by_player_id limit 10")

        # Print out the batting results
        print('===============================================BATTING TOTALS TABLE===================================================')
        idx = 1
        for row in batting_results:
            print("Index: ", "{0:02d}".format(idx), ' | Player: ', "{:<9}".format(row.player_id), ' | Year: ', row.year_id,
                  ' | Team: ', row.team_id, ' | League: ', row.lg_id, ' | HR: ', "{0:02d}".format(row.hr), ' | 3B: ', "{0:02d}".format(row.triple), ' | 2B: ', "{0:02d}".format(row.double), ' | R', "{0:03d}".format(row.r))
            idx += 1
        print('======================================================================================================================')
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


read_table_batting_by_player_id()
read_table_salary_by_player_id()
