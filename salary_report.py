from connect_database import Connection


def salary_report_year_team(year_id, team_id):
    try:
        connection = Connection()

        # ----Query Average, Minimum, Maximum, and Total Salary to produce a Salary Report------

        # ========== Average ==========

        # Select average query on salary_by_team_id
        average_query = connection.session.execute(
            "SELECT AVG(salary) FROM statistics.salary_by_team_id WHERE year_id=%s and team_id=%s", [year_id, team_id])

        # Assign results to variable
        for row in average_query:
            average_salary_year = row.system_avg_salary

        # ========== Minimum ==========

        # Select minimum query on salary_by_team_id
        min_salary_query = connection.session.execute(
            "SELECT min(salary) FROM statistics.salary_by_team_id WHERE year_id=%s and team_id=%s", [year_id, team_id])

        # Assign results to variable
        for row in min_salary_query:
            min_salary_year = row.system_min_salary

        # ========== Maximum =========

        # Select maximum query on salary_by_team_id
        max_salary_query = connection.session.execute(
            "SELECT max(salary) FROM statistics.salary_by_team_id WHERE year_id=%s and team_id=%s", [year_id, team_id])

        # Assign results to variable
        for row in max_salary_query:
            max_salary_year = row.system_max_salary

        # ========== Total ==========

        # Select total query on salary_by_team_id
        total_salary_query = connection.session.execute(
            "SELECT sum(salary) FROM statistics.salary_by_team_id WHERE year_id=%s and team_id=%s", [year_id, team_id])

        # Assign results to variable
        for row in total_salary_query:
            total_salary_year = row.system_sum_salary

        print("=======Average Salary by Year==========")
        print("Team:           ", team_id)
        print("Year:           ", year_id)
        print("Total Salary:  $", "{:,.2f}".format(total_salary_year))
        print("Avg Salary:    $", "{:,.2f}".format(average_salary_year))
        print("Min Salary:    $", "{:,.2f}".format(min_salary_year))
        print("Max Salary:    $", "{:,.2f}".format(max_salary_year))
        print("=======================================")
    except Exception as e:
        print('Error: ', e)
    else:
        connection.close()
        print('\n**Connection closed!**\n')


salary_report_year_team(2005, 'CHA')
