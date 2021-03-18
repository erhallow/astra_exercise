from connect_database import Connection


def search_by_salary_team(team_id, year_id, salary):
    try:
        connection = Connection()

        # Select salary query on salary_by_team_id
        salary_table = connection.session.execute(
            "SELECT * FROM statistics.salary_by_team_id WHERE team_id=%s AND year_id=%s AND salary >%s limit 10", [team_id, year_id, salary])

        # Print Query Details
        print('======================Filter By Salary=======================')
        print('FILTER BY TEAM (', team_id, ') + YEAR(',
              year_id, ') + SALARY > ( $', salary, ')')
        print('-------------------------------------------------------------')

        # Iterate over results to print salary stats
        idx = 1
        for row in salary_table:
            # Print Out Salary Stats
            print("Index: ", "{0:02d}".format(idx), ' | Player: ',
                  "{:<9}".format(row.player_id), ' | Salary: ', "{:,.2f}".format(row.salary))
            idx += 1
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


search_by_salary_team('CHA', 2005, 5000000)
search_by_salary_team('HOU', 2005, 5000000)


# SAI Index utilized on the salary column to allow for filtering
# CREATE CUSTOM INDEX salary_said_idx ON statistics.salary_by_team_id (salary) USING 'StorageAttachedIndex';
