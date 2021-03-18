from connect_database import Connection


def cost_per_off_prod(player_id, year_id):
    try:
        connection = Connection()

        # ------Query Salary table to get Players Yearly Salary------

        # Salary select query on salary_by_player_id
        salary = connection.session.execute(
            "SELECT * FROM statistics.salary_by_player_id WHERE player_id =%s AND year_id =%s", [player_id, year_id])

        # Assign cost as Salary value
        for row in salary:
            cost = row.salary

        # ------Query Batting Table to get Players Yearly Stats------

        # Batting Stats select query on batting_by_player_id
        batting_stats = connection.session.execute(
            "SELECT * FROM statistics.batting_by_player_id WHERE player_id=%s AND year_id=%s", [player_id, year_id])

        # Assign values to variables
        for row in batting_stats:
            homerun = row.hr
            triple = row.triple
            double = row.double
            run = row.r
            rbi = row.rbi
            team = row.team_id

        # Calculate Cost per Stat

        cost_homerun = cost / homerun
        cost_triple = cost / triple
        cost_double = cost / double
        cost_run = cost / run
        cost_run_rbi = cost / (run + rbi)

        # Print Results
        print('============ PLAYER COST PER OFFENSIVE PRODUCTION ===============')
        print('Player_ID: ', player_id, ' | Year: ', year_id, ' | Team: ', team)
        print('-----------------------------------------------------------------')
        print("Cost per homerun:   $", "{:,.2f}".format(cost_homerun))
        print('Cost per triple:    $', "{:,.2f}".format(cost_triple))
        print('Cost per double:    $', "{:,.2f}".format(cost_double))
        print('Cost per run:       $', "{:,.2f}".format(cost_run))
        print('Cost per run + rbi: $', "{:,.2f}".format(cost_run_rbi))
        print('=================================================================')
    except ZeroDivisionError as zero:
        # Zero Division Error occurs when there is no record of the player in the table
        print('\n*****************************************************************')
        print(player_id.capitalize(
        ), ' is not included in the batting table.\nFIX: Insert players statline into table with write_update_tables\nError:', zero)
        print('*****************************************************************')
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


cost_per_off_prod('dyeje01', 2005)  # 4 mil
cost_per_off_prod('berkmla01', 2005)  # 10.5 mil

# cost_per_off_prod('konerpa01', 2005)  # 8.75 mil
# cost_per_off_prod('bagweje01', 2005)  # 18 mil
